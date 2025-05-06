from sqlalchemy import Column, String, Integer, BigInteger, Enum, Text, TIMESTAMP
from sqlalchemy.sql import func
import enum

class CategoryEnum(enum.Enum):
    finished = "finished"
    semi_finished = "semi-finished"
    raw = "raw"

class UnitEnum(enum.Enum):
    mtr = "mtr"
    mm = "mm"
    ltr = "ltr"
    ml = "ml"
    cm = "cm"
    mg = "mg"
    gm = "gm"
    unit = "unit"
    pack = "pack"

