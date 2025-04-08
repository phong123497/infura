from sqlalchemy import create_engine ,inspect
from sqlalchemy.orm import sessionmaker
from enties.master import Base as MasterBase
from enties.base_model import BaseModel
from enties.door import DoorPageData1, DoorPageData2
from enties.under_body import UnderBodyPageData1, UnderBodyPageData2, UnderBodyPageData3
from enties.saimen import SmPageData1, SmPageData2
from enties.andon import AndonPageData
from enties.ndai import NdaiPageData
from .helper import connect_string



def init_tables():
    # Create database engine
    connection_string = connect_string()
    engine = create_engine(connection_string)

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


def test_connection():
    
    try:
        connection_string = connect_string()
        engine = create_engine(connection_string)

        with engine.connect() as connection:
            print("Connected to the database successfully!")
            return True
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return False


def check_tables_exist():
    """Check if tables exist in the database"""
    connection_string = connect_string()
    engine = create_engine(connection_string)
    inspector = inspect(engine)

    existing_tables = inspector.get_table_names()
    
    for table in existing_tables:
        print(f"Table {table} exists")
    return existing_tables 
def delete_tables():
    connection_string = connect_string()
    engine = create_engine(connection_string)
    MasterBase.metadata.drop_all(engine)  
    BaseModel.metadata.drop_all(engine)   
    inspector = inspect(engine)
    existing_tables = inspector.get_table_names()
    for table in existing_tables:
         if table in BaseModel.metadata.tables:
            BaseModel.metadata.tables[table].drop(engine)    
            print(f"Table {table} deleted")

if __name__ == "__main__":
    
    # Initialize database
    # print("\nInitializing database...")
    # init_database()
    # # Check existing tables
    # print("Checking existing tables...")
    # check_tables_exist()
    # delete all table 
    # delete_tables()
    test_connection = test_connection()





