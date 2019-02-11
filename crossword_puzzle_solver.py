
def direction(puzzle_board):
    '''finds all possible direction a word could be located'''

    # directions of move
    direction = {
        "left":[], "right":[],
        "top":[], "down":[],
        "top left":[], "top right":[],
        "down left":[], "down right":[]
    }

    # get row size
    l = len(puzzle_board)
    # get column size
    w = len(puzzle_board[0])
    
    # going right
    for i in range(l):
        for j in range(w):
            direction["right"].append([puzzle_board[i][j], (i, j)])

    # going left
    nl = list(direction["right"])
    nl.reverse()
    direction["left"] = nl

    # going down
    for j in range(w):
        for i in range(l):
            direction["down"].append([puzzle_board[i][j], (i, j)])

    # going top
    nl = list(direction["down"])
    nl.reverse()
    direction["top"] = nl

    # going topright
    for i in range(l+w-1):
        for j in range(max(i-l+1, 0), min(i+1, w)):
            direction["top right"].append([puzzle_board[i-j][j], (i-j, j)])
    
    # going downleft
    nl = list(direction["top right"])
    nl.reverse()
    direction["down left"] = nl

    # going downright
    for i in range(l+w-1):
        for j in range(max(i-l+1, 0), min(i+1, w)):
            direction["down right"].append([puzzle_board[l-i+j-1][j], (l-i+j-1, j)])

    # going topleft
    nl = list(direction["down right"])
    nl.reverse()
    direction["top left"] = nl

    return direction              

def wrapAroundDirection(puzzle_board):
    '''finds wrapping around directions'''

    dict = {
        "wrap right": [],
        "wrap left": [],
        "wrap down": [],
        "wrap up":[]
    }

    l = len(puzzle_board)
    w = len(puzzle_board[0])

    # directions for wrap right and left
    for k in range(l):
        wrapRowRight = []
        wrapRowLeft = []
        for i in range(1, w-1):
            row = []
            for j in range(w):
                char = puzzle_board[k][(i + j) % w]
                row.append([char, (k, (i + j) % w)])
            # insert into wrap row right direction
            wrapRowRight.append(row)
            # copy list
            newRow = list(row)
            # reverse list
            newRow.reverse()
            # insert into wrap left direction
            wrapRowLeft.append(newRow)

        # append to direction value
        dict.get("wrap right").append(wrapRowRight)
        dict.get("wrap left").append(wrapRowLeft)
    
    # directions for wrap down and top
    for k in range(w):
        wrapColDown = []
        wrapColUp = []
        for i in range(1, l-1):
            col = []
            for j in range(l):
                char = puzzle_board[(i + j) % l][k]
                col.append([char, ((i + j) % l, k)])
            # insert into wrap col down direction
            wrapColDown.append(col)
            # copy list
            newCol = list(col)
            # reverse list
            newCol.reverse()
            # insert into wrap left direction
            wrapColUp.append(newCol)

        # append to direction value
        dict.get("wrap down").append(wrapColDown)
        dict.get("wrap up").append(wrapColUp)

    return dict


def join2DString(lst):
    '''Concatenats list of str chars from dict with 2D list values'''

    return ''.join([r[0] for r in lst])


def join3DString(dlst):
    '''Concatenats list of str chars from dict with 2D list values'''

    strList = []
    for k in range(len(dlst)):
        lst = []
        for item in dlst[k]:
            str = []
            for r in item:
                str.append(r[0])
            lst.append(''.join(str))
        strList.append(lst)

    return strList


def strMatching(pattern, text):
    '''does string matching char by char'''

    txtLen = len(text)
    patLen =  len(pattern)
    for i in range(txtLen - patLen + 1):
        for j in range(patLen):
            if text[i+j] != pattern[j]:
                break
            if j == patLen - 1:
                return i


def solvePuzzle(puzzle_board, word_lst):
    '''finds all occurence of word in crossword puzzle'''

    # get possible direction
    directions = direction(puzzle_board)
    wrapAroundDirections = wrapAroundDirection(puzzle_board)

    # searching for pattern
    for word in word_lst:

        for key in directions:
            str = join2DString(directions[key])

            # get matching indices
            ind = strMatching(word, str)
            if ind != None:
                print("recognizing {0} in puzzle ".format(word))
                pos = directions[key][ind][1]
                print("direction is: ", key)
                print("starting position is: ", pos)
                # print empty line
                print()
                # break out of loop assuming
                break

        # search wrap around directions
        if ind == None:
            for key, value in wrapAroundDirections.items():
                strList = join3DString(value)
                for i in range(len(strList)):
                    for j in range(len(strList[i])):
                        ind = strMatching(word, strList[i][j])
                        if ind != None:
                            print("recognizing {0} in puzzle ".format(word))
                            pos = value[i][j][ind][1]
                            print("direction is: ", key)
                            print("starting position is: ", pos)
                            # print empty line
                            print()
                            # break out of loop
                            break
                    # break out of loop
                    if ind != None:
                        break



if __name__ == "__main__":
    # puzzle board 1
    # puzzle_board1 = [

    #     ["T", "P", "G", "S", "B", "S", "B", "E", "R"],
    #     ["U", "D", "Y", "B", "E", "E", "F", "E", "O"],
    #     ["H", "B", "W", "T", "E", "R", "G", "I", "B"],
    #     ["T", "Z", "C", "N", "H", "D", "E", "E", "B"],
    #     ["I", "E", "E", "W", "Z", "O", "S", "V", "I"],
    #     ["G", "C", "H", "A", "N", "B", "N", "Q", "E"]   

    # ]
    
    # # words list
    # word_lst1 = ["PYTHON", "GITHUB", "ROBBIE", "BEEF", "BERT", "WAS"]

    # puzzle board 2
    puzzle_board2 = [
            ["#", "C", "#", "#", "P", "%", "#", "O", "#"],
            ["S", "A", "T", "E", "L", "L", "I", "T", "E"],
            ["#", "N", "I", "N", "E", "S", "#", "T", "A"],
            ["%", "A", "B", "#", "A", "#", "G", "A", "S"],
            ["%", "D", "E", "N", "S", "E", "%", "W", "E"],
            ["C", "A", "T", "H", "E", "D", "R", "A", "L"],
    ]

    # words list
    word_lst2 = [
        "SATELLITE", "CATHEDRAL", "CANADA", "PLEASE",
        "OTTAWA", "TIBET", "EASEL", "NINES", "DENSE",
        "GAS", "LS", "TA", "AB", "NH", "ED", "WE", "DRALC",
        "DACAN", "TA#", "##C#"
    ]

    # run puzzle solver
    solvePuzzle(puzzle_board2, word_lst2)
