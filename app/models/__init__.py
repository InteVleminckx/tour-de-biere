from .setup import Session, Base, engine
from . import tables  # Import all models so Base.metadata knows them

# Automatically create tables
Base.metadata.create_all(engine)

# Optionally expose models for easy import
# from .tables import User  # Add other models as needed

__all__ = ["Session", "Base", "engine"] #, "User"]
