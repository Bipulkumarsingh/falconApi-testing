from falcon import testing, HTTP_200
from testing.cases.endpoint_name_cases import test_list, module_cases
from server.service import function_name
from app import api
import pytest

@pytest.fixture
def client():
	return testing.TestClient(api)

#############################################################
###################  API TESTING ############################
############################################################# 

class TestServices:
	headers = {
	"Content-Type": "application/json",
	"Authorization": "Baerer Token"
	}

	@pytest.mark.parametrize("request_case", "response_case", test_list)
	def test_service1(self, request_case, response_case):
		return_data = client.simulate_post(path='/service1-endpoint', headers=self.headers, json=request_case)
		assert return_data.josn == response_case
		assert return_data.status == HTTP_200 

#############################################################
###################  MODULE TESTING #########################
############################################################# 

class TestParseFile:
    @pytest.mark.parametrize("test_case,expected", module_cases)
    def test_cases_year(self, test_case, expected_date):
        start = function_name(test_case)
        assert start == expected