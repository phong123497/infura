from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from master import RoundMaster, IdMaster

# Tạo kết nối đến cơ sở dữ liệu
engine = create_engine('postgresql://postgres:12345@localhost:5432/test_db')
Session = sessionmaker(bind=engine)
session = Session()

def check_id_master_exists(id_master_id):
    # result = session.query(IdMaster).filter(IdMaster.id == id_master_id).first()
    stmt = select(IdMaster).where(IdMaster.id == id_master_id)
    id_master = session.execute(stmt).scalar_one_or_none()
    print("id_master", id_master)
    return stmt is not None

result = check_id_master_exists(1)
print(result)


