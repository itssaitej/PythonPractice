a={
    "Name1":"Sai Tej",
    "Age1": 28
}

b={
    "Name2": "SpiderMan",
    "Age2": 35
}

m={**a,**b}

"""
m={}

for key,value in a.items():
    m[key]=value
for key,value in b.items():
    m[key]=value
"""

print(m)