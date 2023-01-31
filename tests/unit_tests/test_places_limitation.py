import pytest
import server


@pytest.fixture
def client():
    server.app.config['TESTING'] = True
    clients = server.app.test_client()
    return clients


def test_purchase_more_than_12_places(client):
    club = server.clubs[0]['name']
    competition = server.competitions[0]
    response = client.post('/purchasePlaces',
                           data={
                               'club': club,
                               'competition': competition['name'],
                               'numberOfPlaces': competition['numberOfPlaces'],
                               'places': 16,
                           })
    assert response.status_code == 200


def test_purchase_places_required_according_to_the_number_of_points(client):
    club = server.clubs[0]['name']
    competition = server.competitions[0]
    response = client.post('/purchasePlaces',
                           data={
                               'club': club,
                               'competition': competition['name'],
                               'numberOfPlaces': competition['numberOfPlaces'],
                               'places': 3,
                           })
    assert response.status_code == 200