#********************************************************************
# Filename:  MVCPattern.py
# Author:    Javier Montenegro (https://javiermontenegro.github.io/)
# Copyright:
# Details:   This code is the implementation of the mvc pattern.
#*********************************************************************

class Model:
    def db_data(self):
        print('Model called for data.')
        data = 'Model Data.'
        return data

class View:
    def render(self, data):
        print('Rendering model on view :' , data)

class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View()

    def present(self):
        print('Controller, managing model and view.')
        data = self.model.db_data()
        self.view.render(data)


if __name__ == "__main__":

    controller = Controller()
    controller.present()


