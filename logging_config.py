import logging
import logging.config
import os

# Define the log file path
log_file_path = os.path.join(os.path.dirname(__file__), 'logs.log')
if not os.path.exists(log_file_path):
    os.makedirs(log_file_path)
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
            'filename': log_file_path,
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
            'handlers': ['file', 'console'],
            'level': 'INFO',
            'propagate': True
        },
    }
}

# Apply the logging configuration
logging.config.dictConfig(logging_config)

# Get the root logger
logger = logging.getLogger() 



