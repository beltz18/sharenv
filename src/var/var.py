from dotenv import load_dotenv
import os
load_dotenv()

SECRET = os.getenv('SECRET')
URI    = os.getenv('MONGO_URI')