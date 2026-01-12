from typing import Dict, List, Optional


class UserStorage:
    def __init__(self):
        self._users: Dict[int, dict] = {}
        self._next_id: int = 1
    
    def get_all(self) -> List[dict]:
        return [
            {"id": user_id, "name": data["name"], "lastname": data["lastname"]}
            for user_id, data in self._users.items()
        ]
