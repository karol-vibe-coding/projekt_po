from typing import Dict, List


class UserStorage:
    def __init__(self):
        self._users: Dict[int, dict] = {}
        self._next_id: int = 1
