import logging
import logging.config
import os
import sys
from pathlib import Path
from util.helper import get_root_dir

root_dir = get_root_dir()

# Đường dẫn tệp log
log_file_path = root_dir / 'logs'  #

# Kiểm tra nếu thư mục logs không tồn tại, tạo mới
if not log_file_path.exists():
    log_file_path.mkdir(parents=True, exist_ok=True)

# Định nghĩa đường dẫn tệp log
log_file = log_file_path / 'logs.log'
# Define the logging configuration
logging_config = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
    },
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': log_file,
            'formatter': 'standard',
            'encoding': 'utf-8',
        },
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'standard',
        },
    },
    'loggers': {
        '': {  # root logger
            # 'handlers': ['file', 'console'],
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': True
        },
    }
}

# Apply the logging configuration
logging.config.dictConfig(logging_config)

# Get the root logger
logger = logging.getLogger() 



