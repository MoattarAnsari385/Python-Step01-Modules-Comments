""" This code imports the pyjokes library to fetch a random joke.
    The joke is then printed using the print() function. """

import pyjokes
# print("Printing Jokes")

# This prints random jokes

joke = pyjokes.get_joke()
print(joke)