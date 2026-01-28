for item in range(5): # Outer loop
    print("Item:", item) # Print the current item
    for subitem in range(3): # Inner loop
        print("  Subitem:", subitem) # Print the current subitem
    print("Finished processing item:", item) # Indicate completion of the outer loop iteration

for i in range(1, 6): # Loop from 1 to 5
    print("Number:", i) # Print the current number
    for j in range(i): # Inner loop from 0 to i-1
        print("  Number:", j) # Print the current number
        print(" ", end="") # Print space without newline
    print("End of line", i) # Indicate end of the line for the outer loop

for letter in "Python": # Loop through each letter in the string "Python"
    print("Letter:", letter) # Print the current letter
    for code in range(ord(letter)): # Inner loop from 0 to ASCII value of the letter - 1
        if code % 10 == 0: # If code is a multiple of 10
            print("  Code:", code) # Print the code with newline
        else: # If code is not a multiple of 10
            print("  Code:", code, end="") # Print the code without newline
    print() # Print newline after inner loop

for i in range(3): # Outer loop
    print("Outer loop iteration:", i) # Print the current iteration of the outer loop
    for j in range(2): # Inner loop
        print("  Inner loop iteration:", j) # Print the current iteration of the inner loop
    print("End of outer loop iteration:", i) # Indicate end of the outer loop iteration

for x in range(4): # Outer loop
    print("X value:", x) # Print the current value of x
    for y in range(x + 1): # Inner loop from 0 to x
        print("  Y value:", y) # Print the current value of y
        print(" ", end="") # Print space without newline
    print("Y loop completed for X =", x) # Indicate completion of the inner loop for current x
