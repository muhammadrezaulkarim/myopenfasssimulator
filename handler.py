import sys
import time
import json
import logging

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)

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
    log.debug('Received Message: ' + str_rep)
    log.debug('Sleeping for 25 miliseonds!.')
    time.sleep(0.025)
    log.debug( 'Sleeping completed.')

if(__name__ == "__main__"):
    st = get_stdin()
