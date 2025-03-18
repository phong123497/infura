
class BaseMapper:
    def map_to_model(self, row):
        raise NotImplementedError("Subclasses should implement this method")

    def map_common_fields(self, row, model_instance):
        # model_instance.id = row['id']
        model_instance.round = row['round_number']
        model_instance.round_update = row['round_update']
        model_instance.is_morning = row['is_morning']
        model_instance.year = row['year']
        model_instance.month = row['month']
        model_instance.day = row['day']
        model_instance.hour = row['hour']
        model_instance.minute = row['minute']
        model_instance.update_time = row['update_time']
        model_instance.delete_flag = row['delete_flag']
        return model_instance 

