from datetime import datetime


def search(search_data):
    Query = str(input("Enter Your Word:"))
    queryList = list(set(Query.lower().split()))

    t1 = datetime.now()

    if ('or' in queryList and 'and' not in queryList):
        queryList.remove('or')
        print ("Performing OR search for:" + ('\t').join(queryList))
        for data in search_data:
            for word in queryList:
                if word in data[1]:
                    found = True
                    print("Found At " + data[0]+" "+data[2]+" "+data[3] )
                    break
        if found == False:
                print ("None")
    else:
        if ('and' in queryList and 'or' not in queryList):
            queryList.remove('and')
        elif ('and' in queryList and 'or' in queryList):
            queryList.remove('and')
            queryList.remove('or')
        else:
            queryList = queryList
        print ("Performing AND search for:" + ('\t').join(queryList))
        for data in search_data:
            for word in queryList:
                if word not in data[1]:
                    flag = False
                    break
                else: flag = True
            if flag == True:
                found_once = True
                print("Found At " + data[0] +" "+data[2]+" "+data[3])
        if flag == False:
                print ("None")
    t2 = datetime.now()
    print("Execution time:", t2.microsecond-t1.microsecond)



##############################################################

import pickle

def read_data():
    raw_data = pickle.load(open("raw_data.pickle","rb"))
    return raw_data


#############################################################

import os
import shutil
import fnmatch
import pickle
import time
 
def get_traversal_data():
     traversal_data = []
     for dirpath, dirs, files in os.walk('E:\\h2h'):
          for single_file in files:
               filepath = os.path.abspath(os.path.join(dirpath, single_file))
               F = open(filepath,'r')
               data = F.read().replace('\n', ' ')
               modified = "Last Modified: "+ time.ctime(os.path.getmtime(filepath))
               size = "Size of file: "+str(os.path.getsize(filepath))
               tup = (filepath,data,modified,size)
               traversal_data.append(tup)
     pickle.dump(traversal_data,open("raw_data.pickle", "wb"))


     
###############################################################    


import data_load
import searcher
import indexer


def searchForContent():
    data_load.get_traversal_data()
    search_data = indexer.read_data()
    searcher.search(search_data)


searchForContent()





