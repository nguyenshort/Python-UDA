"""
Author: Tran Cong Nguyen
Date: 27/08/2021
Program: exersice_page_194.py
Problem:
    1. Where are module variables, parameters, and temporary variables introduced and initialized in a program?
Solution:
    1. TEMPORARY VARIABLES :
            INTRODUCED : inside a block, they have very short lifetime and hold data that can be discarded or is later stored in a permanent variable
            INITIALIZED : temporary variables can be initialized anywhere inside the block where they are declared.
        PARAMETERS:
            INTRODUCED : parameters are declared inside the parenthesis of the function definition
            INITIALIZED : parameters can be initialized where they are declared or can be declared in the parenthesis of the function call
        MODULE VARIABLE :
            INTRODUCED : A module-level variable is declared for a particular module. It is available to all procedures within that module but not to the rest of the application. Module-level variables remain in existence for the lifetime of the application and preserve their values.
            INITIALIZED : module variable gets initialized where they are declared inside the module. it is initialized to 0 by default.
    2. What is the scope of a variable? Give an example.
        - A scope is a region of the program and broadly speaking there are three places, where variables can be declared:
            for index in range(2):
                // test is scope var
                test = 4
                print(test)
"""


# Press the green button in the gutter to run the script.

if __name__ == '__main__':
    print()
