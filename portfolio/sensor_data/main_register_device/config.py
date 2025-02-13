import os
from dotenv import load_dotenv

# Cargar las variables desde el archivo .env
load_dotenv()

AWS_API_URL = os.getenv("API_URL")
AWS_API_KEY = os.getenv("API_KEY")

