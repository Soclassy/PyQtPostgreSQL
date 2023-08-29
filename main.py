import psycopg2
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QTabWidget, QAbstractScrollArea,
                             QVBoxLayout, QHBoxLayout, QTableWidget, QGroupBox, QTableWidgetItem, QPushButton,
                             QMessageBox)

class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self._connect_to_db()
        self.setWindowTitle("Shedule")
        self.vbox = QVBoxLayout(self)
        self.tabs = QTabWidget(self)
        self.vbox.addWidget(self.tabs)
        self._create_shedule_tab()

    def _connect_to_db(self):
        self.conn = psycopg2.connect(database="raspisanie", user="postgres", password="46283791", host="localhost",
                                     port="5432")
        self.cursor = self.conn.cursor()

    def _create_shedule_tab(self):
        self.days = ['Ponedelnik1', 'Ponedelnik2', 'Vtornik1', 'Vtornik2',
                     'Sreda1', 'Sreda2', 'Chetverg1', 'Chetverg2',
                     'Pyatnica1', 'Pyatnica2', 'Subbota1', 'Subbota2']
        self.shedule_tab = QWidget()
        self.tabs.addTab(self.shedule_tab, "Shedule")

        self.subj_tab = QWidget()
        self.tabs.addTab(self.subj_tab, "Subj")

        self.teach_tab = QWidget()
        self.tabs.addTab(self.teach_tab, "teach")

        #SHEDULE TAB!!!
        self.monday_gbox = QGroupBox("Monday")
        self.svbox = QVBoxLayout()
        self.shbox1 = QHBoxLayout()
        self.shbox2 = QHBoxLayout()
        self.shbox3 = QHBoxLayout()
        self.svbox.addLayout(self.shbox1)
        self.svbox.addLayout(self.shbox2)
        self.shbox1.addWidget(self.monday_gbox)

        for i in range(len(self.days)):
            self.days[i] = QPushButton(f'{self.days[i]}')
            self.svbox.addWidget(self.days[i])

        self.days[0].clicked.connect(lambda: self.whichbtn(self.days[0].text()))
        self.days[1].clicked.connect(lambda: self.whichbtn(self.days[1].text()))
        self.days[2].clicked.connect(lambda: self.whichbtn(self.days[2].text()))
        self.days[3].clicked.connect(lambda: self.whichbtn(self.days[3].text()))
        self.days[4].clicked.connect(lambda: self.whichbtn(self.days[4].text()))
        self.days[5].clicked.connect(lambda: self.whichbtn(self.days[5].text()))
        self.days[6].clicked.connect(lambda: self.whichbtn(self.days[6].text()))
        self.days[7].clicked.connect(lambda: self.whichbtn(self.days[7].text()))
        self.days[8].clicked.connect(lambda: self.whichbtn(self.days[8].text()))
        self.days[9].clicked.connect(lambda: self.whichbtn(self.days[9].text()))
        self.days[10].clicked.connect(lambda: self.whichbtn(self.days[10].text()))
        self.days[11].clicked.connect(lambda: self.whichbtn(self.days[11].text()))

        self.days[0].clicked.connect(lambda: self._update_monday_table(self.days[0].text()))
        self.days[1].clicked.connect(lambda: self._update_monday_table(self.days[1].text()))
        self.days[2].clicked.connect(lambda: self._update_monday_table(self.days[2].text()))
        self.days[3].clicked.connect(lambda: self._update_monday_table(self.days[3].text()))
        self.days[4].clicked.connect(lambda: self._update_monday_table(self.days[4].text()))
        self.days[5].clicked.connect(lambda: self._update_monday_table(self.days[5].text()))
        self.days[6].clicked.connect(lambda: self._update_monday_table(self.days[6].text()))
        self.days[7].clicked.connect(lambda: self._update_monday_table(self.days[7].text()))
        self.days[8].clicked.connect(lambda: self._update_monday_table(self.days[8].text()))
        self.days[9].clicked.connect(lambda: self._update_monday_table(self.days[9].text()))
        self.days[10].clicked.connect(lambda: self._update_monday_table(self.days[10].text()))
        self.days[11].clicked.connect(lambda: self._update_monday_table(self.days[11].text()))

        self._create_monday_table(name='Ponedelnik1')

        self.update_shedule_button = QPushButton("Update")
        self.shbox2.addWidget(self.update_shedule_button)
        self.update_shedule_button.clicked.connect(self._update_shedule)
        self.shedule_tab.setLayout(self.svbox)

        #SUBJ TAB
        self.monday_gbox_2 = QGroupBox("Monday")
        self.svbox2 = QVBoxLayout()
        self.shbox1_2 = QHBoxLayout()
        self.shbox2_2 = QHBoxLayout()
        self.shbox3_2 = QHBoxLayout()
        self.svbox2.addLayout(self.shbox1_2)
        self.svbox2.addLayout(self.shbox2_2)
        self.shbox1_2.addWidget(self.monday_gbox_2)

        self._create_monday_table_2()

        self.update_shedule_button_2 = QPushButton("Update")
        self.shbox2.addWidget(self.update_shedule_button_2)
        self.update_shedule_button_2.clicked.connect(self._update_shedule2)
        self.subj_tab.setLayout(self.svbox2)

        #TEACH TAB
        self.monday_gbox_3 = QGroupBox("Monday")
        self.svbox3 = QVBoxLayout()
        self.shbox1_3 = QHBoxLayout()
        self.shbox2_3 = QHBoxLayout()
        self.shbox3_3 = QHBoxLayout()
        self.svbox3.addLayout(self.shbox1_3)
        self.svbox3.addLayout(self.shbox2_3)
        self.shbox1_3.addWidget(self.monday_gbox_3)

        self._create_monday_table_3()

        self.update_shedule_button_3 = QPushButton("Update")
        self.shbox3.addWidget(self.update_shedule_button_3)
        self.update_shedule_button_3.clicked.connect(self._update_shedule3)
        self.teach_tab.setLayout(self.svbox3)

    def _create_monday_table(self, name):
        self.monday_table = QTableWidget()
        self.monday_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.monday_table.setColumnCount(4)
        self.monday_table.setHorizontalHeaderLabels(["Subject", "Time", "", ""])
        name1 = name

        self._update_monday_table(name1)

        self.mvbox = QVBoxLayout()
        self.mvbox.addWidget(self.monday_table)
        self.monday_gbox.setLayout(self.mvbox)

    def _create_monday_table_2(self):
        self.monday_table2 = QTableWidget()
        self.monday_table2.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.monday_table2.setColumnCount(2)
        self.monday_table2.setHorizontalHeaderLabels(["Subject", ""])

        self._update_monday_table_2()

        self.mvbox2 = QVBoxLayout()
        self.mvbox2.addWidget(self.monday_table2)
        self.monday_gbox_2.setLayout(self.mvbox2)

    def _create_monday_table_3(self):
        self.monday_table3 = QTableWidget()
        self.monday_table3.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.monday_table3.setColumnCount(3)
        self.monday_table3.setHorizontalHeaderLabels(["full_name", "Subject", ""])

        self._update_monday_table_3()

        self.mvbox3 = QVBoxLayout()
        self.mvbox3.addWidget(self.monday_table3)
        self.monday_gbox_3.setLayout(self.mvbox3)

    def _update_monday_table(self, name):
        print(name)

        self.cursor.execute("SELECT * FROM rasp.timetable WHERE day=%s", (name, ))
        records = list(self.cursor.fetchall())
        self.monday_table.setRowCount(len(records) + 1)
        for i, r in enumerate(records):
            r = list(r)
            joinButton = QPushButton("Join")
            self.monday_table.setItem(i, 0,
                                      QTableWidgetItem(str(r[2])))
            self.monday_table.setItem(i, 1,
                                      QTableWidgetItem(str(r[4])))
            self.monday_table.setItem(i, 2,
                                      QTableWidgetItem(str(r[3])))
            self.monday_table.setCellWidget(i, 3, joinButton)
            joinButton.clicked.connect(lambda ch, num=i:
                                       self._change_day_from_table(num, name))
            self.monday_table.resizeRowsToContents()

    def _update_monday_table_2(self):
        self.cursor.execute("SELECT name FROM rasp.subject")
        self.records = list(self.cursor.fetchall())
        self.fin_rec = []
        for i, r in enumerate(self.records):
            self.fin_rec.append(self.records[i][0])

        print(self.fin_rec)
        self.monday_table2.setRowCount(len(self.records) + 1)
        for i, r in enumerate(self.records):
            r = list(r)
            joinButton2 = QPushButton("Join")
            self.monday_table2.setItem(i, 0,
                                      QTableWidgetItem(str(r[0])))
            self.monday_table2.setCellWidget(i, 1, joinButton2)
            joinButton2.clicked.connect(lambda ch, num=i:
                                       self._change_day_from_table2(num))
            self.monday_table2.resizeRowsToContents()

    def _update_monday_table_3(self):

        self.cursor.execute("SELECT * FROM rasp.teacher")
        records = list(self.cursor.fetchall())
        self.monday_table3.setRowCount(len(records) + 1)
        for i, r in enumerate(records):
            r = list(r)
            joinButton = QPushButton("Join")
            self.monday_table3.setItem(i, 0,
                                      QTableWidgetItem(str(r[1])))
            self.monday_table3.setItem(i, 1,
                                      QTableWidgetItem(str(r[2])))
            self.monday_table3.setCellWidget(i, 2, joinButton)
            joinButton.clicked.connect(lambda ch, num=i:
                                       self._change_day_from_table3(num))
            self.monday_table.resizeRowsToContents()

    def _change_day_from_table(self, rowNum, day):
        row = list()
        for i in range(self.monday_table.columnCount()):
            try:
                row.append(self.monday_table.item(rowNum, i).text())
            except:
                row.append(None)
        print(row)

        try:
            self.cursor.execute("UPDATE rasp.timetable set subj = %s where start_time = %s and day = %s", (row[0], row[1], day))
            self.conn.commit()
        except:
            QMessageBox.about(self, "Error", "Enter all fields")

    def _change_day_from_table2(self, rowNum):
        row = list()
        for i in range(self.monday_table2.columnCount()):
            try:
                row.append(self.monday_table2.item(rowNum, i).text())
            except:
                row.append(None)
        print(row)

        try:
            self.cursor.execute("UPDATE rasp.subject set name = %s where name = %s", (row[0], ))
            self.conn.commit()
        except:
            QMessageBox.about(self, "Error", "Enter all fields")

    def _change_day_from_table3(self, rowNum):
        row = list()
        for i in range(self.monday_table3.columnCount()):
            try:
                row.append(self.monday_table3.item(rowNum, i).text())
            except:
                row.append(None)
        print(row)

        try:
            self.cursor.execute("UPDATE rasp.subject set name = %s where name = %s", (row[0], ))
            self.conn.commit()
        except:
            QMessageBox.about(self, "Error", "Enter all fields")

    def _update_shedule(self):
        self._update_monday_table(name='Ponedelnik1')

    def _update_shedule2(self):
        self._update_monday_table_2()

    def _update_shedule3(self):
        self._update_monday_table_3()

    def whichbtn(self, btn):
        print('clicked button is ' + btn)

app = QApplication(sys.argv)
win = MainWindow()
win.show()
sys.exit(app.exec_())
