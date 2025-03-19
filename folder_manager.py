import os
from logging_config import logger

class FolderManager:
    def __init__(self, root_dir):
        self.root_dir = root_dir

    def check_folder_type(self):
        folder_categories = os.listdir(self.root_dir)
        expected_categories = ["SM", "ドア", "UB"]
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
        folders = os.listdir(category_name_path)
        result_round = []
        for folder in folders:
            if "ラウンド" in folder:
                logger.info(f"Found round: {folder} in category {category_name}")
                result_round.append(folder)
            else:
                logger.warning(f"Unexpected folder found: {folder} in category {category_name}. Skipping.")
        return result_round