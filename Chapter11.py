#In this assignment you will read through and parse a file with text and numbers.
#You will extract all the numbers in the file and compute the sum of the numbers.
import re
name = input("Enter file:")
handle = open(name)
sum = 0
for line in handle:
  number_list = re.findall('[0-9]+', line)
  for number in number_list:
   num = int(number)
   sum = sum + num
print (sum)
