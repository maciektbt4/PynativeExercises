employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

dictionary = {}

for key in employees:
    dictionary[key] = defaults

print(dictionary)

print(dictionary["Kelly"]["salary"])