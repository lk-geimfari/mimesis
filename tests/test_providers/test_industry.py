import pytest

from mimesis import Industry

class TestIndustry(object):

    @pytest.fixture
    def industry(self):
        return Industry()

    def test_plu(self, industry):
        plu = industry.plu_code()

        assert len(plu) == 4

    def test_api_well(self, industry):
        api_well = industry.api_well_number()

        assert len(api_well) == 18
