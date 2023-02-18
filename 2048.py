import random
import time
import tkinter


class Globals():
    rootWindow = None
    TopOne = None
    TopTwo = None
    TopThree = None
    TopFour = None
    SecondOne = None
    SecondTwo = None
    SecondThree = None
    SecondFour = None
    ThirdOne = None
    ThirdTwo = None
    ThirdThree = None
    ThirdFour = None
    FourthOne = None
    FourthTwo = None
    FourthThree = None
    FourthFour = None
    TileDict = {}
    GraphicList = []
    CurrentScore = 0
    ClearButton = None
    CurrentScoreText = None
    GameState = True
    ExecuteUp = True
    ExecuteLeft = True
    ExecuteDown = True
    ExecuteRight = True
    choiceVar = 0
    currentAlg = None
    currentVal = 0
    ExecutedDict = {(1, 1): False, (1, 2): False, (1, 3): False, (1, 4): False, (2, 1): False, (2, 2): False, (2, 3): False, (2, 4)
                     : False, (3, 1): False, (3, 2): False, (3, 3): False, (3, 4): False, (4, 1): False, (4, 2): False, (4, 3): False, (4, 4): False}


class Spawns:
    def __init__(self, value=2, row=random.randint(1, 4), column=random.randint(1, 4)):
        self.value = value
        self.row = row
        self.column = column
        self.grid = (row, column)

    def __repr__(self):
        return ("{} tile in row {} column {}".format(self.value, self.row, self.column))


def change(self, value):

    if value == 2:
        color = "eee4da"
        textColor = "776e65"
    elif value == 4:
        color = "ede0c8"
        textColor = "776e65"
    elif value == 8:
        color = "f2b179"
        textColor = "f9f6f2"
    elif value == 16:
        color = "f59563"
        textColor = "f9f6f2"
    elif value == 32:
        color = "f67c5f"
        textColor = "f9f6f2"
    elif value == 64:
        color = "f65e3b"
        textColor = "f9f6f2"
    elif value == 128:
        color = "edcf72"
        textColor = "f9f6f2"
    elif value == 256:
        color = "edcc61"
        textColor = "f9f6f2"
    elif value == 512:
        color = "edc850"
        textColor = "f9f6f2"
    elif value == 1024:
        color = "edc53f"
        textColor = "f9f6f2"
    elif value == 2048:
        color = "edc22e"
        textColor = "f9f6f2"
    elif value > 2048:
        color = "3c3a32"
        textColor = "f9f6f2"

    self.delete('all')
    self.configure(bg="#{}".format(color))
    self.create_text(50, 50, text="{}".format(value), font=(
        'Helvetica bold', 40), fill="#{}".format(textColor))
    return


def changeBack(self):
    self.configure(bg="#ccc0b3")
    self.delete('all')
    return


def spawnTile():
    temp = random.randint(1, 10)
    if temp == 1:
        value = 4
    else:
        value = 2
    row = random.randint(1, 4)
    column = random.randint(1, 4)
    tile = Spawns(2, row, column)
    if (row, column) in Globals.TileDict:
        spawnTile()
    else:
        if tile.row == 1:
            if tile.column == 1:
                change(Globals.TopOne, value)
                Globals.GraphicList.append((1, 1))
                Globals.TileDict[(1, 1)] = value
            elif tile.column == 2:
                change(Globals.TopTwo, value)
                Globals.GraphicList.append((1, 2))
                Globals.TileDict[(1, 2)] = value
            elif tile.column == 3:
                change(Globals.TopThree, value)
                Globals.GraphicList.append((1, 3))
                Globals.TileDict[(1, 3)] = value
            else:
                change(Globals.TopFour, value)
                Globals.GraphicList.append((1, 4))
                Globals.TileDict[(1, 4)] = value
        elif tile.row == 2:
            if tile.column == 1:
                change(Globals.SecondOne, value)
                Globals.GraphicList.append((2, 1))
                Globals.TileDict[(2, 1)] = value
            elif tile.column == 2:
                change(Globals.SecondTwo, value)
                Globals.GraphicList.append((2, 2))
                Globals.TileDict[(2, 2)] = value
            elif tile.column == 3:
                change(Globals.SecondThree, value)
                Globals.GraphicList.append((2, 3))
                Globals.TileDict[(2, 3)] = value
            else:
                change(Globals.SecondFour, value)
                Globals.GraphicList.append((2, 4))
                Globals.TileDict[(2, 4)] = value
        elif tile.row == 3:
            if tile.column == 1:
                change(Globals.ThirdOne, value)
                Globals.GraphicList.append((3, 1))
                Globals.TileDict[(3, 1)] = value
            elif tile.column == 2:
                change(Globals.ThirdTwo, value)
                Globals.GraphicList.append((3, 2))
                Globals.TileDict[(3, 2)] = value
            elif tile.column == 3:
                change(Globals.ThirdThree, value)
                Globals.GraphicList.append((3, 3))
                Globals.TileDict[(3, 3)] = value
            else:
                change(Globals.ThirdFour, value)
                Globals.GraphicList.append((3, 4))
                Globals.TileDict[(3, 4)] = value
        else:
            if tile.column == 1:
                change(Globals.FourthOne, value)
                Globals.GraphicList.append((4, 1))
                Globals.TileDict[(4, 1)] = value
            elif tile.column == 2:
                change(Globals.FourthTwo, value)
                Globals.GraphicList.append((4, 2))
                Globals.TileDict[(4, 2)] = value
            elif tile.column == 3:
                change(Globals.FourthThree, value)
                Globals.GraphicList.append((4, 3))
                Globals.TileDict[(4, 3)] = value
            else:
                change(Globals.FourthFour, value)
                Globals.GraphicList.append((4, 4))
                Globals.TileDict[(4, 4)] = value
    return


def updateGraphic():
    dictList = Globals.TileDict.keys()
    for a in dictList:
        if a[0] == 1:
            if a[1] == 1:
                change(Globals.TopOne, Globals.TileDict.get(a))
                Globals.GraphicList.append(a)
            elif a[1] == 2:
                change(Globals.TopTwo, Globals.TileDict.get(a))
                Globals.GraphicList.append(a)
            elif a[1] == 3:
                change(Globals.TopThree, Globals.TileDict.get(a))
                Globals.GraphicList.append(a)
            else:
                change(Globals.TopFour, Globals.TileDict.get(a))
                Globals.GraphicList.append(a)
        elif a[0] == 2:
            if a[1] == 1:
                change(Globals.SecondOne, Globals.TileDict.get(a))
                Globals.GraphicList.append(a)
            elif a[1] == 2:
                change(Globals.SecondTwo, Globals.TileDict.get(a))
                Globals.GraphicList.append(a)
            elif a[1] == 3:
                change(Globals.SecondThree, Globals.TileDict.get(a))
                Globals.GraphicList.append(a)
            else:
                change(Globals.SecondFour, Globals.TileDict.get(a))
                Globals.GraphicList.append(a)
        elif a[0] == 3:
            if a[1] == 1:
                change(Globals.ThirdOne, Globals.TileDict.get(a))
                Globals.GraphicList.append(a)
            elif a[1] == 2:
                change(Globals.ThirdTwo, Globals.TileDict.get(a))
                Globals.GraphicList.append(a)
            elif a[1] == 3:
                change(Globals.ThirdThree, Globals.TileDict.get(a))
                Globals.GraphicList.append(a)
            else:
                change(Globals.ThirdFour, Globals.TileDict.get(a))
                Globals.GraphicList.append(a)
        else:
            if a[1] == 1:
                change(Globals.FourthOne, Globals.TileDict.get(a))
                Globals.GraphicList.append(a)
            elif a[1] == 2:
                change(Globals.FourthTwo, Globals.TileDict.get(a))
                Globals.GraphicList.append(a)
            elif a[1] == 3:
                change(Globals.FourthThree, Globals.TileDict.get(a))
                Globals.GraphicList.append(a)
            else:
                change(Globals.FourthFour, Globals.TileDict.get(a))
                Globals.GraphicList.append(a)
    index = 0
    listLength = len(Globals.GraphicList)
    while index < listLength:
        if Globals.GraphicList[index] not in dictList:
            if (Globals.GraphicList[index])[0] == 1:
                if (Globals.GraphicList[index])[1] == 1:
                    changeBack(Globals.TopOne)
                    Globals.GraphicList.pop(index)
                    listLength -= 1
                elif (Globals.GraphicList[index])[1] == 2:
                    changeBack(Globals.TopTwo)
                    Globals.GraphicList.pop(index)
                    listLength -= 1
                elif (Globals.GraphicList[index])[1] == 3:
                    changeBack(Globals.TopThree)
                    Globals.GraphicList.pop(index)
                    listLength -= 1
                else:
                    changeBack(Globals.TopFour)
                    Globals.GraphicList.pop(index)
                    listLength -= 1
            elif (Globals.GraphicList[index])[0] == 2:
                if (Globals.GraphicList[index])[1] == 1:
                    changeBack(Globals.SecondOne)
                    Globals.GraphicList.pop(index)
                    listLength -= 1
                elif (Globals.GraphicList[index])[1] == 2:
                    changeBack(Globals.SecondTwo)
                    Globals.GraphicList.pop(index)
                    listLength -= 1
                elif (Globals.GraphicList[index])[1] == 3:
                    changeBack(Globals.SecondThree)
                    Globals.GraphicList.pop(index)
                    listLength -= 1
                else:
                    changeBack(Globals.SecondFour)
                    Globals.GraphicList.pop(index)
                    listLength -= 1
            elif (Globals.GraphicList[index])[0] == 3:
                if (Globals.GraphicList[index])[1] == 1:
                    changeBack(Globals.ThirdOne)
                    Globals.GraphicList.pop(index)
                    listLength -= 1
                elif (Globals.GraphicList[index])[1] == 2:
                    changeBack(Globals.ThirdTwo)
                    Globals.GraphicList.pop(index)
                    listLength -= 1
                elif (Globals.GraphicList[index])[1] == 3:
                    changeBack(Globals.ThirdThree)
                    Globals.GraphicList.pop(index)
                    listLength -= 1
                else:
                    changeBack(Globals.ThirdFour)
                    Globals.GraphicList.pop(index)
                    listLength -= 1
            else:
                if (Globals.GraphicList[index])[1] == 1:
                    changeBack(Globals.FourthOne)
                    Globals.GraphicList.pop(index)
                    listLength -= 1
                elif (Globals.GraphicList[index])[1] == 2:
                    changeBack(Globals.FourthTwo)
                    Globals.GraphicList.pop(index)
                    listLength -= 1
                elif (Globals.GraphicList[index])[1] == 3:
                    changeBack(Globals.FourthThree)
                    Globals.GraphicList.pop(index)
                    listLength -= 1
                else:
                    changeBack(Globals.FourthFour)
                    Globals.GraphicList.pop(index)
                    listLength -= 1
        else:
            index += 1


def updateChoice(a, b, temp):
    if a == 1:
        if b == 1:
            change(Globals.TopOne, temp)
        elif b == 2:
            change(Globals.TopTwo, temp)
        elif b == 3:
            change(Globals.TopThree, temp)
        else:
            change(Globals.TopFour, temp)
    elif a == 2:
        if b == 1:
            change(Globals.SecondOne, temp)
        elif b == 2:
            change(Globals.SecondTwo, temp)
        elif b == 3:
            change(Globals.SecondThree, temp)
        else:
            change(Globals.SecondFour, temp)
    elif a == 3:
        if b == 1:
            change(Globals.ThirdOne, temp)
        elif b == 2:
            change(Globals.ThirdTwo, temp)
        elif b == 3:
            change(Globals.ThirdThree, temp)
        else:
            change(Globals.ThirdFour, temp)
    else:
        if b == 1:
            change(Globals.FourthOne, temp)
        elif b == 2:
            change(Globals.FourthTwo, temp)
        elif b == 3:
            change(Globals.FourthThree, temp)
        else:
            change(Globals.FourthFour, temp)


def changeScore(temp):
    Globals.CurrentScore += temp
    Globals.CurrentScoreText.configure(state='normal')
    Globals.CurrentScoreText.delete(1.0, tkinter.END)
    Globals.CurrentScoreText.insert(
        tkinter.END, '{}'.format(Globals.CurrentScore))
    Globals.CurrentScoreText.configure(state='disabled')


def UpArrow(event=None):
    for a in Globals.ExecutedDict:
        Globals.ExecutedDict[a] = False
    executed = False
    for b in range(1, 5):
        for a in range(1, 5):
            if (a, b) in Globals.TileDict:
                if a == 1 and ((a+1), b) in Globals.TileDict:
                    if Globals.TileDict.get(((a+1), b)) == Globals.TileDict.get((a, b)):
                        temp1 = Globals.TileDict.pop(((a+1), b))
                        temp = temp1 * 2
                        Globals.TileDict.update({(a, b): temp})
                        updateChoice(a, b, temp)
                        changeScore(temp)
                        executed = True
                        Globals.ExecutedDict[(a, b)] = True
                elif a != 1 and ((a-1), b) not in Globals.TileDict:
                    if a > 2 and ((a-2), b) not in Globals.TileDict:
                        if a == 4 and ((a-3), b) not in Globals.TileDict:
                            temp = Globals.TileDict.pop((a, b))
                            Globals.TileDict[((a-3), b)] = temp
                            updateChoice((a-3), b, temp)
                            executed = True
                        elif a == 4 and Globals.TileDict.get(((a-3), b)) == Globals.TileDict.get((a, b)):
                            temp1 = Globals.TileDict.pop((a, b))
                            temp = temp1 * 2
                            Globals.TileDict.update({((a-3), b): temp})
                            updateChoice((a-3), b, temp)
                            executed = True
                        else:
                            temp = Globals.TileDict.pop((a, b))
                            Globals.TileDict[((a-2), b)] = temp
                            updateChoice((a-2), b, temp)
                            executed = True
                    elif a > 2 and Globals.TileDict.get(((a-2), b)) == Globals.TileDict.get((a, b)) and Globals.ExecutedDict.get(((a-2), b)) == False:
                        temp1 = Globals.TileDict.pop((a, b))
                        temp = temp1 * 2
                        Globals.TileDict.update({((a-2), b): temp})
                        updateChoice((a-2), b, temp)
                        changeScore(temp)
                        executed = True

                    else:
                        temp = Globals.TileDict.pop((a, b))
                        Globals.TileDict[((a-1), b)] = temp
                        updateChoice((a-1), b, temp)
                        executed = True
                elif a != 1 and ((a-1), b) in Globals.TileDict:
                    if Globals.TileDict.get(((a-1), b)) == Globals.TileDict.get((a, b)):
                        if a > 2 and ((a-2), b) not in Globals.TileDict:
                            if a == 4 and ((a-3), b) not in Globals.TileDict:
                                temp1 = Globals.TileDict.pop((a, b))
                                temp2 = Globals.TileDict.pop(((a-1), b))
                                temp = temp1 + temp2
                                Globals.TileDict[((a-3), b)] = temp
                                updateChoice((a-3), b, temp)
                                changeScore(temp)
                                executed = True
                            else:
                                temp1 = Globals.TileDict.pop((a, b))
                                temp2 = Globals.TileDict.pop(((a-1), b))
                                temp = temp1 + temp2
                                Globals.TileDict[((a-2), b)] = temp
                                updateChoice((a-2), b, temp)
                                changeScore(temp)
                                executed = True
                        else:
                            temp1 = Globals.TileDict.pop((a, b))
                            temp = temp1 * 2
                            Globals.TileDict.update({((a-1), b): temp})
                            updateChoice((a-1), b, temp)
                            changeScore(temp)
                            executed = True
                            Globals.ExecutedDict[((a-1), b)] = True

    updateGraphic()
    if executed == True:
        spawnTile()
    testWin()


def LeftArrow(event=None):
    for a in Globals.ExecutedDict:
        Globals.ExecutedDict[a] = False
    executed = False
    for a in range(1, 5):
        for b in range(1, 5):
            if (a, b) in Globals.TileDict:
                if b == 1 and (a, (b+1)) in Globals.TileDict:
                    if Globals.TileDict.get((a, (b+1))) == Globals.TileDict.get((a, b)):
                        temp1 = Globals.TileDict.pop((a, (b+1)))
                        temp = temp1 * 2
                        Globals.TileDict.update({(a, b): temp})
                        updateChoice(a, b, temp)
                        changeScore(temp)
                        executed = True
                        Globals.ExecutedDict[(a, b)] = True
                elif b != 1 and (a, (b-1)) not in Globals.TileDict:
                    if b > 2 and (a, (b-2)) not in Globals.TileDict:
                        if b == 4 and (a, (b-3)) not in Globals.TileDict:
                            temp = Globals.TileDict.pop((a, b))
                            Globals.TileDict[(a, (b-3))] = temp
                            updateChoice(a, (b-3), temp)
                            executed = True
                        elif b == 4 and Globals.TileDict.get((a, (b-3))) == Globals.TileDict.get((a, b)):
                            temp1 = Globals.TileDict.pop((a, b))
                            temp = temp1 * 2
                            Globals.TileDict.update({(a, (b-3)): temp})
                            updateChoice(a, (b-3), temp)
                            executed = True
                        else:
                            temp = Globals.TileDict.pop((a, b))
                            Globals.TileDict[(a, (b-2))] = temp
                            updateChoice(a, (b-2), temp)
                            executed = True
                    elif b > 2 and Globals.TileDict.get((a, (b-2))) == Globals.TileDict.get((a, b)) and Globals.ExecutedDict.get((a, (b-2))) == False:
                        temp1 = Globals.TileDict.pop((a, b))
                        temp = temp1 * 2
                        Globals.TileDict.update({(a, (b-2)): temp})
                        changeScore(temp)
                        updateChoice(a, (b-2), temp)
                        executed = True
                    else:
                        temp = Globals.TileDict.pop((a, b))
                        Globals.TileDict[(a, (b-1))] = temp
                        updateChoice(a, (b-1), temp)
                        executed = True
                elif b != 1 and (a, (b-1)) in Globals.TileDict:
                    if Globals.TileDict.get((a, (b-1))) == Globals.TileDict.get((a, b)):
                        if b > 2 and (a, (b-2)) not in Globals.TileDict:
                            if b == 4 and (a, (b-3)) not in Globals.TileDict:
                                temp1 = Globals.TileDict.pop((a, b))
                                temp2 = Globals.TileDict.pop((a, (b-1)))
                                temp = temp1 + temp2
                                Globals.TileDict[(a, (b-3))] = temp
                                updateChoice(a, (b-3), temp)
                                changeScore(temp)
                                executed = True
                            else:
                                temp1 = Globals.TileDict.pop((a, b))
                                temp2 = Globals.TileDict.pop((a, (b-1)))
                                temp = temp1 + temp2
                                Globals.TileDict[(a, (b-2))] = temp
                                updateChoice(a, (b-2), temp)
                                changeScore(temp)
                                executed = True
                        else:
                            temp1 = Globals.TileDict.pop((a, b))
                            temp = temp1 * 2
                            Globals.TileDict.update({(a, (b-1)): temp})
                            updateChoice(a, (b-1), temp)
                            executed = True
                            changeScore(temp)
                            Globals.ExecutedDict[(a, (b-1))] = True
    updateGraphic()
    if executed == True:
        spawnTile()
    testWin()


def DownArrow(event=None):
    for a in Globals.ExecutedDict:
        Globals.ExecutedDict[a] = False
    executed = False
    for b in range(1, 5):
        for a in range(4, 0, -1):
            if (a, b) in Globals.TileDict:
                if a == 4 and ((a-1), b) in Globals.TileDict:
                    if Globals.TileDict.get(((a-1), b)) == Globals.TileDict.get((a, b)):
                        temp1 = Globals.TileDict.pop(((a-1), b))
                        temp = temp1 * 2
                        Globals.TileDict.update({(a, b): temp})
                        updateChoice(a, b, temp)
                        changeScore(temp)
                        executed = True
                        Globals.ExecutedDict[(a, b)] = True
                elif a != 4 and ((a+1), b) not in Globals.TileDict:
                    if a < 3 and ((a+2), b) not in Globals.TileDict:
                        if a == 1 and ((a+3), b) not in Globals.TileDict:
                            temp = Globals.TileDict.pop((a, b))
                            Globals.TileDict[((a+3), b)] = temp
                            updateChoice((a+3), b, temp)
                            executed = True
                        elif a == 1 and Globals.TileDict.get(((a+3), b)) == Globals.TileDict.get((a, b)):
                            temp1 = Globals.TileDict.pop((a, b))
                            temp = temp1 * 2
                            Globals.TileDict.update({((a+3), b): temp})
                            updateChoice((a+3), b, temp)
                            executed = True
                        else:
                            temp = Globals.TileDict.pop((a, b))
                            Globals.TileDict[((a+2), b)] = temp
                            updateChoice((a+2), b, temp)
                            executed = True
                    elif a < 3 and Globals.TileDict.get(((a+2), b)) == Globals.TileDict.get((a, b)) and Globals.ExecutedDict.get(((a+2), b)) == False:
                        temp1 = Globals.TileDict.pop((a, b))
                        temp = temp1 * 2
                        Globals.TileDict.update({((a+2), b): temp})
                        updateChoice((a+2), b, temp)
                        changeScore(temp)
                        executed = True
                    else:
                        temp = Globals.TileDict.pop((a, b))
                        Globals.TileDict[((a+1), b)] = temp
                        updateChoice((a+1), b, temp)
                        executed = True
                elif a != 4 and ((a+1), b) in Globals.TileDict:
                    if Globals.TileDict.get(((a+1), b)) == Globals.TileDict.get((a, b)):
                        if a < 3 and ((a+2), b) not in Globals.TileDict:
                            if a == 1 and ((a+3), b) not in Globals.TileDict:
                                temp1 = Globals.TileDict.pop((a, b))
                                temp2 = Globals.TileDict.pop(((a+1), b))
                                temp = temp1 + temp2
                                Globals.TileDict[((a+3), b)] = temp
                                updateChoice((a+3), b, temp)
                                changeScore(temp)
                                executed = True
                            else:
                                temp1 = Globals.TileDict.pop((a, b))
                                temp2 = Globals.TileDict.pop(((a+1), b))
                                temp = temp1 + temp2
                                Globals.TileDict[((a+2), b)] = temp
                                updateChoice((a+2), b, temp)
                                changeScore(temp)
                                executed = True
                        else:
                            temp1 = Globals.TileDict.pop((a, b))
                            temp = temp1 * 2
                            Globals.TileDict.update({((a+1), b): temp})
                            updateChoice((a+1), b, temp)
                            executed = True
                            changeScore(temp)
                            Globals.ExecutedDict[((a+1), b)] = True

    updateGraphic()
    if executed == True:
        spawnTile()
    testWin()


def RightArrow(event=None):
    for a in Globals.ExecutedDict:
        Globals.ExecutedDict[a] = False
    executed = False
    for a in range(1, 5):
        for b in range(4, 0, -1):
            if (a, b) in Globals.TileDict:
                if b == 4 and (a, (b-1)) in Globals.TileDict:
                    if Globals.TileDict.get((a, (b-1))) == Globals.TileDict.get((a, b)):
                        temp1 = Globals.TileDict.pop((a, (b-1)))
                        temp = temp1 * 2
                        Globals.TileDict.update({(a, b): temp})
                        updateChoice(a, b, temp)
                        executed = True
                        changeScore(temp)
                        Globals.ExecutedDict[(a, b)] = True
                if b != 4 and (a, (b+1)) not in Globals.TileDict:
                    if b < 3 and (a, (b+2)) not in Globals.TileDict:
                        if b == 1 and (a, (b+3)) not in Globals.TileDict:
                            temp = Globals.TileDict.pop((a, b))
                            Globals.TileDict[(a, (b+3))] = temp
                            updateChoice(a, (b+3), temp)
                            executed = True
                        elif b == 1 and Globals.TileDict.get((a, (b+3))) == Globals.TileDict.get((a, b)):
                            temp1 = Globals.TileDict.pop((a, b))
                            temp = temp1 * 2
                            Globals.TileDict.update({(a, (b+3)): temp})
                            updateChoice(a, (b+3), temp)
                            executed = True
                        else:
                            temp = Globals.TileDict.pop((a, b))
                            Globals.TileDict[(a, (b+2))] = temp
                            updateChoice(a, (b+2), temp)
                            executed = True
                    elif b < 3 and Globals.TileDict.get((a, (b+2))) == Globals.TileDict.get((a, b)) and Globals.ExecutedDict.get((a, (b+2))) == False:
                        temp1 = Globals.TileDict.pop((a, b))
                        temp = temp1 * 2
                        Globals.TileDict.update({(a, (b+2)): temp})
                        updateChoice(a, (b+2), temp)
                        changeScore(temp)
                        executed = True
                    else:
                        temp = Globals.TileDict.pop((a, b))
                        Globals.TileDict[(a, (b+1))] = temp
                        updateChoice(a, (b+1), temp)
                        executed = True
                elif b != 4 and (a, (b+1)) in Globals.TileDict:
                    if Globals.TileDict.get((a, (b+1))) == Globals.TileDict.get((a, b)):
                        if b < 3 and (a, (b+2)) not in Globals.TileDict:
                            if b == 1 and (a, (b+3)) not in Globals.TileDict:
                                temp1 = Globals.TileDict.pop((a, b))
                                temp2 = Globals.TileDict.pop((a, (b+1)))
                                temp = temp1 + temp2
                                Globals.TileDict[(a, (b+3))] = temp
                                updateChoice(a, (b+3), temp)
                                changeScore(temp)
                                executed = True
                            else:
                                temp1 = Globals.TileDict.pop((a, b))
                                temp2 = Globals.TileDict.pop((a, (b+1)))
                                temp = temp1 + temp2
                                Globals.TileDict[(a, (b+2))] = temp
                                updateChoice(a, (b+2), temp)
                                changeScore(temp)
                                executed = True
                        else:
                            temp1 = Globals.TileDict.pop((a, b))
                            temp = temp1 * 2
                            Globals.TileDict.update({(a, (b+1)): temp})
                            updateChoice(a, (b-1), temp)
                            executed = True
                            changeScore(temp)
                            Globals.ExecutedDict[(a, (b-1))] = True
    updateGraphic()
    if executed == True:
        spawnTile()
    testWin()


def Clear():
    Globals.ClearButton.configure(text="New Game")
    Globals.TileDict.clear()
    spawnTile()
    spawnTile()
    updateGraphic()
    Globals.CurrentScore = 0
    Globals.CurrentScoreText.configure(state='normal')
    Globals.CurrentScoreText.delete(1.0, tkinter.END)
    Globals.CurrentScoreText.insert(tkinter.END, '0')
    Globals.CurrentScoreText.configure(state='disabled')
    Globals.GameState = True


def testWin():
    executed = False
    Globals.ExecuteUp = False
    Globals.ExecuteLeft = False
    Globals.ExecuteDown = False
    Globals.ExecuteRight = False
    for b in range(1, 5):
        for a in range(1, 5):
            if (a, b) in Globals.TileDict:
                if a == 1 and ((a+1), b) in Globals.TileDict:
                    if Globals.TileDict.get(((a+1), b)) == Globals.TileDict.get((a, b)):
                        executed = True
                        Globals.ExecuteUp = True
                elif a != 1 and ((a-1), b) not in Globals.TileDict:
                    if a > 2 and ((a-2), b) not in Globals.TileDict:
                        if a == 4 and ((a-3), b) not in Globals.TileDict:
                            executed = True
                            Globals.ExecuteUp = True
                        elif a == 4 and Globals.TileDict.get(((a-3), b)) == Globals.TileDict.get((a, b)):
                            executed = True
                            Globals.ExecuteUp = True
                        else:
                            executed = True
                            Globals.ExecuteUp = True
                    elif a > 2 and Globals.TileDict.get(((a-2), b)) == Globals.TileDict.get((a, b)) and Globals.ExecutedDict.get(((a-2), b)) == False:
                        executed = True
                        Globals.ExecuteUp = True

                    else:
                        executed = True
                        Globals.ExecuteUp = True
                elif a != 1 and ((a-1), b) in Globals.TileDict:
                    if Globals.TileDict.get(((a-1), b)) == Globals.TileDict.get((a, b)):
                        if a > 2 and ((a-2), b) not in Globals.TileDict:
                            if a == 4 and ((a-3), b) not in Globals.TileDict:
                                executed = True
                                Globals.ExecuteUp = True
                            else:
                                executed = True
                                Globals.ExecuteUp = True
                        else:
                            executed = True
                            Globals.ExecuteUp = True
    for a in range(1, 5):
        for b in range(1, 5):
            if (a, b) in Globals.TileDict:
                if b == 1 and (a, (b+1)) in Globals.TileDict:
                    if Globals.TileDict.get((a, (b+1))) == Globals.TileDict.get((a, b)):
                        executed = True
                        Globals.ExecuteLeft = True
                elif b != 1 and (a, (b-1)) not in Globals.TileDict:
                    if b > 2 and (a, (b-2)) not in Globals.TileDict:
                        if b == 4 and (a, (b-3)) not in Globals.TileDict:
                            executed = True
                            Globals.ExecuteLeft = True
                        elif b == 4 and Globals.TileDict.get((a, (b-3))) == Globals.TileDict.get((a, b)):
                            executed = True
                            Globals.ExecuteLeft = True
                        else:
                            executed = True
                            Globals.ExecuteLeft = True
                    elif b > 2 and Globals.TileDict.get((a, (b-2))) == Globals.TileDict.get((a, b)) and Globals.ExecutedDict.get((a, (b-2))) == False:
                        executed = True
                        Globals.ExecuteLeft = True
                    else:
                        executed = True
                        Globals.ExecuteLeft = True
                elif b != 1 and (a, (b-1)) in Globals.TileDict:
                    if Globals.TileDict.get((a, (b-1))) == Globals.TileDict.get((a, b)):
                        if b > 2 and (a, (b-2)) not in Globals.TileDict:
                            if b == 4 and (a, (b-3)) not in Globals.TileDict:
                                executed = True
                                Globals.ExecuteLeft = True
                            else:
                                executed = True
                                Globals.ExecuteLeft = True
                        else:
                            executed = True
                            Globals.ExecuteLeft = True
    for b in range(1, 5):
        for a in range(4, 0, -1):
            if (a, b) in Globals.TileDict:
                if a == 4 and ((a-1), b) in Globals.TileDict:
                    if Globals.TileDict.get(((a-1), b)) == Globals.TileDict.get((a, b)):
                        executed = True
                        Globals.ExecuteDown = True
                elif a != 4 and ((a+1), b) not in Globals.TileDict:
                    if a < 3 and ((a+2), b) not in Globals.TileDict:
                        if a == 1 and ((a+3), b) not in Globals.TileDict:
                            executed = True
                            Globals.ExecuteDown = True
                        elif a == 1 and Globals.TileDict.get(((a+3), b)) == Globals.TileDict.get((a, b)):
                            executed = True
                            Globals.ExecuteDown = True
                        else:
                            executed = True
                            Globals.ExecuteDown = True
                    elif a < 3 and Globals.TileDict.get(((a+2), b)) == Globals.TileDict.get((a, b)) and Globals.ExecutedDict.get(((a+2), b)) == False:
                        executed = True
                        Globals.ExecuteDown = True
                    else:
                        executed = True
                        Globals.ExecuteDown = True
                elif a != 4 and ((a+1), b) in Globals.TileDict:
                    if Globals.TileDict.get(((a+1), b)) == Globals.TileDict.get((a, b)):
                        if a < 3 and ((a+2), b) not in Globals.TileDict:
                            if a == 1 and ((a+3), b) not in Globals.TileDict:
                                executed = True
                                Globals.ExecuteDown = True
                            else:
                                executed = True
                                Globals.ExecuteDown = True
                        else:
                            executed = True
                            Globals.ExecuteDown = True
    for a in range(1, 5):
        for b in range(4, 0, -1):
            if (a, b) in Globals.TileDict:
                if b == 4 and (a, (b-1)) in Globals.TileDict:
                    if Globals.TileDict.get((a, (b-1))) == Globals.TileDict.get((a, b)):
                        executed = True
                        Globals.ExecuteRight = True
                if b != 4 and (a, (b+1)) not in Globals.TileDict:
                    if b < 3 and (a, (b+2)) not in Globals.TileDict:
                        if b == 1 and (a, (b+3)) not in Globals.TileDict:
                            executed = True
                            Globals.ExecuteRight = True
                        elif b == 1 and Globals.TileDict.get((a, (b+3))) == Globals.TileDict.get((a, b)):
                            executed = True
                            Globals.ExecuteRight = True
                        else:
                            executed = True
                            Globals.ExecuteRight = True
                    elif b < 3 and Globals.TileDict.get((a, (b+2))) == Globals.TileDict.get((a, b)) and Globals.ExecutedDict.get((a, (b+2))) == False:
                        executed = True
                        Globals.ExecuteRight = True
                    else:
                        executed = True
                        Globals.ExecuteRight = True
                elif b != 4 and (a, (b+1)) in Globals.TileDict:
                    if Globals.TileDict.get((a, (b+1))) == Globals.TileDict.get((a, b)):
                        if b < 3 and (a, (b+2)) not in Globals.TileDict:
                            if b == 1 and (a, (b+3)) not in Globals.TileDict:
                                executed = True
                                Globals.ExecuteRight = True
                            else:
                                executed = True
                                Globals.ExecuteRight = True
                        else:
                            executed = True
                            Globals.ExecuteRight = True
    if executed == False:
        Globals.ClearButton.configure(text="Try Again")
        Globals.GameState = False


def Random():
    Globals.currentAlg = 1
    while Globals.GameState == True:
        time.sleep(Globals.currentVal)
        Globals.rootWindow.update()
        n = random.randint(1, 4)
        if n == 1:
            UpArrow()
        elif n == 2:
            LeftArrow()
        elif n == 3:
            DownArrow()
        else:
            RightArrow()
    return


def firstAlg():
    Globals.currentAlg = 2
    while Globals.GameState == True:
        time.sleep(Globals.currentVal)
        Globals.rootWindow.update()
        if Globals.ExecuteLeft == True and Globals.ExecuteDown == True:
            n = random.randint(1, 2)
            if n == 1:
                LeftArrow()
            else:
                DownArrow()
        else:
            if Globals.ExecuteLeft == True:
                LeftArrow()
            elif Globals.ExecuteDown == True:
                DownArrow()
            elif Globals.ExecuteRight == True:
                RightArrow()
            else:
                UpArrow()

    return


def secondAlg():
    Globals.currentAlg = 3
    switch = 1
    while Globals.GameState == True:
        time.sleep(Globals.currentVal)
        Globals.rootWindow.update()
        if (4, 1) not in Globals.TileDict and Globals.ExecuteLeft == True:
            LeftArrow()
        elif Globals.ExecuteLeft == True and Globals.ExecuteDown == True:
            if switch == 1:
                LeftArrow()
                switch = 2
            else:
                DownArrow()
                switch = 1
        elif (4, 1) in Globals.TileDict and (4, 2) in Globals.TileDict and (4, 3) in Globals.TileDict and (4, 4) in Globals.TileDict:
            if Globals.TileDict.get((4, 1)) != Globals.TileDict.get((4, 2)) and Globals.TileDict.get((4, 2)) != Globals.TileDict.get((4, 3)) and Globals.TileDict.get((4, 3)) != Globals.TileDict.get((4, 4)):
                if Globals.TileDict.get((3, 1)) == Globals.TileDict.get((4, 2)) and Globals.ExecuteRight == True:
                    RightArrow()
                    DownArrow()
                elif Globals.TileDict.get((3, 2)) == Globals.TileDict.get((4, 3)) and Globals.ExecuteRight == True:
                    RightArrow()
                    DownArrow()
                elif Globals.TileDict.get((3, 3)) == Globals.TileDict.get((4, 4)) and Globals.ExecuteRight == True:
                    RightArrow()
                    DownArrow()
                elif Globals.TileDict.get((2, 1)) == Globals.TileDict.get((3, 2)) and Globals.ExecuteRight == True:
                    RightArrow()
                    DownArrow()
                elif Globals.TileDict.get((2, 2)) == Globals.TileDict.get((3, 3)) and Globals.ExecuteRight == True:
                    RightArrow()
                    DownArrow()
                elif Globals.TileDict.get((2, 3)) == Globals.TileDict.get((3, 4)) and Globals.ExecuteRight == True:
                    RightArrow()
                    DownArrow()
                else:
                    if Globals.ExecuteLeft == True:
                        LeftArrow()
                    elif Globals.ExecuteDown == True:
                        DownArrow()
                    elif Globals.ExecuteRight == True:
                        RightArrow()
                    else:
                        UpArrow()
            else:
                if Globals.ExecuteLeft == True:
                    LeftArrow()
                elif Globals.ExecuteDown == True:
                    DownArrow()
                elif Globals.ExecuteRight == True:
                    RightArrow()
                else:
                    UpArrow()
        else:
            if Globals.ExecuteLeft == True:
                LeftArrow()
            elif Globals.ExecuteDown == True:
                DownArrow()
            elif Globals.ExecuteRight == True:
                RightArrow()
            else:
                UpArrow()

    return


def RandomTest():
    ScoreList = []
    for a in range(100):
        Random()
        ScoreList.append(Globals.CurrentScore)
        Clear()
    print('score list:')
    print(ScoreList)
    print('normal average')
    print(sum(ScoreList)/(len(ScoreList)))


def firstAlgTest():
    ScoreList = []
    for a in range(100):
        firstAlg()
        ScoreList.append(Globals.CurrentScore)
        Clear()
    print('score list:')
    print(ScoreList)
    print('normal average')
    print(sum(ScoreList)/(len(ScoreList)))


def secondAlgTest():
    ScoreList = []
    for a in range(100):
        secondAlg()
        ScoreList.append(Globals.CurrentScore)
        Clear()
    print('score list:')
    print(ScoreList)
    print('normal average')
    print(sum(ScoreList)/(len(ScoreList)))


def Pause():
    if Globals.choiceVar.get() == 1:
        Globals.GameState = False
    else:
        Globals.GameState = True
    if Globals.currentAlg == 1:
        Random()
    elif Globals.currentAlg == 2:
        firstAlg()
    elif Globals.currentAlg == 3:
        secondAlg()

    return


def SliderChanged(var):
    secs = 0.01 * float(var)
    Globals.currentVal = secs
    return


def initializeGUI():
    Globals.rootWindow = tkinter.Tk()
    Globals.rootWindow.title('2048')
    Globals.choiceVar = tkinter.IntVar()

    AllFrame = tkinter.Frame(Globals.rootWindow, bg="#bbac9f")
    AllFrame.pack()

    ControlFrame = tkinter.Frame(AllFrame, background="#bbac9f")
    ControlFrame.pack()

    CurrentScoreLabel = tkinter.Label(
        ControlFrame, bg="#bbac9f", text="Score:", fg="#ffffff")
    CurrentScoreLabel.pack(side=tkinter.LEFT)

    Globals.CurrentScoreText = tkinter.Text(
        ControlFrame, height=1, width=10, bg="#bbada0", bd=0, highlightthickness=0, fg="#ffffff")
    Globals.CurrentScoreText.pack(side=tkinter.LEFT)

    Globals.CurrentScoreText.insert(
        tkinter.END, '{}'.format(Globals.CurrentScore))
    Globals.CurrentScoreText.configure(state='disabled')

    Globals.ClearButton = tkinter.Button(
        ControlFrame, highlightbackground="#bbada0", text="New Game", command=Clear)
    Globals.ClearButton.pack()

    GameFrame = tkinter.Frame(AllFrame, bg="#bbada0")
    Globals.rootWindow.bind('<Left>', LeftArrow)
    Globals.rootWindow.bind('<Right>', RightArrow)
    Globals.rootWindow.bind('<Up>', UpArrow)
    Globals.rootWindow.bind('<Down>', DownArrow)
    GameFrame.pack(side=tkinter.LEFT)

    TopRow = tkinter.Frame(GameFrame)
    TopRow.pack()
    # regular highlightthickness = 5

    Globals.TopOne = tkinter.Canvas(TopRow, bg="#ccc0b3", height=100,
                                    width=100, highlightthickness=5, highlightbackground="#bbada0")
    Globals.TopOne.pack(side=tkinter.LEFT)

    Globals.TopTwo = tkinter.Canvas(TopRow, bg="#ccc0b3", height=100,
                                    width=100, highlightthickness=5, highlightbackground="#bbada0")
    Globals.TopTwo.pack(side=tkinter.LEFT)

    Globals.TopThree = tkinter.Canvas(
        TopRow, bg="#ccc0b3", height=100, width=100, highlightthickness=5, highlightbackground="#bbada0")
    Globals.TopThree.pack(side=tkinter.LEFT)

    Globals.TopFour = tkinter.Canvas(
        TopRow, bg="#ccc0b3", height=100, width=100, highlightthickness=5, highlightbackground="#bbada0")
    Globals.TopFour.pack(side=tkinter.LEFT)

    SecondRow = tkinter.Frame(GameFrame)
    SecondRow.pack()

    Globals.SecondOne = tkinter.Canvas(
        SecondRow, bg="#ccc0b3", height=100, width=100, highlightthickness=5, highlightbackground="#bbada0")
    Globals.SecondOne.pack(side=tkinter.LEFT)

    Globals.SecondTwo = tkinter.Canvas(
        SecondRow, bg="#ccc0b3", height=100, width=100, highlightthickness=5, highlightbackground="#bbada0")
    Globals.SecondTwo.pack(side=tkinter.LEFT)

    Globals.SecondThree = tkinter.Canvas(
        SecondRow, bg="#ccc0b3", height=100, width=100, highlightthickness=5, highlightbackground="#bbada0")
    Globals.SecondThree.pack(side=tkinter.LEFT)

    Globals.SecondFour = tkinter.Canvas(
        SecondRow, bg="#ccc0b3", height=100, width=100, highlightthickness=5, highlightbackground="#bbada0")
    Globals.SecondFour.pack(side=tkinter.LEFT)

    ThirdRow = tkinter.Frame(GameFrame)
    ThirdRow.pack()

    Globals.ThirdOne = tkinter.Canvas(
        ThirdRow, bg="#ccc0b3", height=100, width=100, highlightthickness=5, highlightbackground="#bbada0")
    Globals.ThirdOne.pack(side=tkinter.LEFT)

    Globals.ThirdTwo = tkinter.Canvas(
        ThirdRow, bg="#ccc0b3", height=100, width=100, highlightthickness=5, highlightbackground="#bbada0")
    Globals.ThirdTwo.pack(side=tkinter.LEFT)

    Globals.ThirdThree = tkinter.Canvas(
        ThirdRow, bg="#ccc0b3", height=100, width=100, highlightthickness=5, highlightbackground="#bbada0")
    Globals.ThirdThree.pack(side=tkinter.LEFT)

    Globals.ThirdFour = tkinter.Canvas(
        ThirdRow, bg="#ccc0b3", height=100, width=100, highlightthickness=5, highlightbackground="#bbada0")
    Globals.ThirdFour.pack(side=tkinter.LEFT)

    FourthRow = tkinter.Frame(GameFrame)
    FourthRow.pack()

    Globals.FourthOne = tkinter.Canvas(
        FourthRow, bg="#ccc0b3", height=100, width=100, highlightthickness=5, highlightbackground="#bbada0")
    Globals.FourthOne.pack(side=tkinter.LEFT)

    Globals.FourthTwo = tkinter.Canvas(
        FourthRow, bg="#ccc0b3", height=100, width=100, highlightthickness=5, highlightbackground="#bbada0")
    Globals.FourthTwo.pack(side=tkinter.LEFT)

    Globals.FourthThree = tkinter.Canvas(
        FourthRow, bg="#ccc0b3", height=100, width=100, highlightthickness=5, highlightbackground="#bbada0")
    Globals.FourthThree.pack(side=tkinter.LEFT)

    Globals.FourthFour = tkinter.Canvas(
        FourthRow, bg="#ccc0b3", height=100, width=100, highlightthickness=5, highlightbackground="#bbada0")
    Globals.FourthFour.pack(side=tkinter.LEFT)

    BotFrame = tkinter.Frame(AllFrame, bg="#bbac9f")
    BotFrame.pack(side=tkinter.LEFT)

    PauseButton = tkinter.Radiobutton(
        BotFrame, text="Pause", variable=Globals.choiceVar, value=1, command=Pause, bg="#bbada0")
    PauseButton.pack()

    ContinueButton = tkinter.Radiobutton(
        BotFrame, text="Continue", variable=Globals.choiceVar, value=2, command=Pause, bg="#bbada0")
    ContinueButton.pack()

    SpeedLabel = tkinter.Label(
        BotFrame, text="Algorithm delay(0.01 sec):", bg="#bbada0")
    SpeedLabel.pack()

    SpeedSlider = tkinter.Scale(BotFrame, from_=0, to=100, variable=Globals.currentVal,
                                command=SliderChanged, orient='horizontal', bg="#bbada0")
    SpeedSlider.pack()

    RandomBot = tkinter.Button(
        BotFrame, highlightbackground="#bbada0", text="Random", command=Random)
    RandomBot.pack()

    FirstAlgorithm = tkinter.Button(
        BotFrame, highlightbackground="#bbada0", text="1st Algorithm", command=firstAlg)
    FirstAlgorithm.pack()

    SecondAlgorithm = tkinter.Button(
        BotFrame, highlightbackground="#bbada0", text="2nd Algorithm", command=secondAlg)
    SecondAlgorithm.pack()
    Globals.rootWindow.mainloop()

    spawnTile()
    spawnTile()


initializeGUI()
