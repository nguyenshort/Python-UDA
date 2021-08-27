"""
Author: Tran Cong Nguyen
Date: 27/08/2021
Program: exersice_page_182.py
Problem:
    1. In what way is a recursive design different from top-down design?
    2. The factorial of a positive integer n, fact(n), is defined recursively as follows:
        fact( ) n 1 5 , when n 1 5
        fact( ) n n 5 2 * fact n( ) 1 , otherwise
        Define a recursive function fact that returns the factorial of a given positive
        integer.
    3. Describe the costs and benefits of defining and using a recursive function.
    4. Explain what happens when the following recursive function is called with the value
        4 as an argument:
        def example(n):
           if n > 0:
                print(n)
                example(n - 1)
    5. Explain what happens when the following recursive function is called with the value 4
        as an argument:
        def example(n):
            if n > 0:
                print(n)
                example(n)
            else:
                example(n - 1)
    6. Explain what happens when the following recursive function is called with the
        values "hello" and 0 as arguments:
        def example(aString, index):
           if index < len(aString):
             example(aString, index + 1)
             print(aString[index], end = "")

    7. Explain what happens when the following recursive function is called with the
        values "hello" and 0 as arguments:
        def example(aString, index):
           if index == len(aString):
               return ""
            else:
               return aString[index] + example(aString, index + 1)
Solution:
    ....
    Câu 1:
        The bottom-up approach (to dynamic programming) consists in first looking at the "smaller" subproblems, and then solve the larger subproblems using the solution to the smaller problems.
        The top-down consists in solving the problem in a "natural manner" and check if you have calculated the solution to the subproblem before.

    Câu 3:
        Recursion adds clarity and (sometimes) reduces the time needed to write and debug code (but doesn't necessarily reduce space requirements or speed of execution).
        Reduces time complexity.
        Performs better in solving problems based on tree structures.
    Câu 4:
        Hàm example sẽ dc gọi...check xem param n có lớn hơn không hay không.
        Đúng sẽ in ra n và gọi lại chính nó...khi gọi lại n sẽ giảm 1 đơn vị
        Hàm sẽ dừng khi n = 0
        n = 4 => in 4 => example(3)
        n = 3 => in 3 > example(2)
        n = 2 => in 2 > example(1)
        n = 1 => in 1 > example(0)
        n = 0 > dừng
    Câu 5:
        => vòng lặp vô hạn vì 4 > 0 luôn đúng
    Câu 6:
        index = 0 => 0 < 5 => in h
        index = 1 => 1 < 5 => in e
        index = 2 => 2 < 5 => in l
        index = 3 => 3 < 5 => in l
        index = 4 => 4 < 5 => in o
        index = 5 => 5 < 5 sai => dừng

    Câu 7: => in Hello
"""


# Press the green button in the gutter to run the script.

def cau2(n):

    if n <= 0:
        raise Exception("Đầu vào không hợp lệ")

    def tinh(x):
        if x == 1:
            return x
        return x * tinh(x - 1)
    return tinh(n)


if __name__ == '__main__':
    print(cau2(6))
