from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.models.setup import Base


class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    general_classification = relationship("GeneralClassification", back_populates="user", cascade="all, delete")
    points_classification = relationship("PointsClassification", back_populates="user", cascade="all, delete")
    polka_classification = relationship("PolkaClassification", back_populates="user", cascade="all, delete")


class GeneralClassification(Base):
    __tablename__ = "general_classification"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, unique=True)
    time = Column(Integer, nullable=False, default=0)

    user = relationship("Users", back_populates="general_classification")


class PointsClassification(Base):
    __tablename__ = "points_classification"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, unique=True)
    points = Column(Integer, nullable=False, default=0)

    user = relationship("Users", back_populates="points_classification")


class PolkaClassification(Base):
    __tablename__ = "polka_classification"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, unique=True)
    points = Column(Integer, nullable=False, default=0)

    user = relationship("Users", back_populates="polka_classification")


class Objective(Base):
    __tablename__ = "objective"
    id = Column(Integer, primary_key=True)
    objective_type = Column(String, nullable=False, unique=True)  # Climb, sprint, finish
    category = Column(String)  # different kinds of beer


class EventLog(Base):
    __tablename__ = 'event_log'
    id = Column(Integer, primary_key=True)
    etappe_id = Column(Integer, ForeignKey("etappe.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    objective_id = Column(Integer, ForeignKey("objective.id"), nullable=False)
    timestamp = Column(Integer, nullable=False)


class Etappe(Base):
    __tablename__ = 'etappe'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)


class Objectives(Base):
    __tablename__ = 'objectives'
    id = Column(Integer, primary_key=True)
    etappe_id = Column(Integer, ForeignKey("etappe.id"))
    objective_id = Column(Integer, ForeignKey("objective.id"))
    objective_order = Column(Integer, nullable=False)


class PointsCategoryPoints(Base):
    __tablename__ = 'points_category_points'
    id = Column(Integer, primary_key=True)
    category = Column(String)  # different kinds of beer
    position = Column(Integer)
    points = Column(Integer)


class PolkaCategoryPoints(Base):
    __tablename__ = 'polka_category_points'
    id = Column(Integer, primary_key=True)
    category = Column(String)  # different kinds of beer
    position = Column(Integer)
    points = Column(Integer)
