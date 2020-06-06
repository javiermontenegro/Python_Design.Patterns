#********************************************************************
# Filename:  FactoryPattern.py
# Author:    Javier Montenegro (https://javiermontenegro.github.io/)
# Copyright:
# Details:   This code is the implementation of the factory pattern.
#*********************************************************************

from abc import ABC, abstractmethod

class Database(ABC):
   @abstractmethod
   def connection(self):
        pass

class SqlServer:
    def connection(self):
        return('Sql database connection')


class Oracle:
    def connection(self):
        return('Oracle database connecction.')


class DbFactory:
    def get_database_connection(self, database):
        return database.connection()


if __name__ == "__main__":

    factory = DbFactory()
    
    print(factory.get_database_connection(SqlServer()))
    print(factory.get_database_connection(Oracle()))
