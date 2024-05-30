from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QApplication, QMessageBox
import mysql.connector as sql
from Agent_ui import Ui_MainWindow as AgentUI
from Course_ui import Ui_MainWindow as CourseUI
from Customer_ui import Ui_MainWindow as CustomerUI
from Department_ui import Ui_MainWindow as DepartmentUI
from Property_ui import Ui_MainWindow as PropertyUI
from Transaction_ui import Ui_MainWindow as TransactionUI
from search_result_dialog import SearchResultDialog

class MyGUI(QMainWindow):

    def __init__(self):
        super(MyGUI, self).__init__()
        uic.loadUi("Main.ui",self)

        self.show()

        self.agent_ui = AgentUI()
        self.course_ui = CourseUI()
        self.customer_ui = CustomerUI()
        self.department_ui = DepartmentUI()
        self.property_ui = PropertyUI()
        self.transaction_ui = TransactionUI()
    

        self.login_button.clicked.connect(self.login)
        self.agent.clicked.connect(self.open_agent_ui)
        self.course.clicked.connect(self.open_course_ui)
        self.customer.clicked.connect(self.open_customer_ui)
        self.department.clicked.connect(self.open_department_ui)
        self.prop.clicked.connect(self.open_property_ui)
        self.transaction.clicked.connect(self.open_transaction_ui)



    def login(self):
        if self.username.text() == "vansh" and self.password.text() == "payala":
            self.dataentry.setEnabled(True)
            self.agent.setEnabled(True)
            self.course.setEnabled(True)
            self.customer.setEnabled(True)
            self.department.setEnabled(True)
            self.prop.setEnabled(True)
            self.transaction.setEnabled(True)
        else:
            message = QMessageBox()
            message.setText("Invalid Login")
            message.exec_()

# Agent and Agent_Department Table 

    def open_agent_ui(self):
        self.agent_window = QtWidgets.QMainWindow()
        self.agent_ui.setupUi(self.agent_window) 
        self.agent_window.show()
        self.agent_ui.submit1.clicked.connect(self.get_agent_data) 
        self.agent_ui.submit11.clicked.connect(self.get_agent_data2)
        self.agent_ui.submit111.clicked.connect(self.update_agent_data)
        self.agent_ui.submit1111.clicked.connect(self.get_agent_data4)

# Insertion Function

    def get_agent_data(self):
        agent_data = self.agent_ui.get_agent_data()
        self.agent_data = agent_data

        conn = sql.connect(host = "localhost" , user = "Vanshpayala" , passwd = "vanshpayala" , database = "real_estate_management")
        if conn.is_connected() == True:
            print("Connection is Established")
        else:
            print("Not Established")
        cursor = conn.cursor()
        if (agent_data != []):
            a = "insert into agent values ("+"'"+agent_data[0]+"'"+","+"'"+agent_data[1]+"'"+","+"'"+agent_data[2]+"'"+","+"'"+agent_data[4]+"'"+","+"'"+agent_data[5]+"'"+");"
            cursor.execute(a)
            b = "insert into agent_department values ("+"'"+agent_data[0]+"'"+","+"'"+agent_data[3]+"'"+");"
            cursor.execute(b)

            conn.commit()
            conn.close

            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setText("You have successfully inserted data in the Database !")
            msg_box.setWindowTitle("Success")
            msg_box.exec_()

        print("Insertion is done !")

# Deletion Function

    def get_agent_data2(self):
        agent_data2 = self.agent_ui.get_agent_data2()
        self.agent_data2 = agent_data2

        conn = sql.connect(host = "localhost" , user = "Vanshpayala" , passwd = "vanshpayala" , database = "real_estate_management")
        if conn.is_connected() == True:
            print("Connection is Established")
        else:
            print("Not Established")
        cursor = conn.cursor()
        if (agent_data2 != []):
            a = "delete from agent where agent_id = "+"'"+agent_data2[0]+"'"+";"
            cursor.execute(a)
            b = "delete from agent_department where agent_id = "+"'"+agent_data2[0]+"'"+";"
            cursor.execute(b)

            conn.commit()
            conn.close

            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setText("You have successfully deleted data from the Database !")
            msg_box.setWindowTitle("Success")
            msg_box.exec_()

        print("Deletion is done !")

# Updation Function

    def update_agent_data(self):
        agent_id = self.agent_ui.a1.text()
        name = self.agent_ui.a2.text()
        specialization = self.agent_ui.a3.text()
        department_id = self.agent_ui.a4.text()
        performance_metrics = self.agent_ui.a5.text()
        property_id = self.agent_ui.a6.text()

        conn = sql.connect(host="localhost", user="Vanshpayala", passwd="vanshpayala", database="real_estate_management")
        if conn.is_connected():
            print("Connection is Established")
            cursor = conn.cursor()

            update_query_agent = "UPDATE agent SET "
            update_values_agent = []
            if name:
                update_query_agent += "name = %s, "
                update_values_agent.append(name)
            if specialization:
                update_query_agent += "specialization = %s, "
                update_values_agent.append(specialization)
            if department_id:
                x = "UPDATE agent_department SET department_id = " + "'"+ department_id +"'"+ " where agent_id = " + "'"+ agent_id +"';"
                cursor.execute(x)

                conn.commit()
                print("Agent_department table updated successfully")
            if performance_metrics:
                update_query_agent += "performance_metrics = %s, "
                update_values_agent.append(performance_metrics)
            if property_id:
                update_query_agent += "property_id = %s, "
                update_values_agent.append(property_id)
            update_query_agent = update_query_agent.rstrip(", ")
            update_query_agent += " WHERE agent_id = %s"
            update_values_agent.append(agent_id)
            cursor.execute(update_query_agent, update_values_agent)
            print("Agent table updated successfully")
            print(update_values_agent)

            conn.commit()
            cursor.close()
            conn.close()
            print("Update is done !")

            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setText("You have successfully updated data in the Database !")
            msg_box.setWindowTitle("Success")
            msg_box.exec_()
        else:
            print("Not Established")

# Search Function

    def get_agent_data4(self):
        agent_data4 = self.agent_ui.get_agent_data4()
        self.agent_data4 = agent_data4

        conn = sql.connect(host = "localhost" , user = "Vanshpayala" , passwd = "vanshpayala" , database = "real_estate_management")
        if conn.is_connected() == True:
            print("Connection is Established")
        else:
            print("Not Established")
        cursor = conn.cursor()
        if (agent_data4 != []):
            lst1 = ['Agent ID','Name','Specialization','Perforamnce Metrics','Property ID']
            lst2 = ['Department ID']
            a = "select * from agent where agent_id = "+"'"+agent_data4[0]+"'"+";"
            cursor.execute(a)
            record1 = cursor.fetchall()

            b = "select * from agent_department where agent_id = "+"'"+agent_data4[0]+"'"+";"
            cursor.execute(b)
            record2 = cursor.fetchall()

            headers = ["Field", "Value"]
            data = []

            for i in range(5):
                data.append([lst1[i], record1[0][i]])

            data.append([lst2[0], record2[0][1]])

            search_result_dialog = SearchResultDialog(headers, data, self)
            search_result_dialog.exec_()

            conn.commit()
            conn.close


# Course Table

    def open_course_ui(self):
        self.course_window = QtWidgets.QMainWindow()
        self.course_ui.setupUi(self.course_window) 
        self.course_window.show()
        self.course_ui.submit2.clicked.connect(self.get_course_data)  
        self.course_ui.submit22.clicked.connect(self.get_course_data2)
        self.course_ui.submit222.clicked.connect(self.update_course_data)
        self.course_ui.submit2222.clicked.connect(self.get_course_data4)

# Insertion Function

    def get_course_data(self):
        course_data = self.course_ui.get_course_data()
        self.course_data = course_data

        conn = sql.connect(host = "localhost" , user = "Vanshpayala" , passwd = "vanshpayala" , database = "real_estate_management")
        if conn.is_connected() == True:
            print("Connection is Established")
        else:
            print("Not Established")
        cursor = conn.cursor()
        if (course_data != []):
            a = "insert into course values ("+"'"+course_data[0]+"'"+","+"'"+course_data[1]+"'"+","+"'"+course_data[2]+"'"+","+"'"+course_data[3]+"'"+","+"'"+course_data[4]+"'"+","+"'"+course_data[5]+"'"+","+"'"+course_data[6]+"'"+");"
            cursor.execute(a)

            conn.commit()
            conn.close

            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setText("You have successfully inserted data in the Database !")
            msg_box.setWindowTitle("Success")
            msg_box.exec_()

        print("Insertion is done !")

# Deletion Function

    def get_course_data2(self):
        course_data2 = self.course_ui.get_course_data2()
        self.course_data2 = course_data2
        print(course_data2)

        conn = sql.connect(host = "localhost" , user = "Vanshpayala" , passwd = "vanshpayala" , database = "real_estate_management")
        if conn.is_connected() == True:
            print("Connection is Established")
        else:
            print("Not Established")
        cursor = conn.cursor()
        if (course_data2 != []):
            a = "delete from course where course_id = "+"'"+course_data2[0]+"'"+";"
            cursor.execute(a)

            conn.commit()
            conn.close

            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setText("You have successfully deleted data from the Database !")
            msg_box.setWindowTitle("Success")
            msg_box.exec_()

        print("Deletion is done !")

# Updation Function

    def update_course_data(self):
        course_id = self.course_ui.b1.text()
        course_name = self.course_ui.b2.text()
        description = self.course_ui.b3.text()
        course_number = self.course_ui.b4.text()
        credits = self.course_ui.b5.text()
        level = self.course_ui.b6.text()
        offering_department = self.course_ui.b7.text()

        conn = sql.connect(host="localhost", user="Vanshpayala", passwd="vanshpayala", database="real_estate_management")
        if conn.is_connected():
            print("Connection is Established")
            cursor = conn.cursor()

            update_query_course = "UPDATE course SET "
            update_values_course = []
            if course_name:
                update_query_course += "course_name = %s, "
                update_values_course.append(course_name)
            if description:
                update_query_course += "description = %s, "
                update_values_course.append(description)
            if course_number:
                update_query_course += "course_number = %s, "
                update_values_course.append(course_number)
            if credits:
                update_query_course += "credits = %s, "
                update_values_course.append(credits)
            if level:
                update_query_course += "level = %s, "
                update_values_course.append(level)
            if offering_department:
                update_query_course += "offering_department = %s, "
                update_values_course.append(offering_department)
            update_query_course = update_query_course.rstrip(", ")
            update_query_course += " WHERE course_id = %s"
            update_values_course.append(course_id)
            cursor.execute(update_query_course, update_values_course)
            print("Course table updated successfully")

            conn.commit()
            cursor.close()
            conn.close()
            print("Update is done !")

            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setText("You have successfully updated data in the Database !")
            msg_box.setWindowTitle("Success")
            msg_box.exec_()

        else:
            print("Not Established")

# Search Function

    def get_course_data4(self):
        course_data4 = self.course_ui.get_course_data4()
        self.agent_data4 = course_data4

        conn = sql.connect(host = "localhost" , user = "Vanshpayala" , passwd = "vanshpayala" , database = "real_estate_management")
        if conn.is_connected() == True:
            print("Connection is Established")
        else:
            print("Not Established")
        cursor = conn.cursor()
        if (course_data4 != []):
            lst1 = ['Course ID','Course Name','Description','Course Number','Credits','Level','Offering Department']
            lst2 = ['Department ID']
            a = "select * from course where course_id = "+"'"+course_data4[0]+"'"+";"
            cursor.execute(a)
            record = cursor.fetchall()

            headers = ["Field", "Value"]
            data = []

            for i in range(6):
                data.append([lst1[i], record[0][i]])

            search_result_dialog = SearchResultDialog(headers, data, self)
            search_result_dialog.exec_()

            conn.commit()
            conn.close

# Customer Table

    def open_customer_ui(self):
        self.customer_window = QtWidgets.QMainWindow()
        self.customer_ui.setupUi(self.customer_window) 
        self.customer_window.show()
        self.customer_ui.submit3.clicked.connect(self.get_customer_data) 
        self.customer_ui.submit33.clicked.connect(self.get_customer_data2)
        self.customer_ui.submit333.clicked.connect(self.update_customer_data)
        self.customer_ui.submit3333.clicked.connect(self.get_customer_data4)

# Insertion Function

    def get_customer_data(self):
        customer_data = self.customer_ui.get_customer_data()
        self.customer_data = customer_data

        conn = sql.connect(host = "localhost" , user = "Vanshpayala" , passwd = "vanshpayala" , database = "real_estate_management")
        if conn.is_connected() == True:
            print("Connection is Established")
        else:
            print("Not Established")
        cursor = conn.cursor()
        if (customer_data != []):
            a = "insert into customer values ("+"'"+customer_data[0]+"'"+","+"'"+customer_data[1]+"'"+","+"'"+customer_data[2]+"'"+","+"'"+customer_data[3]+"'"+");"
            cursor.execute(a)
            c = "insert into customer_property values ("+"'"+customer_data[0]+"'"+","+"'"+customer_data[4]+"'"+");"
            cursor.execute(c)

            conn.commit()
            conn.close

            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setText("You have successfully inserted data in the Database !")
            msg_box.setWindowTitle("Success")
            msg_box.exec_()

        print("Insertion is done !")

# Deletion Function

    def get_customer_data2(self):
        customer_data2 = self.customer_ui.get_customer_data2()
        self.customer_data2 = customer_data2

        conn = sql.connect(host = "localhost" , user = "Vanshpayala" , passwd = "vanshpayala" , database = "real_estate_management")
        if conn.is_connected() == True:
            print("Connection is Established")
        else:
            print("Not Established")
        cursor = conn.cursor()
        if (customer_data2 != []):
            a = "delete from customer where customer_id = "+"'"+customer_data2[0]+"'"+";"
            cursor.execute(a)
            b = "delete from customer_property where customer_id = "+"'"+customer_data2[0]+"'"+";"
            cursor.execute(b)

            conn.commit()
            conn.close

            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setText("You have successfully deleted data from the Database !")
            msg_box.setWindowTitle("Success")
            msg_box.exec_()

        print("Deletion is done !")

# Updation Function

    def update_customer_data(self):
        customer_id = self.customer_ui.lineEdit.text()
        name = self.customer_ui.lineEdit_2.text()
        type = self.customer_ui.lineEdit_4.text()
        preferences = self.customer_ui.lineEdit_3.text()
        property_id = self.customer_ui.lineEdit_5.text()

        conn = sql.connect(host="localhost", user="Vanshpayala", passwd="vanshpayala", database="real_estate_management")
        if conn.is_connected():
            print("Connection is Established")
            cursor = conn.cursor()

            update_query_customer = "UPDATE customer SET "
            update_values_customer = []
            if name:
                update_query_customer += "name = %s, "
                update_values_customer.append(name)
            if type:
                update_query_customer += "type = %s, "
                update_values_customer.append(type)
            if preferences:
                update_query_customer += "preferences = %s, "
                update_values_customer.append(preferences)
            if property_id:
                x = "UPDATE customer_property SET property_id = " + "'"+ property_id +"'"+ " where customer_id = " + "'"+ customer_id +"';"
                cursor.execute(x)

                conn.commit()
                print("Customer_Property table updated successfully")
            update_query_customer = update_query_customer.rstrip(", ")
            update_query_customer += " WHERE customer_id = %s"
            update_values_customer.append(customer_id)
            cursor.execute(update_query_customer, update_values_customer)
            print("Customer table updated successfully")

            conn.commit()
            cursor.close()
            conn.close()

            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setText("You have successfully updated data in the Database !")
            msg_box.setWindowTitle("Success")
            msg_box.exec_()

            print("Update is done !")
        else:
            print("Not Established")

# Search Function

    def get_customer_data4(self):
        customer_data4 = self.customer_ui.get_customer_data4()
        self.customer_data4 = customer_data4

        conn = sql.connect(host = "localhost" , user = "Vanshpayala" , passwd = "vanshpayala" , database = "real_estate_management")
        if conn.is_connected() == True:
            print("Connection is Established")
        else:
            print("Not Established")
        cursor = conn.cursor()
        if (customer_data4 != []):
            lst1 = ['Customer ID','Name','Type','Preferences']
            lst2 = ['Property ID']
            a = "select * from customer where customer_id = "+"'"+customer_data4[0]+"'"+";"
            cursor.execute(a)
            record1 = cursor.fetchall()

            b = "select * from customer_property where customer_id = "+"'"+customer_data4[0]+"'"+";"
            cursor.execute(b)
            record2 = cursor.fetchall()

            headers = ["Field", "Value"]
            data = []

            for i in range(4):
                data.append([lst1[i], record1[0][i]])

            data.append([lst2[0], record2[0][1]])

            search_result_dialog = SearchResultDialog(headers, data, self)
            search_result_dialog.exec_()

            conn.commit()
            conn.close

# Department Table

    def open_department_ui(self):
        self.department_window = QtWidgets.QMainWindow()
        self.department_ui.setupUi(self.department_window) 
        self.department_window.show()
        self.department_ui.submit4.clicked.connect(self.get_department_data)  
        self.department_ui.submit44.clicked.connect(self.get_department_data2)
        self.department_ui.submit444.clicked.connect(self.update_department_data)
        self.department_ui.submit4444.clicked.connect(self.get_department_data4)

# Insertion Function

    def get_department_data(self):
        department_data = self.department_ui.get_department_data()
        self.department_data = department_data

        conn = sql.connect(host = "localhost" , user = "Vanshpayala" , passwd = "vanshpayala" , database = "real_estate_management")
        if conn.is_connected() == True:
            print("Connection is Established")
        else:
            print("Not Established")
        cursor = conn.cursor()
        if (department_data != []):
            a = "insert into department values ("+"'"+department_data[0]+"'"+","+"'"+department_data[1]+"'"+","+"'"+department_data[2]+"'"+","+"'"+department_data[3]+"'"+","+"'"+department_data[4]+"'"+","+"'"+department_data[5]+"'"+","+"'"+department_data[6]+"'"+");"
            cursor.execute(a)

            conn.commit()
            conn.close

            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setText("You have successfully inserted data in the Database !")
            msg_box.setWindowTitle("Success")
            msg_box.exec_()

        print("Insertion is done !")

# Deletion Function

    def get_department_data2(self):
        department_data2 = self.department_ui.get_department_data2()
        self.department_data2 = department_data2

        conn = sql.connect(host = "localhost" , user = "Vanshpayala" , passwd = "vanshpayala" , database = "real_estate_management")
        if conn.is_connected() == True:
            print("Connection is Established")
        else:
            print("Not Established")
        cursor = conn.cursor()
        if (department_data2 != []):
            a = "delete from department where department_id = "+"'"+department_data2[0]+"'"+";"
            cursor.execute(a)

            conn.commit()
            conn.close

            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setText("You have successfully deleted data from the Database !")
            msg_box.setWindowTitle("Success")
            msg_box.exec_()

        print("Deletion is done !")

# Updation Function

    def update_department_data(self):
        department_id = self.department_ui.lineEdit.text()
        name = self.department_ui.lineEdit_2.text()
        department_code = self.department_ui.lineEdit_4.text()
        office_number = self.department_ui.lineEdit_3.text()
        office_phone = self.department_ui.lineEdit_5.text()
        college = self.department_ui.lineEdit_6.text()
        course_id = self.department_ui.lineEdit_7.text()

        conn = sql.connect(host="localhost", user="Vanshpayala", passwd="vanshpayala", database="real_estate_management")
        if conn.is_connected():
            print("Connection is Established")
            cursor = conn.cursor()

            update_query_department = "UPDATE department SET "
            update_values_department = []
            if name:
                update_query_department += "name = %s, "
                update_values_department.append(name)
            if department_code:
                update_query_department += "department_code = %s, "
                update_values_department.append(department_code)
            if office_number:
                update_query_department += "office_number = %s, "
                update_values_department.append(office_number)
            if office_phone:
                update_query_department += "office_phone = %s, "
                update_values_department.append(office_phone)
            if college:
                update_query_department += "college = %s, "
                update_values_department.append(college)
            if course_id:
                update_query_department += "course_id = %s, "
                update_values_department.append(course_id)
            update_query_department = update_query_department.rstrip(", ")
            update_query_department += " WHERE department_id = %s"
            update_values_department.append(department_id)

            cursor.execute(update_query_department, update_values_department)
            print("Department table updated successfully")

            conn.commit()
            cursor.close()
            conn.close()

            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setText("You have successfully updated data in the Database !")
            msg_box.setWindowTitle("Success")
            msg_box.exec_()

            print("Update is done !")
        else:
            print("Not Established")

# Search Function

    def get_department_data4(self):
        department_data4 = self.department_ui.get_department_data4()
        self.department_data4 = department_data4

        conn = sql.connect(host = "localhost" , user = "Vanshpayala" , passwd = "vanshpayala" , database = "real_estate_management")
        if conn.is_connected() == True:
            print("Connection is Established")
        else:
            print("Not Established")
        cursor = conn.cursor()
        if (department_data4 != []):
            lst1 = ['Department ID','Name','Department Code','Office Number','Office Phone','College','Course ID']
            a = "select * from department where department_id = "+"'"+department_data4[0]+"'"+";"
            cursor.execute(a)
            record = cursor.fetchall()

            print("Your Search results are:")
            headers = ["Field", "Value"]
            data = []

            for i in range(7):
                data.append([lst1[i], record[0][i]])

            search_result_dialog = SearchResultDialog(headers, data, self)
            search_result_dialog.exec_()
            conn.commit()
            conn.close

# Property Table

    def open_property_ui(self):
        self.property_window = QtWidgets.QMainWindow()
        self.property_ui.setupUi(self.property_window) 
        self.property_window.show()
        self.property_ui.submit5.clicked.connect(self.get_property_data)  
        self.property_ui.submit55.clicked.connect(self.get_property_data2)
        self.property_ui.submit555.clicked.connect(self.update_property_data)
        self.property_ui.submit5555.clicked.connect(self.get_property_data4)

# Insertion Function

    def get_property_data(self):
        property_data = self.property_ui.get_property_data()
        self.property_data = property_data

        conn = sql.connect(host = "localhost" , user = "Vanshpayala" , passwd = "vanshpayala" , database = "real_estate_management")
        if conn.is_connected() == True:
            print("Connection is Established")
        else:
            print("Not Established")
        cursor = conn.cursor()
        if (property_data != []):
            a = "insert into property values ("+"'"+property_data[0]+"'"+","+"'"+property_data[1]+"'"+","+"'"+property_data[2]+"'"+","+"'"+property_data[3]+"'"+","+"'"+property_data[4]+"'"+","+"'"+property_data[5]+"'"+","+"'"+property_data[6]+"'"+","+"'"+property_data[7]+"'"+","+"'"+property_data[8]+"'"+","+"'"+property_data[9]+"'"+");"
            cursor.execute(a)

            conn.commit()
            conn.close

            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setText("You have successfully inserted data in the Database !")
            msg_box.setWindowTitle("Success")
            msg_box.exec_()

        print("Insertion is done !")

# Deletion Function

    def get_property_data2(self):
        property_data2 = self.property_ui.get_property_data2()
        self.property_data2 = property_data2

        conn = sql.connect(host = "localhost" , user = "Vanshpayala" , passwd = "vanshpayala" , database = "real_estate_management")
        if conn.is_connected() == True:
            print("Connection is Established")
        else:
            print("Not Established")
        cursor = conn.cursor()
        if (property_data2 != []):
            a = "delete from property where property_id = "+"'"+property_data2[0]+"'"+";"
            cursor.execute(a)

            conn.commit()
            conn.close

            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setText("You have successfully deleted data from the Database !")
            msg_box.setWindowTitle("Success")
            msg_box.exec_()

        print("deletion is done !")

# Updation Function

    def update_property_data(self):
        property_id = self.property_ui.lineEdit.text()
        size = self.property_ui.lineEdit_2.text()
        type = self.property_ui.lineEdit_4.text()
        prize = self.property_ui.lineEdit_3.text()
        status = self.property_ui.lineEdit_5.text()
        year_built = self.property_ui.lineEdit_6.text()
        amenities = self.property_ui.lineEdit_7.text()
        address = self.property_ui.lineEdit_8.text()
        bedrooms = self.property_ui.lineEdit_10.text()
        bathrooms = self.property_ui.lineEdit_9.text()

        conn = sql.connect(host = "localhost" , user = "Vanshpayala" , passwd = "vanshpayala" , database = "real_estate_management")
        if conn.is_connected():
            print("Connection is Established")
            cursor = conn.cursor()

            update_query_property = "UPDATE property SET "
            update_values_property = []
            if size:
                update_query_property += "size = %s, "
                update_values_property.append(size)
            if type:
                update_query_property += "type = %s, "
                update_values_property.append(type)
            if prize:
                update_query_property += "prize = %s, "
                update_values_property.append(prize)
            if status:
                update_query_property += "status = %s, "
                update_values_property.append(status)
            if year_built:
                update_query_property += "year_built = %s, "
                update_values_property.append(year_built)
            if amenities:
                update_query_property += "amenities = %s, "
                update_values_property.append(amenities)
            if address:
                update_query_property += "address = %s, "
                update_values_property.append(address)
            if bedrooms:
                update_query_property += "bedrooms = %s, "
                update_values_property.append(bedrooms)
            if bathrooms:
                update_query_property += "bathrooms = %s, "
                update_values_property.append(bathrooms)
            update_query_property = update_query_property.rstrip(", ")
            update_query_property += " WHERE property_id = %s"
            update_values_property.append(property_id)
            cursor.execute(update_query_property, update_values_property)
            print("Property table updated successfully")

            conn.commit()
            cursor.close()
            conn.close()

            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setText("You have successfully updated data in the Database !")
            msg_box.setWindowTitle("Success")
            msg_box.exec_()

            print("Update is done !")
        else:
            print("Not Established")

# Search Function

    def get_property_data4(self):
        property_data4 = self.property_ui.get_property_data4()
        self.property_data4 = property_data4

        conn = sql.connect(host = "localhost" , user = "Vanshpayala" , passwd = "vanshpayala" , database = "real_estate_management")
        if conn.is_connected() == True:
            print("Connection is Established")
        else:
            print("Not Established")
        cursor = conn.cursor()
        if (property_data4 != []):
            lst1 = ['Property ID','Address','Size','Type','Price','Status','Bedrooms','Bathrooms','Amenities','Year Built']
            a = "select * from property where property_id = "+"'"+property_data4[0]+"'"+";"
            cursor.execute(a)
            record = cursor.fetchall()

            print("Your Search results are:")
            headers = ["Field", "Value"]
            data = []

            for i in range(10):
                data.append([lst1[i], record[0][i]])

            search_result_dialog = SearchResultDialog(headers, data, self)
            search_result_dialog.exec_()
            conn.commit()
            conn.close

# Transaction Table

    def open_transaction_ui(self):
        self.transaction_window = QtWidgets.QMainWindow()
        self.transaction_ui.setupUi(self.transaction_window)  
        self.transaction_window.show()
        self.transaction_ui.submit6.clicked.connect(self.get_transaction_data)  
        self.transaction_ui.submit66.clicked.connect(self.get_transaction_data2)
        self.transaction_ui.submit666.clicked.connect(self.update_transaction_data)
        self.transaction_ui.submit6666.clicked.connect(self.get_transaction_data4)

# Insertion Function

    def get_transaction_data(self):
        transaction_data = self.transaction_ui.get_transaction_data()
        self.transaction_data = transaction_data

        conn = sql.connect(host = "localhost" , user = "Vanshpayala" , passwd = "vanshpayala" , database = "real_estate_management")
        if conn.is_connected() == True:
            print("Connection is Established")
        else:
            print("Not Established")
        cursor = conn.cursor()
        if (transaction_data != []):
            a = "insert into transaction values ("+"'"+transaction_data[0]+"'"+","+"'"+transaction_data[1]+"'"+","+"'"+transaction_data[2]+"'"+","+"'"+transaction_data[3]+"'"+","+"'"+transaction_data[4]+"'"+");"
            cursor.execute(a)

            conn.commit()
            conn.close

            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setText("You have successfully inserted data in the Database !")
            msg_box.setWindowTitle("Success")
            msg_box.exec_()

        print("Insertion is done !")

# Deletion Function

    def get_transaction_data2(self):
        transaction_data2 = self.transaction_ui.get_transaction_data2()
        self.transaction_data2 = transaction_data2

        conn = sql.connect(host = "localhost" , user = "Vanshpayala" , passwd = "vanshpayala" , database = "real_estate_management")
        if conn.is_connected() == True:
            print("Connection is Established")
        else:
            print("Not Established")
        cursor = conn.cursor()
        if (transaction_data2 != []):
            a = "delete from transaction where transaction_id = "+"'"+transaction_data2[0]+"'"+";"
            cursor.execute(a)

            conn.commit()
            conn.close

            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setText("You have successfully deleted data from the Database !")
            msg_box.setWindowTitle("Success")
            msg_box.exec_()

        print("Deletion is done !")

# Updation Function

    def update_transaction_data(self):
        transaction_id = self.transaction_ui.lineEdit.text()
        property_id = self.transaction_ui.lineEdit_2.text()
        customer_id = self.transaction_ui.lineEdit_4.text()
        amount = self.transaction_ui.lineEdit_5.text()
        agent_id = self.transaction_ui.lineEdit_3.text()

        conn = sql.connect(host="localhost", user="Vanshpayala", passwd="vanshpayala", database="real_estate_management")
        if conn.is_connected():
            print("Connection is Established")
            cursor = conn.cursor()

            update_query_transaction = "UPDATE transaction SET "
            update_values_transaction = []
            if property_id:
                update_query_transaction += "property_id = %s, "
                update_values_transaction.append(property_id)
            if customer_id:
                update_query_transaction += "customer_id = %s, "
                update_values_transaction.append(customer_id)
            if amount:
                update_query_transaction += "amount = %s, "
                update_values_transaction.append(amount)
            if agent_id:
                update_query_transaction += "agent_id = %s, "
                update_values_transaction.append(agent_id)
            update_query_transaction = update_query_transaction.rstrip(", ")
            update_query_transaction += " WHERE transaction_id = %s"
            update_values_transaction.append(transaction_id)
            cursor.execute(update_query_transaction, update_values_transaction)
            print("Transaction table updated successfully")

            conn.commit()
            cursor.close()
            conn.close()

            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setText("You have successfully updated data in the Database !")
            msg_box.setWindowTitle("Success")
            msg_box.exec_()

            print("Update is done !")
        else:
            print("Not Established")

# Search Function

    def get_transaction_data4(self):
        transaction_data4 = self.transaction_ui.get_transaction_data4()
        self.transaction_data4 = transaction_data4

        conn = sql.connect(host = "localhost" , user = "Vanshpayala" , passwd = "vanshpayala" , database = "real_estate_management")
        if conn.is_connected() == True:
            print("Connection is Established")
        else:
            print("Not Established")
        cursor = conn.cursor()
        if (transaction_data4 != []):
            lst1 = ['Transaction ID','Property ID','Customer ID','Agent ID','Amount']
            a = "select * from transaction where transaction_id = "+"'"+transaction_data4[0]+"'"+";"
            cursor.execute(a)
            record = cursor.fetchall()

            print("Your Search results are:")
            headers = ["Field", "Value"]
            data = []

            for i in range(5):
                data.append([lst1[i], record[0][i]])

            search_result_dialog = SearchResultDialog(headers, data, self)
            search_result_dialog.exec_()
            
            conn.commit()
            conn.close

# Main Function

def main():
    app = QApplication([])
    window = MyGUI()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()