from dataclasses import dataclass
from enum import Enum


class Gender(Enum):
    MALE = "Male"
    FEMALE = "Female"
    OTHER = "Other"

class Hobbies(Enum):
    SPORTS = ("Sports", '1')
    READING = ("Reading", '2')
    MUSIC = ("Music", '3')

@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: Gender
    phone_number: str
    date_of_birth_year: int
    date_of_birth_month: str
    date_of_birth_day: int
    subject: str
    hobbies: list[Hobbies]
    picture: str
    address: str
    state: str
    city: str
