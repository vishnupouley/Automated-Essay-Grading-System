import google.generativeai as genai
import os
from PIL import Image
import shutil
from modules.get_key import GetAPIKey


def generate_image_descriptions(question: str, topic: str) -> str:
    """
    Generate descriptions for images in a folder.

    Returns:
        str: A string with descriptions for each image.
    """

    # Configure the API key for the Gemini Pro model
    api_key = GetAPIKey(1)
    model_name = "gemini-1.0-pro-vision-latest"

    # Configure the Gemini Pro model with the API key
    genai.configure(api_key=api_key)

    # Set up the model

    generation_config = {
      "temperature": 0,
      "top_p": 1,
      "top_k": 1,
      "max_output_tokens": 1000,
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
    prompt = (
        f"You are a helpful assistant who provides the complete description (not more than 300 words) of the image in the topic {topic}. "
        f"Given the following question: {question}"
    )

    # List to store descriptions of images
    descriptions = []

    # Path to the folder containing images
    folder_path = "./images-extracted"

    # Iterate over each file in the folder
    # Check if the folder is empty
    if not os.listdir(folder_path):
        shutil.rmtree("./images-extracted")

    else:
        for filename in os.listdir(folder_path):
            # Check if the file is a valid image
            if filename.endswith((".jpg", ".png")):
                # Path to the image file
                image_path = os.path.join(folder_path, filename)

                try:
                    # Open the image
                    with Image.open(image_path) as img:
                        # Generate the description
                        response = model.generate_content([prompt, img])
                        # Append the description to the list
                        descriptions.append(
                            f"Image {len(descriptions) + 1}: {response.text}"
                        )
                except (FileNotFoundError, OSError) as e:
                    # Handle case when image cannot be opened
                    descriptions.append(f"Failed to open {filename}: {e}")
                except Exception as e:
                    # Handle any other exceptions
                    descriptions.append(
                        f"Failed to generate description for {filename}: {e}"
                    )

        # Remove the folder containing images after descriptions are generated
        shutil.rmtree("./images-extracted")

    # Join the descriptions into a string and return
    return "\n".join(descriptions)


if __name__ == "__main__":
    # Specify the folder containing your images
    question = ""
    topic = ""
    description = generate_image_descriptions(question, topic)
    print(description)
