from sqlalchemy import Column, Integer, String, ForeignKey, orm
from sqlalchemy.orm import relationship, backref

from app.models.base import Base


class Menu(Base):
    __tablename__ = 'menu'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    submenu = relationship('Submenu')

    @orm.reconstructor
    def __init__(self):
        self.fields = ['id', 'name', 'submenu']


