##for classes

class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)


class Artist(object):

    def __init__(self, artist_name):
        self.artist_name = artist_name


##showing has a and  

class Animal(object):
    pass

class Dog(Animal):
    def __init__(self, name):
        self.name = name

class Cat(Animal):
    def __init__(self, name):
        self.name = name

class Person(object):

    def __init__(self, name):
        self.name = name

        #does person have pet
        self.pet = None

class Employee(Person):

    def __init__(self, name, salary):
        super(Employee, self).__init__(name)

        self.salary = salary

class Fish(object):
    pass

class Salmon(Fish):
    pass

class Halibut(Fish):
    pass



"""happy_bday = Song(["Happy birthday to you",
                    "I don't want to get sued",
                    "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family", "With pockets full of shells"])


happy_bday.sing_me_a_song()
print("§§§§HERE COMES THE NEXT SONG!!!!!")
bulls_on_parade.sing_me_a_song()"""



from datetime import datetime

judas = '2019-07-15 15:03:16'

judasout = datetime.strptime(judas, "%Y-%m-%d %H:%M:%S")
