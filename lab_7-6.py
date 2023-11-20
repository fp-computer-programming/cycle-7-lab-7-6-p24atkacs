"""
Create a Python file named lab_7-6.py

*** You must write a comment for every chunk of code you write from now on along with your author tag***

Create a 2 separate functions within the same document. 
Create a 3rd function which requires both the first two functions within it
Create 4 test cases for your 3rd function. 
"""
# Author: Andrew Tkacs

def add_numbers(a, b):
    """
    This function adds two numbers.
    """
    return a + b

def multiply_numbers(c, d):
    """
    This function multiplies two numbers.
    """
    return c * d

def combined_operation(x, y, z):
    """
    This function requires the results of add_numbers and multiply_numbers functions.
    It adds the results of the two functions and then multiplies the sum by the third parameter.
    """
    # Call add_numbers with parameters x and y
    sum_result = add_numbers(x, y)

    # Call multiply_numbers with parameters sum_result and z
    final_result = multiply_numbers(sum_result, z)

    return final_result

# Test cases

# Test Case 1
result_1 = combined_operation(2, 3, 4)
print("Test 1 Result:", result_1)


# Test Case 2
result_2 = combined_operation(-1, 5, 2)
print("Test 2 Result:", result_2)


# Test Case 3
result_3 = combined_operation(0, 0, 1)
print("Test 3 Result:", result_3)


# Test Case 4
result_4 = combined_operation(10, -2, 3)
print("Test 4 Result:", result_4)

