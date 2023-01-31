def test_get_purchase_page_with_valid_arguments(mocker, client, clubs, competitions):
    mocker.patch('server.clubs', clubs)
    mocker.patch('server.competitions', competitions)
    response = client.get(f"book/{competitions[0]['name']}/{clubs[0]['name']}")
    assert response.status_code == 200

def test_get_purchase_page_with_invalid_arguments(mocker, client, clubs, competitions):
    mocker.patch('server.clubs', clubs)
    mocker.patch('server.competitions', competitions)
    response = client.get('book/none/none/')
    assert response.status_code == 404

def test_purchase_places_with_valid_data(mocker, client,  clubs, competitions):
    mocker.patch('server.clubs', clubs)
    mocker.patch('server.competitions', competitions)
    data = {
        'club': clubs[0]['name'],
        'competition': competitions[0]['name'],
        'numberOfPlaces': f"{1}",
    }
    response = client.post('purchase-places', data=data)
    assert response.status_code == 200
    assert 'Great-booking complete!' in response.data.decode()
    assert "You can't purchase that many places" not in response.data.decode()


def test_purchase_places_with_invalid_competition_or_club_data(mocker, client,  clubs, competitions):
    mocker.patch('server.clubs', clubs)
    mocker.patch('server.competitions', competitions)
    data = {
        'club': 'none',
        'competition': 'none',
        'places': f"{1}",
    }
    response = client.post('purchase-places', data=data)
    assert response.status_code == 404


