from enum import Enum

class Header(Enum):
    Form = {
        "Accept-Encoding": "gzip, deflate, br",
        "Accept": "*/*",
        "Content-Type": "application/x-www-form-urlencoded",        
    }
    Json = {
        "Accept-Encoding": "gzip, deflate, br",
        "Accept": "*/*",
        "Content-Type": "application/json",        
    }