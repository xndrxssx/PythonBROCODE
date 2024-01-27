usernames = ["Dude", "Bro", "Mister"]
passwords = ("password", "abc123", "guest")
#login_date = ["1/1/2021", "1/2/2021", "1/3/2021"]

users = dict(zip(usernames, passwords))

print(type(users))

for key, value in users.items():
    print(key+" "+value)
    
