from sqlalchemy import ForeignKey, Column, Integer, String, MetaData, create_engine
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('sqlite:///shitty.db')
Session = sessionmaker(bind=engine)
session =Session()

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)

class Shitty_Idea(Base):
    __tablename__='shitty_ideas'

    id = Column(Integer(), primary_key=True)
    idea_name = Column(String())
    idea_description = Column(String())
    shittiness_scale = Column(Integer())

    phase_3_projects = relationship('Phase_3_Project', back_populates = 'shitty_idea')

    def __repr__(self):
        return f'<Shitty_Idea {self.idea_name}>'

class Developer(Base):
    __tablename__='developers'

    id = Column(Integer(), primary_key=True)
    name = Column(String())

    phase_3_projects = relationship('Phase_3_Project', back_populates = 'developer')

    def __repr__(self):
        return f'<Dev {self.name}>'
    
class Phase_3_Project(Base):
    __tablename__ = 'phase_3_projects'

    id = Column(Integer(), primary_key=True)
    project_name = Column(String())
    fun_scale = Column(Integer())
    shitty_idea_id = Column(Integer(), ForeignKey('shitty_ideas.id')) 
    developer_id = Column(Integer(), ForeignKey('developers.id')) 

    shitty_idea = relationship('Shitty_Idea', back_populates = 'phase_3_projects')
    developer = relationship('Developer', back_populates = 'phase_3_projects')