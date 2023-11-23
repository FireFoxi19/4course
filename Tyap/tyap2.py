import sys
import networkx as nx
import matplotlib.pyplot as plt
from dataclasses import dataclass
from typing import Dict, List
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtWebChannel import QWebChannel
from PyQt5 import QtCore
from PyQt5.QtGui import *
from PyQt5.QtCore    import *
from PyQt5.QtWidgets import *
from numpy._typing import _128Bit


app = QApplication(sys.argv)

#######-----создание интерфейса-------#######

class TableView(QWidget):
    def __init__(self, countStates): #кол-во состояний

        super(TableView, self).__init__()
        self.table = QTableWidget()
        self.table.setFixedHeight(200)
        self.countStates = countStates
        self.table.setColumnCount(countStates)
        self.table.setRowCount(countStates)
        for row in range(countStates):
            for column in range(countStates):
                self.table.setItem(row, column, QTableWidgetItem(""))


        layout = QVBoxLayout()
        Hlayout = QHBoxLayout()
        self.drawButton = QPushButton()
        self.drawButton.clicked.connect(lambda: self.DrawGraph())
        self.drawButton.setIcon(QIcon("draw.png"))
        self.drawButton.setIconSize(QSize(35,35))
        self.drawButton.setFixedSize(35, 35)
        self.drawButton.setToolTip("Вывести граф ДКА") 
        self.drawButton.setFlat(True)

        self.text = QLabel()
        self.text.setText("")

        self.enterButton = QPushButton()
        self.enterButton.clicked.connect(lambda: self.Enter())
        self.enterButton.setIcon(QIcon("enter.png"))
        self.enterButton.setIconSize(QSize(35,35))
        self.enterButton.setFixedSize(35, 35)
        self.enterButton.setToolTip("Продолжить") 
        self.enterButton.setFlat(True)       

        self.radioButton1 = QRadioButton('Четная длина цепочки', self)
        self.radioButton1.clicked.connect(lambda: self.multiplicity())
        #self.radioButton1.setFlat(True)

        self.radioButton2 = QRadioButton('Нечетная длина цепочки', self)
        self.radioButton1.clicked.connect(lambda: self.multiplicity())
        #self.radioButton1.setFlat(True)

        self.textLabel1 = QLabel()
        self.textLabel1.setText("Введите алфавит")

        self.alphabet = QLineEdit()
        self.alphabet.setFixedHeight(20)

        self.textLabel2 = QLabel()
        self.textLabel2.setText("Введите конечные состояния через пробел : Ваше начальное состоняие (1)")

        self.endStates = QLineEdit()
        self.endStates.setFixedHeight(20)

        layout.addWidget(self.radioButton1)
        layout.addWidget(self.radioButton2)
        layout.addWidget(self.textLabel1)
        layout.addWidget(self.alphabet)
        layout.addWidget(self.textLabel2)
        layout.addWidget(self.endStates)
        layout.addWidget(self.table)

        self.textLabel3 = QLabel()
        self.textLabel3.setText("Введите цепочку")

        self.chain = QLineEdit()
        self.chain.setFixedHeight(20)

        layout.addWidget(self.textLabel3)
        layout.addWidget(self.chain)

        Hlayout.addWidget(self.drawButton)
        Hlayout.addStretch()
        Hlayout.addWidget(self.text)
        Hlayout.addWidget(self.enterButton)

        self.textEnd = QTextEdit()
        self.textEnd.setText("Здесь будет вывод")

        layout.addLayout(Hlayout)
        layout.addWidget(self.textEnd)

        self.setLayout(layout)
        self.matrix = []

##########---------отрисовка графа и проверка алфавита и переходов----------###########

    def DrawGraph(self):

        self.GetMatrix()

        graph = nx.DiGraph()
        graph.add_nodes_from(range(1, self.countStates + 1))
        for row in range(self.countStates):
            for column in range(self.countStates):
                if self.matrix[row][column] != "":
                    graph.add_edge(row + 1, column + 1)

        pos = nx.spring_layout(graph)
        nx.draw(graph, pos, with_labels=True, node_size=1000, node_color='lightblue')
        plt.show()

    def CheckEndStates(self):
        endStates = self.endStates.text().split()
        for subString in endStates:
            if subString.isdigit() == False:
                return False
            if int(subString) > self.countStates:
                return False

    def CheckChain(self):
        values = self.alphabet.text()
        chain = self.chain.text()

        for symbol in chain:
            if symbol in values:
                1
            else:
                return False

    def CheckMatrixAlphabet(self):
        values = self.alphabet.text()
        for row in range(self.countStates):
            for column in range(self.countStates):
                for symbol in self.matrix[row][column]:
                    if symbol in values:
                        1
                    else:
                        return False
        return True
    def CheckMatrixDKA(self):
        values = self.alphabet.text()
        for row in range(self.countStates):
            string = ""

            for column in range(self.countStates):
                string += self.matrix[row][column]

            for symbol in values:
                if string.count(symbol) > 1:
                    return False
            

        return True

    def GetMatrix(self):
        self.matrix = []
        for row in range(self.countStates):
            a = []
            for column in range(self.countStates):   
                a.append(self.table.item(row, column).text())
            self.matrix.append(a)

    ###----сам алгоритм----###        
    def RunMachine(self):
        chain = self.chain.text() # цепочка
        string = " (1) " + chain
        wayChain = ""
        index = 0 # нач состояние
        endStates = self.endStates.text().split() # конечные состояние

        self.textEnd.clear()

        for symbol in chain:
            wayChain += symbol # отслеживание пути
            checkState = False # проверка наличия перехода по симв
            for column in range(self.countStates):
                if symbol in self.matrix[index][column]: # проверка перехода из тек сост в след
                    index = column # обновление сост
                    chain = chain[1:]
                    checkState = True
                    string += " |-- " + wayChain + " (" + str(index+1) + ") " + chain
                    break
               

            if checkState == False:
                string += " Нет перехода из" + " ("+ str(index + 1) +") по символу " + symbol
                self.textEnd.setText(string)
                return False

        if chain == "":
            if str(index+1) not in endStates:
                string += " Цепочка находится не в конечном состоянии"
                self.textEnd.setText(string)
                return False
        self.textEnd.setText(string + " Цепочка подходит")


    def Enter(self):
        self.GetMatrix()

        if self.CheckEndStates() == False:
            self.text.setText("Невозможное конечное состояние")
            return False
        if self.CheckMatrixAlphabet() == False:
            self.text.setText("Используется символ не находящийся в алфавите")
            return False
        if self.CheckMatrixDKA() == False:
            self.text.setText("Имеются несколько переходов по одинаковому символу")
            return False
        if self.CheckChain() == False:
            self.text.setText("В цепочке находится символ не из алфавита")
            return False

        self.text.setText("")
        self.RunMachine()
####при нажатии кнопки продолжить сделать диалог окно, в файле записать или в окне
    def WriteFile():
        global start, end
        with open("File.txt") as file:
            start = file.readline().split()[1]

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
        self.restartButton.setIconSize(QSize(35,35))
        self.restartButton.setFixedSize(35, 35)
        self.restartButton.setToolTip("Обновить") 
        self.restartButton.setFlat(True)

        self.exitButton = QPushButton()
        self.exitButton.clicked.connect(lambda: self.Exit())
        self.exitButton.setIcon(QIcon("cross.png"))
        self.exitButton.setIconSize(QSize(35,35))
        self.exitButton.setFixedSize(35, 35)
        self.exitButton.setToolTip("Exit") 
        self.exitButton.setFlat(True)

        self.HlayoutMenu = QHBoxLayout()
        self.HlayoutMenu.addWidget(self.exitButton)
        self.HlayoutMenu.addWidget(self.restartButton)
        self.HlayoutMenu.addStretch()

        self.VlayoutMenu = QVBoxLayout()
        self.VlayoutMenu.addLayout(self.HlayoutMenu)
        self.VlayoutMenu.addStretch()

        self.HlayoutMenu = QHBoxLayout()
        self.countStates =  QSpinBox(self) 
        self.countStates.setRange(0, 100) 

        self.enterButton = QPushButton()
        self.enterButton.clicked.connect(lambda: self.Enter())
        self.enterButton.setIcon(QIcon("enter.png"))
        self.enterButton.setIconSize(QSize(35,35))
        self.enterButton.setFixedSize(35, 35)
        self.enterButton.setToolTip("Выход") 
        self.enterButton.setFlat(True)

        self.HlayoutMenu.addWidget(self.countStates)
        self.HlayoutMenu.addWidget(self.enterButton)

        self.text = QLabel()
        self.text.setText("Введите количество состояний")

        self.VlayoutMenu.addWidget(self.text)
        self.VlayoutMenu.addLayout(self.HlayoutMenu)
        self.VlayoutMenu.addStretch()

        self.menu = QDialog()
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
    clock.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

