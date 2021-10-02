from PyQt5.QtWidgets import QTableWidgetItem


class BuscaUsuario:

    # Função para buscar usuários, principal menu superior - argumentos: coluna que será buscada, se busca entre
    # ativados ou desativados e se a busca é pelo número(cadastro) pois caso não a busca será especial com a
    # possibilidade de somente primeiro nome ou referência '%'
    def buscar_usuario(self, sql, ativado='(situacao = "ativo")', numero=False):
        self.tableWidget_2.setSortingEnabled(False)
        self.tableWidget_2.clearContents()

        # Verificar se CheckBox está ativo ou inativa para especificar busca no banco de dados
        if (self.checkBoxAtivos.isChecked() and self.checkBoxInvativos.isChecked()) or \
                (not self.checkBoxAtivos.isChecked() and not self.checkBoxInvativos.isChecked()):
            ativado = '(situacao = "ativo" OR situacao = "inativo")'
        elif not self.checkBoxAtivos.isChecked() and self.checkBoxInvativos.isChecked():
            ativado = '(situacao = "inativo")'
        else:
            pass

        self.disable_all_buttons()

        if numero is False:  # Busca especial caso a busca não seja pelo número
            self.lineEditBusca.setText(f'{self.lineEditBusca.text()}%')

        # Realizando a contagem das linhas do elemento que vai ser buscado para definir o número de linhas da tabela
        for a in self.cursor.execute(f'SELECT COUNT(*) FROM dados WHERE {sql} LIKE ? AND {ativado}',
                                     (str(self.lineEditBusca.text()),)):
            self.tamanho = a[0]
        self.tableWidget_2.setRowCount(self.tamanho)
        if self.tamanho == 0:  # Caso não seja encontrado nenhum resultado feedback para usuário programa
            self.lineEditBusca.clear()
            self.lineEditBusca.insert('Usuário não encontrado')

        else:  # Caso encontrado seguir para o código SQL
            self.more_menu.setVisible(False)  # Sumir com menu intermediário para mostrar tabela em tela inteira
            self.stackedWidget.setCurrentWidget(self.pageTable)  # Ativar página principal
            sqlstr = f'SELECT nome, cadastro, prontuario, ubs, regional, referencia, medico, ano_inicio, situacao, ' \
                     f'sexo, raca, telefone, data_nascimento, CAST((julianday("now") - julianday(data_nascimento))' \
                     f' / 365 AS INTEGER) as idade, cpf, pri_dose_covid, seg_dose_covid_pre, seg_dose_covid_efe, ' \
                     f'id_vacina FROM dados WHERE {sql} LIKE ? AND {ativado}'
            results = self.cursor.execute(sqlstr, (str(self.lineEditBusca.text()),))  # Executar o que foi escrito
            self.lineEditBusca.clear()
            self.insert_rows(results)
            self.tableWidget_2.setSortingEnabled(True)  # Ativar sorting das colunas da tabela

    def insert_rows(self, comando):  # Inserir na tabela do QTDesigner o que tivemos de resultado do SQL
        tablerow = 0
        for row in comando:
            coluna = 0
            for item in row:
                self.tableWidget_2.setItem(tablerow, coluna, QTableWidgetItem(str(row[coluna])))
                coluna += 1
            tablerow += 1