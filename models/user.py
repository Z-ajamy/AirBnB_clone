#!/usr/bin/python3
from models.base_model import BaseModel
from datetime import datetime

class User(BaseModel):

    email = ""
    password = ""
    first_name = ""
    last_name = ""
            
