from fastapi import FastAPI, Query, Body
from modules.essay_gpt import essay_correction_gemini
from modules.extract import extract_text_from_pdf, extract_images_from_pdf
from modules.image_gpt import generate_image_descriptions
from modules.pdf_decrypt import base64_to_pdf
from modules.topic_fetch import topic_fetch_all
import os
import json

app = FastAPI()


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
    except ValueError:
        # If parsing fails, return False
        return False


@app.post("/submit")
async def submit_data(
    user_id: int = Query(description="user_id") and Body(...),
    question_id: int = Query(description="question_id") and Body(...),
    assessment_id: str = Query(description="assessment_id") and Body(...),
    question_text: str = Query(description="question_text") and Body(...),
    pdf_file_base64: str = Query(description="pdf_file_base64") and Body(...),
    max_mark: int = Query(description="max_mark") and Body(...),
):
    """
    A function to submit data including `user_id`, `question_id`, `question_text`, `pdf_file_base64`, and `max_mark`.
    Calls multiple functions to process the submitted data and generate a result in JSON format.
    Returns the processed result with added `user_id` and `question_id`.
    """

    if pdf_file_base64 is None:
        raise ValueError("pdf_file_base64 cannot be None")
    if question_text is None:
        raise ValueError("question_text cannot be None")
    if max_mark is None:
        raise ValueError("max_mark cannot be None")

    # Call the base64_to_pdf function with the received data
    pdf_path = "decrypted.pdf"
    base64_to_pdf(pdf_file_base64, pdf_path)

    # Call the extract_images_from_pdf function with the received data
    extract_images_from_pdf(pdf_path)

    # Call the extract_text_from_pdf function with the received data
    extracted_text = extract_text_from_pdf(pdf_path)

    # Call the topic_fetch_all function with the received data
    topics = topic_fetch_all(question_text)

    # check if the image-extracted folder has any files
    if len(os.listdir("./images-extracted")) == 0:
        image_descriptions = ""
    else:
        image_descriptions = generate_image_descriptions(question_text, topics)

    # delete the decrypted file
    os.remove(pdf_path)

    # Call the essay_correction_gemini function with the received data
    result = essay_correction_gemini(
        question_text, topics, extracted_text, max_mark, image_descriptions
    )

    if not is_valid_json(result):
        return "Invalid JSON format in 'result' variable", result

    result_dict = json.loads(result)

    # append the user_id and question_id to the result_dict
    result_dict["user_id"] = user_id
    result_dict["question_id"] = question_id
    result_dict["assessment_id"] = assessment_id

    # Return the processed data
    return result_dict


# uvicorn main:app --reload
# uvicorn main:app --port 8080 --reload
# uvicorn main:app --host 0.0.0.0 --port 8000 --reload
