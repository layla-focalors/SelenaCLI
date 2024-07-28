import json

def JSON_READER(path):
    with open(path, 'r') as f:
        json_data = json.load(f)
    return json_data

def parser(user_input, lang):
    csplit = user_input.split(" ")
    if csplit[1] == "help" and lang == "English":
        data = JSON_READER('./data/language.json')["helps"][0]["output"]
        for i in data:
            print(i)
    elif csplit[1] == "modules" and lang == "English":
        data = JSON_READER('./data/language.json')["modules"][0]["output"]
        for i in data:
            print(i)
        if csplit[2] == "download":
            data = JSON_READER('./data/language.json')["downloads"][0]["output"]
            for i in data:
                print(i)