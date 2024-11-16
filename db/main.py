## PlanCraft
## inceptive

import os
import ast

default_Presets = """
762132893530 : {
    'desp' : "",
    1 : "makeFile('main.cpp')",
    2 : "writeToFile('main.cpp', 'cout<<\"Hello World\"')",
},
"""


DB_folder = "ProjectMaker"
DB_name = "db.pmdb"
settings_name = "values.pmdb"



documents_path = os.path.expanduser("~/Documents")


def initDB(workDic):

    folder_path = os.path.join(documents_path, DB_folder)
    file_path = os.path.join(folder_path, DB_name)
    settings_path = os.path.join(folder_path, settings_name )

    os.makedirs(folder_path, exist_ok=True)

    with open(file_path, "w") as file:
        file.write(default_Presets)
    with open(settings_path, 'w') as file:
        file.write(workDic)



def getDB() :
    
    folder_path = os.path.join(documents_path, DB_folder)
    file_path = os.path.join(folder_path, DB_name)

    with open(file_path, "r") as file:
        content = file.read()

    db_data = ast.literal_eval("{" + content + "}")

    return db_data



def getUserValues():
    folder_path = os.path.join(documents_path, DB_folder)
    settings_path = os.path.join(folder_path, settings_name)

    with open(settings_path, "r") as file:
        content = file.read()
    
    values_data = eval("{" + content + "}")
    
    return values_data


