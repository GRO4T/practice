import time
TABLE_DATA = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(tableData):
    columnWidthList = [0] * len(tableData)
    for i in range(len(tableData)):
        for elem in tableData[i]:
            if (len(elem) > columnWidthList[i]):
                columnWidthList[i] = len(elem)

    for i in range(len(tableData[0])):
        row = ""
        for j in range(len(tableData)):
            s = tableData[j][i].rjust(columnWidthList[j] + 1)
            row += s
        print(row)

start_time = time.time()
printTable(TABLE_DATA)
print("--- %s seconds ---" % (time.time() - start_time))
