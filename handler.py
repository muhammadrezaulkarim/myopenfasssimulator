import sys
import time
import json

def get_stdin():
    # extract the lines
    req = ""
    for line in sys.stdin:
        req = req + line

    #convert the json representation into a python object
    json_req = json.loads(req)
    
    # extract key and value
    result = {"key": json_req["key"], "value": json_req["value"]}
    
    # serialize to a JSON formatted string 
    str_rep = json.dumps(result)
    print str_rep

if(__name__ == "__main__"):
    st = get_stdin()
    print 'Sleeping for 50 miliseonds!.'
    time.sleep(0.05)
    print 'Sleeping completed.'
