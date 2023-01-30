from server import loadClubs, loadCompetitions


def test_load_clubs_and_check_data():
    clubs = loadClubs()
    for club in clubs:
        assert 'name' and 'email' and 'points' in club


def test_load_competitions_and_check_data():
    competitions = loadCompetitions()
    for competitions in competitions:
        assert 'name' and 'date' and 'numberOfPlaces' in competitions