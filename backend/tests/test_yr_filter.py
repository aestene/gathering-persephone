class TestYrFilter:
    def test_get_current_temperature(self, yr_filter):
        temperature = yr_filter.get_current_temperature(63.4305, 10.3951)
        assert isinstance(temperature, float)
