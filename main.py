from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.orm import sessionmaker, Session, declarative_base
from pydantic import BaseModel
from typing import List
import os
from dotenv import load_dotenv
from data.seed import cocktails

# Database setup
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@localhost:5432/cocktails_db")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Models
class CocktailDB(Base):
    __tablename__ = "cocktails"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(Text)
    ingredients = Column(Text)
    instructions = Column(Text)

# Create tables
Base.metadata.create_all(bind=engine)

# Seed data
def seed_database():
    db = SessionLocal()
    try:
        # Check if database is empty
        if db.query(CocktailDB).first() is None:
            # Add cocktails to database
            for cocktail_data in cocktails:
                try:
                    cocktail = CocktailDB(**cocktail_data)
                    db.add(cocktail)
                    db.commit()
                except Exception as e:
                    db.rollback()
                    print(f"Error adding {cocktail_data['name']}: {str(e)}")
    finally:
        db.close()

# Seed on startup
seed_database()

class CocktailBase(BaseModel):
    name: str
    description: str
    ingredients: str
    instructions: str

class Cocktail(CocktailBase):
    id: int
    class Config:
        orm_mode = True

# Service
class CocktailService:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> List[CocktailDB]:
        return self.db.query(CocktailDB).all()

    def get_by_name(self, name: str) -> CocktailDB:
        cocktail = self.db.query(CocktailDB).filter(CocktailDB.name == name).first()
        if not cocktail:
            raise HTTPException(status_code=404, detail=f"Cocktail '{name}' not found")
        return cocktail

    def create(self, cocktail: CocktailBase) -> CocktailDB:
        try:
            db_cocktail = CocktailDB(**cocktail.dict())
            self.db.add(db_cocktail)
            self.db.commit()
            self.db.refresh(db_cocktail)
            return db_cocktail
        except Exception:
            self.db.rollback()
            raise HTTPException(status_code=400, detail=f"Cocktail with name '{cocktail.name}' already exists")

# App
app = FastAPI(title="Cocktail Manager")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_service(db: Session = Depends(get_db)) -> CocktailService:
    return CocktailService(db)

@app.get("/")
async def welcome():
    return {"message": "Welcome to Cocktail Manager API"}

@app.get("/api/cocktails")
def get_cocktails(service: CocktailService = Depends(get_service)):
    return service.get_all()

@app.post("/api/cocktails/add")
def create_cocktail(cocktail: CocktailBase, service: CocktailService = Depends(get_service)):
    return service.create(cocktail)

@app.get("/api/cocktails/{name}")
def get_cocktail(name: str, service: CocktailService = Depends(get_service)):
    return service.get_by_name(name) 