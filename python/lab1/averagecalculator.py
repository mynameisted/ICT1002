import sys

try:
    if len(sys.argv) != 4:
        print("Invalid number of arguments.\nUsage: averagecalculator.py [value1] [value2] [value3]")
        sys.exit()
    a = float(sys.argv[1])
    b = float(sys.argv[2])
    c = float(sys.argv[3])
except ValueError:
    print("Your input is invalid!")
    sys.exit()

avrg = (a+b+c)/3
print "Average:%1.2f" % avrg