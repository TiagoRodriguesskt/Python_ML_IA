# Both code snippets produce the same results.
counter = 0
counter += 10           # => 10
counter = 0
counter = counter + 10  # => 10

message = "Part 1."

# => Part 1.Part 2.
message += "Part 2."
print(counter)
print(message)

