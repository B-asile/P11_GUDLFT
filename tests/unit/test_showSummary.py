
def test_with_know_email(mocker, client, clubs):
    mocker.patch('server.clubs', clubs)
    response = client.post('showSummary', data=clubs[0])
    assert response.status_code == 200


def test_with_unknow_email(mocker, client, clubs):
    mocker.patch('server.clubs', clubs)
    response = client.post('showSummary', data={'email': 'test@unknow.mail'})
    assert response.status_code == 302