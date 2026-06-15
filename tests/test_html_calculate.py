def test_get_home_page_returns_200(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Distance' in response.data

def test_get_home_page_returns_200(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Distance' in response.data

def test_post_calculates_distance(client):
    response = client.post('/', data={'apoint': '0,0', 'bpoint': '3,4'})
    assert response.status_code == 200
    assert b'5.0' in response.data  # distance(0,0 -> 3,4) = 5

def test_post_same_points_returns_zero(client):
    response = client.post('/', data={'apoint': '2,2', 'bpoint': '2,2'})
    assert response.status_code == 200
    assert b'0.0' in response.data