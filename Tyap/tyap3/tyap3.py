#!/usr/bin/env python
import sys
import networkx as nx
import matplotlib.pyplot as plt
from dataclasses import dataclass
from typing import Dict, List
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtWebChannel import QWebChannel
#from PyQt5.QtWebEngineWidgets import *
from PyQt5 import QtCore
from PyQt5.QtGui import *
from PyQt5.QtCore    import *
from PyQt5.QtWidgets import *
from numpy._typing import _128Bit

app = QApplication(sys.argv)

class TableView(QWidget):
    def __init__(self, countStates):

        super(TableView, self).__init__()
        self.table = QTableWidget()
        self.table.setFixedHeight(200)
        self.countStates = countStates
        self.table.setColumnCount(5)
        self.table.setRowCount(countStates)


        for row in range(countStates):
            for column in range(5):
                self.table.setItem(row, column, QTableWidgetItem(""))
                if column < 3:
                    self.table.item(row, column).setBackground(QColor(250,186,252))
                if column >= 3:
                    self.table.item(row, column).setBackground(QColor(186,208,252))

        
        self.table.setHorizontalHeaderLabels(["Состояние", "Символ в цепочке", "Символ в стеке", "Переход в состояние", "Действие"])

        self.table.horizontalHeader().resizeSection(0, 100)
        self.table.horizontalHeader().resizeSection(1, 160)
        self.table.horizontalHeader().resizeSection(2, 100)
        self.table.horizontalHeader().resizeSection(3, 160)
        self.table.horizontalHeader().resizeSection(4, 100)

        layout = QVBoxLayout()
        Hlayout = QHBoxLayout()

        self.text = QLabel()
        self.text.setText("")

        self.enterButton = QPushButton()
        self.enterButton.clicked.connect(lambda: self.Enter())
        self.enterButton.setIcon(QIcon("enter.png"))
        self.enterButton.setIconSize(QSize(50,50))
        self.enterButton.setFixedSize(50, 50)
        self.enterButton.setToolTip("Продолжить") 
        self.enterButton.setFlat(True)

        self.textLabel1 = QLabel()
        self.textLabel1.setText("Введите алфавит")

        self.alphabet = QLineEdit()
        self.alphabet.setFixedHeight(20)

        self.textLabel3 = QLabel()
        self.textLabel3.setText("Введите начальное состояние")

        self.startStates = QLineEdit()
        self.startStates.setFixedHeight(20)

        self.textLabel2 = QLabel()
        self.textLabel2.setText("Введите конечные состояния через пробел")

        self.endStates = QLineEdit()
        self.endStates.setFixedHeight(20)

        layout.addWidget(self.textLabel1)
        layout.addWidget(self.alphabet)
        layout.addWidget(self.textLabel3)
        layout.addWidget(self.startStates)
        layout.addWidget(self.textLabel2)
        layout.addWidget(self.endStates)
        layout.addWidget(self.table)

        self.textLabel3 = QLabel()
        self.textLabel3.setText("Введите цепочку")

        self.chain = QLineEdit()
        self.chain.setFixedHeight(20)

        layout.addWidget(self.textLabel3)
        layout.addWidget(self.chain)

        Hlayout.addStretch()
        Hlayout.addWidget(self.text)
        Hlayout.addWidget(self.enterButton)

        self.textEnd = QTextEdit()
        self.textEnd.setText("Здесь будет вывод")

        layout.addLayout(Hlayout)
        layout.addWidget(self.textEnd)

        self.setLayout(layout)

        self.matrixStates = []
        self.matrixTransitions = []
    
    #проверка на конечные состояния и проверка на совпадение с эл матрицы
    def CheckEndStates(self): 
        endStates = self.endStates.text().split()
        for subString in endStates:
            if subString.isdigit() == False:
                return False
            for states in self.matrixStates:
                if int(subString) == int(states[0]):
                    return True
        return False
    #проверка симвл на принадлежность алфавиту
    def CheckMatrixAlphabet(self):
        values = self.alphabet.text() + " λ"
        for row in range(self.countStates):
            for symbol in self.matrixStates[row][1]:
                if (symbol in values) == False:
                    return False
        return True
    #проверка на диблирование состояний
    def CheckMatrixDMP(self):
        for row in range(self.countStates):
            for row2 in range(self.countStates):
                if self.matrixStates[row] == self.matrixStates[row2] and row != row2:
                    print(self.matrixStates[row])
                    print(self.matrixStates[row2])
                    return False
        return True
    #проверка принадлежности симлв в переходах к алфавиту
    def CheckMatrixTransition(self):
        values = self.alphabet.text() + " Z"
        for item in self.matrixTransitions:
            if item[1] != "eps":
               for symbol in item[1]:
                    if (symbol in values) == False:
                        return False
    #извлечение инфы о состояниях и переходах
    def GetMatrix(self):
        self.matrixStates = []
        self.matrixTransitions = []

        for row in range(self.countStates):
            a = []
            b = []
            for column in range(5):   
                if column < 3:
                    a.append(self.table.item(row, column).text())
                if column >= 3:
                    b.append(self.table.item(row, column).text())
            self.matrixStates.append(a)
            self.matrixTransitions.append(b)
#принадлежит ли входная цепочка регулярному языку
    def CheckDMPResult(self,symbol,stack,nowState,endStates,string):
        if symbol == "λ" and stack == "λ" and (nowState in endStates) == False:
            self.textEnd.setText(string + " [ Пустая цепочка, пустой стек, не конечное состояние - цепочка не пренадлежит к регулярному языку ]")
            return False

        if symbol != "λ" and stack == "λ" and (nowState in endStates) == False:
            self.textEnd.setText(string + " [ Не пустая цепочка, пустой стек, не конечное состояние - цепочка не пренадлежит к регулярному языку ]")
            return False

        if symbol != "λ" and stack == "λ" and nowState in endStates:
            self.textEnd.setText(string + " [ Не пустая цепочка, пустой стек, конечное состояние - цепочка не пренадлежит к регулярному языку ]")
            return False

        if symbol == "λ" and stack != "λ" and nowState in endStates:
            self.textEnd.setText(string + " [ Пустая цепочка, не пустой стек, конечное состояние - цепочка не пренадлежит к регулярному языку ]")
            return False
        if symbol == "λ" and stack != "λ" and (nowState in endStates) == False:
            self.textEnd.setText(string + " [ Пустая цепочка, не пустой стек, не конечное состояние - цепочка не пренадлежит к регулярному языку ]")
            return False
        if symbol != "λ" and stack != "λ" and (nowState in endStates) == False:
            self.textEnd.setText(string + " [ Не пустая цепочка, не пустой стек, не конечное состояние - цепочка не пренадлежит к регулярному языку ]")
            return False
        if symbol != "λ" and stack != "λ" and nowState in endStates:
            self.textEnd.setText(string + " [ Не пустая цепочка, не пустой стек, конечное состояние - цепочка не пренадлежит к регулярному языку ]")
            return False
        return True
#запускает автомат для предоставленной цепочки
    def RunMachine(self):
        chain = self.chain.text() + "λλ"
        chainTemp = self.chain.text()

        string = chainTemp

        stack = "Z"
        endStates = self.endStates.text().split()
        startStates = self.startStates.text().split()[0]
        nowState = startStates

        self.textEnd.clear()

        string += " ===> "

        for symbol in chain:

            if symbol == "λ" and stack == "λ" and nowState in endStates:
                string += "(q" + nowState + ", "+stack+", "+ symbolStack+ ")"
                break

            #if self.CheckDMPResult(symbol,stack,nowState,endStates,string) == False:
            #    return False;

            if symbol == "λ":
                chain += "λ"

            symbolStack = stack[0]
            listNowState = [nowState,symbol,symbolStack]
            string += "(q" + nowState + ", "+symbol+", "+ symbolStack+ ")"
            foundCheck = False
            for row in range(self.countStates):
                if listNowState == self.matrixStates[row]:
                    foundCheck = True
                    chainTemp = chainTemp[1:]

                    if chainTemp == "":
                        chainTemp = "λ"

                    nowState = self.matrixTransitions[row][0]
                    stack = stack[1:]

                    if self.matrixTransitions[row][1] == "eps" and symbolStack == "Z":
                        stack = "λ"
                        break
                    
                    if self.matrixTransitions[row][1] != "eps":
                        stack = self.matrixTransitions[row][1] + stack

            if foundCheck == False:
                if self.CheckDMPResult(symbol,stack,nowState,endStates,string) == False:
                    return False;
                else:
                    self.textEnd.setText(string + " [ Не существует перехода, цепочка или стек не пуст! - цепочка не пренадлежит к регулярному языку ]")
                    return False

            string += " |- "

        self.textEnd.setText(string + " [ Цепочка пренадлежит к регулярному языку ]")
        return True

    def Enter(self):
        self.GetMatrix()

        #if self.CheckEndStates() == False:
        #    self.text.clear()
        #    self.text.setText("Имеется невозможное конечное состояние")
        #    return False
        if self.CheckMatrixAlphabet() == False:
            self.text.clear()
            self.text.setText("Используется символ не находящийся в алфавите")
            return False

        if self.CheckMatrixDMP() == False:
            self.text.clear()
            self.text.setText("Имеются несколько переходов по одинаковым состояниям")
            return False

        if self.CheckMatrixTransition() == False:
            self.text.clear()
            self.text.setText("Имеются неопознаные действия")
            return False

        self.text.setText("Выполнение")
        #self.text.clear()
        #self.text.setText("")
        self.RunMachine()



class Window(QMainWindow):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        self.setWindowTitle("2 lab")
        icon = QIcon()
        icon.addPixmap(QPixmap("icon.png"))
        self.setWindowIcon(icon)

        self.widget = QStackedWidget()
        self.widget.setFixedHeight(100)
        self.widget.setFixedWidth(800)

        self.restartButton = QPushButton()
        self.restartButton.clicked.connect(lambda: self.Restart())
        self.restartButton.setIcon(QIcon("restart.png"))
        self.restartButton.setIconSize(QSize(50,50))
        self.restartButton.setFixedSize(50, 50)
        self.restartButton.setToolTip("Обновить") 
        self.restartButton.setFlat(True)

        self.exitButton = QPushButton()
        self.exitButton.clicked.connect(lambda: self.Exit())
        self.exitButton.setIcon(QIcon("cross.png"))
        self.exitButton.setIconSize(QSize(50,50))
        self.exitButton.setFixedSize(50, 50)
        self.exitButton.setToolTip("Exit") 
        self.exitButton.setFlat(True)

        self.HlayoutMenu = QHBoxLayout()
        self.HlayoutMenu.addWidget(self.exitButton)
        self.HlayoutMenu.addWidget(self.restartButton)
        self.HlayoutMenu.addStretch()

        self.VlayoutMenu = QVBoxLayout()
        self.VlayoutMenu.addLayout(self.HlayoutMenu)

        self.HlayoutMenu = QHBoxLayout()
        self.countStates =  QSpinBox(self) 
        self.countStates.setRange(1, 100) 

        self.enterButton = QPushButton()
        self.enterButton.clicked.connect(lambda: self.Enter())
        self.enterButton.setIcon(QIcon("enter.png"))
        self.enterButton.setIconSize(QSize(50,50))
        self.enterButton.setFixedSize(50, 50)
        self.enterButton.setToolTip("Выход") 
        self.enterButton.setFlat(True)

        self.HlayoutMenu.addWidget(self.countStates)
        self.HlayoutMenu.addWidget(self.enterButton)

        self.text = QLabel()
        self.text.setText("Введите количество переходов")

        self.VlayoutMenu.addWidget(self.text)
        self.VlayoutMenu.addLayout(self.HlayoutMenu)
        self.VlayoutMenu.addStretch()

        self.menu = QDialog()

        self.menu.setFixedHeight(150)
        self.widget.setFixedHeight(150)

        self.menu.setLayout(self.VlayoutMenu)
        self.widget.addWidget(self.menu)

        self.centralWidget = QWidget()
        self.centralLayout = QVBoxLayout()

        self.centralLayout.addWidget(self.widget)
        self.centralWidget.setLayout(self.centralLayout)
        self.setCentralWidget(self.centralWidget)

        self.mainTable = None

    def Restart(self):
        QtCore.QCoreApplication.quit()
        status = QtCore.QProcess.startDetached(sys.executable, sys.argv)

    def Exit(self):
        sys.exit(app.exec_())

    def Enter(self):
        if self.mainTable is not None:
            self.centralLayout.removeWidget(self.mainTable)

        self.mainTable = TableView(self.countStates.value())
        self.mainTable.setFixedHeight(600)

        self.centralLayout.addWidget(self.mainTable)
        self.widget.setCurrentWidget(self.mainTable)
    

def main():

    clock = Window()
    style = """
    Window{
    background:  #97FCA3;
    }
    QLabel{
    color: #000000;
    font-size: 15px;
    }
    QLineEdit{
    background:  #FFFFFF;
    color: #000000;
    font-size: 15px;
    border: 1px solid #000000;
    border-radius: 10px;
    padding-left: 20px;
    }
    QTextEdit{
    background:  #FFFFFF;
    color: #000000;
    font-size: 15px;
    border: 1px solid #000000;
    border-radius: 10px;
    padding-left: 20px;
    }
    QSpinBox{
    background:  #FFFFFF;
    color: #000000;
    font-size: 15px;
    border: 1px solid #000000;
    border-radius: 10px;
    padding-left: 20px;
    }
    QTableWidget{
    background:  #97FCA3;
    color: #000000;
    font-size: 15px;
    border: 1px solid #000000;

    }
    """
    clock.setStyleSheet(style)
    clock.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
