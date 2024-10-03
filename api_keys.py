from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
CHATGPT_API_KEY = os.getenv('CHATGPT_API_KEY')