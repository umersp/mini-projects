print("Press 1 for converting CELSIUS to Farenheit \nPress 2 for Converting FARENHEIT to Celcius")
# CONVERTING CELSIUS to FARENHEIT
x = input("Enter here : ")

if x == "1":
    cel = int(input("enter celcius : "))
# calculate fahrenheit
    output= (cel * 1.8) + 32
    print(output, "F")

# CONVERTING FARENHEIT to CELSIUS

if x == "2":
    fer  = float(input("Enter farenheit :"))
    out = ((fer - 32)/1.8)
    form = " {:.2f}".format(out)
    print(out, "C")