import json
import sys

filename = sys.argv[-1]

if filename == 'BitwardenJSON.py':
    print('Usage: python3 BitwardenJSON.py bitwarden_export_XXXXXXXXXXXXXX.json')
else:
    f = open("logins.txt", "w")
    with open(filename, 'r') as json_file:
        data = json.load(json_file)
        for p in data['items']:
            if 'login' in p:
                res = p['name'] + ': ' + p['login']['username'] + ' | ' + p['login']['password'] + '\n'
                f.write(str(res))
    print('Done!')
    f.close()