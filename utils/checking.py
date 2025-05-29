"""Methods for checking responses"""
import json

class Checking:

    """Method for checking a status code of response"""
    @staticmethod
    def check_status_code(result, status_code):
        assert status_code == result.status_code, "Error, Status code do not match."
        print(f"Successfully! Status code is {result.status_code}")


    """Method for checking required fields in response"""
    @staticmethod
    def check_json_token(result, expected_value):
        fields = json.loads(result.text)
        assert list(fields) == expected_value, "Error. The list of fields doesn't match with the expected one."
        print(list(fields))
        print("All fields are presented")


    """Method for checking a length of response"""

    @staticmethod
    def check_len_of_response(result, num):
        assert len(result.json()) == num, f"Error. We expected that the length of response is  {num} but got {len(result.json())}"
        print(f"Length of response is correct!")