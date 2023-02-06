from fastapi import HTTPException
from datetime import datetime
import uuid

date_format='%Y/%m/%d %H:%M:%S'

def enum_checker(importantLevel : int, status: int, isQuery : bool):

    _implevel = importantLevel
    _status = status

    imp_bool = _implevel < 1 or _implevel > 3 
    sta_bool = _status < 1 or _status > 3

    if  (_implevel or not isQuery) and imp_bool :
        raise HTTPException(status_code= 400,detail ={'status': "Bad request", 'message': "Invalid importantLevel, importantLevel must be enum"} )
    if  (_status or not isQuery) and sta_bool:
        raise HTTPException(status_code= 400,detail ={'status': "Bad request", 'message': "Invalid status, status must be enum"} )

def date_format_checker(date : str):
    try:
        datetime.strptime(date,date_format)
    except Exception:
        raise HTTPException(status_code= 400,detail ={'status': "Bad request", 'message': "Invalid date input, date must be in format Y/m/d H:M:S"} )

def uuid_checker(id: str):
    try:
        uuid.UUID(id)
    except Exception:

        raise HTTPException(status_code=400, detail={'status': "Bad request", 'message': "Ids are not valid"})

