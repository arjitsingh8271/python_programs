import pandas as pd  # here pd is aliases(short form) of pandas

abc = pd.DataFrame({"Name":["Arjit","Prakash","Raju"],
"Roll":[71,34,66],
"Branch":["BCA","Electrical","Mechanical"]})

# abc.loc[len(abc.index)] = ["Ankit", 33, "BBA"]
abc.loc[3] = ["Ankit", 33, "BBA"]

print(abc.index)