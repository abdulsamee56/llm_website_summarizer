import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv
import openai

# Load environment variables
load_dotenv()

# Fetch OpenAI API key
API_KEY = os.getenv('OPENAI_API_KEY')  # Ensure the environment variable name matches

# Set the API key for OpenAI
openai.api_key = API_KEY

class Website:
    def __init__(self, url):
        """
        Initialize the Website object by fetching the content from the given URL.
        """
        self.url = url
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
        }
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        self.title = soup.title.string if soup.title else "No title found"
        for tag in soup(['script', 'style', 'img', 'input']):
            tag.decompose()
        self.text = soup.get_text(separator="\n", strip=True)

# Function to summarize the content using OpenAI
def summarize_text(text):
    try:
        # New syntax for openai>=1.0.0
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an assistant that summarizes website content."},
                {"role": "user", "content": text},
            ]
        )
        # Extract the summary from the assistant's response
        return response.choices[0].message["content"]
    except Exception as e:
        return f"Error: {e}"
