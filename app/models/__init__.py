from .setup import Session, Base, engine
from . import tables  # Import all models so Base.metadata knows them

# Automatically create tables
Base.metadata.create_all(engine)

# Optionally expose models for easy import
from .tables import Users, GeneralClassification, PointsClassification, PolkaClassification, Objective, EventLog, Etappe, \
    PointsCategoryPoints, PolkaCategoryPoints, Objectives  # Add other models as needed

__all__ = ["Session", "Base", "engine", "Users", "GeneralClassification", "PointsClassification", "PolkaClassification",
           "Objective", "EventLog", "Etappe", "PointsCategoryPoints", "PolkaCategoryPoints", "Objectives"]
