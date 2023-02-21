"""Task 1 A Person class

Make a class called Person. Make the __init__() method take firstname, lastname, and age as parameters and add them as
attributes. Make another method called talk() which makes prints a greeting from the person containing, for example like
 this: “Hello, my name is Carl Johnson and I’m 26 years old”."""


class Person:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def talk(self):
        return f'Hello, my name is {self.firstname} {self.lastname} I"m {self.age} years old'


"""Task 2 Doggy age

Create a class Dog with class attribute `age_factor` equals to 7. Make __init__() which takes values for a dog’s age. 
Then create a method `human_age` which returns the dog’s age in human equivalent."""


class Dog:
    age_factor = 7

    def __init__(self, dog_age):
        self.dog_age = dog_age

    def human_age(self):
        return f' if this dog was a human, it would be {self.dog_age * self.age_factor} years old'





def main():
    pass

    guy = Person('Ivan', 'Ivanenko', 30)
    print(guy.talk())

    flafy = Dog(7)
    print(flafy.human_age())


if __name__ == '__main__':
    main()
