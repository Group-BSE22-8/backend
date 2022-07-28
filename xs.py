names = ['john', 'simon', 'Sean', 'Phoebe']

for name in names:
    if(name[0].isupper()):
        print(name)


class User():
    name =''
    age = 0
    email =''
    friends= []

    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email
        self.friends = []

    def add_friend(self, friend):
        self.friends.append(friend)

    def remove_friend(self, friend):
        self.friends.remove(friend)
    
    def get_friends(self):
        return self.friends

    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age

    def get_email(self):
        return self.email

    def __str__(self):
        return f'{self.name} is {self.age} years old and has {len(self.friends)} friends'


x1 = User('John', '20', 'john@example.com')

print(x1)
