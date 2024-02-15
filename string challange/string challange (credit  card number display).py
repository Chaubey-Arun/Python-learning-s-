# display credit card Number 16-0123 4 5678 9 10121314 15 16171819
cardno = input('Enter the Card Number ')
disp= cardno[15::]
four = '*' * 4 +' '
show = four*3 + disp
print(show)