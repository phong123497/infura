
class BaseMapper:
    def map_to_model(self, row):
        raise NotImplementedError("Subclasses should implement this method")

    def map_common_fields(self, row, model_instance):
        # model_instance.id = row['id']
        model_instance.round = row.get('round_number')
        model_instance.round_update = row.get('round_update')
        model_instance.is_morning = row.get('is_morning')
        model_instance.year = row.get('year')
        model_instance.month = row.get('month')
        model_instance.day = row.get('day')
        model_instance.hour = row.get('hour')
        model_instance.minute = row.get('minute')
        model_instance.update_time = row.get('update_time')
        model_instance.delete_flag = row.get('delete_flag')
        return model_instance 

