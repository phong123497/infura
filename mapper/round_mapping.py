from datetime import datetime
from pathlib import Path
import os
round_times = [
    {'start': '06:30', 'end': '07:30', 'round': 1, 'morning': 0},
    {'start': '17:10', 'end': '18:10', 'round': 1, 'morning': 1},
    {'start': '07:30', 'end': '08:30', 'round': 2, 'morning': 0},
    {'start': '18:10', 'end': '19:10', 'round': 2, 'morning': 1},
    {'start': '08:40', 'end': '09:40', 'round': 3, 'morning': 0},
    {'start': '19:20', 'end': '20:20', 'round': 3, 'morning': 1},
    {'start': '09:40', 'end': '10:40', 'round': 4, 'morning': 0},
    {'start': '20:20', 'end': '21:20', 'round': 4, 'morning': 1},
    {'start': '11:30', 'end': '12:30', 'round': 5, 'morning': 0},
    {'start': '22:10', 'end': '23:10', 'round': 5, 'morning': 1},
    {'start': '12:30', 'end': '13:30', 'round': 6, 'morning': 0},
    {'start': '23:10', 'end': '23:59', 'round': 6, 'morning': 1}, 
    {'start': '00:00', 'end': '00:10', 'round': 6, 'morning': 1},
    {'start': '13:40', 'end': '14:40', 'round': 7, 'morning': 0},
    {'start': '00:20', 'end': '01:20', 'round': 7, 'morning': 1},
    {'start': '14:40', 'end': '15:10', 'round': 8, 'morning': 0},
    {'start': '01:20', 'end': '01:50', 'round': 8, 'morning': 1},
    {'start': '15:20', 'end': '16:20', 'round': 9, 'morning': 0},
    {'start': '02:00', 'end': '03:00', 'round': 9, 'morning': 1},
    {'start': '16:20', 'end': '17:09', 'round': 10, 'morning': 0},
    {'start': '03:00', 'end': '03:59', 'round': 10, 'morning': 1}
]
round_update_time =[
    {'time_input': '07:29', 'round_update': 1},
    {'time_input': '18:09', 'round_update': 1},
    {'time_input': '08:29', 'round_update': 1},
    {'time_input': '19:09', 'round_update': 1},
    {'time_input': '20:19', 'round_update': 1},
    {'time_input': '10:39', 'round_update': 1},
    {'time_input': '21:19', 'round_update': 1},
    {'time_input': '12:29', 'round_update': 1},
    {'time_input': '23:09', 'round_update': 1},
    {'time_input': '13:29', 'round_update': 1},
    {'time_input': '00:09', 'round_update': 1},
    {'time_input': '14:39', 'round_update': 1},
    {'time_input': '01:19', 'round_update': 1},
    {'time_input': '15:09', 'round_update': 1},
    {'time_input': '01:49', 'round_update': 1},
    {'time_input': '16:19', 'round_update': 1},
    {'time_input': '02:59', 'round_update': 1},
    {'time_input': '17:08', 'round_update': 1},
    {'time_input': '03:58', 'round_update': 1},
]
    
def round_and_is_morning_mapping(time_input: str):
    # change time input to time object
    time_obj = datetime.strptime(time_input, '%H:%M').time()
    
    round_number = 0
    is_morning = 0
    for time_range in round_times:
        start_time = datetime.strptime(time_range['start'], '%H:%M').time()
        end_time = datetime.strptime(time_range['end'], '%H:%M').time()
        # check time input is between start and end time
        if start_time <= time_obj < end_time:
            round_number = time_range['round']
            is_morning = time_range['morning']
            break  
        else:
            round_number, is_morning
            
    # print("round_number", round_number, "is_morning", is_morning)
    return round_number, is_morning

def check_round_update(time_input: str):
    time_obj = datetime.strptime(time_input, '%H:%M').time()

    for update in round_update_time:
        round_time = datetime.strptime(update['time_input'], '%H:%M').time()
        
        if time_obj == round_time:
            return 1  
    return 0


def get_round_times( round_number: int, is_morning: int) -> tuple:
        """
        Returns start and end times for a given round and shift
        """
        round_times = {
            (1, 0): ('06:30', '07:30'),
            (1, 1): ('17:10', '18:10'),
            (2, 0): ('07:30', '08:30'),
            (2, 1): ('18:10', '19:10'),
            (3, 0): ('08:40', '09:40'),
            (3, 1): ('19:20', '20:20'),
            (4, 0): ('09:40', '10:40'),
            (4, 1): ('20:20', '21:20'),
            (5, 0): ('11:30', '12:30'),
            (5, 1): ('22:10', '23:10'),
            (6, 0): ('12:30', '13:30'),
            (6, 1): ('23:10', '00:10'),
            (7, 0): ('13:40', '14:40'),
            (7, 1): ('00:20', '01:20'),
            (8, 0): ('14:40', '15:10'),
            (8, 1): ('01:20', '01:50'),
            (9, 0): ('15:20', '16:20'),
            (9, 1): ('02:00', '02:59'),
            (10, 0): ('16:20', '17:09'),
            (10, 1): ('03:00', '03:59'),
        }
        
        return round_times.get((round_number, is_morning))

# timestep = datetime.now().strftime("%H:%M")
# timestep = "07:30"
# print(timestep)
# # round_number, is_morning=  round_and_is_morning_mapping(timestep)
# round_update=  check_round_update(timestep)
# print(round_update )


# def csv_files_in_directory(directory):
#     files = list(Path(directory).glob("**/*.csv"))
#     for file_path in files:
#         length  = len(files)
#     print(length)
            
   
        
# dir_path = "C:\\Users\\nguyen-duy-phong\\Downloads\\infura_data\\0322andon\\新しいフォルダー\\Andon" 
# csv_files_in_directory(dir_path)

# def get_folder_round_name( ):
#     timenow = datetime.now().strftime("%H:%M")
#     print(timenow)
#     timenow = "18:52"
    
#     current_round_number = None
#     for round_time in round_times:
#         if round_time['start'] <= timenow <= round_time['end']:
#             current_round_number = round_time['round']
#             print(f"Current round: {current_round_number:02d}") 
#             break
#         else:
#             print ("kiuke")
    
# get_folder_round_name()