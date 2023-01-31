import pytest
import server


@pytest.fixture
def client():
    server.app.config['TESTING'] = True
    clients = server.app.test_client()
    return clients


def test_points_not_available(client):
    club = server.clubs[0]['name']
    competition = server.competitions[0]
    result = client.post('/purchasePlaces',
                         data={
                             'club': club,
                             'competition': competition['name'],
                             'numberOfPlaces': competition['numberOfPlaces'],
                             'places': 20,
                         })
    assert result.status_code == 200


def test_points_available(client):
    club = server.clubs[0]['name']
    competition = server.competitions[0]
    result = client.post('/purchasePlaces',
                         data={'club': club,
                               'competition': competition['name'],
                               'places': 3,
                               })
    assert result.status_code == 200
