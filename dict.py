# user ={'name' : 'shuvranil', 'age' : 21}
# print(user['name'])
# print(user["age"])


# user = dict(name = 'shuvranil' , age = 21)
# print(user['name'])                            # shuvranil = output


# user_info = {
#     'name' : 'shvranil',
#     'age'  : 21,
#     'fav movie' : ['interstaller','your name'],
#     'music'     : ["pop","jazz"]
# }
# # print(user_info['fav movie'])         # output = ['interstaller','your name']
# if 'name' in user_info:                # for key 
#     print('present')
# else:
#     print('not present') 
    
    # output = present


# user_info = {
#     'name' : 'shvranil',
#     'age'  : 21,
#     'fav movie' : ['interstaller','your name'],
#     'music'     : ["pop","jazz"]
# }
    
# if 'shvranil' in user_info.values():    # for valoues of key             
#     print('present')
# else:
#     print('not present')  



# user_info = {
#     'name' : 'shvranil',
#     'age'  : 21,
#     'fav movie' : ['interstaller','your name'],
#     'music'     : ["pop","jazz"]
# }


# user_info['height'] = "5'5"
# print(user_info)

# print(user_info.pop('name'))
# print(user_info)

# d = dict.fromkeys(('name' , 'age'),'unknown')
# print(d)                                                                       # output - {'name': 'unknown', 'age': 'unknown'}
# f = d.get("name")
# print(f)                                                                        # unknown

# if d.get("names"):
#     print("prasent")
# else:
#     print('not present')                                                   # not present

# print(d.get('names', 'not found !!'))                                      # not found !!


# def cube(c):
#     cub = {}
#     for i in range(1,c+1):
#         cub[i] =i**3
#     return cub

# number = int(input("Enter your number : "))
# print(cube(number))                                                         # ourput = {1: 1, 2: 8, 3: 27, 4: 64, 5: 125}



# def count(n):
#     c = {}
#     for i in n:
#         c[i] = n.count(i)
#     return c

# name = input("Enter your name : ")
# nam = name.lower()                                             # {'s': 2, 'h': 1, 'u': 1, 'v': 1, 'r': 1, 'a': 1, 'n': 1, 'i': 1}  
# print(count(nam))




# name = input("Enter your name : ")
# nam = name.title()
# age = input("Enter your age : ")
# movie = input("Enter your movies use coma : ").split(",")
# music = input("Enter your musics use coma : ").split(",")

# info = {}
# info['name'] = nam
# info['age'] = age
# info['fav_movies'] = movie
# info['fav_musics'] = music

# for key, value in info.i:
#     print(F'{key}:{value}')


n = int(input("Enter your number : "))
cub = {}
for i in range(1,n+1):
    cub[i] =i**3

for key, value in cub.items():
    print(value , end =" ")




