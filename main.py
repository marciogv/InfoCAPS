import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QAbstractItemView, QDialog
from PyQt5.QtGui import QIntValidator
from designer.menu_ui import *
from designer.login_ui import *
import sqlite3
from functions.search_users.search_users import BuscaUsuario
from functions.insert_user.insert_user import InsereUsuario
from functions.modifiy_user.activate_disable import AtivaDesativa
from functions.modify_button.modify_button import ModificaBotao
from functions.covid_data.covid_data import DadosCovid
from functions.haldol_decanoato.haldol_decanoato import HaldolDecanoato
from functions.menu_telas.menu_telas import MenuTelas
from functions.apagar_preencher_line_edit.apagar_preencher_line_edit \
    import ApagarPreencherLineEdit
from functions.graphics.graphics import Graficos

"""
Arquivo principal do programa que possui duas classes: a primeira cria a janela principal e herda as classes auxiliares 
que contém as funções do programa que buscam, inserem e atualizam os diversos dados do banco de dados; 
a segunda cria uma caixa de diálogo onde está a tela de login para a realização de funções específicas de certos 
trabalhadores do serviço
"""

class Menu(QMainWindow, Ui_MainWindow, BuscaUsuario, InsereUsuario, AtivaDesativa, ModificaBotao, DadosCovid,
           HaldolDecanoato, MenuTelas, ApagarPreencherLineEdit, Graficos):
    def __init__(self, arquivo, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.conn = sqlite3.connect(arquivo)
        self.cursor = self.conn.cursor()
        self.tableWidget_2.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.stackedWidget.setCurrentWidget(self.pageFirst)
        self.pushButton_InsUser.clicked.connect(lambda: self.tela_login('inserir_usuario', 'recepção'))
        self.pushButtonSearchReg.clicked.connect(lambda: self.buscar_usuario('prontuario', numero=True))
        self.pushButtonSearchName.clicked.connect(lambda: self.buscar_usuario('nome'))
        self.pushButtonSearchRef.clicked.connect(lambda: self.buscar_usuario('referencia'))
        self.pushButtonInsert.clicked.connect(lambda: self.middle_menu(self.page_Insert, self.pushButtonInsert))
        self.pushButton_Search.clicked.connect(lambda: self.middle_menu(self.page_Pesq, self.pushButton_Search))
        self.pushButton_COVID.clicked.connect(lambda: self.middle_menu(self.page_COVID, self.pushButton_COVID))
        self.pushButton_Inf.clicked.connect(lambda: self.middle_menu(self.pageInf, self.pushButton_Inf))
        self.pushButton_COVID_2.clicked.connect(lambda: self.main_page(self.pageFaixaCovid,
                                                                              self.pushButton_COVID_2))
        self.pushButton_AtivarPront.clicked.connect(lambda: self.main_page(self.pageModificar,
                                                                                  self.pushButton_AtivarPront))
        self.pushButtonSearchVacina.clicked.connect(self.search_data_covid)
        self.pushButtonADDUser_3.clicked.connect(self.search_and_fill)
        self.pushButtonADDUser_2.clicked.connect(self.activate_disable)
        self.more_menu.setVisible(False)
        self.pushButtonADDUser.clicked.connect(self.inserir_usuario)
        self.pushButtonInsAtendRef.clicked.connect(lambda: self.main_page(self.pageModificar,
                                                                                 self.pushButtonInsAtendRef))
        self.pushButtonInsAtendRef.clicked.connect(lambda: self.pushButtonInsAtendRef.setCheckable(True))
        self.pushButtonGrafico.clicked.connect(lambda: self.main_page(self.pageGrafico,
                                                                             self.pushButtonGrafico))
        self.pushButtonShowInf.clicked.connect(self.mostrar_grafico)
        self.pushButton_COVID_3.clicked.connect(lambda: self.main_page(self.pageInsertCOVID,
                                                                              self.pushButton_COVID_3))
        self.pushButtonADDUser_5.clicked.connect(self.fill_covid)
        self.pushButtonADDUser_7.clicked.connect(self.insert_vaccine_data)
        self.pushButtonInsHalDec.clicked.connect(lambda: self.tela_login('inserir_decanoato', 'enfermagem'))
        self.pushButtonADDUser_8.clicked.connect(self.fill_haldol_decanoato)
        self.lineEditAmpolas.setValidator(QIntValidator(1, 10, self))
        self.pushButtonADDUser_9.clicked.connect(self.insert_haldol_decanoato)
        self.main_page_functions()
        self.pushButtonADDUser_10.clicked.connect(self.erase_vaccine_data)

    # Abrindo tela para fazer login e fechando a tela inicial
    def tela_login(self, pagina, categoria):
        self.hide()
        tela = Login('usuarios_caps.db', pagina, categoria)
        tela.exec()


# Classe para abrir tela de diálogo de login
class Login(QDialog, Ui_Dialog):
    def __init__(self, arquivo, pagina, categoria, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.conn = sqlite3.connect(arquivo)
        self.cursor = self.conn.cursor()
        self.pushButton_2.clicked.connect(self.sair)
        self.pushButton.clicked.connect(self.login)
        self.categoria = categoria
        self.pagina = pagina

    def login(self):
        busca_atual = f'SELECT categoria, nome FROM funcionarios WHERE login = ? and senha = ?'
        busca = self.cursor.execute(busca_atual, (self.lineEditName.text(), self.lineEditName_2.text()))
        for dado in busca:
            categoria, nome = dado
            if categoria == self.categoria and self.pagina == 'inserir_usuario':
                rolou = Menu('usuarios_caps.db')
                rolou.main_page(rolou.pageSearch, rolou.pushButton_InsUser)
                rolou.show()
                self.hide()
            if categoria == self.categoria and self.pagina == 'inserir_decanoato':
                rolou = Menu('usuarios_caps.db')
                rolou.main_page(rolou.pageInsertDec, rolou.pushButtonInsHalDec)
                rolou.show()
                self.hide()

    def sair(self):
        rolou = Menu('usuarios_caps.db')
        rolou.show()
        self.hide()


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    menu = Menu('usuarios_caps.db')
    menu.show()
    qt.exec_()
