

def test_list_get(app):
    '''test if the model initialized with correct valus'''
    response = app.get('/')
    assert response.status_code == 200
