import argparse

def __main__():
    parser = argparse.ArgumentParser() #use argparse to get filename from commandline input
    parser.add_argument('-n', '--normalise', type=str)
    parser.add_argument('-t', '--table', type=str)

    args = parser.parse_args()
    
    filename = args.normalise #get parameters (filename)
    table = args.table

    tableContent = getSQL(filename, table)

    FindPrimary(tableContent, table)

def getSQL(filename, table): #get specific SQL table as an array
    fs = open(filename, 'r')
    content = fs.readlines()
    fe.close()

    start = 0
    end = 0
    returnList = []

    for i in range (0, len(content)):
        wordsinline = content[i].split(' ')
        if (len(wordsinline) == 3):
            if (wordsinline[0] == "CREATE" and wordsinline[1] == "TABLE" and wordsinline[2].strip('(') == table): #means wanted table contained below
                start = i
                end = getEndOfSQL(content, start)
                break

            for i in range (start, end): #add table details to returnList
                returnList.append(content[i])

    return returnList

def getEndOfSQL(content, start): #get where the specific SQL table ends
    for i in range(start, content.length):
        if (')' in content[i]):
            return i
        
    return 0

def FindPrimary(tableContent, tableName): #see if table contains a primary key
    for i in range (0, len(tableContent)):
        wordsinline = tableContent[i].split(' ')
        if (len(wordsinline) == 3):
            if (wordsinline[0] == "PRIMARY" and wordsinline[1] == "KEY"): #means table has defined primary key
                print("Table contains 1 primary key: "+ wordsinline[2])
                return wordsinline[2] # return the primary key

    print("Table contains 0 primary keys")
    print("Creating Primary Key...")

    AddSQL("""ALTER TABLE """+tableName+""""
        ADD [ID] INT IDENTITY PRIMARY KEY
        GO""")

def AddSQL(sqlString): #Add an sql string to a new file
    fsql = open("TableAdd.sql", 'a')

    fsql.writelines(sqlString)

    fsql.close()