# Uses python3
def edit_distance(s, t):
    numRows = len(s)
    numColumns = len(t)
    distances = [[] for i in range(0, numRows + 1)]
    # go down the first column
    for i in range(0, numRows + 1):
        distances[i].append(i)
    # go acress the first row
    for j in range(1, numColumns + 1):
        distances[0].append(j)

    for i in range(1, numRows + 1): #go down column
        for j in range(1, numColumns + 1): #go across row
            insert = distances[i][j - 1] + 1
            delete = distances[i - 1][j] + 1
            mismatch = distances[i - 1][j - 1] + 1
            match = distances[i - 1][j - 1]
            if s[i - 1] == t[j - 1]:
                distances[i].append(match)
            else:
                distances[i].append(min(insert, delete, mismatch))

    return distances[numRows][numColumns]

if __name__ == "__main__":
    print(edit_distance(input(), input()))
