from typing import Dict, Tuple
from datetime import datetime
from enties.master import IdMaster, RoundMaster

class MasterCache:
    def __init__(self):
        self._id_master_cache: Dict[str, IdMaster] = {}
        self._round_master_cache: Dict[Tuple[int, int], RoundMaster] = {}
        self.cache_timestamp = datetime.now()

    def get_id_master(self, table_name: str) -> IdMaster:
        return self._id_master_cache.get(table_name)

    def set_id_master(self, table_name: str, id_master: IdMaster):
        self._id_master_cache[table_name] = id_master

    def get_round_master(self, round_number: int, is_morning: int) -> RoundMaster:
        return self._round_master_cache.get((round_number, is_morning))

    def set_round_master(self, round_number: int, is_morning: int, round_master: RoundMaster):
        self._round_master_cache[(round_number, is_morning)] = round_master

    def clear_cache(self):
        self._id_master_cache.clear()
        self._round_master_cache.clear()
        self.cache_timestamp = datetime.now()

    def is_cache_valid(self, max_age_minutes: int = 30) -> bool:
        age = datetime.now() - self.cache_timestamp
        return age.total_seconds() / 60 < max_age_minutes