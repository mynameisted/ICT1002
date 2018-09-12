import sys

metricValues = ['metric','Metric','METRIC']
imperialValues = ['imperial','Imperial','IMPERIAL']
acceptableUnits = metricValues + imperialValues

try:
    #Check valid number of arguments
    if len(sys.argv) != 4:
        print "Your input is invalid!"
        sys.exit("Invalid number of arguments.\nUsage: bmicalculator.py [metric/imperial] [height] [weight]")
    #If passed unit is not acceptable, or height and weight is less than 0, exit.
    elif (str(sys.argv[1]) not in acceptableUnits) or float(sys.argv[2]) <= 0 or float(sys.argv[3]) <= 0:
        print("Your input is invalid!")
        sys.exit(0)
    if sys.argv[1] in metricValues:
        unitType = 'metric'
    elif sys.argv[1] in imperialValues:
        unitType = 'imperial'
    userHeight = float(sys.argv[2])
    userWeight = float(sys.argv[3])
except ValueError:
    print "Your input is invalid!"
    sys.exit(0)

def calculateBMI (unit,height,weight):
    "Calculates the user's BMI based on his preferred unit, and categorizes it"
    if unit == 'metric':
        bmiValue = weight / height / height
    elif unit == "imperial":
        bmiValue = (weight / height / height) * 703
    if bmiValue < 16:
        bmiCategory = 'Severe Thinness'
    elif 16 <= bmiValue < 17:
        bmiCategory = 'Moderate Thinness'
    elif 17 <= bmiValue < 18.5:
        bmiCategory = 'Mild Thinness'
    elif 18.5 <= bmiValue < 25:
        bmiCategory = 'Normal'
    elif 25 <= bmiValue < 30:
        bmiCategory = 'Overweight'
    elif 30 <= bmiValue < 35:
        bmiCategory = 'Obese Class I'
    elif 35 <= bmiValue < 40:
        bmiCategory = 'Obese Class II'
    elif bmiValue >= 40:
        bmiCategory = 'Obese Class III'
    return('%0.2f\t%s' % (bmiValue, bmiCategory))

print calculateBMI(unitType,userHeight,userWeight)