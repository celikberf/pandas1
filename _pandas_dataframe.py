import pandas as pd

list = [["Berf",50],["Guler",60],["Soner",50],["Zeynep",60]]
dict = {"Name" : ["Berf","Guler","Soner","Zeynep"],"Grade" : [50,60,70,80]}
dict_list = [
                {"Name" : "Berf","Grade": 50},
                {"Name" : "Guler","Grade": 60},
                {"Name" : "Soner","Grade": 70},
                {"Name" : "Zeynep","Grade": 40}
            ]

#df = pd.DataFrame()
#df = pd.DataFrame([1,2,3,4])
#df = pd.DataFrame(data,index = [1,2,3,4], columns=['Name','Grade'])
#df = pd.DataFrame(dict, index = ["212","245","123","432"])
df = pd.DataFrame(dict_list, index = ["212","245","123","432"])



print(df)


# s1 = pd.Series([3,2,0,1])
# s2 = pd.Series([0,3,7,2])

# data = dict(apples = s1, orange = s2)

# df = pd.DataFrame(data)

# print(df)

