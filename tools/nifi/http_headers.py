from enum import Enum

class HttpHeader(Enum):
    FORM = {
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept': '*/*',
        'Content-Type': 'application/x-www-form-urlencoded',        
    }
    JSON = {
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept': '*/*',
        'Content-Type': 'application/json',        
    }