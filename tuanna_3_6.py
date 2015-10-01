names = "cho meo ga chuot vit ngan"
list_new = list()
for i in range(len(names)):
    if names.count(names[i]) == 1:
        list_new.append(names[i])
print list_new
# ['m', 'e', 'u', 'v', 'i']