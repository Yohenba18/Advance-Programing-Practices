dict = [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'},
{'make': 'Samsung', 'model': 7, 'color': 'Blue'}]

print("orignal: ")
print(dict)

print("\n")

sort_dict = sorted(dict, key = lambda x: x['color'])

print("after sorting: ")
print(sort_dict)