from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv

# Database setup
load_dotenv()
# For other envs, DATABASE_URL has to set as env variable
# Values are located in .env folder
# flyio proxy has to be used
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@localhost:5432/cocktails_db")
print(f"Using database URL: {DATABASE_URL}")

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

# Sample cocktails data
cocktails = [
    {
        "name": "Mojito",
        "description": "A refreshing Cuban highball",
        "ingredients": "White rum, Sugar, Lime juice, Soda water, Mint",
        "instructions": "Muddle mint leaves with sugar and lime juice. Add rum and top with soda water."
    },
    {
        "name": "Old Fashioned",
        "description": "A classic cocktail with bourbon",
        "ingredients": "Bourbon, Angostura bitters, Sugar cube, Orange peel",
        "instructions": "Muddle sugar cube with bitters. Add bourbon and stir. Garnish with orange peel."
    },
    {
        "name": "Margarita",
        "description": "A Mexican classic",
        "ingredients": "Tequila, Triple sec, Lime juice, Salt",
        "instructions": "Shake tequila, triple sec, and lime juice with ice. Strain into a salt-rimmed glass."
    },
    {
        "name": "Martini",
        "description": "The king of cocktails",
        "ingredients": "Gin, Dry vermouth, Olive or lemon twist",
        "instructions": "Stir gin and vermouth with ice. Strain into a chilled glass. Garnish with olive or lemon twist."
    },
    {
        "name": "Negroni",
        "description": "Italian aperitif",
        "ingredients": "Gin, Campari, Sweet vermouth, Orange peel",
        "instructions": "Stir all ingredients with ice. Strain into a glass. Garnish with orange peel."
    },
    {
        "name": "Manhattan",
        "description": "Classic whiskey cocktail",
        "ingredients": "Rye whiskey, Sweet vermouth, Angostura bitters, Maraschino cherry",
        "instructions": "Stir whiskey, vermouth, and bitters with ice. Strain into a glass. Garnish with cherry."
    },
    {
        "name": "Daiquiri",
        "description": "Cuban rum cocktail",
        "ingredients": "White rum, Lime juice, Simple syrup",
        "instructions": "Shake all ingredients with ice. Strain into a chilled glass."
    },
    {
        "name": "Gin and Tonic",
        "description": "British classic",
        "ingredients": "Gin, Tonic water, Lime wedge",
        "instructions": "Pour gin over ice. Top with tonic water. Garnish with lime."
    },
    {
        "name": "Whiskey Sour",
        "description": "Classic sour cocktail",
        "ingredients": "Bourbon, Lemon juice, Simple syrup, Egg white",
        "instructions": "Shake all ingredients with ice. Strain into a glass."
    },
    {
        "name": "Espresso Martini",
        "description": "Coffee cocktail",
        "ingredients": "Vodka, Coffee liqueur, Fresh espresso, Coffee beans",
        "instructions": "Shake all ingredients with ice. Strain into a glass. Garnish with coffee beans."
    },
    {
        "name": "Aperol Spritz",
        "description": "Italian aperitif",
        "ingredients": "Aperol, Prosecco, Soda water, Orange slice",
        "instructions": "Build in glass over ice. Garnish with orange slice."
    },
    {
        "name": "Moscow Mule",
        "description": "Vodka and ginger beer",
        "ingredients": "Vodka, Ginger beer, Lime juice, Mint",
        "instructions": "Build in copper mug over ice. Garnish with mint and lime."
    },
    {
        "name": "French 75",
        "description": "Champagne cocktail",
        "ingredients": "Gin, Champagne, Lemon juice, Simple syrup",
        "instructions": "Shake gin, lemon juice, and syrup. Top with champagne."
    },
    {
        "name": "Gimlet",
        "description": "Classic gin cocktail",
        "ingredients": "Gin, Lime juice, Simple syrup",
        "instructions": "Shake all ingredients with ice. Strain into a glass."
    },
    {
        "name": "Dark and Stormy",
        "description": "Rum and ginger beer",
        "ingredients": "Dark rum, Ginger beer, Lime juice",
        "instructions": "Build in glass over ice. Garnish with lime."
    },
    {
        "name": "Paloma",
        "description": "Mexican tequila cocktail",
        "ingredients": "Tequila, Grapefruit soda, Lime juice, Salt",
        "instructions": "Build in glass over ice. Garnish with lime and salt rim."
    },
    {
        "name": "Tom Collins",
        "description": "Classic gin cocktail",
        "ingredients": "Gin, Lemon juice, Simple syrup, Soda water",
        "instructions": "Shake gin, lemon juice, and syrup. Top with soda water."
    },
    {
        "name": "Boulevardier",
        "description": "Whiskey Negroni",
        "ingredients": "Bourbon, Campari, Sweet vermouth, Orange peel",
        "instructions": "Stir all ingredients with ice. Strain into a glass."
    },
    {
        "name": "Sazerac",
        "description": "New Orleans classic",
        "ingredients": "Rye whiskey, Absinthe, Peychaud's bitters, Sugar",
        "instructions": "Rinse glass with absinthe. Stir remaining ingredients with ice."
    },
    {
        "name": "Mai Tai",
        "description": "Tiki classic",
        "ingredients": "White rum, Dark rum, Orange curaçao, Lime juice, Orgeat",
        "instructions": "Shake all ingredients with ice. Strain into a glass."
    },
    {
        "name": "Pisco Sour",
        "description": "Peruvian classic",
        "ingredients": "Pisco, Lime juice, Simple syrup, Egg white, Angostura bitters",
        "instructions": "Shake all ingredients with ice. Strain into a glass."
    },
    {
        "name": "Penicillin",
        "description": "Modern classic",
        "ingredients": "Blended scotch, Islay scotch, Lemon juice, Honey syrup, Ginger syrup",
        "instructions": "Shake all ingredients with ice. Strain into a glass."
    },
    {
        "name": "Paper Plane",
        "description": "Modern classic",
        "ingredients": "Bourbon, Aperol, Amaro Nonino, Lemon juice",
        "instructions": "Shake all ingredients with ice. Strain into a glass."
    },
    {
        "name": "Last Word",
        "description": "Classic equal parts",
        "ingredients": "Gin, Green Chartreuse, Maraschino liqueur, Lime juice",
        "instructions": "Shake all ingredients with ice. Strain into a glass."
    },
    {
        "name": "Corpse Reviver No.2",
        "description": "Classic equal parts",
        "ingredients": "Gin, Lillet Blanc, Cointreau, Lemon juice, Absinthe",
        "instructions": "Shake all ingredients with ice. Strain into a glass."
    },
    {
        "name": "Aviation",
        "description": "Classic gin cocktail",
        "ingredients": "Gin, Maraschino liqueur, Crème de violette, Lemon juice",
        "instructions": "Shake all ingredients with ice. Strain into a glass."
    },
    {
        "name": "Bee's Knees",
        "description": "Prohibition classic",
        "ingredients": "Gin, Honey syrup, Lemon juice",
        "instructions": "Shake all ingredients with ice. Strain into a glass."
    },
    {
        "name": "Gold Rush",
        "description": "Modern classic",
        "ingredients": "Bourbon, Honey syrup, Lemon juice",
        "instructions": "Shake all ingredients with ice. Strain into a glass."
    },
    {
        "name": "Naked and Famous",
        "description": "Modern equal parts",
        "ingredients": "Mezcal, Yellow Chartreuse, Aperol, Lime juice",
        "instructions": "Shake all ingredients with ice. Strain into a glass."
    },
    {
        "name": "Vieux Carré",
        "description": "New Orleans classic",
        "ingredients": "Rye whiskey, Cognac, Sweet vermouth, Bénédictine, Peychaud's bitters, Angostura bitters",
        "instructions": "Stir all ingredients with ice. Strain into a glass."
    },
    {
        "name": "South Side",
        "description": "Classic gin cocktail",
        "ingredients": "Gin, Lime juice, Simple syrup, Mint",
        "instructions": "Muddle mint with syrup. Shake with remaining ingredients. Strain into a glass."
    },
    {
        "name": "French Gimlet",
        "description": "Modern classic",
        "ingredients": "Gin, St. Germain, Lime juice",
        "instructions": "Shake all ingredients with ice. Strain into a glass."
    },
    {
        "name": "Industry Sour",
        "description": "Modern classic",
        "ingredients": "Fernet Branca, Lime juice, Simple syrup",
        "instructions": "Shake all ingredients with ice. Strain into a glass."
    },
    {
        "name": "Ti' Punch",
        "description": "Martinique classic",
        "ingredients": "Rhum agricole, Lime, Cane syrup",
        "instructions": "Muddle lime with syrup. Add rum and stir."
    },
    {
        "name": "Pisco Punch",
        "description": "San Francisco classic",
        "ingredients": "Pisco, Pineapple, Lemon, Sugar, Water",
        "instructions": "Mix all ingredients and let sit. Strain and serve."
    },
    {
        "name": "Brandy Crusta",
        "description": "New Orleans classic",
        "ingredients": "Cognac, Curaçao, Lemon juice, Angostura bitters, Sugar",
        "instructions": "Shake all ingredients with ice. Strain into a glass with sugar rim."
    },
    {
        "name": "Champagne Cocktail",
        "description": "Classic",
        "ingredients": "Champagne, Sugar cube, Angostura bitters, Cognac, Lemon twist",
        "instructions": "Soak sugar cube in bitters. Add cognac and top with champagne."
    },
    {
        "name": "Mint Julep",
        "description": "Kentucky classic",
        "ingredients": "Bourbon, Mint, Sugar, Water",
        "instructions": "Muddle mint with sugar and water. Add bourbon and crushed ice."
    },
    {
        "name": "Scofflaw",
        "description": "Prohibition classic",
        "ingredients": "Gin, Dry vermouth, Grenadine, Pomegranate juice",
        "instructions": "Shake all ingredients with ice. Strain into a glass."
    },
    {
        "name": "Monte Carlo",
        "description": "Whiskey variation",
        "ingredients": "Rye whiskey, Bénédictine, Angostura bitters",
        "instructions": "Stir all ingredients with ice. Strain into a glass."
    },
    {
        "name": "Remember the Maine",
        "description": "Classic variation",
        "ingredients": "Rye whiskey, Sweet vermouth, Cherry Heering, Absinthe",
        "instructions": "Stir all ingredients with ice. Strain into a glass."
    },
    {
        "name": "Trident",
        "description": "Modern classic",
        "ingredients": "Aquavit, Dry sherry, Cynar, Peach bitters",
        "instructions": "Stir all ingredients with ice. Strain into a glass."
    },
    {
        "name": "Division Bell",
        "description": "Modern classic",
        "ingredients": "Mezcal, Aperol, Yellow Chartreuse, Lime juice",
        "instructions": "Shake all ingredients with ice. Strain into a glass."
    },
    {
        "name": "Final Ward",
        "description": "Modern variation",
        "ingredients": "Rye whiskey, Green Chartreuse, Maraschino liqueur, Lemon juice",
        "instructions": "Shake all ingredients with ice. Strain into a glass."
    },
    {
        "name": "Saturn",
        "description": "Tiki classic",
        "ingredients": "Gin, Passion fruit syrup, Orgeat, Velvet falernum, Lemon juice",
        "instructions": "Shake all ingredients with ice. Strain into a glass."
    },
    {
        "name": "Corn 'n' Oil",
        "description": "Tiki classic",
        "ingredients": "Dark rum, Lime juice, Simple syrup, Blackstrap rum, Mint",
        "instructions": "Muddle mint with syrup. Add remaining ingredients and crushed ice."
    },
    {
        "name": "Painkiller",
        "description": "Tiki classic",
        "ingredients": "Dark rum, Pineapple juice, Orange juice, Cream of coconut, Nutmeg",
        "instructions": "Shake all ingredients with ice. Strain into a glass."
    },
    {
        "name": "Jungle Bird",
        "description": "Tiki classic",
        "ingredients": "Dark rum, Campari, Pineapple juice, Lime juice, Simple syrup",
        "instructions": "Shake all ingredients with ice. Strain into a glass."
    },
    {
        "name": "Three Dots and a Dash",
        "description": "Tiki classic",
        "ingredients": "Aged rum, Rhum agricole, Orange juice, Honey syrup, Falernum, Allspice dram",
        "instructions": "Shake all ingredients with ice. Strain into a glass."
    },
    {
        "name": "Zombie",
        "description": "Tiki classic",
        "ingredients": "Light rum, Gold rum, Dark rum, 151 rum, Donn's mix, Grenadine, Falernum, Absinthe, Angostura bitters",
        "instructions": "Shake all ingredients with ice. Strain into a glass."
    },
    {
        "name": "Hurricane",
        "description": "New Orleans classic",
        "ingredients": "Light rum, Dark rum, Passion fruit syrup, Orange juice, Lime juice, Simple syrup",
        "instructions": "Shake all ingredients with ice. Strain into a glass."
    },
    {
        "name": "Fog Cutter",
        "description": "Tiki classic",
        "ingredients": "Light rum, Gin, Vodka, Amontillado sherry, Orange juice, Lemon juice, Orgeat, Amaretto",
        "instructions": "Shake all ingredients with ice. Strain into a glass."
    },
    {
        "name": "Scorpion",
        "description": "Tiki classic",
        "ingredients": "Light rum, Brandy, Gin, Dry vermouth, Orange juice, Lemon juice, Orgeat",
        "instructions": "Shake all ingredients with ice. Strain into a glass."
    },
    {
        "name": "Navy Grog",
        "description": "Tiki classic",
        "ingredients": "Light rum, Gold rum, Dark rum, Lime juice, Simple syrup, Demerara syrup",
        "instructions": "Shake all ingredients with ice. Strain into a glass."
    },
    {
        "name": "Jet Pilot",
        "description": "Tiki classic",
        "ingredients": "Light rum, Gold rum, Dark rum, 151 rum, Lime juice, Grapefruit juice, Cinnamon syrup, Falernum, Allspice dram",
        "instructions": "Shake all ingredients with ice. Strain into a glass."
    }
]

def seed_database():
    db = SessionLocal()
    try:
        # Add cocktails to database
        for cocktail_data in cocktails:
            try:
                cocktail = CocktailDB(**cocktail_data)
                db.add(cocktail)
                db.commit()
                print(f"Added {cocktail.name} to database")
            except Exception as e:
                db.rollback()
                print(f"Error adding {cocktail_data['name']}: {str(e)}")
    finally:
        db.close()

if __name__ == "__main__":
    print("Seeding database...")
    seed_database()
    print("Seeding completed!") 