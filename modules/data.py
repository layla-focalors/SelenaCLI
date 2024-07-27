from dotenv import load_dotenv

import getpass
import uuid
import os

def CreateUUID():
    return uuid.uuid4()

def Read_Env_Variables(key):
    load_dotenv("./data/settings.env") 
    return os.environ.get(key)

def Get_System_Name():
    return getpass.getuser()