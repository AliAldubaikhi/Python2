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
