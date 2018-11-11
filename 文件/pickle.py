import pickle
age = ["Jich",18,[166,70]]
with open(r"test03.txt", 'wb') as f:
    pickle.dump(age,f)

with open(r"test03.txt", 'rb') as f:
    age = pickle.load(f)
    print(age)