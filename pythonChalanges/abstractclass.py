"""
1 Create an abstract base class called "Human".Give
  it an abstract function called "run"

2. Create an abstract base class called "Robot". Give it
    an abstract function called vacuum

3. Create a subclass which inherits from both "Human"
   and "Robots" called cyborg and create an instance of cyborg

"""


from abc import ABCMeta, abstractmethod

class Human(object):
    __metaclass__ = ABCMeta
    #abstarct class is a decorator . need to learn decorator deeply
    @abstractmethod
    def run(self):
        pass

class Robot(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def vacum(self):
        pass


class Cyborg(Human, Robot):
    #overriding of both classes abstract method
    def run(self):
        print('cyborg is running')

    def vacum(self):
        print('cyborg is in vacum')

x = Cyborg()
x.run()
x.vacum()
# .........................................
