from backend.yrclient.yr_client import YrClient

def test_YrClient_ping():
    client = YrClient()
    assert client.ping().status_code == 200
