import pickle
pickle_in=open("instances_dev.pickle","rb")
data=pickle.load(pickle_in)
for i in range(10):
    print(data[i])
