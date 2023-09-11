from pydantic import Optional, List
from uuid import UUID, uuid4
from typing import Optional
from enum import Enum

class Gender(str,Enum):
    male='male'
    female='female'

class Role(str, Enum):
    admin = 'admin'
    user = 'user'
    student = 'student'

class User(Basemodel):
    id: Optional[UUID]=uuid4()
    first_name=str 
    last_name=str
    middle_name=Optional[str]
    gender: Gender
    roles: List[Role]