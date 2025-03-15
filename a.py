import os
from dotenv import load_dotenv

load_dotenv()
SECRET_KEY = os.getenv('SECRET_KEY')
b = os.getenv('USER_PSQL')

print("gi: ", SECRET_KEY, b)