# Essay Analysis and Grading System

Developed an AI-driven automated essay grading system using Generative AI(Gemini) and Python libraries like PyMuPDF and Pillow. The system processes essay PDFs with text and images received from an LMS platform, analyzes the content using tailored prompts, and provides a comprehensive report with grades and detailed feedback through APIs. Implemented stages for grading essays with images, and created a web API using FastAPI for LMS integration.

## Setup this software into your system

### 1. Make sure Python 3.11 and pip are installed using these commands

*For python*

```bash
python --version
```

*For pip*

```bash
pip --version
```

> If not installed you need to install **Python 3.11** to download Python and pip

### 2. Download necessary executable files

1. Download [Visual Studio Community](https://visualstudio.microsoft.com/downloads/) executable file from your browser
2. Install Visual Studio Community and open it.
3. Install this two things
   -  Python development
   -  Desktop developement with C++

### 3. After that, download the necessary packages of Python 3.11

```bash
pip install -r requirements.txt
```

### 4. Get Gemini API keys from your Gemini account and setup to the code

1. Create Gemini API key from [Google AI Studio](https://aistudio.google.com/app/apikey). Create three API keys for smooth performance.
2. Copy the three API keys and paste it in the `module/get_key.py` code in a list format
   ```python
   def GetAPIKey(index: int) -> str:
    """
    A function to retrieve an API key based on the provided index.

    Args:
        index (int): The index of the API key to retrieve from the list.

    Returns:
        str: The API key corresponding to the provided index.
    """
   
    api_key = [] # Paste the three API keys in this list
    return api_key[index - 1]
   ```
3. Save the code

## Instruction and explaination for using this code

### 1. Run command

1. Make sure that you're in the workspace directory in your command prompt
2. This is the command to run the API:
   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000 --reload
   ```
   and this would run on the [link](http://0.0.0.0:8000) `http://0.0.0.0:8000`. You could configure with any IP address or host it in your server.
   to be specific this is the breakdown of this above command
   > `uvicorn <program name>:app --host <your suitable host number> --port <your suitable port number> --reload 

### 2. Inputs structure

- As this is running on FastAPI framework, the input will be in JSON format. The format is
   ```json
   {
        "user_id": 1,
        "question_id": 101,
        "assessment_id": "1A001",
        "question_text": "Question",
        "pdf_file_base64": "PDF file in base64 format",
        "max_mark": 100,
   }
   ```
- For testing purpose, I created a python porgram `client.py` where I send this JSON file to the API and return the output with the help of the `requests` library. I configure the link in "/submit".
- If you need to run for testing the API, you could simply run this command instead of that long one
  ```bash
  uvicorn main:app --reload
  ```
  The API would just run at the [link](http://127.0.0.1:8000) on your default localhost `127.0.0.1` and in your default port number `8000`
