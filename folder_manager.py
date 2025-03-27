import os
from logging_config import logger
from datetime import datetime
from mapper.round_mapping import round_times
from pathlib import Path
import time
class FolderManager:
    def __init__(self, root_dir):
        self.root_dir = root_dir

    def check_folder_type(self):
        folder_categories = os.listdir(self.root_dir)
        expected_categories = ["SM", "ドア", "UB","Andon", "Ndai"]
        result_categories = []
        for category in folder_categories:
            if category in expected_categories:
                logger.info(f"Found category: {category}")
                result_categories.append(category)
            else:
                logger.warning(f"Unexpected category found: {category}. Skipping.")
                return None  # Or raise an exception if it's critical
        return result_categories

    def check_folder_round(self, category_name):
        category_name_path = os.path.join(self.root_dir, category_name)
        timenow = datetime.now().strftime("%H%M%S")
        # check time now between start time  and time end
        # round 1 => 10 
        folders = os.listdir(category_name_path)
        result_round = []
        for folder in folders:
            if "ラウンド" in folder:
                logger.info(f"Found round: {folder} in category {category_name}")
                result_round.append(folder)
            else:
                logger.warning(f"Unexpected folder found: {folder} in category {category_name}. Skipping.")
        return result_round
    
    def get_folder_round_name(self,root_dir,category_name):
        timenow = datetime.now().strftime("%H:%M")
        # timenow = "19:21"
        current_round_number = None
        for round_time in round_times:
            if round_time['start'] <= timenow < round_time['end']:
                current_round_number = round_time['round']
                print(f"Current round: {current_round_number:02d}") 
                break
            # else:
            #     print ("kiuke")
        
        # Tạo đường dẫn thư mục cho vòng
        current_round_number_formatted = f"{current_round_number:02d}"  
        round_now = f"ラウンド{current_round_number_formatted}"
        # round_now = "ラウンド01"
        # curren_path = os.path.join(root_dir, category_name, f"ラウンド{current_round_number_formatted}")
        # print(curren_path)
        
        return round_now
    
    def delete_csv_files_in_directory(self,  directory):
        try:
            path_round = directory
            files = list(Path(path_round).glob("**/*.csv"))
            for file_path in files:
                try:
                    # os.remove(file_path)
                    logger.info(f"Deleted file: {file_path}")
                    # length = len(files)
                except Exception as e:
                    logger.error(f"Error deleting file {file_path}: {e}", exc_info=True)
            # print(f"Number of CSV files in {path_round} for category {category_name}: {length}", category_name, length)
            time.sleep(1)
        except Exception as e:
            logger.error(f"Error listing files in directory {directory}: {e}", exc_info=True)
    def check_files_exist_in_category(self,root, category_name,round_num):
        if category_name in [ "UB", "ドア"]:  
            path_round = os.path.join(root, category_name, round_num)
            files = list(Path(path_round).glob("**/*.csv"))
            if len(files) < 6:  
                return  False#  number file must >6 
            else:
                return True
        elif category_name in ["Andon", "Ndai"]:  
            path_round = os.path.join(root, category_name)
            files = list(Path(path_round).glob("**/*.csv"))
            if len(files) < 1:
                return  False 
            else:
                return True
        elif category_name  == "SM":  
            if round_num == "ラウンド01":
                path_round = os.path.join(root, category_name, round_num)
                files = list(Path(path_round).glob("**/*.csv"))
                if len(files) <6:
                    return  False 
            return True
      