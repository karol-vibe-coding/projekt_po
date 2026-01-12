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
    
    def get_by_id(self, user_id: int) -> Optional[dict]:
        if user_id in self._users:
            data = self._users[user_id]
            return {"id": user_id, "name": data["name"], "lastname": data["lastname"]}
        return None
    
    def create(self, name: str, lastname: str) -> dict:
        user_id = self._next_id
        self._users[user_id] = {"name": name, "lastname": lastname}
        self._next_id += 1
        return {"id": user_id, "name": name, "lastname": lastname}
    
    def update(self, user_id: int, name: str, lastname: str) -> Optional[dict]:
        self._users[user_id] = {"name": name, "lastname": lastname}
        if user_id >= self._next_id:
            self._next_id = user_id + 1
        return {"id": user_id, "name": name, "lastname": lastname}
    
