import random 

n = 0

#This is a list
r_number = []

#This loop makes the list only 50 numbers
while n < 50:
    
    #This generates the numbers
    number = random.randint(1, 1000)

    #This ensures that the number is even and greater than 50
    if number % 2 == 0 and number > 50:

        #This adds the number to the list
        r_number.append(number)

        #And this adds 1 to the loop
        n = n + 1

#Finally this print the list
print(r_number[:])