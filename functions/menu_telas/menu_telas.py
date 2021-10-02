from datetime import datetime
from PyQt5.QtWidgets import QTableWidgetItem


class MenuTelas:
    #  Função para mostrar o segundo menu de botões - argumentos: página do meio a ser mostrada
    #  e botão que ficará pressionado
    def middle_menu(self, pagina, botao):
        self.more_menu.setVisible(True)  # Deixando o menu visível
        self.stackedWidget.setCurrentWidget(self.pageFirst)  # Colocando a página inicial menu principal
        self.main_page_functions()
        self.disable_all_buttons()
        self.activate_button(botao)
        self.stackedWidget_2.setCurrentWidget(pagina)
        self.stackedWidget_2.setMinimumWidth(68)

    # Função para mostrar a página principal - argumentos: página principal a ser mostrada, botão para ficar pressionado
    # e botão a ser desativado (se necessário)
    def main_page(self, pagina, botao, botao_desativar=None):
        self.more_menu.setVisible(False)
        self.stackedWidget.setCurrentWidget(pagina)
        botoes_meio = [self.pushButton_InsUser, self.pushButton_InsConsPsiq, self.pushButtonInsAtendRef,
                       self.pushButtonInsHalDec, self.pushButton_COVID_2, self.pushButton_COVID_3,
                       self.pushButton_COVID_4]
        for botao_des in botoes_meio:
            self.disable_button(botao_des)
        self.activate_button(botao)
        if botao_desativar is not None:
            self.disable_button(botao_desativar)
        self.erase_line_edit()
        self.lineEditPront_2.setPlaceholderText('Digite o prontuário e clique em GO')
        self.lineEditPront_2.setStyleSheet("QLineEdit {background-color: rgb(63, 63, 63); border-width: 2px; "
                                           "border-radius: 10px; border-color: rgb(0, 170, 255); font: bold 10px; "
                                           "padding-left: 20px; padding-right: 20px; color: rgb(255, 255, 255)}")
        self.lineEditPront_3.setPlaceholderText('Digite o prontuário e clique em GO')
        self.lineEditPront_3.setStyleSheet("QLineEdit {background-color: rgb(63, 63, 63); border-width: 2px; "
                                           "border-radius: 10px; border-color: rgb(0, 170, 255); font: bold 10px; "
                                           "padding-left: 20px; padding-right: 20px; color: rgb(255, 255, 255)}")
        self.lineEditPront_4.setPlaceholderText('Digite o prontuário e clique em GO')
        self.lineEditPront_4.setStyleSheet("QLineEdit {background-color: rgb(63, 63, 63); border-width: 2px; "
                                           "border-radius: 10px; border-color: rgb(0, 170, 255); font: bold 10px; "
                                           "padding-left: 20px; padding-right: 20px; color: rgb(255, 255, 255)}")

    def main_page_functions(self):
        hj = datetime.now()
        data = hj.strftime('%m/%Y')
        self.label_19.setText(f'Próximas aplicações - Decanoato - mês: {data}')
        for a in self.cursor.execute('SELECT COUNT(*) FROM haldol_decanoato WHERE mes_next '
                                     '=(SELECT strftime("%m", "now")) AND dia_next >= (SELECT strftime("%d", "now"))'):
            self.tamanho = a[0]
        self.tableWidget_5.setRowCount(self.tamanho)

        sqlite = self.cursor.execute('SELECT (SELECT nome FROM dados WHERE prontuario = usuarios_prontuario), '
                                     '(SELECT referencia FROM dados WHERE prontuario = usuarios_prontuario), '
                                     'usuarios_prontuario, dia_next FROM haldol_decanoato WHERE mes_next '
                                     '=(SELECT strftime("%m", "now")) AND dia_next >= (SELECT strftime("%d", "now")) '
                                     'ORDER BY dia_next')

        self.insert_rows_haldol_decanoato(sqlite)

    def insert_rows_haldol_decanoato(self, sqlite):
        tablerow = 0
        for row in sqlite:
            coluna = 0
            for item in row:
                self.tableWidget_5.setItem(tablerow, coluna, QTableWidgetItem(str(row[coluna])))
                coluna += 1
            tablerow += 1
