import argparse

def __main__():
    parser = argparse.ArgumentParser() #use argparse to get filename from commandline input
    parser.add_argument('-n', '--normalise', type=str)
    parser.add_argument('-t', '--table', type=str)

    args = parser.parse_args()
    
    filename = args.normalise #get parameters (filename)
    table = args.table

    tableContent = getSQL(filename, table)

def getSQL(filename, table): #get specific SQL table as an array
    fs = open(filename, 'r')
    content = fs.readlines()

    start = 0
    end = 0
    returnList = []

    for i in range (0, len(content)):
        wordsinline = content[i].split(' ')
        if (wordsinline[0] == "CREATE" and wordsinline[1] == "TABLE" and wordsinline[2].strip('(') == table): #means wanted table contained below
            start = i
            end = getEndOfSQL(content, start)
            break

    for i in range (start, end):
        returnList.append(content[i])

    return returnList

def getEndOfSQL(content, start): #get where the specific SQL table ends
    for i in range(start, content.length):
        if (')' in content[i]):
            return i
        
    return 0