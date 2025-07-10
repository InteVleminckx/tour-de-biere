from config import Config
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Declare base
Base = declarative_base()

# Create engine
engine = create_engine(Config.DATABASE_URI, echo=True)

# Create session factory
Session = sessionmaker(bind=engine)
