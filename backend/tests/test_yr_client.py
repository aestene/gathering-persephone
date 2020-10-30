from backend.yrclient.yr_client import YrClient


def test_YrClient_ping():
    client = YrClient()
    assert client.ping().status_code == 200


def test_YrClient_compact_forecast():
    client = YrClient()
    result = client.compact_forecast({"lon": 50, "lat": 50})
    # We only assert that the status_code is good. The entry point always returns
    # forecasts, hence testing on actually data won't be possible.
    assert result.status_code == 200
