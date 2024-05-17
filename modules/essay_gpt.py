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


def essay_correction_gemini(
    question: str, topic: str, essay: str, mark: int, description: str
) -> str:
    """
    Generate a corrected version of the text using the Gemini Pro model.

    Args:
        question (str): The essay question.
        topic (str): The topic of the essay.
        essay (str): The essay text to be corrected.
        mark (str): The maximum mark for the essay.
        description (str): The description of the images (optional).

    Returns:
        str: The corrected text.

    Raises:
        Exception: If an error occurs during the correction process.
    """

    # Configure the API key for Google's Generative AI
    api_key = GetAPIKey(3)
    # Define the name of the model to be used
    model_name = "gemini-1.0-pro"

    # Configure the API key
    genai.configure(api_key=api_key)

    # Set up the model
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

    # Initialize the Gemini Pro model
    model = genai.GenerativeModel(
        model_name=model_name,
        generation_config=generation_config,  # type: ignore
        safety_settings=safety_settings,
    )

    # Prepare the prompt for the model
    # The prompt is a generic question to the model asking for the corrected text
    prompt = (
        f"You are a strict professor who corrects the answer from this following topics: {topic}. "
        f"Given the following question: {question}. "
        f"This is the answer: \n{essay}"
    )

    # Add the description of the images to the prompt (if provided)
    if description:
        prompt += f" Description of the images (these images are included in the answer): \n{description}"

    # Specify the format of the response
    # The format should be a JSON with a key "Mark" and "Suggestions"
    prompt += (
        "Answer me in a JSON format. The format should be: "
        '{"Mark": "the mark (out of '
        f"{mark}"
        ') (in numbers)", "Suggestions": ["all of the Suggestions(positive and negative) in a list(not more than 10 suggestions)"]}'
        "Avoid adding any symbols like '\\n', '\\t', '\\r' in the JSON format. Make sure the answer is in JSON format."
        "While giving the suggestions, don't add any additional information. Just give the accurate suggestions related to the topics above. "
        "If the answer is not related to the question and the topic at the least, the mark should be 0 and give suggestions to improve."
    )

    # Add a suggestion about the images using the description of the images (if provided)
    if description:
        prompt += "Also add a suggestion about the images with the help of the description of the images that I provided"

    # token_count = model.count_tokens(prompt)
    # print(f"Token count: {token_count}")

    # Generate the topic using the model
    response = model.generate_content(prompt)

    return response.text
