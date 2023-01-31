import server
import pytest


@pytest.fixture
def client():
    server.app.config['TESTING'] = True
    clients = server.app.test_client()
    return clients

def test_club_refresh_points(client):
    club = server.clubs[1]
    before_points = club["points"]
    competition = server.competitions[0]['name']
    response = client.post('/purchasePlaces',
                           data={
                               'club': club['name'],
                               'competition': competition,
                               'places': 3
                           })
    assert response.status_code == 200
    assert before_points != club['points']


def test_competition_refresh_places(client):
    club = server.clubs[0]['name']
    competition = server.competitions[0]
    before_points = competition["numberOfPlaces"]
    response = client.post('/purchasePlaces',
                           data={
                               'club': club,
                               'competition': competition['name'],
                               'numberOfPlaces': competition['numberOfPlaces'],
                               'places': 3,
                           })
    assert response.status_code == 200
    assert before_points != competition["numberOfPlaces"]
