import json

def test_api_distances_returns_empty_list(client):
    response = client.get('/api/distances')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert isinstance(data, list)

def test_api_distance_post_calculates_correctly(client):
    payload = {'start_point': '0,0', 'end_point': '3,4'}
    response = client.post(
        '/api/distance',
        data=json.dumps(payload),
        content_type='application/json'
    )
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['result_distance'] == 5.0

def test_api_distance_get_is_not_allowed(client):
    """GET sur /api/distance est accepté par Flask alors qu'il ne devrait pas l'être.
    La route accepte GET, PUT et POST — non conforme REST.
    Flask retourne 415 (pas de body JSON) plutôt que 405 (méthode interdite).
    Ce test documente le comportement bugué actuel."""
    response = client.get('/api/distance')
    assert response.status_code == 415  # comportement actuel (bugué)