from sqlalchemy import create_engine, delete
from sqlalchemy.orm import sessionmaker
from master_no_check import Base as MasterBase
from door import DoorPageData1,DoorPageData2
from under_body import UnderBodyPageData1,UnderBodyPageData2, UnderBodyPageData3
from base_model import BaseModel
from datetime import datetime, time
from sqlalchemy import inspect
from sqlalchemy.schema import (
    DropTable,
)
def init_database():
    # Create database engine
    engine = create_engine('postgresql://postgres:12345@localhost:5432/demo1')

    # Create all tables except door, under_body, saimen
    MasterBase.metadata.create_all(engine)  
    BaseModel.metadata.create_all(engine)   

    # Exclude door, under_body, saimen tables from creation
    tables_to_exclude = ['door_page_data1', 'door_page_data2',
                         'under_body_page_data1', 'under_body_page_data2', 'under_body_page_data3',
                         'sm_page_data1', 'sm_page_data2']
    for table_name in tables_to_exclude:
        if table_name in BaseModel.metadata.tables:
            BaseModel.metadata.tables[table_name].create(engine, checkfirst=True)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        # Initialize master data if needed
        # init_master_data(session)
        session.commit()
        print("Database tables created successfully!")
    except Exception as e:
        session.rollback()
        print(f"Error initializing database: {e}")
    finally:
        session.close()

def init_master_data(session):
    """Initialize master data with default values"""
    from master_no_check import IdMaster, RoundMaster

    # Initialize id_master with default values
    default_tables = [
        'door_page_data1', 'door_page_data2',
        'under_body_page_data1', 'under_body_page_data2', 'under_body_page_data3',
        'sm_page_data1', 'sm_page_data2'
    ]

    for table_name in default_tables:
        id_master = IdMaster(
            table_name=table_name,
            created_at=datetime.now(),
            delete_flag=False
        )
        session.add(id_master)

    # Initialize round_master with default values
    round_times = [
        (1, time(6, 30), time(7, 30), 0),
        (1, time(17, 10), time(18, 10), 1),
        (2, time(7, 30), time(8, 30), 0),
        (2, time(18, 10), time(19, 10), 1),
        (3, time(8, 40), time(9, 40), 0),
        (3, time(19, 20), time(20, 20), 1),
        (4, time(9, 40), time(10, 40), 0),
        (4, time(20, 20), time(21, 20), 1),
        (5, time(11, 30), time(12, 30), 0),
        (5, time(22, 10), time(23, 10), 1),
        (6, time(12, 30), time(13, 30), 0),
        (6, time(23, 10), time(0, 10), 1),
        (7, time(13, 40), time(14, 40), 0),
        (7, time(0, 20), time(1, 20), 1),
        (8, time(14, 40), time(15, 10), 0),
        (8, time(1, 20), time(1, 50), 1),
        (9, time(15, 20), time(16, 20), 0),
        (9, time(2, 0), time(3, 0), 1),
        (10, time(16, 20), time(17, 0), 0),
        (10, time(3, 10), time(6, 10), 1)
    ]

    for round_num, start, end, is_morning in round_times:
        round_master = RoundMaster(
            round_number=round_num,
            start_time=start,
            end_time=end,
            is_morning=is_morning,
            delete_flag=False,
            update_time=datetime.now()
        )
        session.add(round_master)

def check_tables_exist():
    """Check if tables exist in the database"""
    engine = create_engine('postgresql://postgres:12345@localhost:5432/demo1')
    inspector = inspect(engine)
    
    master_tables = ['id_master', 'round_master', 'parameter_master']
    data_tables = ['door_page_data1', 'door_page_data2', 
                  'under_body_page_data1', 'under_body_page_data2', 'under_body_page_data3',
                  'sm_page_data1', 'sm_page_data2']
    
    all_tables = master_tables + data_tables
    existing_tables = inspector.get_table_names()
    
    for table in all_tables:
        if table in existing_tables:
            print(f"Table {table} exists")
        else:
            print(f"Table {table} does not exist")
def delete_tables():
    engine = create_engine('postgresql://postgres:12345@localhost:5432/fm')
    MasterBase.metadata.drop_all(engine)  
    BaseModel.metadata.drop_all(engine)   
    inspector = inspect(engine)
    existing_tables = inspector.get_table_names()
    # tables_to_exclude = ['door_page_data1', 'door_page_data2',
    #                      'under_body_page_data1', 'under_body_page_data2', 'under_body_page_data3',
    #                      'sm_page_data1', 'sm_page_data2']

    for table in existing_tables:
         if table in BaseModel.metadata.tables:
            BaseModel.metadata.tables[table].drop(engine)

if __name__ == "__main__":
    # Check existing tables
    # print("Checking existing tables...")
    # check_tables_exist()
    
    # # Initialize database
    # print("\nInitializing database...")
    # init_database()
    
    # delete all table 
    delete_tables()
    





