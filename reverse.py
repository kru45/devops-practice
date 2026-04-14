# Reverse each word of a string
def reverse_words(input_str):
   return ' '.join(word[::-1] for word in input_str.split())
# Test the function
print(reverse_words('My Name is Jessa')) # Output: yM emaN si asseJ
