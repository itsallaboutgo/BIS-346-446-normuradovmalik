# Exercise 6.8

# Defining dictionaries for words representation of numbers
ones = {"1":"One","2":"Two","3":"Three","4":"Four","5":"Five","6":"Six", "7":"Seven","8":"Eight","9":"Nine"}
afterTens = {"10":"Ten","11":"Eleven","12":"Twelve","13":"Thirteen","14":"Fourteen","15":"Fifteen","16":"Sixteen", "17":"Seventeen","18":"Eighteen","19":"Nineteen"}
tens = {"2":"Twenty","3":"Thirty","4":"Fourty","5":"Fifty","6":"Sixty", "7":"Seventy","8":"Eighty","9":"Ninety"}
# Taking input from the user
x = input("Enter the number: ")
# Function to convert number to word
def number_to_word(x, digits):
  # If the number has only one digit then simply return the value from "ones" dictionary
  if digits == 1:
    # Check if the number is zero or not
    if x[0] != '0':
      return ones[x[0]]
    return "Zero"
  # Handle the two digit number
  elif digits == 2:
    # If the first element is 0 then call the function recursively for string after first element
    # Because it is actually a one digit number
    if x[0] == '0':
      return number_to_word(x[1], 1)
    # If the number is in afterTens dictionary then return the value
    # Otherwise return the value for first element from tens dictionary and 
    # for second element from ones dictionary
    if x in afterTens:
      return afterTens[x]
    else:
      return tens[x[0]] + " " + ones[x[1]]
  # Handle the three digit number
  elif digits == 3:
    # If the first element is 0 then call the function recursively for string after first element
    # Because it is actually a two digit number
    if x[0] == '0':
      return number_to_word(x[1:], 2)
    # Call method recursively after Adding Hundred'th position for 2 digit number
    return ones[x[0]] + " Hundred " + number_to_word(x[1:], 2)
before_decimal = x.split(".")[0]
word = number_to_word(before_decimal, len(before_decimal)).upper()
# Handle the fraction part
if len(x.split(".")) == 2:
  after_decimal = " AND " + x.split(".")[1] + "/" + "1" + "0" * len(x.split(".")[1])
  word += after_decimal
# Print the result
print(word)