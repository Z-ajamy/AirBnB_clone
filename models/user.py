#!/usr/bin/python3
from models.base_model import BaseModel

class User(BaseModel):
    def __init__(self, *args, **kwargs):
        if kwargs:
            for i in kwargs:
                if i == "__class__":
                    continue
                elif i == "created_at" or i == "updated_at":
                    setattr(self, i, datetime.fromisoformat(kwargs[i]))
                else:
                    setattr(self, i, kwargs[i])

        else:
            self.email = ""
            self.password = ""
            self.first_name = ""
            self.last_name = ""
            super().__init__()
            
