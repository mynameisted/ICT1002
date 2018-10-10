'''There are 2 functions:

1) The first function(top5()) allows the display of the top 5 registered and non-registered contractors awarded with 
the most total procurement amount.

2) The second function(regiconStatistics()) calculates the registered contractors with the sum of the procurement amount
of more than $100,000 and less than $100,000 and display the percentages in a pie chart. This effectively highlights the
percentage of registered contractors who are not receiving much from the procurements.
'''

from collections import Counter
import copy
import matplotlib.pyplot as plt

regconAmt = []
nonregconAmt = []
descregconAmt = []
descnonregconAmt = []
top5Regi = []
top5Nonregi = []
regconList = []
nonregconList = []

def top5(regconList,nonregconList,supplyList):
    print "Function 5: Tabulating total awards.."
    conAmt = []
    # Storing the registered suppliers name and awarded amount to another list
    for i in range(len(supplyList)):
        conAmt.append([supplyList[i]["supplier_name"], supplyList[i]["awarded_amt"]])

    # Sum up total procurement amount
    c = Counter()
    for i, j in conAmt:
        c.update({str(i): float(j)})
    conAmt = list(c.items())

    for i in range(len(conAmt)):
        if (conAmt[i][0]) in regconList:
            # Append registered contractors and the sum of their procurement amount to a list
            regconAmt.append(conAmt[i])
        else:
            # Append non-registered contractors and the sum of their procurement amount to a list
            nonregconAmt.append(conAmt[i])

    # Make a copy of list
    descregconAmt = copy.copy(regconAmt)
    descnonregconAmt = copy.copy(nonregconAmt)

    # Sort registered contractors according to total amount in decending
    descregconAmt.sort(key=lambda x: x[1], reverse=True)
    # Sort non-registered contractors according to total amount in decending
    descnonregconAmt.sort(key=lambda x: x[1], reverse=True)

    # Append top 5 registered contractors to list
    for i in range(len(descregconAmt)):
        if i < 5:
            top5Regi.append(descregconAmt[i])
    # Append top 5 non-registered contractors to list
    for i in range(len(descnonregconAmt)):
        if i < 5:
            top5Nonregi.append(descnonregconAmt[i])

    # Returning values
    print "Function 5: Completed.."
    return {"regConAwards":regconAmt, "unregConAwards":nonregconAmt, "regConAwardsDesc":descregconAmt,"unregConAwardsDesc":descnonregconAmt,"top5Reg":top5Regi, "top5Unreg":top5Nonregi}


def regconStatistic(regconAmt):
    count = 0
    for i in range(len(regconAmt)):
        # Count number of registered contractors with total procurement < $100,000
        if(regconAmt[i][1]) < 100000:
            count += 1
        below = count
        # Count number of registered contractors with total procurement > $100,000
    above = len(regconAmt) - below

    # Pie chart(graphical representation of registered contractors procurement amount)
    labels = u'Total Procurement < $100,000', u'Total Procurement > $100,000'
    sizes = [below, above]
    fig1, ax1 = plt.subplots()
    patches, texts = plt.pie(sizes, startangle=90)
    plt.legend(patches, labels, loc="lower left")
    plt.title('Registered Contractors Procurement Amount', fontweight="bold")
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.show()
  

