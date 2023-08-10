from models import Shitty_Idea, Developer, Phase_3_Project
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
import inquirer 
import pyfiglet
import random





Black = "\033[30m"
Red = "\033[31m"
Green = "\033[32m"
Yellow = "\033[33m"
Blue = "\033[34m"
Magenta = "\033[35m"
Cyan = "\033[36m"
White = "\033[37m"
Reset = "\033[0m"


def make_an_idea():
    input1 = input(f'{Green}What do you want to name your idea?{Reset}')
    input2 = input(f'{Blue}What\'s shitty about your idea? {Reset}')
    input3 = int(input(f'{Yellow}On a scale of 1 to shitty, how shitty is your idea?{Reset}{Red}(This must be an integer. Ex. The wording here is about a 6000 on the shitty scale) {Reset}'))
    s1 = Shitty_Idea(idea_name=input1, idea_description=input2, shittiness_scale=input3)
    session.add(s1)
    session.commit()

def delete_an_idea():
    idea_list = session.query(Shitty_Idea).all()
    use_list = [idea.idea_name for idea in idea_list]
    use_list.append("Exit") 

    name = inquirer.list_input(f"{Yellow}Select an idea to delete:{Reset}", choices=use_list)

    if name == "Exit":
        return  
    
    for idea in idea_list:
        if idea.idea_name == name:
            session.delete(idea)
            session.commit()
            print(f"Idea '{idea.idea_name}' has been deleted.")
            break


def delete_a_project():
    project_list = session.query(Phase_3_Project).all()
    use_list = [project.project_name for project in project_list]
    use_list.append("Exit") 

    name = inquirer.list_input(f"{Yellow}Select a project to delete:{Reset}", choices=use_list)
    
    if name == "Exit":
        return  

    for project in project_list:
        if project.project_name == name:
            session.delete(project)
            session.commit()
            print(f"Project '{project.project_name}' has been deleted.")
            break

def delete_a_developer():
    developer_list = session.query(Developer).all()
    use_list = [developer.name for developer in developer_list]
    use_list.append("Exit")

    name = inquirer.list_input(f"{Yellow}Select a developer to delete:{Reset}", choices=use_list)

    if name == "Exit":
        return

    for developer in developer_list:
        if developer.name == name:
            session.delete(developer)
            session.commit()
            print(f"The developer '{developer.name}' has been deleted.")
            break
    else:
        print("Invalid developer name selected.")

def find_shittiest():
    max_shittiness_scale = session.query(Shitty_Idea).order_by(Shitty_Idea.shittiness_scale.desc()).first()
   
    list_of_shitty_projects = []
    
    all_projects = session.query(Phase_3_Project).all()
    for project in all_projects:
        if project.shitty_idea_id == max_shittiness_scale.id:
         list_of_shitty_projects.append(project)

    for project in list_of_shitty_projects:
        project_ima_use = project
        dev = session.query(Developer).filter_by(id = project.developer_id).all()
        for person in dev:
            if person.id == project.developer_id:
                use_person = person
        project_details = {
                "Project Name": White + project_ima_use.project_name + Reset,
                "Developer Name": Yellow + use_person.name + Reset,
                "Idea Description": White + max_shittiness_scale.idea_description + Reset,
                "Shittiness Scale": f'{White}  {max_shittiness_scale.shittiness_scale} {Reset}',
            }
        print(Blue + "PROJECT/S WITH THE HIGHEST SHITTINESS SCORE:\n" + Reset)
        for key, value in project_details.items():
            print(Magenta+ f"{key}: {value}\n"+ Reset)

def find_busy_body():
     all_projects = session.query(Phase_3_Project).all()
     project_counts= {}
     for project in all_projects:
         dev_id = project.developer_id
         project_counts[dev_id] = project_counts.get(dev_id, 0) +1
     most_proj_id = max(project_counts, key= project_counts.get)
    #  print('this is project_counts', project_counts)


     dev = session.query(Developer).filter_by(id = project.developer_id).all()
     for person in dev:
        # print('this is what i get back from most_proj_id', most_proj_id)
        if person.id == most_proj_id:
                # print('this is person.id', person.id)
        #  text = f'{Yellow}{person.name}{Reset}{Blue} worked on like {Reset}{Yellow}{project_counts[person.id]} {Reset}{Blue}shitty projects.  They must be hella tired. {Reset}'
        #  font_style = 'acrobatic'
        #  print(pyfiglet.figlet_format(text, font = font_style))
         print(f'{Yellow}{person.name}{Reset}{Blue} worked on like {Reset}{Yellow}{project_counts[person.id]} {Reset}{Blue}shitty projects.  They must be hella tired. {Reset}')

def most_fun():
    all_projects = session.query(Phase_3_Project).all()
    fun_scores = {}
    for project in all_projects:
        name = project.project_name
        fun_scores[name] = project.fun_scale

    sorted_scores = sorted(fun_scores.items(), key=lambda x: x[1], reverse=True)
    for item in sorted_scores:
        print(f'{Cyan}{item[0]}{Reset}, is a {Yellow}{item[1]}{Reset} on the fun scale. Now that sounds fun! Weeeeeeeeee! 🥳')

        
inCli = True

if __name__ == '__main__':
    engine = create_engine('sqlite:///shitty.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    # while inCli:
    text = 'Welcome to my CLI'
    font_style = 'slant'
    print(pyfiglet.figlet_format(text, font = font_style), f"""{Red}
                                                            *%#                                    
                                                #%%                                    
                            .                 =%%=                                    
                            #%#               =%%+                                     
                            #%%              .%%*                                      
                            =%%=              -%%-                                      
                            =%%+               .%%+         ..                           
                        :%%*                 .:         =%%.                          
                        =%%:            ..              +%%.                          
                        :%%+        :=*%%%=            :%%*                           
                            :-.     -+%%%*=*%%:          :%%*                            
                                +%%%+:    #%%:         %%#                             
                                -%%#-        *%%=       .%%+                             
                            =%%+           =%%#:      #%%                             
                            %%#             .*%%*-     :.                             
                            :=*%%%%###%%%#-      .+%%%*-                                 
                        =%%%*=----------          :+#%%*-                              
                        .#%%=                          :+%%#-                            
                        #%#.                              =%%#.                          
                    -%%-                                .*%%:                         
                    -%%:                                  #%%                         
                    .%%+                                  -%%-                        
                        *%%+============-     .======:       +%%:                        
                    :*%%%%##############.    =######+       *%%%*:                      
                    *%%+:                                      :+%%*.                    
                *%%:                                          .%%#                    
                .%%+                                            =%%:                   
                .%%*                                            +%%:                   
::                 +%%=                                          -%%*                    
::                  =%%#=:....................................:=#%%+                     
.:                   .=*%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#=.                      
.:                       .::::::::::::::::::::::::::::::::::::.                         
            {Reset}""")

    prompt = input(Yellow + "Enter your name to login: \n" + Reset)
    existing_developer = session.query(Developer).filter_by(name=prompt).first()

    if existing_developer:
        print(f"{Cyan}Welcome back {White}{prompt}{Reset}{Cyan}, can't wait to hear even more of your 💩💩💩 ideas!{Reset}")
        
    else:
        d1 = Developer(name=prompt)
        session.add(d1)
        session.commit()
        print("New here, huh?! Stoked to hear alllll your 💩💩💩  ideas.")

    while inCli:
# ====================THIS IS WHERE I'D LIKE TO RETURN AFTER ENTRIES ARE MADE=====================


        first_choice = input(f'''
                    {Yellow} May as well get started, {Green}{prompt}{Reset} {White} (i bet you like how i'm interpolating your name, which is {Green}{prompt}{Reset}, all over this joint.) \n {Reset}
        {Blue} Choose an option out of the below choices: {Reset}
        
        {White}1.{Reset}{Green} Create a 💩💩💩 idea
        {White}2.{Reset}{Green} Delete a 💩💩💩 idea {Reset}{Red} (turned out to be a good idea){Reset}
     
        {White}3.{Reset}{Blue} Create a phase 3 project
        {White}4.{Reset}{Blue} Delete a phase 3 project
        {Reset}
        {White}5.{Reset}{Yellow} Find the project/s based on the shittiest ideas.
        {White}6.{Reset}{Yellow} Find the Developer w/ the most projects. 
        {White}7.{Reset}{Yellow} Show me all the projects in a list from most fun to least fun.
        {Reset}
        {White}8.{Reset}{Red} Want to see a Tuple? It helps us hit the MVP. 
        {Reset}
        {White}9.{Reset}{Magenta} Delete Developer{Reset}
        {White}10.{Reset}{Magenta} Exit the system{Reset}
        ''' )

        if first_choice == "1":
            make_an_idea()


        if first_choice == "2":
            delete_an_idea()

        if first_choice == "3":
            idea_list = session.query(Shitty_Idea).all()
            use_list = [idea.idea_name for idea in idea_list]
            use_list.append(f"{Blue}I'D ACTUALLY RATHER CREATE AN IDEA. THE IDEA TO PICK AN IDEA HERE IS SHITTY{Reset}")

            input1 = input(f'{White}What do you want to name your project?{Reset} ')
            input2 = input(f'{White}On a scale of 1 to fun, how fun do you think your project is gonna be?{Reset}{Red} (must be an integer. dumb wording, i know.){Reset}')
            input3 = None

            name = inquirer.list_input("Shitty ideas:", choices=use_list)
            if name == "I'D ACTUALLY RATHER CREATE AN IDEA. THE IDEA TO PICK AN IDEA HERE IS SHITTY":
                make_an_idea()
                idea_list = session.query(Shitty_Idea).all()
                use_list = [idea.idea_name for idea in idea_list]

            for idea in idea_list:
                if idea.idea_name == name:
                    input3 = idea.id

            p1 = Phase_3_Project(project_name=input1, fun_scale=input2, shitty_idea_id=input3, developer_id=existing_developer.id)
            if p1.shitty_idea_id == None:
                break
            session.add(p1)
            session.commit()

        if first_choice == "4":
            delete_a_project()

        if first_choice == "5":
            find_shittiest()

        if first_choice == "6":
            find_busy_body()
        
        if first_choice == "7":
            most_fun()

        if first_choice == "8":
            text = 'The Magic of Tuples'
            font_style = 'slant'
            print(pyfiglet.figlet_format(text, font = font_style))
            
            print(f"""
{Green}A simple use case of a tuple in Python is to represent an ordered collection of related values that are immutable (cannot be changed). Here's an example:{Reset}

{White}person = ("John", 25, "USA"){Reset}
In this example, the tuple person represents information about a person. Each element in the tuple corresponds to a different piece of information, such as the person's name, age, and country.

{Green}You can access individual elements of a tuple using indexing, just like you would with a list:{Reset}

{White}name = person[0]
age = person[1]
country = person[2]{Reset}
{Green}Tuples are useful when you want to group related data together that should not be modified. They can also be used for functions that need to return multiple values.

Since tuples are immutable, you cannot change the values stored in a tuple. If you need to modify the data, you would need to create a new tuple with the updated values.{Reset}
""")
            tuple1 = ('This', 'is', 'literally', 'being', 'printed', 'from', 'a', 'tuple.', 'NAILED', 'THE', 'MVP!!!', 'LETS GO! 🙌')
            for word in tuple1:
                color_list = [Red, Green,Yellow, Blue ,Magenta, Cyan ,White]
                random_color = random.choice(color_list)
                print(f'{random_color}{word}{Reset}')

        if first_choice == "9":
            delete_a_developer()    

        if first_choice == "10":
            inCli = False