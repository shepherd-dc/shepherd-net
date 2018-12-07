from sqlalchemy import Column, Integer, String, ForeignKey, orm
from sqlalchemy.orm import relationship

from app.models.base import Base


class Submenu(Base):
    __tablename__ = 'submenu'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    path = Column(String(50), nullable=False)
    pic = Column(String(50), nullable=False)
    mid = Column(Integer, ForeignKey('menu.id'))

    @orm.reconstructor
    def __init__(self):
        self.fields = ['id', 'name', 'path', 'pic']
