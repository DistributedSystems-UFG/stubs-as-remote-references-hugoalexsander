import pickle
from client   import *

if __name__ == "__main__":
    c2   = Client(PORTC2)
    data = c2.recvAny()
    dbC2 = pickle.loads(data)
    dbC2.appendData('Client 2')
    print(dbC2.getValue())
    c2.sendTo(HOSTS, PORTS, [STOP])
