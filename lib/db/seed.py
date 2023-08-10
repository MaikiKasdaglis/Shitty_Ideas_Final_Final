from models import Shitty_Idea, Developer, Phase_3_Project
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':

    engine = create_engine('sqlite:///shitty.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    session.query(Shitty_Idea).delete()
    session.query(Developer).delete()
    session.query(Phase_3_Project).delete()
    session.commit()

    mikey = Developer(name = 'Mike')
    mark = Developer(name='Mark')
    cooper = Developer(name='Cooper')

    session.add_all([mikey, mark, cooper])
    session.commit()

    forced_many_to_many = Shitty_Idea(idea_name = 'forced many to many', idea_description= 'tried to force an unnatrual many to many relationship on a schema', shittiness_scale = 200)

    no_many_to_many = Shitty_Idea(idea_name = 'No many 2 many', idea_description= 'wanted to do a project on tables that had no many to many relationships', shittiness_scale = 5)

    no_proble_to_solve = Shitty_Idea(idea_name = 'No real problem', idea_description= 'came up with a solution without a problem', shittiness_scale = 78)


    session.add_all([forced_many_to_many,  no_many_to_many,  no_proble_to_solve])
    session.commit()

    liquor_inventory = Phase_3_Project(project_name = 'Liquor Inventory', fun_scale = 2, shitty_idea_id = forced_many_to_many.id, developer_id = mikey.id)

    sql_todo_list = Phase_3_Project(project_name = 'SQL Todo List', fun_scale = 8, shitty_idea_id =  no_many_to_many.id, developer_id = mark.id)

    left_sock_organizer = Phase_3_Project(project_name = 'Left Sock Orgaanizer', fun_scale = 1, shitty_idea_id =  no_proble_to_solve.id, developer_id = cooper.id)

    session.add_all([liquor_inventory,sql_todo_list, left_sock_organizer])
    session.commit()