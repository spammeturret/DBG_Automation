import json

def load_json(file_path):
    with open(file_path, 'r') as my_data_file:
        dict={
            'path': file_path,
            'status': json.load(my_data_file)
        }
        return dict

def save_json(json_obj):
    #json_obj['status'][key] = value
    file_path = json_obj['path']
    with open(file_path, 'w') as json_file:
        print(json_obj['status'])
        json.dump(json_obj['status'], json_file)

# def save_dailyCompletions(key, value):
#     dailyCompletions[key] = value
#     with open(jsonDailyCompletions, 'w') as json_file:
#         json.dump(dailyCompletions, json_file)

# def save_questList(key, value):
#     questList[key] = value
#     with open(jsonQuestList, 'w') as json_file:
#         json.dump(questList, json_file)