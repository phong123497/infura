# Database related constants
DB_CONFIG = {
    'HOST': 'localhost',
    'PORT': '5432',
    'DATABASE': 'test_db',
    'USER': 'postgres',
    'PASSWORD': '12345'
}

# Category names
CATEGORY_DOOR = "ドア"
CATEGORY_UB = "UB"
CATEGORY_SM = "SM"
CATEGORY_ANDON = "Andon"
CATEGORY_NDAI = "Ndai"

#  not 100 devide with column names 
DAISU = "daisu"
SHOKUSEI_YOBIDASHI = "shokusei_yobidashi"

# Categories requiring round number
UB_DOOR_SM_CATEGORIES = [CATEGORY_SM, CATEGORY_UB, CATEGORY_DOOR]
ALL_CATEGORIES = [CATEGORY_DOOR, CATEGORY_UB, CATEGORY_SM, CATEGORY_ANDON, CATEGORY_NDAI]

#  time work by 直　１日は２直
START_TIME_AM = "06:30:00"
END_TIME_AM  = "17:10:00"
END_TIME_PM = "03:10:00"

# Date format 
DATETIME_FORMAT = '%Y/%m/%d %H:%M'
TIME_FORMAT = '%H:%M'
DATE_FORMAT = '%Y%m%d'

# Default values
DEFAULT_DELETE_FLAG = 0 