import requests
import json
from modules.pdf_decrypt import pdf_to_base64


if __name__ == "__main__":

    base64_data = pdf_to_base64("./Registration Assessment.pdf")

    question = 'Create a spring boot application to develop registration form with fields Employee name, dob, address, department, emailid. if the submit is clicked when the url "/employeeregistration", display the message " successful registration".'
    mark = 100
    url = " http://127.0.0.1:8000/submit"
    data = {
        "user_id": 1,
        "question_id": 101,
        "assessment_id": "1A001",
        "question_text": question,
        "pdf_file_base64": base64_data.decode("utf-8"),
        "max_mark": mark,
    }

    # print(json.dumps(data))

    headers = {"Content-Type": "application/json"}

    response = requests.post(url, data=json.dumps(data), headers=headers)

    if response.status_code != 200:

        # switch case for different status codes
        if response.status_code == 400:
            print("The request body is malformed. Bad request: ", response)
        elif response.status_code == 403:
            print("Your API key doesn't have the required permissions: ", response)
        elif response.status_code == 429:
            print("You've exceeded the rate limit: ", response)
        elif response.status_code == 404:
            print("Not found: ", response)
        elif response.status_code == 500:
            print(
                "An unexpected error occurred on Google's side. Internal server error: ",
                response,
            )
        elif response.status_code == 503:
            print(
                "The service may be temporarily overloaded or down. Service unavailable: ",
                response,
            )
        else:
            print("Unknown error: ", response)
        exit()
        # print("Request failed: ", response)
        # raise Exception("Request failed with status code:", response.status_code)

    if not json.loads(response.text):
        print("Error response: ", response)
        raise Exception("No JSON data returned")
    # print("\nLogical error: Yes, Syntax error: Yes\n")

    try:
        for key, value in response.json().items():
            # print in a table format if the value is a list
            if isinstance(value, list):
                print(f"{key}:")
                for item in value:
                    print(f"-> {item}")
            else:
                print(f"{key}: {value}")
            print("")
    except ValueError:
        raise Exception(
            f"Invalid JSON response: Status code {response.status_code}, Response text: {response.text}"
        )
    except Exception as e:
        raise e

#  http://127.0.0.1:8000/submit
