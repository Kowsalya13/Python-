#comprehension append() join()
def pig_latin(text):
  say = []
  # Separate the text into words
  words = text.split(" ")
  for word in words:
    say.append(word[1:] + word[0]+"ay")
    # Turn the list back into a phrase
  return " ".join(x for x in say)

		
print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"