import base64


def pdf_to_base64(pdf_file_path: str) -> bytes:
    """
    Convert a PDF file to base64 encoding.

    Parameters:
    pdf_file_path (str): The file path to the PDF file.

    Returns:
    bytes: The base64 encoded data of the PDF file.
    """
    with open(pdf_file_path, "rb") as pdf_file:
        return base64.b64encode(pdf_file.read())


def base64_to_pdf(base64_data: str, pdf_file_path: str) -> None:
    """
    Decode base64 encoded data and save it as a PDF file.

    Args:
        base64_data (bytes): The base64 encoded data.
        pdf_file_path (str): The path to save the decrypted PDF file.

    Returns:
        None
    """
    # Decode base64 encoded data
    pdf_data: bytes = base64.b64decode(base64_data)

    # Save decrypted data as a PDF file
    with open(pdf_file_path, "wb") as pdf_file:  # type: ignore
        pdf_file.write(pdf_data)
