import argparse
import sys

#ask user for filename and tablename to normalise
#search file for that table and isolate the table as a list
#use the list to search for various items e.g. 'PRIMARY KEY'


def main():
    fsql = open("TableAdd.sql", 'w')

    fsql.writelines("")

    fsql.close()

    parser = argparse.ArgumentParser() #use argparse to get filename from commandline input
    parser.add_argument('-n', '--normalise', type=str)
    parser.add_argument('-t', '--table', type=str)

    args = parser.parse_args()

    if len(sys.argv) > 0:
    
        filename = args.normalise #get parameters (filename)
        table = args.table

        print("Starting")

        tableContent = getSQL(filename, table)

        #print(tableContent)

        Primary = FindPrimary(tableContent, table)

        print(Primary)
    else:
        print("No parameters given")


def getSQL(filename, table): #get specific SQL table as an array
    fs = open(filename, 'r')
    content = fs.readlines()
    fs.close()

    start = 0
    end = 0
    returnList = []

    print("Searching file for SQL")

    for i in range (0, len(content)):
        #print(content[i])
        wordsinline = content[i].strip('\n')
        wordsinline = wordsinline.split(" ") #get each word from line in file
        #print(wordsinline)

        returnList.append(wordsinline)

        if len(wordsinline) > 2:
            if wordsinline[2] == ")":
                return returnList
            
        """
        count = 0    
        for word in wordsinline:
            if (word == "TABLE" and wordsinline[count+2].strip('(') == table): #search for start of TABLE
                start = i
                end = getEndOfSQL(content, start) #Find end of TABLE
                break

            for i in range (start, end): #add table details to returnList
                returnList.append(content[i])

        count=count+1
        """

    return None


def getEndOfSQL(content, start): #get where the specific SQL table ends
    for i in range(start, len(content)):
        if content[i].split(" ") == ")":
            print("content[i]: ",content[i])
            print("End of TABLE found i:",i)
            return i
        
    return 0


def FindPrimary(tableContent, tableName): #see if table contains a primary key
    """
    for i in range (0, len(tableContent)):
        wordsinline = tableContent[i].split(' ')
        print(wordsinline)
        if (len(wordsinline) == 3):
            if (wordsinline[0] == "PRIMARY" and wordsinline[1] == "KEY"): #means table has defined primary key
                print("Table contains 1 primary key: "+ wordsinline[2])
                return wordsinline[2] # return the primary key
    """

    for i in range (0, len(tableContent)):
        #print(tableContent[i])
        if "PRIMARY" in tableContent[i]:
            return tableContent[i][len(tableContent[i]) - 1].rstrip(",")

    return None


def AddSQL(sqlString): #Add an sql string to a new file
    fsql = open("TableAdd.sql", 'a')

    fsql.writelines(sqlString)

    fsql.close()


if __name__ == "__main__":
    main()