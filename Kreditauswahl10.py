import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import datetime
from functools import partial

from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

from PyQt5 import QtWidgets, uic, sip, QtCore
from pyqtgraph import PlotWidget, GraphicsLayoutWidget
import pyqtgraph as pg
import sys


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        #Load the UI Page
        uic.loadUi('D:/Informatik_ETech/Python/Eigene Module/Kreditauswahl/mainwindow.ui', self)
        
        self.neuerKredit1()
        # self.spinBox_Kreditbetrag_1.valueChanged.connect(self.neuerKredit1)
        # self.spinBox_Kreditbetrag_2.valueChanged.connect(self.neuerKredit2)
        # self.spinBox_Kreditbetrag_3.valueChanged.connect(self.neuerKredit3)
        # self.spinBox_Monatsrate_1.valueChanged.connect(self.neuerKredit1)
        # self.spinBox_Monatsrate_2.valueChanged.connect(self.neuerKredit2)
        # self.spinBox_Monatsrate_3.valueChanged.connect(self.neuerKredit3)
        self.spinBox_Kreditbetrag_1.valueChanged.connect(self.neuerKredit1)
        self.spinBox_Monatsrate_1.valueChanged.connect(self.neuerKredit1)
        self.doubleSpinBox_Zinssatz_1.valueChanged.connect(self.neuerKredit1)
        self.doubleSpinBox_2Zinssatz_1.valueChanged.connect(self.neuerKredit1)
        self.lineEdit_2Zinssatz_Tag.textChanged.connect(self.neuerKredit1)
        self.lineEdit_2Zinssatz_Monat.textChanged.connect(self.neuerKredit1)
        self.lineEdit_2Zinssatz_Jahr.textChanged.connect(self.neuerKredit1)
        self.spinBox_SonTilgRate1_1.valueChanged.connect(self.neuerKredit1)
        self.lineEdit_SonTilgRate1_Tag.textChanged.connect(self.neuerKredit1)
        self.lineEdit_SonTilgRate1_Monat.textChanged.connect(self.neuerKredit1)
        self.lineEdit_SonTilgRate1_Jahr.textChanged.connect(self.neuerKredit1)
        self.spinBox_SonTilgRate2_1.valueChanged.connect(self.neuerKredit1)
        self.lineEdit_SonTilgRate2_Tag.textChanged.connect(self.neuerKredit1)
        self.lineEdit_SonTilgRate2_Monat.textChanged.connect(self.neuerKredit1)
        self.lineEdit_SonTilgRate2_Jahr.textChanged.connect(self.neuerKredit1)

        self.spinBox_Kreditbetrag_2.valueChanged.connect(self.neuerKredit2)
        self.spinBox_Monatsrate_2.valueChanged.connect(self.neuerKredit2)
        self.doubleSpinBox_Zinssatz_2.valueChanged.connect(self.neuerKredit2)
        self.doubleSpinBox_2Zinssatz_2.valueChanged.connect(self.neuerKredit2)
        self.lineEdit_2Zinssatz_Tag_2.textChanged.connect(self.neuerKredit2)
        self.lineEdit_2Zinssatz_Monat_2.textChanged.connect(self.neuerKredit2)
        self.lineEdit_2Zinssatz_Jahr_2.textChanged.connect(self.neuerKredit2)
        self.spinBox_SonTilgRate1_2.valueChanged.connect(self.neuerKredit2)
        self.lineEdit_SonTilgRate1_Tag_2.textChanged.connect(self.neuerKredit2)
        self.lineEdit_SonTilgRate1_Monat_2.textChanged.connect(self.neuerKredit2)
        self.lineEdit_SonTilgRate1_Jahr_2.textChanged.connect(self.neuerKredit2)
        self.spinBox_SonTilgRate2_2.valueChanged.connect(self.neuerKredit2)
        self.lineEdit_SonTilgRate2_Tag_2.textChanged.connect(self.neuerKredit2)
        self.lineEdit_SonTilgRate2_Monat_2.textChanged.connect(self.neuerKredit2)
        self.lineEdit_SonTilgRate2_Jahr_2.textChanged.connect(self.neuerKredit2)

        self.spinBox_Kreditbetrag_3.valueChanged.connect(self.neuerKredit3)
        self.spinBox_Monatsrate_3.valueChanged.connect(self.neuerKredit3)
        self.doubleSpinBox_Zinssatz_3.valueChanged.connect(self.neuerKredit3)
        self.doubleSpinBox_2Zinssatz_3.valueChanged.connect(self.neuerKredit3)
        self.lineEdit_2Zinssatz_Tag_3.textChanged.connect(self.neuerKredit3)
        self.lineEdit_2Zinssatz_Monat_3.textChanged.connect(self.neuerKredit3)
        self.lineEdit_2Zinssatz_Jahr_3.textChanged.connect(self.neuerKredit3)
        self.spinBox_SonTilgRate1_3.valueChanged.connect(self.neuerKredit3)
        self.lineEdit_SonTilgRate1_Tag_3.textChanged.connect(self.neuerKredit3)
        self.lineEdit_SonTilgRate1_Monat_3.textChanged.connect(self.neuerKredit3)
        self.lineEdit_SonTilgRate1_Jahr_3.textChanged.connect(self.neuerKredit3)
        self.spinBox_SonTilgRate2_3.valueChanged.connect(self.neuerKredit3)
        self.lineEdit_SonTilgRate2_Tag_3.textChanged.connect(self.neuerKredit3)
        self.lineEdit_SonTilgRate2_Monat_3.textChanged.connect(self.neuerKredit3)
        self.lineEdit_SonTilgRate2_Jahr_3.textChanged.connect(self.neuerKredit3)

    def neuerKredit1(self):
        self.betrag_1 = self.spinBox_Kreditbetrag_1.value()
        self.m_zahlung_1 = self.spinBox_Monatsrate_1.value()
        self.zsatz_1 = self.doubleSpinBox_Zinssatz_1.value()
        self.zsatz2_1 = self.doubleSpinBox_2Zinssatz_1.value()
        self.zsatz2_1_tag = self.lineEdit_2Zinssatz_Tag.text()
        self.zsatz2_1_monat = self.lineEdit_2Zinssatz_Monat.text()
        self.zsatz2_1_jahr = self.lineEdit_2Zinssatz_Jahr.text()
        self.sonTilgRate1_1 = self.spinBox_SonTilgRate1_1.value()
        self.sonTilgRate1_1_tag = self.lineEdit_SonTilgRate1_Tag.text()
        self.sonTilgRate1_1_Monat = self.lineEdit_SonTilgRate1_Monat.text()
        self.sonTilgRate1_1_Jahr = self.lineEdit_SonTilgRate1_Jahr.text()
        self.sonTilgRate2_1 = self.spinBox_SonTilgRate2_1.value()
        self.sonTilgRate2_1_tag = self.lineEdit_SonTilgRate2_Tag.text()
        self.sonTilgRate2_1_Monat = self.lineEdit_SonTilgRate2_Monat.text()
        self.sonTilgRate2_1_Jahr = self.lineEdit_SonTilgRate2_Jahr.text()
        self.kredit_1 = Kredit(self.betrag_1, self.m_zahlung_1, self.zsatz_1, self.zsatz2_1, self.zsatz2_1_tag, self.zsatz2_1_monat, self.zsatz2_1_jahr, self.sonTilgRate1_1,
                        self.sonTilgRate1_1_tag, self.sonTilgRate1_1_Monat, self.sonTilgRate1_1_Jahr, self.sonTilgRate2_1, self.sonTilgRate2_1_tag, self.sonTilgRate2_1_Monat,
                        self.sonTilgRate2_1_Jahr)
        self.neuerKredit2()
        self.neuerKredit3()
        self.del_plot1()
        
    def neuerKredit2(self):
        self.betrag_2 = self.spinBox_Kreditbetrag_2.value()
        self.m_zahlung_2 = self.spinBox_Monatsrate_2.value()
        self.zsatz_2 = self.doubleSpinBox_Zinssatz_2.value()
        self.zsatz2_2 = self.doubleSpinBox_2Zinssatz_2.value()
        self.zsatz2_2_tag = self.lineEdit_2Zinssatz_Tag_2.text()
        self.zsatz2_2_monat = self.lineEdit_2Zinssatz_Monat_2.text()
        self.zsatz2_2_jahr = self.lineEdit_2Zinssatz_Jahr_2.text()
        self.sonTilgRate1_2 = self.spinBox_SonTilgRate1_2.value()
        self.sonTilgRate1_2_tag = self.lineEdit_SonTilgRate1_Tag_2.text()
        self.sonTilgRate1_2_Monat = self.lineEdit_SonTilgRate1_Monat_2.text()
        self.sonTilgRate1_2_Jahr = self.lineEdit_SonTilgRate1_Jahr_2.text()
        self.sonTilgRate2_2 = self.spinBox_SonTilgRate2_2.value()
        self.sonTilgRate2_2_tag = self.lineEdit_SonTilgRate2_Tag_2.text()
        self.sonTilgRate2_2_Monat = self.lineEdit_SonTilgRate2_Monat_2.text()
        self.sonTilgRate2_2_Jahr = self.lineEdit_SonTilgRate2_Jahr_2.text() 
        self.kredit_2 = Kredit(self.betrag_2, self.m_zahlung_2, self.zsatz_2, self.zsatz2_2, self.zsatz2_2_tag, self.zsatz2_2_monat, self.zsatz2_2_jahr, self.sonTilgRate1_2,
                        self.sonTilgRate1_2_tag, self.sonTilgRate1_2_Monat, self.sonTilgRate1_2_Jahr, self.sonTilgRate2_2, self.sonTilgRate2_2_tag, self.sonTilgRate2_2_Monat,
                        self.sonTilgRate2_2_Jahr)
        self.neuerKredit3()
        self.del_plot2()

    def neuerKredit3(self):
        self.betrag_3 = self.spinBox_Kreditbetrag_3.value()
        self.m_zahlung_3 = self.spinBox_Monatsrate_3.value()
        self.zsatz_3 = self.doubleSpinBox_Zinssatz_3.value()
        self.zsatz2_3 = self.doubleSpinBox_2Zinssatz_3.value()
        self.zsatz2_3_tag = self.lineEdit_2Zinssatz_Tag_3.text()
        self.zsatz2_3_monat = self.lineEdit_2Zinssatz_Monat_3.text()
        self.zsatz2_3_jahr = self.lineEdit_2Zinssatz_Jahr_3.text()
        self.sonTilgRate1_3 = self.spinBox_SonTilgRate1_3.value()
        self.sonTilgRate1_3_tag = self.lineEdit_SonTilgRate1_Tag_3.text()
        self.sonTilgRate1_3_Monat = self.lineEdit_SonTilgRate1_Monat_3.text()
        self.sonTilgRate1_3_Jahr = self.lineEdit_SonTilgRate1_Jahr_3.text()
        self.sonTilgRate2_3 = self.spinBox_SonTilgRate2_3.value()
        self.sonTilgRate2_3_tag = self.lineEdit_SonTilgRate2_Tag_3.text()
        self.sonTilgRate2_3_Monat = self.lineEdit_SonTilgRate2_Monat_3.text()
        self.sonTilgRate2_3_Jahr = self.lineEdit_SonTilgRate2_Jahr_3.text()
        self.kredit_3 = Kredit(self.betrag_3, self.m_zahlung_3, self.zsatz_3, self.zsatz2_3, self.zsatz2_3_tag, self.zsatz2_3_monat, self.zsatz2_3_jahr, self.sonTilgRate1_3,
                        self.sonTilgRate1_3_tag, self.sonTilgRate1_3_Monat, self.sonTilgRate1_3_Jahr, self.sonTilgRate2_3, self.sonTilgRate2_3_tag, self.sonTilgRate2_3_Monat,
                        self.sonTilgRate2_3_Jahr)
        self.del_plot3()

    def del_plot1(self):
        try:
            self.graphWidget.clear()
        except:
            pass
        self.draw([self.kredit_1, self.kredit_2, self.kredit_3], ["Gesamtkosten", "Kontostand", "Zinsen gesamt"])
        self.print_table1()

    def del_plot2(self):
        try:
            self.graphWidget.clear()
        except:
            pass
        self.draw([self.kredit_1, self.kredit_2, self.kredit_3], ["Gesamtkosten", "Kontostand", "Zinsen gesamt"])
        self.print_table2()

    def del_plot3(self):
        try:
            self.graphWidget.clear()
        except:
            pass
        self.draw([self.kredit_1, self.kredit_2, self.kredit_3], ["Gesamtkosten", "Kontostand", "Zinsen gesamt"])
        self.print_table3()

    def draw(self, objects, variables, linestyles=[QtCore.Qt.SolidLine, QtCore.Qt.DashLine, QtCore.Qt.DashDotLine, QtCore.Qt.DotLine], colors=["y", "b", "r", "g"]):
        self.w = self.graphWidget
        for i, var in enumerate(variables):
            p = self.w.addPlot(row=i, col=0)
            p.setTitle(var)
            p.addLegend()
            for j, obj in enumerate(objects):
                pen = pg.mkPen(color=colors[j], style=linestyles[j])
                p.plot(obj.frame[var], pen=pen, name=obj.name)
            # ax[i].plot(obj.frame.Zahlungen, "-k", linewidth=0.5, label="monatliche Raten")
            # ax[i].set_title(var)
            # #ax[i].set_facecolor("0.5")
            # ax[i].grid(True)
            # ax[i].legend()
        #plt.tight_layout()
        #return fig

    def print_table1(self):
        t = self.tableWidget_Kredit_1
        t.setFormat("%20.2f")
        t.setData(self.kredit_1.frame_grouped_DEdat.values)
        t.setHorizontalHeaderLabels(["Zeitindex", "Zahlungen", "Gesamtkosten", "Tilgung", "Zinsen", "Zinsen gesamt", "Kontostand"])
        t.horizontalHeader().setDefaultAlignment(QtCore.Qt.AlignRight)
    
    def print_table2(self):
        t = self.tableWidget_Kredit_2
        t.setFormat("%20.2f")
        t.setData(self.kredit_2.frame_grouped_DEdat.values)
        t.setHorizontalHeaderLabels(["Zeitindex", "Zahlungen", "Gesamtkosten", "Tilgung", "Zinsen", "Zinsen gesamt", "Kontostand"])
        t.horizontalHeader().setDefaultAlignment(QtCore.Qt.AlignRight)

    def print_table3(self):
        t = self.tableWidget_Kredit_3
        t.setFormat("%20.2f")
        t.setData(self.kredit_3.frame_grouped_DEdat.values)
        t.setHorizontalHeaderLabels(["Zeitindex", "Zahlungen", "Gesamtkosten", "Tilgung", "Zinsen", "Zinsen gesamt", "Kontostand"])
        t.horizontalHeader().setDefaultAlignment(QtCore.Qt.AlignRight)
                
        
class Kredit:
    def __init__(self, betrag, m_zahlung, zsatz, zsatz2=0, zsatz2_tag=None, zsatz2_monat=None, zsatz2_jahr=None, son_tilg_rate1=0, son_tilg_rate1_tag=None, son_tilg_rate1_monat=None, son_tilg_rate1_jahr=None,
                son_tilg_rate2=0, son_tilg_rate2_tag=None, son_tilg_rate2_monat=None, son_tilg_rate2_jahr=None) -> None:
        self.betrag = betrag
        self.m_zahlung = m_zahlung
        self.zsatz = zsatz/100/12
        self.zsatz2 = zsatz2/100/12
        self.zsatz2_tag = zsatz2_tag
        self.zsatz2_monat = zsatz2_monat
        self.zsatz2_jahr = zsatz2_jahr
        self.son_tilg_rate1 = son_tilg_rate1
        self.son_tilg_rate1_tag = son_tilg_rate1_tag
        self.son_tilg_rate1_monat = son_tilg_rate1_monat
        self.son_tilg_rate1_jahr = son_tilg_rate1_jahr
        self.son_tilg_rate2 = son_tilg_rate2
        self.son_tilg_rate2_tag = son_tilg_rate2_tag
        self.son_tilg_rate2_monat = son_tilg_rate2_monat
        self.son_tilg_rate2_jahr = son_tilg_rate2_jahr
        if (zsatz2_tag and zsatz2_monat and zsatz2_jahr):
            self.zsatz2_dat = datetime.date(int(zsatz2_jahr), int(zsatz2_monat), int(zsatz2_tag))
        if (son_tilg_rate1_tag and son_tilg_rate1_monat and son_tilg_rate1_jahr):
            self.son_tilg_rate1_dat = datetime.date(int(son_tilg_rate1_jahr), int(son_tilg_rate1_monat), int(son_tilg_rate1_tag))
        if (son_tilg_rate2_tag and son_tilg_rate2_monat and son_tilg_rate2_jahr):
            self.son_tilg_rate2_dat = datetime.date(int(son_tilg_rate2_jahr), int(son_tilg_rate2_monat), int(son_tilg_rate2_tag))
        self.name = f"{betrag}_{m_zahlung}_{zsatz}_2zs{zsatz2}_1st{son_tilg_rate1}_2st{son_tilg_rate2}"
        self.m()

    def m(self):
        i = 1
        self.restbetrag = [self.betrag]
        self.mon_zahlung = [0]
        self.tilgung = [0]
        self.zinsen = [0]
        while self.restbetrag[-1] > 0:
            i += 1
            index = pd.date_range("31-08-2021", periods=i, freq="M")
            self.mon_zahlung.append(self.m_zahlung)
            if (self.son_tilg_rate1 > 0 and self.son_tilg_rate1_tag and self.son_tilg_rate1_monat and self.son_tilg_rate1_jahr):
                if index[-1] == self.son_tilg_rate1_dat:
                    self.mon_zahlung[-1] = self.son_tilg_rate1 + self.m_zahlung
            if (self.son_tilg_rate2 > 0 and self.son_tilg_rate2_tag and self.son_tilg_rate2_monat and self.son_tilg_rate2_jahr):
                if index[-1] == self.son_tilg_rate2_dat:
                    self.mon_zahlung[-1] = self.son_tilg_rate2 + self.m_zahlung     
            if (self.zsatz2 > 0 and self.zsatz2_tag and self.zsatz2_monat and self.zsatz2_jahr):
                if index[-1] >= self.zsatz2_dat:
                    self.zsatz = self.zsatz2
            self.restbetrag.append(round(self.restbetrag[-1] * (1 + self.zsatz) - self.mon_zahlung[-1], 2))
            self.tilgung.append(round(self.restbetrag[-2] - self.restbetrag[-1], 2))
            self.zinsen.append(round(self.restbetrag[-2] * self.zsatz, 2))
        if self.restbetrag[-1] < 0:
            self.restbetrag[-1] = 0
            self.tilgung[-1] = self.restbetrag[-2] * (1 + self.zsatz)
            self.mon_zahlung[-1] = self.tilgung[-1]
        self.frame = pd.DataFrame({"Zahlungen": self.mon_zahlung, "Gesamtkosten": np.cumsum(self.mon_zahlung), "Tilgung": self.tilgung, "Zinsen": self.zinsen, "Zinsen gesamt": np.cumsum(self.zinsen),
                                    "Kontostand": self.restbetrag}, index=index)
        frame2 = self.frame.resample("Y").sum()
        frame2 = frame2.round(2)
        frame3 = self.frame["Gesamtkosten"].resample("Y").max()
        frame4 = self.frame["Zinsen gesamt"].resample("Y").max()
        frame5 = self.frame["Kontostand"].resample("Y").min()
        frame2["Gesamtkosten"] = frame3
        frame2["Zinsen gesamt"] = frame4
        frame2["Kontostand"] = frame5  
        self.frame_grouped = pd.concat([pd.DataFrame([self.frame.iloc[0,:]]), frame2])
        self.frame_grouped_DEdat = self.frame_grouped.copy()
        self.frame_grouped_DEdat.index = self.frame_grouped.index.strftime("%d.%m.%Y")
        self.frame_grouped_DEdat.reset_index(inplace=True)
        self.frame_grouped_DEdat.iloc[-1,0] = self.frame.index[-1].strftime("%d.%m.%Y")

    def save_grouped_frame(self):
        self.frame_grouped_DEdat.to_csv(f"D:/Informatik & ETech/Python/Eigene Module/Kreditauswahl/Output/grouped_frame_{self.name}.csv", float_format="%.2f")

    def save_frame(self):
        self.frame.to_csv(f"D:/Informatik & ETech/Python/Eigene Module/Kreditauswahl/Output/frame_{self.name}.csv", float_format="%.2f")



def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    
    # tp_50_500 = Kredit(main.betrag, m_zahlung=500, zsatz=2.0)
    # tp_60_600 = Kredit(betrag=60000, m_zahlung=600, zsatz=2.0)

    
    main.show()
    
    # tp_50_500.save_grouped_frame()
    # tp_50_500.save_frame()
    
    # p = draw([tp_50_500, tp_60_600], ["Gesamtkosten", "Kontostand", "Zinsen gesamt"])
    # main.add_plot(p)

    #plt.show()
    
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()