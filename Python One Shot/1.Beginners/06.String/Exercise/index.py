# Challenge 1: Write a program that uses double quotes to store a famous quote.
quote = "The only limit to our realization of tomorrow is our doubts of today."
print(quote)

# Challenge 1: Write a program that uses triple quotes to create a multiline poem/paragraph.
poem = """Roses are red,
Violets are blue,
Sugar is sweet,
And so are you."""
print(poem)

# Challenge 2: Create two variables: first_name and last_name. Concatenate them with a space to form a full name.
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(full_name)

# Challenge 2: Create a greeting message by combining a string literal with the full name.
greeting = "Hello, " + full_name + "! Welcome!"
print(greeting)

# Challenge 3: Prompt the user to enter their name and then print the length of the entered name.
name = input("Enter your name: ")
print("The length of your name is:", len(name))

# Challenge 4: Prompt the user to enter a word and then print the first and last characters of the word using indexing.
word = input("Enter a word: ")
print("First character:", word[0])
print("Last character:", word[-1])

# Challenge 4: Extract a substring using slicing. Prompt the user for the starting and ending indices.
start = int(input("Enter the starting index: "))
end = int(input("Enter the ending index: "))
substring = word[start:end]
print("Extracted substring:", substring)

# Challenge 5: Prompt the user to enter a sentence. Convert the sentence to uppercase and lowercase using the upper() and lower() methods.
sentence = input("Enter a sentence: ")
print("Uppercase:", sentence.upper())
print("Lowercase:", sentence.lower())

# Challenge 6: Prompt the user to enter a sentence with potential leading or trailing spaces. Use the strip() method to remove these spaces.
sentence_with_spaces = input("Enter a sentence with spaces: ")
trimmed_sentence = sentence_with_spaces.strip()
print("Trimmed sentence:", trimmed_sentence)

# Challenge 7: Ask the user for their name, age, and city. Then, use f-strings to create a formatted message.
name = input("Enter your name: ")
age = input("Enter your age: ")
city = input("Enter your city: ")

message = f"Hello, my name is {name}. I am {age} years old and I live in {city}."
print(message)
