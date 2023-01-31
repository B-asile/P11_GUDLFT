import server

server.app.config['TESTING'] = True
client = server.app.test_client()

def test_unknow_email():
    """ """
    response = client.post('/showSummary',
                           data={'email': 'undifined@user.com'})
    assert response.status_code == 302

def test_good_email():
    """ """
    response = client.post('/showSummary',
                           data={'email': 'john@simplylift.co'})
    assert response.status_code == 200

def test_empty_email():
    response = client.post('/showSummary',
                          data={'email': ''})
    assert response.status_code == 302

def test_invalid_email():
    response = client.post('/showSummary',
                          data={'email': 'invalid'})
    assert response.status_code == 302

def test_logout():
    response = client.get('/logout')
    assert response.status_code == 302

def test_index():
    response = client.get('/')
    assert response.status_code == 200