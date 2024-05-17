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
3. efer
4. 
