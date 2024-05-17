import google.generativeai as genai
import json
from modules.get_key import GetAPIKey


def is_valid_json(json_str: str) -> bool:
    """
    Check if a given string is a valid JSON format.

    Args:
        json_str (str): The string to be checked.

    Returns:
        bool: True if the string is a valid JSON, False otherwise.
    """
    try:
        # Attempt to parse the string as JSON
        json.loads(json_str)
        # If parsing is successful, return True
        return True
    except Exception:
        # If parsing fails, return False
        return False


def topic_fetch_all(question: str) -> str:
    """
    Fetch the topic of the question using the Gemini Pro model.

    Args:
        question (str): The question to be fetched.

    Returns:
        str: The list of topics and tags related to the question.
              If the response is empty, an empty string is returned.
    """
    api_key = GetAPIKey(2)
    model_name = "gemini-1.0-pro"
    genai.configure(api_key=api_key)

    generation_config = {
        "temperature": 0,
        "top_p": 1,
        "top_k": 1,
        "max_output_tokens": 700,
    }

    safety_settings = [
        {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
        {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"},
        {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE"},
        {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"},
    ]

    model = genai.GenerativeModel(
        model_name=model_name,
        generation_config=generation_config,  # type: ignore
        safety_settings=safety_settings,
    )

    prompt = (
        "You are a helpful assistant who provides the topic and tags related to the question. "
        f"Given the following question: {question}"
    )

    prompt += (
        "Answer me in a JSON format. The format should be: "
        '{"Topic": [the topics and the tags related to the question in a list]}'
    )

    # Generate the response
    response = model.generate_content(prompt)

    if not response.text:
        return ""
    elif is_valid_json(response.text):
        return str(json.loads(response.text)["Topic"])
    else:
        return response.text
