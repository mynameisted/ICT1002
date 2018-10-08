from collections import Counter

regconAmt = []
nonregconAmt = []
top5Regi = []
top5Nonregi = []
regconList = []
nonregconList = []


def top5(regconList,nonregconList,supplyList):
    print "Function 5: Tabulating total awards.."
    conAmt = []

    for i in range(len(supplyList)):
        conAmt.append([supplyList[i]['supplier_name'], supplyList[i]['awarded_amt']])

    # Adding up procurement amount
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
    
    # Sort registered contractors according to total amount in decending
    regconAmt.sort(key=lambda x: x[1], reverse=True)
    # Sort non-registered contractors according to total amount in decending
    nonregconAmt.sort(key=lambda x: x[1], reverse=True)

    # Print top 5 registered contractors
    for i in range(len(regconAmt)):
        if i < 5:
            top5Regi.append(regconAmt[i])

    for i in range(len(nonregconAmt)):
        if i < 5:
            top5Nonregi.append(nonregconAmt[i])
    print "Function 5: Completed.."
    return {"regConAwards":regconAmt, "unregConAwards":nonregconAmt, "top5Reg":top5Regi, "top5Unreg":top5Nonregi}


