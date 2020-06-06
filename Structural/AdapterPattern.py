#********************************************************************
# Filename:  AdapterPattern.py
# Author:    Javier Montenegro (https://javiermontenegro.github.io/)
# Copyright:
# Details:   This code is the implementation of the adapter pattern.
#*********************************************************************

from abc import ABC, abstractmethod

# Target Interface
class Target(ABC):
    """ Interface for Client """

    def __init__(self):
       self._adaptee = Adaptee()

    @abstractmethod
    def request(self):
        pass

# Adapter Class
class Adapter(Target):
    def request(self):
        self._adaptee.adaptee_request()

# Adaptee Class
class Adaptee:
    def adaptee_request(self):
        print("Adaptee function called.")


if __name__ == "__main__":

    adapter = Adapter()
    adapter.request()
