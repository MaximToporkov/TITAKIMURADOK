from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMainWindow, QDialog, QApplication, QTableWidgetItem
from PyQt6.uic import loadUi
from PyQt6 import uic
import sys
from DB.db_insert import add_user_db, add_goods_db, add_order_db, add_pc_db  # add_model_db, add_brand_db, add_order_db
from DB.db_select import select_cat, select_user, \
    select_cpu, select_cpu, select_gpu, select_power, select_ram, select_motherboard, select_cooling, select_hdd, \
    select_master, \
    select_price, \
    select_pc# , select_order #select_brand, select_auto, select_price, select_order, select_user, select_auto_for_form
from settings import REC
from datetime import date, timedelta, datetime


class MainForm(QMainWindow):

    def __init__(self):
        super(MainForm, self).__init__()
        loadUi("main.ui", self)
        self.add_user.clicked.connect(self.__open_add_user)
        self.add_car.clicked.connect(self.__open_add_car)
        self.add_model.triggered.connect(self.__open_add_model)
        self.add_brand.triggered.connect(self.__open_add_brand)
        self.add_order.clicked.connect(self.__open_add_order)
        self.show_user_butt.clicked.connect(self.__show_user)
        #self.show_car_butt.clicked.connect(self.__show_car)
        #self.__show_order()

    def __open_add_user(self) -> None:
        add_user = AddUser()
        widget.addWidget(add_user)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        #widget.setFixedWidth(350)
        #widget.setFixedHeight(200)

    def __open_add_car(self):
        add_car = AddCar()
        widget.addWidget(add_car)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def __open_add_model(self):
        add_model = AddModel()
        widget.addWidget(add_model)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        #widget.setFixedWidth(350)
        #widget.setFixedHeight(200)

    def __open_add_brand(self):
        add_brand = AddBrand()
        widget.addWidget(add_brand)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        #widget.setFixedWidth(350)
        #widget.setFixedHeight(200)

    def __open_add_order(self):
        add_order = AddOrder()
        widget.addWidget(add_order)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        #widget.setFixedWidth(720)
        #widget.setFixedHeight(500)

    def __show_user(self):
        show_user = UserShow()
        widget.addWidget(show_user)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        #widget.setFixedWidth(450)
        #widget.setFixedHeight(270)

    def __show_car(self):
        show_car = AutoShow()
        widget.addWidget(show_car)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def __show_order(self):
        row_index = 0
        for order in select_order():
            self.tableWidget.setRowCount(row_index + 1)
            self.tableWidget.setItem(row_index, 0, QTableWidgetItem(str(order[0])))
            self.tableWidget.setItem(row_index, 1, QTableWidgetItem(str(order[1])))
            self.tableWidget.setItem(row_index, 2, QTableWidgetItem(str(order[2])))
            self.tableWidget.setItem(row_index, 3, QTableWidgetItem(str(order[3])))
            self.tableWidget.setItem(row_index, 4, QTableWidgetItem(str(order[4])))

            row_index += 1


class AddUser(QDialog):

    def __init__(self):
        super(AddUser, self).__init__()
        loadUi("user_add_form.ui", self)
        self.add_button.clicked.connect(self.add_user)

    def add_user(self):
        number = self.number.text()
        name = self.name.text()
        lastname = self.lastname.text()

        print(type(number), "/", name, "/", lastname, "/")
        if number and name and lastname:
            if REC:
                add_user_db(number, name, lastname)
            main_form = MainForm()
            widget.addWidget(main_form)
            widget.setCurrentIndex(widget.currentIndex() + 1)



class AddCar(QDialog):

    def __init__(self):
        super(AddCar, self).__init__()
        loadUi("PC_add_form.ui", self)
        self.add_car.clicked.connect(self.add_car_but)

        for brand in select_cat():
            self.comboBox_3.addItem(f"{brand[1]}")


    def add_car_but(self):
        number = self.number.text()
        brend = self.comboBox_3.currentText()
        location = self.location.text()
        if REC:
            add_goods_db(number, brend, location)
        main_form = MainForm()
        widget.addWidget(main_form)
        widget.setCurrentIndex(widget.currentIndex() + 1)



class AddModel(QDialog):

    def __init__(self):
        super(AddModel, self).__init__()
        loadUi("model_add_form.ui", self)
        self.add_model_but.clicked.connect(self.__add_model)




class AddBrand(QDialog):

    def __init__(self):
        super(AddBrand, self).__init__()
        loadUi("brand_add_form.ui", self)
        self.add_brand_but.clicked.connect(self.__add_brand)



class AddOrder(QDialog):

    def __init__(self):
        super(AddOrder, self).__init__()
        loadUi("order_add_form.ui", self)
        #self.show_but.clicked.connect(self.__show_auto)
        self.calculate.clicked.connect(self.__show_calculate)
        self.creat_order_but.clicked.connect(self.create_order)

        for brand in select_cpu():
            self.brand.addItem(f"{brand[0]}")
        for model in select_gpu():
            self.model.addItem(f"{model[0]}")
        for i in select_ram():
            self.comboBox.addItem(f"{i[0]}")
        for i in select_motherboard():
            self.comboBox_2.addItem(f"{i[0]}")
        for i in select_hdd():
            self.comboBox_3.addItem(f"{i[0]}")
        for i in select_cooling():
            self.comboBox_4.addItem(f"{i[0]}")
        for i in select_power():
            self.comboBox_5.addItem(f"{i[0]}")
        for i in select_master():
            self.comboBox_6.addItem(f"{i[1]}")

    def create_order(self):
        cpu = self.brand.currentText()
        gpu = self.model.currentText()
        ram = self.comboBox.currentText()
        mother = self.comboBox_2.currentText()
        hdd = self.comboBox_3.currentText()
        col = self.comboBox_4.currentText()
        power = self.comboBox_5.currentText()

        if REC:
            add_pc_db(cpu, gpu, ram, mother, hdd, col, power)
            add_order_db(select_master(), select_user(), select_pc(), select_price())
        main_form = MainForm()
        widget.addWidget(main_form)
        widget.setCurrentIndex(widget.currentIndex() + 1)



    def __cacalculate_price(self):
        if self.cout_hour.text():
            cout_hour = int(self.cout_hour.text())
            price = int(select_price(self.number_auto.text()))
            return cout_hour * price

    def __show_calculate(self):
        self.for_payment.setText(f"{self.__cacalculate_price()}")


class UserShow(QDialog):

    def __init__(self):
        super(UserShow, self).__init__()
        loadUi("user_form.ui", self)
        self.exit_butt.clicked.connect(self.__exit)
        row_index = 0
        for user in select_user():
            self.tableWidget.setRowCount(row_index + 1)
            self.tableWidget.setItem(row_index, 0, QTableWidgetItem(user[1]))
            self.tableWidget.setItem(row_index, 1, QTableWidgetItem(str(user[2])))
            self.tableWidget.setItem(row_index, 2, QTableWidgetItem(str(user[3])))
            #self.tableWidget.setItem(row_index, 3, QTableWidgetItem(str(user[4])))
            row_index += 1

    def __exit(self):
        main_form = MainForm()
        widget.addWidget(main_form)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class AutoShow(QDialog):

    def __init__(self):
        super(AutoShow, self).__init__()
        loadUi("auto_form.ui", self)
        self.exit.clicked.connect(self.__exit)


    def __exit(self):
        main_form = MainForm()
        widget.addWidget(main_form)
        widget.setCurrentIndex(widget.currentIndex() + 1)


app = QApplication(sys.argv)
main_window = MainForm()
widget = QtWidgets.QStackedWidget()
widget.addWidget(main_window)
#widget.setFixedWidth(620)
#widget.setFixedHeight(300)
widget.show()
app.exec()