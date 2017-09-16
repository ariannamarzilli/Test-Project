import sys
import json
import requests

args = sys.argv[1:]


try:
    # commits of the specified repository sorted by date
    # results are splitted by pages of per_page elements each
    r = requests.get('https://api.github.com/repos/'+str(args[0])+'/'+str(args[1])+'/commits?page=1&per_page=3')


    # deserialization of the string instance containing the JSON document to a Python object
    comItem = json.loads(r._content)

    if (r.ok): #response check


        if (len(comItem) == 3):

            # building of json object
            data = {'items': [{'last commit': {'author': comItem[0]['commit']['author']}},
                              {'3rd to last commit': {'author': comItem[2]['commit']['author']}}]}


        else:

            data = {'items': [{'last commit': {'author': comItem[0]['commit']['author']}}]}

            print('There is not 3rd to last commit')

        # serialization of the object to a JSON formatted string
        json_data = json.dumps(data, indent=4, sort_keys=True)

        print(json_data)


    else:

        print('Response http failed')
        print(comItem[u'message']) #message field of comItem contains type of error

except ConnectionError:

    print ('Connection issue.')

except:

    print('Unexpected error.')

