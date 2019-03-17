# # def yell_it():
# #     words_to_yell = input("Enter words: ")
# #     print(words_to_yell.upper())
# # yell_it()
#
# #calculate area of a circle
#
# # from math import pi
# # r = float(input ("Input the radius of the circle : "))
# # print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))
#
# object_type = type(22.3)
# print(object_type)
#
# def msg_double(phrase):
#     double = phrase + " " + phrase
#     return double
# print(msg_double("Ridbay"))

# def calc_sum(a,b):
#     sum_no = a+b
#     return sum_no
# print(calc_sum("ridbay","Baba"))
# print(type(calc_sum(3,5)))
# def make_doctor(name):
#     full_name = input("Enter your full name: ")
#     return full_name
# print(make_doctor("Ridbay"))

# def make_schedule(period1, period2, period3):
#     schedule = ("[1st] " + period1.upper() + "\n[2nd] " + period2.lower() + "\n[3rd] " + period3.title())
#     return schedule
# student_schedule = make_schedule("Mathematics", "English", "Yoruba")
# print(student_schedule)
# def low_case(words_in):
#     return words_in.lower()
# words_lower = low_case("Return THIS lower")
# print(words_lower)

# def hat_available(color):
#     hat_colors = 'black, red, blue, green, white, grey, brown, pink'
#     # return Boolean
#     return (color.lower() in hat_colors)
# have_hat = hat_available('green')
#
# print('hat available is', have_hat)
#
# def bird_available(bird):
#     bird_types = 'crow robin parrot eagle sandpiper hawk pigeon'
#     return (bird.lower() in bird_types)
# have_bird = bird_available(input("Enter the name of the bird: "))
#
# print("Bird is available: ", have_bird)

# define function how_many
# def how_many():
#     requested = input("enter how many you want: ")
#     return requested
#
# # get the number_needed
# number_needed = how_many()
# print(number_needed, "will be ordered")

# def short_rhyme():
# def title_it(msg):
#     return msg.title()
# enter_title = title_it(input("what is the title?"))
# title_it_rtn = enter_title.isupper()
# print(title_it_rtn)

# def book_store(book, price):
#
#     return "Title: " + book + ", costs " + price
#
#
# book_choice = input("Enter books title: ")
# book_price = input("Enter books price: ")
#
# print (book_store(book_choice, book_price))

# Example:
#
# def make_greeting(name, greeting = "Hello"):
#     return (greeting + " " + name + "!")
#
# def get_name():
#     name_entry = input("enter a name: ")
#     return name_entry
# def get_greeting():
#     greeting_entry = input("enter a greeting: ")
#     return greeting_entry
# # get name and greeting, send to make_greeting
# print(make_greeting(get_name(), get_greeting()))
#
# def fishstore(fish, price):
#     sentence = "Fish Type: " + fish + " costs $" + price
#     return sentence
# fish_entry = input("Enter the fish name: ")
# price_entry = input("Enter the fish price: ")
# # print(fishstore(fish_entry, price_entry))
#
#
# hot_tea = False
#
# if hot_tea:
#     print("This is hot tea")
# else:
#     print("This is a cold tea")
# []Another Example
#
# favourite_meal = input("Enter your favoruite meal: ")
#
# if favourite_meal.isalpha():
#     print("Your favourite meal is: ",favourite_meal.upper())
# else:
#     print("Kindly enter your favourite meal using alphabets only")
#
# meals_available = 'Amala, Eba, Iyan, Fufu, Semo'
# if favourite_meal.lower() in meals_available.lower():
#     print(favourite_meal.title(),"is available.")
# else:
#     print("Check our other restaurant")


# #Another Example
# test_string_1 = "welcome"
# test_string_2 = "I have $3"
#
# if test_string_1.islower():
#     print("It is in lower case")
#     pass

# x = 9+4
# print(" X=13 is ", x == 13)
# print(" X = 13 is", x!=13)

# x = 3+3
# print( x> 2+4)

# x = 3
# y = x - 3
#
# if y > x:
#     print(" Y is greater than X")
# elif y >= x:
#     print(" Y is greater than or equal to X")
# else:
#     print("Y is less than X")

# name = input("What is your name: ")
# gender = input("What is your gender:")
#
# if gender.lower() == "male":
#     print("Welcome,",name,", You're a ",gender.lower(),"!")
# else:
#     print("Welcome,",name,"You're a female")

# print("'Hello ' + 'World!' " < "Hello World!")
# ask_user = input("What is 8+13: ")
# if ask_user == "21":
#     print("You are correct, the answer is 21")
# else:
#     print("Please,redo the calculation and enter the correct answer")

# answer_quiz = input("Are humans higher animals? (T/F): ")
# if answer_quiz.upper() == "T":
#     print("You're correct")
# else:
#     print("You're wrong")

#Ask users for variable size
# shirt_sale = input("Enter size (S/M/L): ")
#conditional statement for the size variable

# if shirt_sale.upper() == "S":
#     print("The small size costs $6")
# elif shirt_sale.upper() == "M":
#     print("The medium size costs $7")
# elif shirt_sale.upper() == "L":
#     print("The large size costs $8")
# elif shirt_sale.isdigit():
#     print("Shirt size can't be in Digits, enter alphabets")
# else:
#     print("Invalid entry, please use 'S/M/L'")

# student_age = input("Enter your age: ")
# if student_age.isalpha():
#     print("Only numbers are expected not alpha, enter age using numbers")
# else:
#     age_next_year = int(student_age) + 1
#     print("Next year, student will be",age_next_year)

# int1 = int(input("Enter first number: "))
# int2 = int(input("Enter second number: "))
# sum_of_int = int1 + int2
# print("The sum of the 2 numbers is: ", sum_of_int)
#
# def multiply(num1,num2):
#     return num1 * num2
# f_num = int(input("Enter first Number: "))
# s_num = int(input("Enter second Number: "))
# result = str(multiply(f_num,s_num))
# print(type(result))

#Programme to Calculate Body Mass Index (BMI) using the weight and height

# #Ask users to input the data
# weight = int(input("Enter your weight in KM: "))
# height = float(input("Enter your height in 'm': "))
# #Calculating the data
#
# bmi = weight/(height * height)
#
# #Out put the result to the screen
# print("Your BMI is: ", bmi)

# # ***TIP:*** click in input box before typing
#
# sandwich_type = input('"c" for Cheese or "v" for Veggie Special: ')
#
# if sandwich_type.lower() == "c":
#     # select cheese type
#     cheese_type = input('"c" for Cheddar or "m" for Manchego: ')
#
#     if cheese_type.lower() == "c":
#         print("Here is your Cheddar Cheese sandwich")
#     else:
#         print("Here is your Manchego Cheese sandwich")
#
# else:
#     print("Here is your Veggie Special")


# # ***TIP:*** click in input box before typing
#
# print("Hi, welcome to the sandwich shop.  Please select a sandwich.")
# sandwich_type = input('"c" for Cheese or "v" for Veggie Special: ')
# # select sandwich type sandwich_type = input('"c" for Cheese or "v" for Veggie Special: ')
# print()
#
# if sandwich_type.lower() == "c":
#     # select cheese type
#     print("Please select a cheese.")
#     cheese_type = input('"c" for Cheddar or "m" for Manchego: ')
#     print()
#
#     if cheese_type.lower() == "c":
#         print("Here is your Cheddar Cheese sandwich.  Thank you.")
#     elif cheese_type.lower() == "m":
#         print("Here is your Manchego Cheese sandwich.  Thank you.")
#     else:
#         print("Sorry, we don't have", cheese_type, "choice today.")
#
# elif sandwich_type.lower() == "v":
#     print("Here is your Veggie Special. Thank you.")
#
# else:
#     print("Sorry, we don't have", sandwich_type, "choice today.")
# print()
# print("Goodbye!")


# # [] Program: Say "Hello"
# print("Say Hello?")
#
# say_hello = input("'Say Hello' y/n: ")
#
# if say_hello.lower() == "y":
#     full_hello = input("Full 'Hello'? y/n: ")
#     if full_hello.lower() == "y":
#         print("Hello")
#     elif full_hello.lower() == "n":
#         print("Hi")
#     else:
#         print(" Please use y/n")
# elif say_hello.lower() == "n":
#     print("{friendly nod}")
# else:
#     print("Your input is not allowed, use y/n")

#[] 3 Guesses

# print("Guess the bird")
#
# bird_names = "1,2,3,4"
# bird_guess = input("1st try; Enter your guess in integer: ")
# if bird_guess in bird_names :
#     print("Yes, 1st try!")
#
# else:
#     print("You have two more chances")
#     bird_guess = input("2nd try; Enter your guess in integer: ")
#     if bird_guess in bird_names :
#         print("Yes, 2nd try!")
#     else:
#         print("You have one more chance")
#         bird_guess = input("3rd try; Enter your guess in integer: ")
#         if bird_guess in bird_names:
#             print("Yes, 3rd try!")
#         else:
#             print("You have exhausted your 3 chances")
#             print("Bye Bye!!!")
#

# # def pre_word(s):
# #     return s
# word_pre = input("enter a word that starts with \"pre\": ")
# default_word = "pre"
# if default_word in word_pre:
#     print("It is there")
# else:
#     print("Enter word starting with \"pre\"")

# number_guess = "0"
# secret_number = "5"
#
# while True:
#     number_guess = input("guess the number 1 to 5: ")
#     if number_guess == secret_number:
#         print("Yes", number_guess,"is correct!\n")
#         break
#     else:
#         print(number_guess,"is incorrect\n")

# while True:
#     weather = input("Enter weather (sunny, rainy, snowy, or quit): ")
#     print()
#
#     if weather.lower() == "sunny":
#         print("Wear a t-shirt and sunscreen")
#         break
#     elif weather.lower() == "rainy":
#         print("Bring an umbrella and boots")
#         break
#     elif weather.lower() == "snowy":
#         print("Wear a warm coat and hat")
#         break
#     elif weather.lower().startswith("q"):
#         print('"quit" detected, exiting')
#         break
#     else:
#         print("Sorry, not sure what to suggest for", weather +"\n")


# familiar_name = "Ridbay"
#
# while True:
#     familiar_name = input("Enter common name of friends/family: ")
#     if familiar_name.isalpha():
#         print("How are you",familiar_name)
#         break
#     else:
#         print("Sorry enter another name")


# seat_count = 0
# while True:
#     print("seat count:",seat_count)
#     seat_count = seat_count + 1
#
#     if seat_count > 4:
#         break

# # initialize variables
# seat_count = 0
# soft_seats = 0
# hard_seats = 0
# num_seats = 4
#
# # loops tallying seats using soft pads vs hard, until seats full or user "exits"
# while True:
#     seat_type = input('enter seat type of "hard","soft" or "exit" (to finish): ')
#
#     if seat_type.lower().startswith("e"):
#         print()
#         break
#     elif seat_type.lower() == "hard":
#         hard_seats += 1
#     elif seat_type.lower() == "soft":
#         soft_seats += 1
#     else:
#         print("invalid entry: counted as hard")
#         hard_seats += 1
#     seat_count += 1
#     if seat_count >= num_seats:
#         print("\nseats are full")
#         break
#
# print(seat_count, "Seats Total: ", hard_seats, "hard and", soft_seats, "soft")

# #Shirt Count
# sizes = 0
# small_size = 0
# medium_size = 0
# large_size = 0
# size_count = 4
# while True:
#     size = input("Enter the size you want (S, M, L): ")
#     if size.lower() == "s":
#         small_sizes += 1
#     elif size.lower() == "m":
#         medium_sizes += 1
#     elif size.lower() == "l":
#         large_sizes += 1
#     else:
#         print("Enter correct size")
#     if sizes >= size_count:
#         print("Sizes have finished")
#         break
#
# num_1 = ""
# num_temp = ""
# num_final = ""
#
# while True:
#     num_1 = input("Enter an integer: ")
#     if num_1.isdigit():
#         num_final = num_temp + num_1
#         num_temp = num_final
#     else:
#         print(num_final)
#         break



# student_fname = ""
# while student_fname.isalpha() == True:
#     student_fname = input("Enter Name with no digits not spaces: ")
#     print(student_fname)


# int_num = input("Enter Number (Only digits): ")
# long_num = ""
#
# while int_num.isdigit() == True:
#     long_num = int_num
#     int_num = input("Enter Number (Only digits): ")
#     print(long_num)
#     break
#


# count = 1
#
# # loop 5 times
# while count < 6:
#     print(count, "x", count, "=", count*count)
#     count +=1

# x = 0
#
# while x < 5:
#     x += 1
#     print('loop')

# def quote_me(s):
#     new_string = s + "!"
#     return new_string
# print(quote_me("ridbay"))

# def quote_me():
#     s =input("Enter the value of string: ")
#     new_string = s
#     return new_string
# print(quote_me())

# def quote_me(s):
#     string_arg = "\"" + s +"\""
#     return string_arg
# print(quote_me("Ridbay"))

# tickets = int(input("enter tickets remaining (0 to quit): "))
#
#
# while tickets > 0:
#         # if tickets are multiple of 3 then "winner"
#     if tickets/3:
#         print("you win!")
#     else:
#         print("sorry, not a winner.")
#     tickets = int(input("enter tickets remaining (0 to quit): "))
#
# print("Game ended")

# student_name = input("Enter your name: ")
#
# if student_name[0].lower() == "b":
#     print("Your name starts with", student_name)
# elif student_name[0].lower() == "r":
#     print("Your name starts with",student_name)
# else:
#     print("I can\'t read what you wrote")


# long_word = "juxtaposition"
# for letter in long_word:
#     print(letter)

# fav_color = input("Enter your favourite color: ")
# # for color in fav_color[::-1]:
# #     color += color
# #     print(color)
# long_word = "juxtaposition is bitch"
# len_long_word = len(long_word)
# mid_point = int(len_long_word/2)
# print(long_word[mid_point:])

# long_word = "juxtaposition is bitch"
# slicing = long_word[7:]
#
# print(slicing.count("i"))


# random_tip = "wear a hat when it rains"
# half_tip = int(len(random_tip)/2)
# print(random_tip[:half_tip])
# print(random_tip[half_tip:])
# print(random_tip.count("e"))
# print(random_tip.count("a"))
# if random_tip.count("a") > random_tip.count("e"):
#     print("\"a\" is more frequent")
# else:
#     print("\"e\" is more frequent")

# long_word = "juxtaposition"
# where_is = long_word.find("t",3,9)
# print(long_word[where_is:10])

# quote = "they stumble who run fast"
# start = 0
# space_index = quote.find(" ")
# while space_index != -1:
#     print(quote[start:space_index])
#     start = (space_index + 1)
#     space_index = quote.find(" ", start)
# print(quote[start:])

# my_list = ["Ridbay", "Balogun"]
# typeof = type(my_list)
# print(typeof,my_list)


# streets = ["Adegbayi", "Adeogun", "Balogun", "Timileyin", "Ademola", "Ajasa"]
# parking = "No Parking"
# print(parking,"on",streets[0], "or " + streets[4], "streets.")

# num_2_add = [4,5,6,7,8]
# print(num_2_add[0] + num_2_add[1] + num_2_add[2] + num_2_add[3] +num_2_add[4])

# pay_checks = [1,2,3,4,5]
# print(" Total of checks 3 & 4 = $", pay_checks[2] + pay_checks[3])

# cur_values = [.01, .05, 0.2, 0.3, 0.4]
# print(cur_values)
# cur_values.append(0.7)
# print(cur_values)
# add_cur = cur_values.append(float(input("Enter the currency: ")))
# print(cur_values)

# bday_survey = []
#
# while True:
#     bday = input("Enter the day of the month of your birthday: ")
#
#     if bday == "q":
#         break
#
#     elif bday.isnumeric():
#         if int(bday) > 0 and int(bday) < 32:
#             bday_survey.append(bday)
#         else:
#             print("Invalid input.")
#
#     else:
#         print("Invalid input.")
#
# print(bday_survey)


# single_digits = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
# print("single_digits: ", single_digits)
# print("single_digits[3]: ", single_digits[3], type(single_digits[3]),"\n")
# single_digits[3] = 3
# print("single_digits: ", single_digits)
# print("single_digits[3]: ", single_digits[3], type(single_digits[3]))

# three_num = [8,4,5]
# print(three_num)
# if three_num[0] < 5:
#     three_num[0] = "small"
# else:
#     three_num[0] = "large"
# print(three_num)

# three_words = ["RIDWAN", "BABATUNDE", "BALOGUN"]
# print(three_words)
# three_words[0] = three_words[0].title()
# three_words[2] = three_words[2].swapcase()
# print(three_words)

#
# ft_bones = ["calcaneus", "talus", "cuboid", "navicular", "lateral cuneiform", "intermediate cuneiform", "medial cuneiform"]
# print(ft_bones)
# del ft_bones[2]
# del ft_bones[2]
# print(ft_bones)

# ft_bones = ["calcaneus", "talus", "cuboid", "navicular", "lateral cuneiform",
#             "intermediate cuneiform", "medial cuneiform"]
# ft_bones.pop()
# ft_bones.pop(0)
# print(ft_bones)

# dogs = ["Lab", "Pug", "Poodle", "Poodle", "Pug", "Poodle"]
# print("Before: ", dogs)
# while "Poodle" in dogs:
#     dogs.remove("Poodle")
#     print(dogs)
#
#
# team_a = [0,2,2,2,4,4,4,5,6,6,6]
# team_b = [0,0,0,1,1,2,3,3,3,6,8]
# print("Team A: ",team_a,"\nTeam B: ", team_b)
# team_total = team_a + team_b
# team_a.extend(team_b)
# print(team_a)


# all_num = []
# zero_nine = 9
# for numb1 in range(zero_nine):
#    all_num == all_num.append(numb1)
# ten_onehundred = 101
# for numb2 in range(10,ten_onehundred,10):
#     all_num == all_num.append(numb2)
# print("Normal order: ", all_num)
# all_num.reverse()
# print("Reversed order: ", all_num)
# num_len = len(all_num)
# print("Three multiple")
# for num in all_num:
#     if num/3 == int(num/3):
#         print(num)
#     else:
#         pass


# count_list = list(range(21))
# print("before list:",count_list)
# count_list.reverse()
# print("After reversed:",count_list)



# # mult_5 = list(range(0,101,5))
# mult_51 = list(range(101))
# for num in mult_51:
#     if num/5 == int(num/5):
#         print(num)
#     else:
#         pass


# fours = list(range(0,44,4))
# more_fours = list(range(0,44,4))
# more_fours.reverse()
# all_fours = more_fours + fours
# print("Unsorted fours:", all_fours)
# all_fours.sort()
# print("Sorted fours:", all_fours)

# visited_cities = ["New York", "Shanghai", "Munich", "Tokyo", "Dubai", "Mexico", "Sao Paulo", "Hyderabad"]
# visited_cities.sort()
# for city in visited_cities:
#     if city.:
#         print(city)
#     else:
#         pass



# rhyme = 'Jack and Jill went up the hill To fetch a pail of water'
# rhyme_words = rhyme.split()
# print(rhyme_words)
#
# for words in rhyme_words:
#     print(words)
#
# rhyme_words.reverse()
# print(rhyme_words)


# code_tip = "Python uses spaces for indentation"
# code_tip_list = code_tip.split()
# code_tip_list_len = len(code_tip_list)
# print(code_tip_list[0:code_tip_list_len:2])

# poem = "Write code frequently*Save code frequently*Comment code frequently*Study code frequently*"
# poem_split = poem.split("*")
#
# for word in poem_split:
#     print(word)


# letters = ["A", "s", "t", "e", "r", "i", "s", "k"]
# to_join = "*"
#
# print(to_join.join(letters))

# separator = input(" Enter one of these separators (" ", *, -, etc):")
# phrase_words = ['Jack', 'and', 'Jill', 'went', 'up', 'the', 'hill', 'To', 'fetch', 'a', 'pail', 'of', 'water']
# output = separator.join(phrase_words)
# print(output)

# word = "The String"
# for words in word:
#     print(words, end="-")
#     print(words, end="-")
#     print(words, end="-")

# Msg_characters = list("Always test your code")
# fact = "I love my boo so much that I am so obsessed about her"
# fact_letters = list(fact)
# for word in fact_letters:
#     print(word, end= "\n")

#
# digi = "2,3,4,5,6,7,8,9,23,43,3,56,76,54,6,33,45,32,66,70"
# digi_split = digi.split(",")
# sum_total= ""
# for word in digi_split:
#     print("+".join(word))

# adj = ["red", "big", "tasty"]
# fruits = ["apple", "banana", "cherry"]
# mats = ["things", "stuffs"]
# for x in adj:
#     for y in fruits:
#         for z in mats:
#             print(x,y,z)


# def tri_recursion(k):
#   if(k>0):
#     result = k+tri_recursion(k-1)
#     print(result)
#   else:
#     result = 0
#   return result
#
# print("\n\nRecursion Example Results")
# tri_recursion(3)
#
# n = input("Please enter 'hello':")
# while n == 'hello':
#     n = input("Please enter 'hello':")
#
# while True:
#     n = input("Please enter 'hello':")
#     if n.strip() == 'hello':
#         break



# while True:
#     reply = input('Enter text, [type "stop" to quit]: ')
#     print(reply.lower())
#     if reply == 'stop':
#         break



# numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]
#
# # variable to store the sum
# sum = 0
#
# # iterate over the list
# for val in numbers:
# 	sum = sum+val
#
# # Output: The sum is 48
# print("The sum is", sum)


# Python program to check if the input number is prime or not

# num = 9
#
# # take input from the user
# # num = int(input("Enter a number: "))
#
# # prime numbers are greater than 1
# if num > 1:
#     # check for factors
#     for i in range(2, num):
#         if (num % i) == 0:
#             print(num, "is not a prime number")
#             print(i, "times", num // i, "is", num)
#             break
#     else:
#         print(num, "is a prime number")
#
# # if input number is less than
# # or equal to 1, it is not prime
# else:
#     print(num, "is not a prime number")



#
# x = -2
#
# if x > 0:
#     print("This is a positive number")
# elif x == 0:
#     print("This is Zero")
# else:
#     print("This is a negative number")



# # change the value for a different result
# num = 7
#
# # uncomment to take input from the user
# #num = int(input("Enter a number: "))
#
# factorial = 1
#
# # check if the number is negative, positive or zero
# if num < 0:
#    print("Sorry, factorial does not exist for negative numbers")
# elif num == 0:
#    print("The factorial of 0 is 1")
# else:
#    for i in range(1,num + 1):
#        print(i)
#        factorial *= i
#    print("The factorial of",num,"is",factorial)

# import cmath
# a = 1
# b = 5
# c = 6
#
# # To take coefficient input from the users
# # a = float(input('Enter a: '))
# # b = float(input('Enter b: '))
# # c = float(input('Enter c: '))
#
# # calculate the discriminant
# d = (b**2) - (4*a*c)
#
# # find two solutions
# sol1 = (-b-cmath.sqrt(d))/(2*a)
# sol2 = (-b+cmath.sqrt(d))/(2*a)
#
# print('The solution are {0} and {1}'.format(sol1,sol2))



# s = (a+b+c)/2
# area = √(s(s-a)*(s-b)*(s-c))

# # Naira to dollar converion
#
# dollar = float(input("Enter dollar amount: "))
# naira = 363.00
# convert_cur = naira * dollar
#
#print("$"+ str(dollar),"equals",convert_cur,"in Naira")




