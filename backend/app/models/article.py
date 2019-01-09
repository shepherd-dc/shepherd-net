from sqlalchemy import Column, Integer, String, orm, Text

from app.models.base import Base


class Article(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    author = Column(String(30))
    content = Column(Text())
    column_id = Column(Integer)

    @orm.reconstructor
    def __init__(self):
        self.fields = ['id', 'title', 'author', 'content', 'column_id']
