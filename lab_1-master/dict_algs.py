ivan = {
    'name': 'ivan',
    'age':34,
    'children':[{
        'name':'vasja',
        'age':19,
    }, {
        'name':'petja',
        'age':20,
    }],
}
darja = {
    'name':'darja',
    'age':41,
    'children':[{
        'name':'kirill',
        'age':21,
    }, {
        'name':'pavel',
        'age':15,
    }],
}
emps = [ivan, darja]
age=18
def filter (emps, age):
    z=''
    for name in emps:
        emp=name['children']
        for i in emp:
            if i['age']>age:
                z+= name['name']+'\n'
                break
    return z
print(filter(emps, age))