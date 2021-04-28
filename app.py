import json
import re
import datetime

print("Crowd-Funding App")
print("Choose a number")
print("1- for Registeration")
print("2- for Login")
print("3- for Exit")
select = input("Enter Your Number: ")

new_user = {}
new_project = {}
isLoggedIn = False
isExists = False
author = ''

phone_regex = '^01[0125][0-9]{8}'
email_regix = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'

while True:
    if select == "1":
        print("Registeration")
        print("----------------")
        fname = input("Enter Your First Name : ")
        new_user["fname"] = fname

        lname = input("Enter Your Last Name : ")
        new_user["lname"] = lname

        while True:
            email = input("Enter Your Email : ")
            if re.search(email_regix,email):
                new_user["email"] = email
                break
            print("Email not valid try again")

        while True:
            password = input("Enter Your Password : ")
            confirm_password = input("Enter Confirm Password : ")
            if password == confirm_password:
                new_user["password"] = password
                break
            print("password not match try again")

        while True:
            phone = input("Enter Your Mobile Phone : ")
            if re.search(phone_regex,phone):
                new_user["phone"] = phone
                break
            print("Phone not valid try again")
       

        db = open("usersdb.json",'r')
        data = db.read()
        db.close()

        users = json.loads(data)
        users.append(new_user)

        db = open("usersdb.json",'w')
        db.write(json.dumps(users))
        db.close()

        break
    elif select == "2":
        print("Login")
        print("-------")

        email = input("Enter Your Email : ")
        password = input("Enter Your Password : ")

        db = open("usersdb.json",'r')
        data = db.read()
        db.close()

        users = json.loads(data)

        for user in users:

            if user['email'] == email and user['password'] == password:
                print("-------------------------------------------")
                print(f"Wellcome {user['fname']} {user['lname']}")
                print("-------------------------------------------")
                isLoggedIn = True
                author = user['email']

                print("Choose a number")
                print("1- for Create Project")
                print("2- for View All Projects")
                print("3- for Edit Project")
                print("4- for Delete Project")
                print("5- for Search for a Project using Date")
                print("6- for Exit")
                sub_menu_select = input("Enter Your Number : ")

                while True:
                    if sub_menu_select == "1":
                        print("Create Project")
                        print("----------------")
                        
                        print("--------------------------------")
                        title = input("Enter Project Title : ")
                        new_project["title"] = title

                        details = input("Enter Project Details : ")
                        new_project["details"] = details

                        total_target = input("Enter Project Total Target : ")
                        new_project["total_target"] = total_target

                        while True:
                            start_time = input("Enter Project Start Time : ")
                            try:
                                datetime.datetime.strptime(start_time, '%Y-%m-%d')
                                new_project["start_time"] = start_time
                                break
                            except ValueError:
                                print("Incorrect data format, should be YYYY-MM-DD")

                        while True:
                            end_time = input("Enter Project End Time : ")
                            try:
                                datetime.datetime.strptime(end_time, '%Y-%m-%d')
                                new_project["end_time"] = end_time
                                break
                            except ValueError:
                                print("Incorrect data format, should be YYYY-MM-DD")

                        new_project['auther'] = author

                        print("--------------------------------")

                        db = open("projectsdb.json",'r')
                        data = db.read()
                        db.close()

                        projects = json.loads(data)
                        projects.append(new_project)

                        db = open("projectsdb.json",'w')
                        db.write(json.dumps(projects))
                        db.close()

                        break
                    elif sub_menu_select == "2":
                        print("View All Projects")
                        print("-------------------")
                        db = open("projectsdb.json",'r')
                        data = db.read()
                        db.close()

                        projects = json.loads(data)

                        for project in projects:

                            print("----------------------------------")
                            print(f"Title: {project['title']}")
                            print(f"Details: {project['details']}")
                            print(f"Total Target: {project['total_target']}")
                            print(f"Start Time: {project['start_time']}")
                            print(f"End Time: {project['end_time']}")
                            print(f"Auther: {project['auther']}")
                            print("----------------------------------")

                        break
                    elif sub_menu_select == "3":
                        print("Edit Project")
                        print("---------------")
                        
                        project_title = input("Enter Project Title To Edit : ")

                        db = open("projectsdb.json",'r')
                        data = db.read()
                        db.close()

                        projects = json.loads(data)

                        for project in projects:
                            
                            if project['title'] == project_title and project['auther'] == author:
                                
                                isExists = True
                                
                                print("-----------------------------------------------------")
                                title = input("Enter New Title or press enter to skip it : ")
                                if title:
                                    project["title"] = title

                                details = input("Enter New Details or press enter to skip it : ")
                                if details:
                                    project["details"] = details

                                total_target = input("Enter New Total Target or press enter to skip it : ")
                                if total_target:
                                    project["total_target"] = total_target

                                start_time = input("Enter New Start Time or press enter to skip it : ")
                                if start_time:
                                    while True:
                                        try:
                                            datetime.datetime.strptime(start_time, '%Y-%m-%d')
                                            project["start_time"] = start_time
                                            break
                                        except ValueError:
                                            print("Incorrect data format, should be YYYY-MM-DD")

                                        start_time = input("Enter New Start Time or press enter to skip it : ")

                                        if not start_time:
                                            break

                                end_time = input("Enter New End Time or press enter to skip it : ")
                                if end_time:
                                    while True:
                                        try:
                                            datetime.datetime.strptime(end_time, '%Y-%m-%d')
                                            project["end_time"] = end_time
                                            break
                                        except ValueError:
                                            print("Incorrect data format, should be YYYY-MM-DD")

                                        end_time = input("Enter New End Time or press enter to skip it : ")

                                        if not end_time:
                                            break


                                print("-----------------------------------------------------")
                                
                                db = open("projectsdb.json",'w')
                                db.write(json.dumps(projects))
                                db.close()
                                print("Project Edited successfully")
                                break
                        
                        if isExists == False:
                            print("This Product Doesn't Exists")

                        break
                    elif sub_menu_select == "4":
                        print("Delete Project")
                        print("----------------")

                        project_title = input("Enter Project Title To Delete : ")

                        db = open("projectsdb.json",'r')
                        data = db.read()
                        db.close()

                        projects = json.loads(data)
                        
                        for index,project in enumerate(projects):
                            
                            if project['title'] == project_title and project['auther'] == author:
                                
                                isExists = True

                                projects.pop(index)

                                db = open("projectsdb.json",'w')
                                db.write(json.dumps(projects))
                                db.close()
                                print("Project Deleted successfully")
                                break

                        if isExists == False:
                            print("This Product Doesn't Exists")

                        break
                    elif sub_menu_select == "5":
                        print("Search for a Project using Start Date")
                        print("--------------------------------------")

                        while True:
                            project_start_date = input("Enter Project Start Date to Search : ")
                            try:
                                datetime.datetime.strptime(project_start_date, '%Y-%m-%d')

                                db = open("projectsdb.json",'r')
                                data = db.read()
                                db.close()

                                projects = json.loads(data)
                                
                                for project in projects:
                                    
                                    if project['start_time'] == project_start_date and project['auther'] == author:
                                        
                                        isExists = True

                                        print("----------------------------------")
                                        print(f"Title: {project['title']}")
                                        print(f"Details: {project['details']}")
                                        print(f"Total Target: {project['total_target']}")
                                        print(f"Start Time: {project['start_time']}")
                                        print(f"End Time: {project['end_time']}")
                                        print(f"Auther: {project['auther']}")
                                        print("----------------------------------")
                                        break

                            except ValueError:
                                print("Incorrect data format, should be YYYY-MM-DD")

                            if isExists == False:
                                print("This Product Doesn't Exists")
                                
                            break

                    elif sub_menu_select == "6":
                        break
        
        if isLoggedIn == False:
            print("your email or password not correct please try again")

        break
    elif select == "3":
        break
    else:
        select = input("Enter Your Number: ")
