import sys
import time

def get_stdin():
    buf = ""
    for line in sys.stdin:
        buf = buf + line
    return buf

if(__name__ == "__main__"):
    st = get_stdin()
    print(st)
    print 'Sleeping for 50 miliseonds!.'
    time.sleep(0.05)
    print 'Sleeping completed.'
