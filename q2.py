class Student(Person):
    """
    A subclass of Person. Student objects are assigned a unique
    id number. The first Student object created in a program
    gets an id of 0, the second gets an id of 1, and so on.
    """
    next_id = 0

    def __init__(self, name, age):
        """
        Assume name is a str, and age is a positive int.
        Create a Student as a Person with the given name and age,
        and also with its unique id.
        """
        super().__init__(name, age)
        self.id = Student.next_id
        Student.next_id += 1

    def get_id(self):
        """Return the id of self."""
        return self.id
