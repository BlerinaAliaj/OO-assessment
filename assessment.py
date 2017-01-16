"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

    a. Abstraction: The ability to hide complexity away. Programmer/user does
                    not need to know information a method is using internally,
                    just how to use it. For example, we have leared to use String,
                    tuples, files and apply their methods to our code by knowing
                    how to use them without knowing how they are build.
    b. Encapsulation: All data is kept together and lives close to its
                      functinality. Programmer can place all attributes and
                      methods in one package that can be used later by subclasses.
    c. Polymorphism: Interchangeability of components. This allows for many subclasses
                     to inherit from the same parent class in a predictable way.

2. What is a class?

    A class is a construct that allows you to structure the code in a particular
    way. It is grouping of data and functions in a logical way.

3. What is an instance attribute?

    An instance attribute is a characteristic or trait who is specific to a
    particular object. An instance of a dog called "fiddo" is its name.

4. What is a method?

    A method is a function defined in a class. They have access to all data
    inside a class and must have (self) as an argument.

5. What is an instance in object orientation?

    An instance in OO is an object. For example, if we have Fiddo which is an
    object with certain characteristics from a particular class, we have created
    an instance of that particular class.

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.

   A class attribute is a property that belongs to the entire class. For example,
   if you have a class Car you can have a class attribute called wheel, because
   all cars have wheels.

   An instance attribute is a property that belongs only to the instance. For
   example, an instance of car can have car_class, car_frunk etc that
   may not specifically belong to other cars.


"""


# Parts 2 through 5:
# Create your classes and class methods


class Student(object):
    """ A class that stores student information.

    This class requires three parameters:
    self.first_name: a string representing first name
    self.last_name: a string representing last name
    self.address: a string representing address

    """

    def __init__(self, first_name, last_name, address):
        """ Initialize student info attributes. """

        self.first_name = first_name
        self.last_name = last_name
        self.address = address


class Question(object):
    """ A class that takes in a question and correct answer and stores them

    This class requires two parameters:
    self.question: a string containing a question
    self.answer: a string containing the correct answer

    """

    def __init__(self, question, answer):
        """ Initialize questions and answer attributes. """

        self.question = question
        self.answer = str(answer).lower()

    def ask_and_evaluate(self):
        """ A method that prints question to console and asks user for answer. """

        print self.question
        user_answer = raw_input("> ")

        return user_answer.lower() == self.answer


class Exam(object):
    """ A class that takes in a name and has an empty list attribute

    This class requires one parameter and one attribute:
    self.name: a string containing exam name
    self.question: a list containing exam questions """

    def __init__(self, name):
        """ Initialize exam name and questions attributes. """

        self.name = name
        self.questions = []

    def add_question(self, question, correct_answer):
        """ A method that takes question and correct_answer and adds to exam's
        list of questions. """

        new_question = Question(question, correct_answer)
        self.questions.append(new_question)

    def administer(self):
        """ A method that administers all exams questions and returns score """

        score = 0

        for question in self.questions:
            evaluation = question.ask_and_evaluate()

            if evaluation:
                score += 1

        return score


class Quiz(Exam):
    """ A subclass of class Exam. The subclass Quiz inherits all attributes
    of class Exam but it overwrites it's administer method. """

    def administer(self):
        """ A method that administers all exams questions and returns Pass or
        Fail. """

        score = 0
        total_questions = 0

        for question in self.questions:
            evaluation = question.ask_and_evaluate()
            total_questions += 1

            if evaluation:
                score += 1

        if score >= (total_questions / 2.0):
            return "Pass"
        else:
            return "Fail"


def take_test(exam, student):
    """ A function that administers an exam and prints out student score. """

    score = exam.administer()

    print "The student score is {}".format(score)


def example():
    """ A function that creates exam, student and administers exam. """

    # Creates an exam:
    final = Exam("Final Exam")

    # Add questions:
    final.add_question("What are three benefits of OO?",
                       "Abstraction, Encapsulation, Polymorphism")
    final.add_question("What does OO stand for?", "Object orientation")
    final.add_question("Where is Hackbright located?", "San Francisco")
    final.add_question("What does API stand for?",
                       "Application programing interface")

    # Creates student:
    student = Student("Blerina", "Aliaj", "2900 Bush")

    # Administers test for student:
    take_test(final, student)


def quiz_example():
    """ A function that creates and administers quiz. """

    # Creates an exam:
    quiz_weekly = Quiz("Weekly Quiz")

    # Add questions:
    quiz_weekly.add_question("What are three benefits of OO?",
                       "Abstraction, Encapsulation, Polymorphism")
    quiz_weekly.add_question("What does OO stand for?", "Object orientation")
    quiz_weekly.add_question("Where is Hackbright located?", "San Francisco")
    quiz_weekly.add_question("What does API stand for?",
                       "Application programing interface")

    # Creates student:
    student = Student("Blerina", "Aliaj", "2900 Bush")

    # Administers test for student:
    take_test(quiz_weekly, student)
