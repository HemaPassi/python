import random

health = random.randint(10,25);

print(health)

# First, create a variable called start, and set it equal to "I am ".
start = "i am "
# Remember the space after the word "am" !


# Next, create a variable called age and set it equal to your age in years.
# This must be a number
age = 43

# Next, create a variable called end, and set it equal to " years old".
# Remember the space before the word "years"
end = " years old"

# Next, create a variable called output and use {} symbols and the format() function to stick the start, age and end variables
# together to make a string.
output = "{} {} {}".format(start,age,end)
# An example output string would be "I am 15 years old"


# Finally, print the output to the screen using the print() function.
print(output)


 # here is a very long word

word = "antidisestablishmentarianism"


# use a slice to take out the word "establishment"
# and store it in the answer variable....

answer = word[word.index('esta'):word.index('ari')]
print(answer)


