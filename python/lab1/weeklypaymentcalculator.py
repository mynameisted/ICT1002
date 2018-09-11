import sys
overtimeHours = 0
try:
    if len(sys.argv) != 4:
        sys.exit("Invalid number of arguments.\nUsage: weeklypaymentcalculator.py [Working Hours] [Normal Rate] [Overtime Rate]")
    elif float(sys.argv[1]) < 0 or float(sys.argv[1]) > 168:
        print("Your input is invalid!")
        sys.exit(0)
    elif float(sys.argv[2]) < 0:
        print("Please key in a valid rate for working hours.")
    elif float(sys.argv[3]) < 0:
        print("Please key in a valid rate for extra hours.")
    totalHours = float(sys.argv[1])
    normalRate = float(sys.argv[2])
    overtimeRate = float(sys.argv[3])
except ValueError:
    print "Your input is invalid!"

if totalHours > 40:
    normalHours = 40.0
    overtimeHours = totalHours - normalHours
else:
    normalHours = totalHours

#print 'Normal Hours:',str(normalHours)
#print 'Overtime Hours:',str(overtimeHours)
#print 'Normal Rate:',str(normalRate)
#print 'Overtime Rate:',str(overtimeRate)

normalSalary = normalHours * normalRate
overtimeSalary = overtimeHours * overtimeRate
totalSalary = normalSalary + overtimeSalary

print 'Normal Salary:%1.2f, Extra Salary:%1.2f, Total Salary:%1.2f' %(normalSalary, overtimeSalary, totalSalary)

#print 'Salary for normal hours is:%1.2f' %normalSalary
#print 'Salary for extra hours is:%1.2f' %overtimeSalary
#print 'Total salary is:%1.2f' %totalSalary
#print "%1.2f" % avrg
