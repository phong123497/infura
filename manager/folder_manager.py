import os
from datetime import datetime
import time
from .logging_config import logger
from pathlib import Path
from util.round_relate import round_times
from util.constants import (CATEGORY_DOOR, CATEGORY_UB, CATEGORY_SM, CATEGORY_ANDON, CATEGORY_NDAI,
                       ALL_CATEGORIES, TIME_FORMAT, DATE_FORMAT)
class FolderManager:
    def __init__(self, root_dir):
        self.root_dir = root_dir

    def check_category_type(self):
        folder_categories = os.listdir(self.root_dir)
        result_categories = []
        for category in folder_categories:
            if category in ALL_CATEGORIES:
                logger.info(f"Found category: {category}")
                result_categories.append(category)
            else:
                logger.warning(f"Unexpected category found: {category}. Skipping.")
        return result_categories

    
    def get_folder_round_name(self):
        timenow = datetime.now().strftime(TIME_FORMAT)
        current_round_number = None
        for round_time in round_times:
            if round_time['start'] <= timenow < round_time['end']:
                current_round_number = round_time['round']
                print(f"Current round: {current_round_number:02d}") 
                break
        current_round_number_formatted = f"{current_round_number:02d}"  
        round_now = f"ラウンド{current_round_number_formatted}"
        return round_now
    
    def delete_csv_files_in_directory(self, dir_category):
        try:
            files = list(Path(dir_category).glob("**/*.csv"))
            current_date = datetime.now().strftime(DATE_FORMAT)
            for file_path in files:
                if current_date  not in file_path.name:
                    continue
                try:
                    os.remove(file_path)
                    # logger.info(f"Deleted file: {file_path}")
                except Exception as e:
                    logger.error(f"Error deleting file {file_path}: {e}", exc_info=True)
            time.sleep(1)
        except Exception as e:
            logger.error(f"Error listing files in directory {dir_category}: {e}", exc_info=True)
    def check_files_exist_in_category(self,root, category_name,round_num):
        if category_name in [ CATEGORY_UB, CATEGORY_DOOR]:  
            path_round = os.path.join(root, category_name, round_num)
            files = list(Path(path_round).glob("**/*.csv"))
            if len(files) < 6:  
                return  False#  number file must >6 
            else:
                return True
        elif category_name in [CATEGORY_ANDON, CATEGORY_NDAI]:  
            path_round = os.path.join(root, category_name)
            files = list(Path(path_round).glob("**/*.csv"))
            if len(files) < 1:
                return  False 
            else:
                return True
        elif category_name  == CATEGORY_SM:  
            if round_num == "ラウンド01":
                path_round = os.path.join(root, category_name, round_num)
                files = list(Path(path_round).glob("**/*.csv"))
                if len(files) <6:
                    return  False 
            return True
      