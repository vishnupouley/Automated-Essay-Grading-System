import fitz  # PyMuPDF
import os


def extract_text_from_pdf(pdf_path: str) -> str:
    """
    Extracts text from a PDF file.

    Args:
        pdf_path: The path to the PDF file.

    Returns:
        The extracted text.
    """
    with fitz.open(pdf_path) as doc:
        return " ".join(page.get_text("text") for page in doc)  # type: ignore


def extract_images_from_pdf(pdf_path: str) -> None:
    """
    Extracts images from a PDF and saves them to the "images-extracted" directory.

    :param pdf_path: The path to the PDF file.
    """

    output_dir = "./images-extracted"

    # Open the PDF
    doc = fitz.open(pdf_path)

    # Create the output directory if it does not exist
    os.makedirs(output_dir, exist_ok=True)

    # Iterate through each page and extract images
    for page_num, page in enumerate(doc, start=1):  # type: ignore
        # Extract images from the current page
        images = page.get_images()
        for image_num, image in enumerate(images, start=1):
            # Extract the image data
            image_data = doc.extract_image(image[0])["image"]
            # Generate the image name
            image_name = f"page_{page_num}_image_{image_num}.png"
            # Save the image to the output directory
            with open(os.path.join(output_dir, image_name), "wb") as img_file:
                img_file.write(image_data)

    doc.close()
