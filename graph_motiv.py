'''LIBRARIES REQUIRED FOR THE CONSTRUCTION OF THE GRAPHIC'''
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QApplication, QWidget
plt.style.use("ggplot")


#IMPORTING THE DATAFRAME WITH PANDAS
motivo = pd.read_csv('https://raw.githubusercontent.com/zackcmariano/AdvPrev---'
                     'Desktop/main/Obten%C3%A7%C3%A3o%20e%20Limpeza%20(database)'
                     '/motivo.csv')


#CONSTRUCTION OF THE GRAPHIC FROM DATA
class Canvas(FigureCanvas):
    def __init__(self, parent):
        fig, self.ax = plt.subplots(figsize=(7, 4), dpi=80)
        super().__init__(fig)
        self.setParent(parent)

        x = motivo.id_motivo
        self.y = motivo.quantos

        self.especie = motivo.id_motivo
        self.especies = ['Motivo 1', 'Motivo 2', 'Motivo 3',
                     'Motivo 4', 'Motivo 5']

        self.x = np.arange(len(self.especie))
        self.fig, ax = plt.subplots(figsize=(10, 7))
        self.ax.bar(x, motivo.quantos, width=0.60, color='#5a854c')
        self.ax.set_title('Motivos', fontsize=20, color='#37542e')

        self.ax.set_ylim([0, 60000])
        self.ax.set_xticks(x)
        self.ax.set_xticklabels(self.especies)


class AppDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 350)

        chart = Canvas(self)


#PERFORMING THE CONSTRUCTION OF THE GRAPHIC
app = QApplication(sys.argv)
demo = AppDemo()
#plt.savefig('img\GraphMotives.png',dpi = 80)
demo.show()
sys.exit(app.exec_())