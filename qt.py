import sys
from time import time

from PyQt6.QtWidgets import QApplication, QWidget
from ACO import ACO

from TSP import generate_problem, TSP
from ant import Ui_ANTAlg


class ANT(QWidget):
    def __init__(self):
        super().__init__()
        self.size = 0
        self.len = 0
        # use the Ui_login_form
        self.ui = Ui_ANTAlg()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.get_params)

    def get_params(self):
        self.n = int(self.ui.lineEdit_5.text())
        self.ants = int(self.ui.lineEdit.text())
        self.iter = int(self.ui.lineEdit_2.text())
        self.a = float(self.ui.lineEdit_3.text())
        self.b = float(self.ui.lineEdit_4.text())
        self.p = float(self.ui.lineEdit_6.text())
        self.q = float(self.ui.lineEdit_7.text())
        print(self.n, self.ants, self.iter, self.a, self.b, self.p, self.q)
        self.run_ant()

    def run_ant(self):
        points = generate_problem(self.n)
        paths = []
        print(points)

        aco = ACO(ants=self.ants, iter=self.iter, a=self.a, b=self.b, p=self.p, q=self.q)
        print("aco")
        paths.append(aco.run(points=points, name="ACO"))
        print(paths)
        #print(f"ACO time: {time() - ts}")
        TSP(points=points, paths=paths)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_window = ANT()
    login_window.show()
    app.exec()
