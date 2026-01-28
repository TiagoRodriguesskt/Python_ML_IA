def my_function(): # This is a simple function that prints a message
    print("Hello from my_function!")

my_function()

def greet(name): # Function to greet a person by name
    print(f"Hello, {name}!")
greet("Alice")
def add(a, b): # Function to add two numbers
    return a + b
result = add(3, 5)
print(result)
def factorial(n): # Function to compute factorial of a number
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1) # Recursive call
print(factorial(5))
def fibonacci(n): # Function to print first n Fibonacci numbers
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ") # Print the current Fibonacci number
        a, b = b, a + b
    print()
fibonacci(5)
def power(base, exponent=2): # Function to compute power with default exponent
    return base ** exponent
print(power(3))
print(power(2, 3))
def is_even(num): # Function to check if a number is even
    return num % 2 == 0
print(is_even(4))    
print(is_even(5))
def print_multiples_of(n, limit): # Function to print multiples of n up to limit
    for i in range(1, limit + 1): # Loop from 1 to limit
        print(n * i, end=" ") # Print the multiple
    print() # Print newline after the loop
print_multiples_of(5, 10) # Print multiples of 5 up to 10
def outer_function(x): # Function demonstrating nested functions
    def inner_function(y): # Nested function
        return y * 2 # Inner function logic
    return inner_function(x) + 3 # Call inner function and add 3
print(outer_function(4)) # Call outer function
def greet_user(name, greeting="Hello"): # Function to greet user with optional greeting
    print(f"{greeting}, {name}!") # Print the greeting message
greet_user("Alice") # Use default greeting
greet_user("Bob", "Hi") # Use custom greeting



