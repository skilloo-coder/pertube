import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()  # loads .env file

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL not found in .env file")

engine = create_engine(DATABASE_URL, pool_pre_ping=True)
