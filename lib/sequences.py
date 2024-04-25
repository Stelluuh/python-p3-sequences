#!/usr/bin/env python3

# Write a function print_fibonacci() that prints a list of the fibonacci sequence up to the length provided in the function's parameters.
    # print_fibonacci(9)
    # => [0, 1, 1, 2, 3, 5, 8, 13, 21]

def print_fibonacci(length):
    my_list = [] 
    if length > 0: 
        my_list.append(0)
    if length >= 2: 
        my_list.append(1) 
        for i in range(2, length): 
            my_list.append(my_list[-1] + my_list[-2])

    print(my_list)

    #1. initialzes an emply list
    #2. check if length is greater than 0, if it is itmeans user wants at least 1 Fib number in the sequence.
    #3. append the first fib number, which is 0, to my_list
    #4. check to see if length is >=2, if it is, it means user wants at least 2 fib numbers in the sequence
    #5. append the second number of a fib sequence, which is 1 to the end of the my_list. So now we have [0, 1]
    #6. start a for loop from the third fib number. it iterates over the range starting from 2 b/c the first two fib numbers (0 and 1) are already in my_list.
    #7. Inside the loop, it calculates the next Fibonacci number by adding the last two numbers in my_list (which are my_list[-1] and my_list[-2]) and appends the result to my_list.
    #8. prints the generated Fibonacci sequence.