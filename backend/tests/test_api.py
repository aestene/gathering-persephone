
def test_api(test_client):
     response = test_client.get("/example_namespace/hello-world")
     print(response.data)
     print(response.mimetype)
     assert response.json == {'value': 'Hello World'}
