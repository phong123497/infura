from sqlalchemy import create_engine, delete , text ,inspect
from sqlalchemy.orm import sessionmaker
from enties.master_no_check import Base as MasterBase
from enties.base_model import BaseModel
from enties.door import DoorPageData1, DoorPageData2
from enties.under_body import UnderBodyPageData1, UnderBodyPageData2, UnderBodyPageData3
from enties.saimen import SmPageData1, SmPageData2
from enties.andon import AndonPageData
from enties.ndai import NdaiPageData


def init_database():
    # Create database engine
    engine = create_engine('postgresql://postgres:12345@localhost:5432/test_db')

    # Create a metadata object
    metadata = BaseModel.metadata

    # Create tables in the correct order
    MasterBase.metadata.create_all(engine)  
    BaseModel.metadata.create_all(engine) 

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        session.commit()
        print("Database tables created successfully!")
    except Exception as e:
        session.rollback()
        print(f"Error initializing database: {e}")
    finally:
        session.close()

def check_tables_exist():
    """Check if tables exist in the database"""
    engine = create_engine('postgresql://postgres:12345@localhost:5432/test_db')
    inspector = inspect(engine)
    
    existing_tables = inspector.get_table_names()
    
    for table in existing_tables:
        print(f"Table {table} exists")
       
def delete_tables():
    engine = create_engine('postgresql://postgres:12345@localhost:5432/test_db')
    MasterBase.metadata.drop_all(engine)  
    BaseModel.metadata.drop_all(engine)   
    inspector = inspect(engine)
    existing_tables = inspector.get_table_names()
    for table in existing_tables:
         if table in BaseModel.metadata.tables:
            BaseModel.metadata.tables[table].drop(engine)    
            print(f"Table {table} deleted")
    # print("All tables deleted successfully!")     

if __name__ == "__main__":
    
    # Initialize database
    print("\nInitializing database...")
    init_database()
    # Check existing tables
    print("Checking existing tables...")
    check_tables_exist()
    # delete all table 
    # delete_tables()
    





