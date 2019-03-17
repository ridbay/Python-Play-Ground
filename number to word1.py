unit = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
unit_ten = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen",
            "seventeen", "eighteen", "nineteen"]
tens = ["zero", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", 
        "eighty", "ninety"]


def unit_convert(number):
    if int(number) < 1:
        return ""
    else:
        return unit[int(number)]


def tens_convert(number):
    if int(number) < 10:
        return unit_convert(number[1])
    elif (int(number) > 9) and (int(number) < 20):
        return unit_ten[int(number[1])]
    elif int(number[1]) == 0:
        return tens[int(number[0])]
    else:
        return tens[int(number[0])] + "-" + unit_convert(number[1])


def hundred_convert(number):
    if int(number) < 100:
        return " and " + tens_convert(number[1:])
    elif number[1:] == "00":
        return unit_convert(number[0]) + " hundred"
    else:
        return unit_convert(number[0]) + " hundred and " + tens_convert(number[1:])


def thousand_convert(number):
    if int(number) < 1000:
        return hundred_convert(number[1:])
    elif number[1:] == "000":
        return unit_convert(number[0]) + " thousand"
    else:
        return unit_convert(number[0]) + " thousand, " + hundred_convert(number[1:])


def ten_thousand_convert(number):
    if int(number) < 10000:
        return thousand_convert(number[1:])
    elif number[1:] == "0000":
        return tens_convert(number[0:2]) + " thousand"
    else:
        return tens_convert(number[0:2]) + " thousand " + hundred_convert(number[2:])


def hundred_thousand_convert(number):
    if int(number) < 100000:
        return " and " + ten_thousand_convert(number[1:])
    elif number[1:] == "0000":
        return tens_convert(number[0:2]) + " hundred thousand"
    else:
        return hundred_convert(number[0:3]) + " thousand " + hundred_convert(number[3:])


def million_convert(number):
    if int(number) < 1000000:
        return hundred_thousand_convert(number[1:])
    elif number[1:] == "000000":
        return unit_convert(number[0]) + " million"
    else:
        return unit_convert(number[0]) + " million, " + hundred_thousand_convert(number[1:])


def ten_million_convert(number):
    if int(number) < 10000000:
        return million_convert(number[1:])
    elif number[2:] == "000000":
        return tens_convert(number[0:2]) + " million"
    else:
        return tens_convert(number[0:2]) + " million, " + hundred_thousand_convert(number[2:])


def hundred_million_convert(number):
    if int(number) < 100000000:
        return ten_million_convert(number[1:])
    elif number[1:] == "00000000":
        return hundred_convert(number[0:3]) + " million"
    else:
        return hundred_convert(number[0:3]) + " million, " +  \
               hundred_thousand_convert(number[3:])


def billion_convert(number):
    if int(number) < 1000000000:
        return hundred_million_convert(number[1:])
    elif number[:] == "1000000000":
        return "One billion"
    else:
        return "Hello there, computer get tired too, work that out yourself"
    
    
user = input("Enter a value between 1 and 900 and I will change it into word for you")
while True:
    if user.isdigit():
        if len(user) == 1:
            value = unit_convert(user)
            break
        elif len(user) == 2:
            value = tens_convert(user)
            break
        elif len(user) == 3:
            value = hundred_convert(user)
            break
        elif len(user) == 4:
            value = thousand_convert(user)
            break
        elif len(user) == 5:
            value = ten_thousand_convert(user)
            break
        elif len(user) == 6:
            value = hundred_thousand_convert(user)
            break
        elif len(user) == 7:
            value = million_convert(user)
            break
        elif len(user) == 8:
            value = ten_million_convert(user)
            break
        elif len(user) == 9:
            value = hundred_million_convert(user)
            break
        elif len(user) == 10:
            value = billion_convert(user)
            break
        else:
            print("Hello there, computer get tired too, work that out yourself")
            user = input("Enter a value between 1 and 1000000 and I will change it into \
                         word for you:\n")


    else:
        print("You are inputting a non-integer value")
        user = input("Enter a value between 1 and 1000000 and I will change it into \
                     word for you:\n")

print("The value of {0} in word is: ".format(value))
print("*" * 20)
print()
print("{0}".format(value))
print()
print("*" * 20)