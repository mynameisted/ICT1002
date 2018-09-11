import sys

try:
    if len(sys.argv) != 4:
        print("Invalid number of arguments.\nUsage: calculator.py [value1] [value2] [value3]")
    a = float(sys.argv[1])
    b = float(sys.argv[2])
    c = float(sys.argv[3])
except ValueError:
    print("Your input is invalid!")

avrg = (a+b+c)/3
print "Average:%1.2f" % avrg