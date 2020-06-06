#********************************************************************
# Filename:  SingletonPattern_Lazy.Instantiation.py
# Author:    Javier Montenegro (https://javiermontenegro.github.io/)
# Copyright:
# Details:   This code is the implementation of the singleton pattern.
#*********************************************************************

class Singleton:
    __instance = None
    def __init__(self):
        if not Singleton.__instance:
            print("__init__ method called.")
        else:
            print("Instance already created.", self.getInstance())

    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance=Singleton()
        return cls.__instance


if __name__ == "__main__":

    # Initialized object.
    s1 = Singleton()

    print ("Object created:", Singleton.getInstance())

    # Instance already created.
    s2 = Singleton()

