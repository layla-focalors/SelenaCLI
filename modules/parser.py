from modules import data

import locale
import json
import random

def get_system_language():
    lang, _ = locale.getdefaultlocale()
    return lang

def output_hello_message():
    with open('./data/language.json', 'r') as f:
        json_data = json.load(f)
    lang = get_system_language()
    if lang == "en_US":
        en = json_data["lang"][0]["hello_text"]
        for i in en:
            print(i)
        return json_data["lang"][0]["language"]
    elif lang == "ko_KR":
        en = json_data["lang"][1]["hello_text"]
        for i in en:
            print(i)
        return json_data["lang"][1]["language"]
    else:
        print("Sorry, This language is not supported now.")
        en = json_data["lang"][0]["hello_text"]
        for i in en:
            print(i)
        return json_data["lang"][0]["language"]
    return None

def Get_User_Input(lang):
    pass

def content():
    # hello text가 false인 경우 작성
    if data.Read_Env_Variables("PRINT_HELLO_SHELL") == "true":
        language = output_hello_message()
        Get_User_Input(language)
    elif data.Read_Env_Variables("PRINT_HELLO_SHELL") == "auto":
        number = random.randint(0, 1)
        if number == 0:
            language = output_hello_message()
            Get_User_Input(language)
        else:
            Get_User_Input()
    else:
        Get_User_Input()