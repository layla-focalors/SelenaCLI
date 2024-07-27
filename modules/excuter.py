import os

def excute_command(command):
    try:
        os.system(command)
    except Exception as e:
        print(e)
        return False
    return True