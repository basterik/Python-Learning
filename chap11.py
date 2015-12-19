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
