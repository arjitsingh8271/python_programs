import pandas as pd   # here pd is aliases(short form) of pandas

#df = pd.read_csv("sec_bhavdata_full.csv")     # first file is present in the directory

#print(df)
#print(df.dtypes)      # print data type of each column 
#print(df.head)        # print first 5 row
#print(df.head(n=60))  # here n returns rows, print first 10 rows
#print(df.shape)       # print (rows, column)
#print(df.tail)        # print last row

# creat own data frame using Dictionary
creat_own = pd.DataFrame({"Name":["Arjit","Rahul","Ravi"],
	"Roll":[71,23,22],
	"Branch":["BCA","BBA","BSc"]})
print(creat_own)








