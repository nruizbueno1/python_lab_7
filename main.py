# Project:      Lab7
# Author:       Nicole Ruiz-Bueno
# Date:         02/27/2023
# File:         main.py
# Description:  Use Python string functions to check if a user entered password meets the following requirements:
#               Must be at least 8 characters long.
#               Must contain at least one lowercase letter
#               Must contain at least one uppercase letter
#               Must contain at least one digit.
#
#               If the password meets the above criteria display a message box with the message
#               “Meets all requirements”.
#               If the password does not meet the requirements, display a message box stating why.
#               For example:
#               Must be at least 8 characters
#               Must have at least 1 uppercase letter
#               Must have at least 1 lowercase letter
#               Must have at least 1 digit

# Input:        User enters in password of choice
# Output:       The password is either accepted or rejected based on the password requirements

# Processing:   Declare a variable to hold the password
#                Check password length (must be at least 8 characters)
#                    If not at least 8 characters, display error message ('Must be at least 8 characters')
#               Run for loop to make sure there is at least 1 lowercase character
#                        count = 0
#                            for character in password:
#                            if character.islower():
#                               count = count + 1
#                        If there are no lowercase characters, display error message ('Must have at least 1 lowercase
#                            letter')
#                                    else:
#                                     if count < 1:
#                                        self.kivy_message_box('Password Check', 'Must have at least 1 lowercase
#                                        letter')
#                                         return
#                Run a similar for loop but check for uppercase characters (change lower to upper in code)
#                    If there are no uppercase characters, display error message ('Must have at least 1 uppercase
#                            letter')
#                Run a similar for loop but check for digits (change upper to digit in code)
#                    If there are no digits, display error message ('Must have at least 1 digit')
#                Run a for loop to check for special character:
#                   (assign variable) special = '!@#$%^&*'
#                       for special_char in special:
#                           if special_char in password:
#                               count = count + 1
#                    If there are no special character, display error message ('Must have at least 1 special character')
#
#                Exit button releases event function that closes application.

# import the Kivy library components
from kivy.lang import Builder
from kivy.app import App
from kivy.uix.widget import Widget

# imports for Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.metrics import dp

# designate our .kv design file
# we are using gui.kv for the Graphical user Interface
Builder.load_file('gui.kv')


# A Widget is the base building block of GUI interfaces in Kivy.
# It provides a Canvas that can be used to draw on screen.
# It receives user events and reacts to them.
# MyLayout is the root window of the application
class MyLayout(Widget):
    pass


# Lab7 is the name of the Python application that will be using Kivy
class Lab7(App):
    # set the title of the window frame
    title = 'Lab7: Check password by Ruiz-Bueno'

    # the build method is called when the application starts
    def build(self):
        print("build called")
        # when app starts, return main root window in the kivy gui file
        return MyLayout()

        # ckeck button release event handler
        # this function is called by the Kivy event loop
        # when a user presses the While Loop button
    def check_button(self):
        # get data from text inputs
        # self means this or the current object
        # root is the root window or MyLayout
        # ids is the id's of the widgets contained in the root window
        # start is the id of the first Fahrenheit text input box
        # conversions is the id of the number of conversions
        # print the input for debugging
        print(f'check_button password: {self.root.ids.password.text}')

        # declare a variable to hold the password
        password = self.root.ids.password.text

        # check if password is at least 8 characters
        if len(password) < 8:
            self.kivy_message_box('Password Check', 'Must be at least 8 characters')
            return

        # count the number of lowercase letters
        count = 0
        for character in password:
            if character.islower():
                count = count + 1
        else:
            if count < 1:
                self.kivy_message_box('Password Check', 'Must have at least 1 lowercase letter')
                return

        # count the number of uppercase letters
        count = 0
        for character in password:
            if character.isupper():
                count = count + 1
        else:
            if count < 1:
                self.kivy_message_box('Password Check', 'Must have at least 1 uppercase letter')
                return

        # count the number of digits
        count = 0
        for character in password:
            if character.isdigit():
                count = count + 1
        else:
            if count < 1:
                self.kivy_message_box('Password Check', 'Must have at least 1 digit')
                return
        count = 0
        special = '!@#$%^&*'
        for special_char in special:
            if special_char in password:
                count = count + 1
        else:
            if count < 1:
                self.kivy_message_box('Password Check', 'Must have at least 1 special character')
                return


        # if we got to here password must be good.
        self.kivy_message_box('Password Check', 'Meets all requirements')

    # exit button release event handler
    # this function is called by the Kivy event loop when a user presses the exit button
    def exit_button(self):
        # call the stop function in the app
        self.stop()

    # creates a kivy Message Box
    # it is a static method because self is not used
    @staticmethod
    def kivy_message_box(title, message):
        # create the button and label, add them to BoxLayout
        button = Button(text='Close',
                        size_hint=(.3, .3),
                        pos_hint={'right': 1}
                        )
        label = Label(text=message)
        box = BoxLayout(orientation='vertical')
        box.add_widget(label)
        box.add_widget(button)

        # create the popup object
        popup = Popup(title=title,
                      content=box,
                      size_hint=(None, None),
                      size=(dp(300), dp(200)),
                      auto_dismiss=False)
        # bind the on_press event of the button to the dismiss function
        button.bind(on_press=popup.dismiss)
        popup.open()


# If this Python file is called as the main starting point of the application
# start the Python/Kivy app running.
if __name__ == '__main__':
    Lab7().run()
