import redisco
from redis import *
from rcg import *

if __name__=='__main__':
	redisco.connection_setup(host='localhost',port=6379,db=0)
	prase = Prase("./201703122259_32094.rcg")
	prase.prase()