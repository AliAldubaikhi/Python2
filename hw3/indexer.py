import pickle

def read_data():
    raw_data = pickle.load(open("raw_data.pickle","rb"))
    return raw_data


