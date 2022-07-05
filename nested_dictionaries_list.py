#herw we have to grab tlist that we need ans then go to that list index
x = [ [5,2,3], [10,8,9] ]
print(x)
x[1][0]=15
print(x)

#we need to grab the index then the key name 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
print(students[0]['last_name'])
students[0]["last_name"] = 'Bryan'
print(students[0]['last_name'])

#we need to grab the  key name then the index of that dictionanry 
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
print(sports_directory['soccer'][0])
sports_directory['soccer'][0] = 'Andres'
print(sports_directory['soccer'][0])


#we grab the index then the key
z = [ {'x': 10, 'y': 20} ]
print(z[0]["y"])
z[0]['y']=30
print(z)






students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

#prints the items of a list that are in a dictionary
def iterateDictionary(some_list):
#things inside of a list
    for item in some_list:
#print the keys and their values
        for key in item:
            print(key)
            print(item[key])

iterateDictionary(students)


students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

#prints the values of one key
def iterateDictionary(key_name,some_list):
    for item in some_list:
            print(item[key_name])

iterateDictionary("first_name",students)
iterateDictionary("last_name",students)



def print_info(some_dict):
#prints the key of the dictionary
    for key in some_dict:
        print(key)
#printst the lenght of the list
        some_var = some_dict[key]
        print(len(some_var))
#print the indexes that re inside of the list
        for item in some_var:
            print(item)

dojo = {
'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

print_info(dojo)




