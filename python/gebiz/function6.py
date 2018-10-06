import csv
import pandas as pd
import matplotlib.pyplot as plt

def recategorize(originalcsvfile):

    pd.set_option('display.max_columns', None)
    pd.set_option('display.expand_frame_repr', False)
    pd.set_option('max_colwidth', -1)

    df = pd.read_csv(originalcsvfile,sep=",",usecols=["tender_no.","agency","awarded_amt"])

    a = df.groupby('agency').sum()

    a.to_csv("Total spending by agency.csv")

    with open('Total spending by agency.csv', mode='r') as infile:
        reader = csv.reader(infile)
        mydict = {rows[0]:rows[1] for rows in reader}

        authorities = list()
        for k, v in mydict.iteritems():
            if 'authority' in k.lower():
                authorities.append(v)
        authres = map(float, authorities)
        authval = sum(authres)

        cncagn = list()
        for k, v in mydict.iteritems():
            if 'council' in k.lower():
                cncagn.append(v)
            elif 'agencies' in k.lower():
                cncagn.append(v)
            elif 'environment' in k.lower():
                cncagn.append(v)
        cncagnres = map(float, cncagn)
        cncagnval = sum(cncagnres) - 19744616.76 - 29261830.7

        edu = list()
        for k, v in mydict.iteritems():
            if 'college' in k.lower():
                edu.append(v)
            elif 'school' in k.lower():
                edu.append(v)
            elif 'polytechnic' in k.lower():
                edu.append(v)
            elif 'education' in k.lower():
                edu.append(v)
            elif 'university' in k.lower():
                edu.append(v)
            elif 'skillsfuture' in k.lower():
                edu.append(v)
        edures = map(float, edu)
        eduval = sum(edures) - 630418.7 - 2639524683 - 630418.7

        law = list()
        for k, v in mydict.iteritems():
            if 'general' in k.lower():
                law.append(v)
            elif 'judiciary' in k.lower():
                law.append(v)
            elif 'intellectual' in k.lower():
                law.append(v)
        lawres = map(float, law)
        lawval = sum(lawres) - 22378538.2

        boards = list()
        for k, v in mydict.iteritems():
            if 'board' in k.lower():
                boards.append(v)
            elif 'association' in k.lower():
                boards.append(v)
            elif 'iseas' in k.lower():
                boards.append(v)
            elif 'competition' in k.lower():
                boards.append(v)
            elif 'international' in k.lower():
                boards.append(v)
            elif 'jurong' in k.lower():
                boards.append(v)
            elif 'spring' in k.lower():
                boards.append(v)
            elif 'workforce' in k.lower():
                boards.append(v)
            elif 'labour' in k.lower():
                boards.append(v)
        boardsres = map(float, boards)
        boardsval = sum(boardsres) - 10527066.88

        misc = list()
        for k, v in mydict.iteritems():
            if 'project' in k.lower():
                misc.append(v)
            elif 'sentosa' in k.lower():
                misc.append(v)
            elif 'rehabilitative' in k.lower():
                misc.append(v)
            elif 'islam' in k.lower():
                misc.append(v)
        miscres = map(float, misc)
        miscval = sum(miscres)

        ministries = list()
        for k, v in mydict.iteritems():
            if 'ministry of' in k.lower():
                ministries.append(v)
            elif 'technology' in k.lower():
                ministries.append(v)
        ministriesres = map(float, ministries)
        ministriesval = sum(ministriesres) - 1495406.2

        pmo = list()
        for k, v in mydict.iteritems():
            if 'prime minister' in k.lower():
                pmo.append(v)
            elif 'parliament' in k.lower():
                pmo.append(v)
            elif 'istana' in k.lower():
                pmo.append(v)
        pmores = map(float, pmo)
        pmoval = sum(pmores)

        #pass info to dataframe
        col_names = ['Authorities', 'Councils & Agencies', 'Education', 'Law', 'Statutory Boards', 'Miscellaneous', 'Ministries', 'PMO']
        my_df = pd.DataFrame(columns=col_names)
        my_df.loc[len(my_df)] = [authval, cncagnval, eduval, lawval, boardsval, miscval, ministriesval, pmoval]
        my_df.to_csv('Categorized agency spending.csv')

    sizes = [my_df['Authorities'], my_df['Councils & Agencies'], my_df['Education'], my_df['Law'], my_df['Statutory Boards'], my_df['Miscellaneous'], my_df['Ministries'], my_df['PMO']]
    labels = list(col_names)
    colors = ['yellowgreen', 'lightgreen', 'darkgreen', 'gold', 'red', 'lightsalmon', 'darkred', 'orange']
    plt.pie(sizes, explode=None, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True,
            startangle=90)
    plt.axis('equal')
    plt.title('Amount Spent on Various Sectors')
    plt.legend()
    plt.show()
