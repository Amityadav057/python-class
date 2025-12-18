data = {
    "address":"kathmandu",
    "num":[1,2,3],
    "name":"amit"
}
print(type(data))
print(data)
print(data["num"])
print(len(data))


data['pan_no']=1234
data['vat_no']=1235

print(data)

#del
#popitem
#pop
#clear

del data['name']


#pop
data.pop("pan_no")
print(data)

data.popitem()
data.clear()
print(data)


data1={
    "name":"amit",
    "num":{
        "type":"ntc",
        "number":98867
    }
}
print(data1["num"]['type'])

    