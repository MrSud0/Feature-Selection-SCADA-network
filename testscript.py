#python 3.5.2

from sklearn import preprocessing
import numpy as np
from scapy.all import *
from sklearn.feature_extraction import DictVectorizer
import pandas as pd


#loading the pcap file
x=rdpcap('datasetSmall.pcap')

#vec=DictVectorizer()

#
# raw=np.empty((len(x),),dtype=object )
#
# for i in range (0,len(x)):
#     tmp=bytes(x[i])
#     raw[i]=np.fromstring(tmp,dtype=np.uint8)



s={}
myFinalList= np.empty((x.__len__(), 0)).tolist()
count = 0
for pkt in x:

        #paket number
        print(count)
        i = 0
        while (pkt[i].name != pkt.lastlayer().name):
            print(pkt[i].name)
            # changing key on the dictionary according to each layer i.e
            k = 0
            keylist = list(pkt[i].fields.keys())
            for k in keylist:
                pkt[i].fields[pkt[i].name + '_' + k] = pkt[i].fields.pop(k, None)
            print(pkt[i].fields)
            i += 1


        #update the dictionary with the new keys
        for k in range(i-1):
            pkt[0].fields.update(pkt[k+1].fields)


        print(pkt.fields)
        #create a list of dictionaries
        myFinalList[count] = [pkt.fields for k in range(pkt.fields.__len__())]
        print(myFinalList[count])
        #create a series type object with pkt dictinaries
        s[count] = pd.Series(pkt.fields)
        count+=1




        ###testing####

        #flow control for testing
        #count += 1
        # if count ==1:
        #     break

        # for pkt in x:
        #     print(count)
        #     i = 0
        #     while (pkt[i].name != pkt.lastlayer().name):
        
