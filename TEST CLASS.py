


data = [{"name": "Bob", "age": [23,34, {"dfs": [224, 234, "ewerwe"]}, 5344]}, {"name": "George", "age": 42}, {"name": "Max", "age": 20}]


for i in data:
    print(i)
    print(type(i))
    print(i.items())
    for key in i.keys():
        print(key)