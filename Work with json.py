import json
from random import randint
from datetime import datetime





str_json = """
{
    "response": {
        "count": 32363,
        "items": [
            {
                "id": 287350527,
                "first_name": "Маша",
                "last_name": "Kargina",
                "photo_50": true
            },
            {
                "id": 341523166,
                "first_name": "Slava",
                "last_name": "Kholod",
                "photo_50": "https://pp.vk.me/...321/eTxKNQSJMuk.jpg"
            }
        ]
    }
}
"""
# this is string
print(type(str_json))

# we are doing dict
data = json.loads(str_json)
print(type(data))

# we are delete and add new items in dict
for i in data['response']['items']:
    del i['id']
    i['likes']=randint(100, 200)
    i['item'] = None
    i['now']= datetime.now().strftime('%d.%m.%y')
print(data['response']['items'])

# we are serialized dict from string(json)
new_json = json.dumps(data, indent=2)
print(type(new_json))
print(new_json)

print(json.loads(new_json))

# we are created new file and wrote string(json)
with open('file.json', 'w') as f:

    json.dump(data, f, indent=3)

# we are read the file and print string(json)
with open('file.json', 'r') as f:
    data = json.load(f)
print(type(data))


from string import ascii_lowercase
a = ascii_lowercase
count = 1
alphabet = {}
for i in a:
    alphabet[i] = count
    count +=1
print(alphabet)