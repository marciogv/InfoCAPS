from PyQt5.QtWidgets import QTableWidgetItem


class DadosCovid:
    # Inserir dados line edit ao add usuário
    def fill_covid(self):
        pront = self.lineEditPront_3.text()
        if pront == '':
            return
        results = self.cursor.execute(f'SELECT nome, cadastro, prontuario, situacao, referencia, medico, '
                                      f'pri_dose_covid, seg_dose_covid_pre, seg_dose_covid_efe FROM dados '
                                      f'WHERE prontuario = {pront}')
        for encontrado in results:
            nome, registro, prontuario, situacao, referencia, medico, pri_dose, seg_dose_pre, seg_dose_efe = encontrado
            self.lineEditName_3.setPlaceholderText(nome)
            self.lineEditCad_3.setPlaceholderText(str(registro))
            self.lineEditPront_3.setPlaceholderText(str(prontuario))
            self.lineEditUBS_3.setPlaceholderText(situacao)
            self.lineEditRef_3.setPlaceholderText(referencia)
            self.lineEditMed_3.setPlaceholderText(medico)
            if pri_dose is not None:
                if pri_dose == 'Não tomou' or pri_dose =='Recusou':
                    pass
                else:
                    pri_dose = f'{pri_dose[8:]}/{pri_dose[5:7]}/{pri_dose[:4]}'
            if seg_dose_pre is not None:
                if seg_dose_pre == 'Não tomou' or seg_dose_pre == 'Recusou':
                    pass
                else:
                    seg_dose_pre = f'Prevista: {seg_dose_pre[8:]}/{seg_dose_pre[5:7]}/{seg_dose_pre[:4]}'
                self.lineEditSegDose.setPlaceholderText(seg_dose_pre)
            if seg_dose_efe is not None:
                if seg_dose_efe == 'Não tomou' or seg_dose_efe == 'Recusou':
                    pass
                else:
                    seg_dose_efe = f'Realizada: {seg_dose_efe[8:]}/{seg_dose_efe[5:7]}/{seg_dose_efe[:4]}'
                self.lineEditSegDose.setPlaceholderText(seg_dose_efe)
            self.lineEditPriDose.setPlaceholderText(pri_dose)

    def erase_vaccine_data(self):
        dados = [self.lineEditCad_3, self.lineEditPront_3, self.lineEditUBS_3, self.lineEditRef_3,
                 self.lineEditMed_3, self.lineEditPriDose, self.lineEditSegDose, self.lineEditName_3]
        for dado in dados:
            dado.setPlaceholderText('')
            dado.clear()
        grupos = [self.buttonGroup_7, self.buttonGroup_10, self.buttonGroup_11, self.buttonGroup_6]
        for grupo in grupos:
            grupo.setExclusive(False)
        botoes = [self.checkBox, self.checkBox_2, self.checkBox_3, self.checkBox_4, self.checkBox_5,
                  self.radioButton_15, self.radioButton_48, self.radioButton_18, self.radioButton_21,
                  self.radioButton_28]
        for botao in botoes:
            botao.setChecked(False)
        for grupo in grupos:
            grupo.setExclusive(True)
        self.lineEditPront_3.setPlaceholderText('Digite o prontuário e clique em GO')

    # Adicionar dados vacina nas colunas do SQL
    def insert_vaccine_data(self):
        try:
            botao_vacina = [self.radioButton_15, self.radioButton_48, self.radioButton_18]
            for botao in botao_vacina:
                if botao.isChecked():
                    marca = botao.text()
            seg_dose_option = [self.radioButton_21, self.radioButton_28]
            pront = int(self.lineEditPront_3.text())
            opcoes_segdose = [self.checkBox_3, self.checkBox_4]
            for opcao in opcoes_segdose:
                if opcao.isChecked():
                    seg_dose = opcao.text()
                    break
                else:
                    seg_dose = f'{self.dateEdit_3.text()[6:]}-{self.dateEdit_3.text()[3:5]}-{self.dateEdit_3.text()[:2]}'
            for bota_seg in seg_dose_option:
                if bota_seg.text() == 'Prevista' and bota_seg.isChecked():
                    add = 'UPDATE dados SET seg_dose_covid_pre = ? WHERE prontuario = ?'
                    colocar = self.cursor.execute(add, (seg_dose, pront))
                    self.conn.commit()
                if bota_seg.text() == 'Realizada' and bota_seg.isChecked():
                    add = 'UPDATE dados SET seg_dose_covid_efe = ? WHERE prontuario = ?'
                    colocar = self.cursor.execute(add, (seg_dose, pront))
                    self.conn.commit()
            pri_dose = f'{self.dateEdit_2.text()[6:]}-{self.dateEdit_2.text()[3:5]}-{self.dateEdit_2.text()[:2]}'
            opcoes_pridose = [self.checkBox, self.checkBox_2]
            for opcao in opcoes_pridose:
                if opcao.isChecked():
                    pri_dose = opcao.text()
                    marca = ''
            if not self.checkBox_5.isChecked():
                execucao = 'UPDATE dados SET pri_dose_covid = ?, id_vacina = ? WHERE prontuario = ?'
                results = self.cursor.execute(execucao, (pri_dose, marca, pront))
            self.conn.commit()
            # Após adicionar os dados da vacina tirar o texto dos Line Edit
            self.apagar_dados_vacina()
            self.lineEditName_3.setPlaceholderText('Dados inseridos com sucesso')
        except Exception as erro:
            self.apagar_dados_vacina()
            self.lineEditName_3.setPlaceholderText('Dados Incorretos')

    # Pesquisar dados covid de usuários por idade
    def search_data_covid(self):
        self.disable_all_buttons()
        for a in self.cursor.execute('SELECT COUNT(*) FROM dados WHERE (SELECT (julianday("now") - '
                                     'julianday(data_nascimento)) / 365) >=?',
                                     (int(self.lineEditFaixaVacina.text()),)):
            self.tamanho = a[0]
        self.tableWidget.setRowCount(self.tamanho)
        self.more_menu.setVisible(False)
        self.stackedWidget.setCurrentWidget(self.pageTableCOVID)
        sqlstr = 'SELECT nome, cadastro, prontuario, ubs, regional, referencia, data_nascimento, ' \
                 'CAST((julianday("now") - julianday(data_nascimento)) / 365 AS INTEGER) as idade, pri_dose_covid, ' \
                 'seg_dose_covid_pre, seg_dose_covid_efe, id_vacina FROM dados WHERE idade >= ?'
        results = self.cursor.execute(sqlstr, (int(self.lineEditFaixaVacina.text()),))
        self.insert_row_vacina(results)
        self.tableWidget.setSortingEnabled(True)

    # Adicionar dados de COVID à tabela do QTDesigner
    def insert_row_vacina(self, comando):
        tablerow = 0
        for row in comando:
            coluna = 0
            for item in row:
                self.tableWidget.setItem(tablerow, coluna, QTableWidgetItem(str(row[coluna])))
                coluna += 1
            tablerow += 1
