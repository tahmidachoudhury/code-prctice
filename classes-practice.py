class Person():
    def __init__(self, name, birthday, favourite_language):
        self.name = name
        self.birthday = birthday
        self.favourite_language = favourite_language

person1 = Person("Alan Turing", "June 23, 1912", "Standard Description")
person2 = Person("Ada Lovelace", "December 10", "n/a")
person3 = Person("Grace Hopper", "December 9", "COBOL")
person4 = Person("John von Neumann", "December 28", "C")
person5 = Person("Claude Shannon", "April 30", "C")

print(person2.name)