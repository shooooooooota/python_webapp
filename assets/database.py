# coding: utf-8
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

import datetime
import os
import pandas as pd

# 今回絶対pathを使っている
databese_file = os.path.join(os.path.abspath(
    os.path.dirname(__file__)), 'data.db')

# どのデータベースを使っているのか
'''engine = create_engine('sqlite:///' + databese_file,
                       convert_unicode=True, echo=True) '''
#herokuにアップロードするので、このように変更
engine = create_engine(os.environ.get('DATABSE_URL') or 'sqlite:///' + databese_file,
                       convert_unicode=True, echo=True)

# 自動でコミット、自動で反映しますか？
db_session = scoped_session(
    sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=engine
    )
)
Base = declarative_base()
Base.query = db_session.query_property()


# データベースの初期化
def init_db():
    import assets.models
    Base.metadata.create_all(bind=engine)


def read_data():
    from assets import models
    df = pd.read_csv('assets/data.csv')

    # _dfは一行ずつとってくる
    for index, _df in df.iterrows():
        # date型への変更
        date = datetime.datetime.strptime(_df['date'], '%Y/%m/%d').date()
        row = models.Data(
            date=date, subscribers=_df['subscribers'], reviews=_df['reviews'])
        db_session.add(row)
    db_session.commit()
