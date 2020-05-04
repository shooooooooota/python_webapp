# coding: utf-8
from sqlalchemy import Column, Integer, DateTime, Date
#from .database import Baseを下のように変更した
from assets.database import Base
from datetime import datetime as dt

# Table情報


class Data(Base):
    # TableNameの設定
    __tablename__ = "data"
    # Column情報を設定する
    id = Column(Integer, primary_key=True)
    date = Column(Date, unique=False)
    subscribers = Column(Integer, unique=False)
    reviews = Column(Integer, unique=False)
    timestamp = Column(DateTime, default=dt.now())

    # 初期の情報
    # 4つの情報は同時に入れる必要がある
    def __init__(self, date=None, subscribers=None, reviews=None, timestamp=None):
        self.date = date
        self.subscribers = subscribers
        self.reviews = reviews
        self.timestamp = timestamp
