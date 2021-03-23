'''LIBRARIES REQUIRED FOR THE CONSTRUCTION OF THE GRAPHIC'''
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QApplication, QWidget
plt.style.use("ggplot")


#IMPORTING THE DATAFRAME WITH PANDAS
uf = pd.read_csv('https://raw.githubusercontent.com/zackcmariano/'
                 'AdvPrev---Desktop/main/Obten%C3%A7%C3%A3o%20e%20'
                 'Limpeza%20(database)/uf.csv')



#CONSTRUCTION OF THE GRAPHIC FROM DATA
class Canvas(FigureCanvas):
    def __init__(self, parent):
        fig, self.ax = plt.subplots(figsize=(7, 4), dpi=80)
        super().__init__(fig)
        self.setParent(parent)

        x = uf.id_UF
        self.y = uf.quantos

        self.estado = uf.id_UF
        self.estados = ['Dist. Federal', 'São Paulo', 'Minas Gerais',
                     'Rio G do Sul', 'Bahia']

        self.x = np.arange(len(self.estado))
        self.fig, ax = plt.subplots(figsize=(10, 7))
        self.ax.bar(x, uf.quantos, width=0.60, color='#2d5277')
        self.ax.set_title('Estados', fontsize=20, color='#244362')

        self.ax.set_ylim([0, 90000])
        self.ax.set_xticks(x)
        self.ax.set_xticklabels(self.estados)

class AppDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 350)

        chart = Canvas(self)


#PERFORMING THE CONSTRUCTION OF THE GRAPHIC
app = QApplication(sys.argv)
demo = AppDemo()
#plt.savefig('img\GraphState.png',dpi = 80)
demo.show()
sys.exit(app.exec_())