class ApagarPreencherLineEdit:


    # Função apagar todas as Line Edit do código
    def erase_line_edit(self):
        line_edits = [self.lineEditCad, self.lineEditName, self.lineEditPront, self.lineEditName_2,
                      self.lineEditCad_2, self.lineEditPront_2, self.lineEditUBS_2, self.lineEditReg_2,
                      self.lineEditRef_2, self.lineEditMed_2, self.lineEditName_3, self.lineEditCad_3,
                      self.lineEditPront_3, self.lineEditUBS_3, self.lineEditRef_3, self.lineEditMed_3,
                      self.lineEditPriDose, self.lineEditSegDose, self.lineEditCad_4, self.lineEditPront_4,
                      self.lineEditUBS_4, self.lineEditRef_4, self.lineEditMed_4, self.lineEditAmpolas,
                      self.lineEditHalResp, self.lineEditName_4, self.lineEditAplicacaoAtual, self.lineEditDataHoje]
        for line in line_edits:
            line.setPlaceholderText('')
            line.clear()

    # Inserir dados line edit - atendimentos CAPS, ativar/desativar prontuário
    def search_and_fill(self):
        pront = self.lineEditPront_2.text()
        if pront == '':
            return
        results = self.cursor.execute(f'SELECT nome, cadastro, prontuario, situacao, regional, referencia, medico FROM '
                                      f'dados WHERE prontuario = {pront}')  # Buscar inf SQL a partir cadastro
        for encontrado in results:  # Desempacotando tupla SQL e add nos Line Edit
            nome, registro, prontuario, situacao, regional, referencia, medico = encontrado
            self.lineEditName_2.setPlaceholderText(nome)
            self.lineEditCad_2.setPlaceholderText(str(registro))
            self.lineEditPront_2.setPlaceholderText(str(prontuario))
            self.lineEditUBS_2.setPlaceholderText(situacao)
            self.lineEditReg_2.setPlaceholderText(regional)
            self.lineEditRef_2.setPlaceholderText(referencia)
            self.lineEditMed_2.setPlaceholderText(medico)
            self.pushButtonADDUser_2.setEnabled(True)
            self.pushButtonADDUser_6.setText('')
            if situacao == 'ativo':
                self.situacao_modificacao = 'inativo'
                self.pushButtonADDUser_2.setText('DESATIVAR')
            elif situacao == 'inativo':
                self.situacao_modificacao = 'ativo'
                self.pushButtonADDUser_2.setText('ATIVAR')
            else:
                self.lineEditName_2.setPlaceholderText('Não encontrado')
        if self.pushButtonInsAtendRef.isCheckable():
            self.pushButtonADDUser_6.setText('INSERIR \nATENDIMENTO')
            self.pushButtonADDUser_6.setEnabled(True)
            self.pushButtonADDUser_2.setEnabled(False)
            self.pushButtonADDUser_2.setText('')
        else:
            self.pushButtonADDUser_6.setEnabled(False)
