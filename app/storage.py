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
    
    def patch(self, user_id: int, name: Optional[str] = None,
              lastname: Optional[str] = None) -> Optional[dict]:
        if user_id not in self._users:
            return None
        
        if name is not None:
            self._users[user_id]["name"] = name
        if lastname is not None:
            self._users[user_id]["lastname"] = lastname
        
        data = self._users[user_id]
        return {"id": user_id, "name": data["name"], "lastname": data["lastname"]}
    
    def delete(self, user_id: int) -> bool:
        if user_id in self._users:
            del self._users[user_id]
            return True
        return False
    
    def exists(self, user_id: int) -> bool:
        return user_id in self._users
    
    def clear(self) -> None:
        self._users.clear()
        self._next_id = 1
