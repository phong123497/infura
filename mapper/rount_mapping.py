from datetime import datetime

def round_and_is_morning_mapping(time_input: str):
    # change time input to time object
    time_obj = datetime.strptime(time_input, '%H:%M').time()
    
    round_number = 0
    is_morning = 0

    # define time mapping for each round
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
        {'start': '23:10', 'end': '00:10', 'round': 6, 'morning': 1},
        {'start': '13:40', 'end': '14:40', 'round': 7, 'morning': 0},
        {'start': '00:20', 'end': '01:20', 'round': 7, 'morning': 1},
        {'start': '14:40', 'end': '15:10', 'round': 8, 'morning': 0},
        {'start': '01:20', 'end': '01:50', 'round': 8, 'morning': 1},
        {'start': '15:20', 'end': '16:20', 'round': 9, 'morning': 0},
        {'start': '02:00', 'end': '03:00', 'round': 9, 'morning': 1},
        {'start': '16:20', 'end': '17:00', 'round': 10, 'morning': 0},
        {'start': '03:10', 'end': '06:10', 'round': 10, 'morning': 1}
    ]
    
    # extract start and end time for each round
    for time_range in round_times:
        start_time = datetime.strptime(time_range['start'], '%H:%M').time()
        end_time = datetime.strptime(time_range['end'], '%H:%M').time()

        # check time input is between start and end time
        if start_time <= time_obj <= end_time:
            round_number = time_range['round']
            is_morning = time_range['morning']
            break  
    print("round_number", round_number, "is_morning", is_morning)
    return round_number, is_morning


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
            (9, 1): ('02:00', '03:00'),
            (10, 0): ('16:20', '17:00'),
            (10, 1): ('03:10', '06:10'),
        }
        
        return round_times.get((round_number, is_morning))



# round_number, is_morning=  round_and_is_morning_mapping('00:30')
# round_times = get_round_times(round_number, is_morning)
# print(round_times)
