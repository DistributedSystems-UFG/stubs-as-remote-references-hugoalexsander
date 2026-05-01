from time     import sleep
from client   import *
from dbclient import *

if __name__ == "__main__":
    c1   = Client(PORTC1)
    dbC1 = DBClient(HOSTS, PORTS)
    dbC1.create()
    dbC1.appendData('Client 1')
    sleep(2)
    c1.sendTo(HOSTC2, PORTC2, dbC1)
