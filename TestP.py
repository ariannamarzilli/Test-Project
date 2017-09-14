import sys
import json
import requests

args = sys.argv[1:]


#commits of the specified repository sorted by date
#results are splitted by pages of per_page elements each
r = requests.get('https://api.github.com/repos/'+str(args[0])+'/'+str(args[1])+'/commits?page=1&per_page=3')


if(r.ok): #response check

#deserialization of the string instance containing the JSON document to a Python object
  comItem = json.loads(r._content)

  if (len(comItem) == 3):

      #building of json object
      data ={'items' : [{'last commit':{'author': comItem[0]['commit']['author']}},
          {'3rd to last commit':{'author': comItem[2]['commit']['author']}}]}

      #serialization of the object to a JSON formatted string
      json_data = json.dumps(data, indent=4, sort_keys=True)

      print(json_data)

  else:

    data = {'items': [{'last commit': {'author': comItem[0]['commit']['author']}}]}
    json_data = json.dumps(data, indent=4, sort_keys=True)

    print(json_data)

    print('There is not 3rd to last commit')

else:

  print('Owner or Repository are not correct or Repository is empty')





