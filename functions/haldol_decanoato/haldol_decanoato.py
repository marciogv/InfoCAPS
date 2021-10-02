from datetime import datetime


class HaldolDecanoato:
    # Preencher Line Edit página para inserir dados Haldol Decanoato
    def fill_haldol_decanoato(self):
        prontuario = self.lineEditPront_4.text()
        if prontuario == '':
            return
        results = self.cursor.execute(f'SELECT nome, cadastro, prontuario, situacao, referencia, medico FROM '
                                      f'dados WHERE prontuario = {prontuario}')  # Buscar inf SQL a partir cadastro
        for encontrado in results:  # Desempacotando tupla SQL e add nos Line Edit
            nome, registro, prontuario, situacao, referencia, medico = encontrado
            self.lineEditName_4.setPlaceholderText(nome)
            self.lineEditCad_4.setPlaceholderText(str(registro))
            self.lineEditPront_4.setPlaceholderText(str(prontuario))
            self.lineEditUBS_4.setPlaceholderText(situacao)
            self.lineEditRef_4.setPlaceholderText(referencia)
            self.lineEditMed_4.setPlaceholderText(medico)

        busca_atual = self.cursor.execute(f'SELECT dia_next, mes_next, ano_next FROM haldol_decanoato WHERE '
                                          f'usuarios_prontuario = {prontuario}')
        for dado in busca_atual:
            dia_atual, mes_atual, ano_atual = dado
            self.lineEditAplicacaoAtual.setPlaceholderText(f'{dia_atual}/{mes_atual}/{ano_atual}')
        hj = datetime.now()
        data = hj.strftime('%d/%m/%Y')
        self.lineEditDataHoje.setPlaceholderText(data)

    def insert_haldol_decanoato(self):
        try:
            proxima_aplicacao = self.dateEdit_5.text()
            # Dividindo data proxima aplicação em dia, mês, ano para add em colunas diferentes
            dia_proxima = int(proxima_aplicacao[:2])
            mes_proxima = int(proxima_aplicacao[3:5])
            ano_proxima = int(proxima_aplicacao[6:])
            hj = datetime.now()
            dia_atual = int(hj.strftime('%d'))  # Dividindo data atual em dia, mês, ano para add em colunas diferentes
            mes_atual = int(hj.strftime('%m'))
            ano_atual = int(hj.strftime('%Y'))
            ampolas = int(self.lineEditAmpolas.text())
            responsavel = self.lineEditHalResp.text()
            usuarios_prontuario = int(self.lineEditPront_4.text())
            sqlite = 'INSERT INTO haldol_decanoato (usuarios_prontuario, dia_atual, mes_atual, ano_atual, dia_next, ' \
                     'mes_next, ano_next, ampolas, responsavel) VALUES (?,?,?,?,?,?,?,?,?)'
            executando = self.cursor.execute(sqlite, (usuarios_prontuario, dia_atual, mes_atual, ano_atual, dia_proxima,
                                                      mes_proxima, ano_proxima, ampolas, responsavel))
            self.conn.commit()
            lines_edits = [self.lineEditCad_4, self.lineEditPront_4, self.lineEditUBS_4, self.lineEditRef_4,
                           self.lineEditMed_4, self.lineEditAmpolas, self.lineEditHalResp]
            for line in lines_edits:
                line.setPlaceholderText('')
                line.clear()
            self.lineEditName_4.setText('Dados inseridos com sucesso')
        except Exception as erro:  # Tratando exceções de erros referentes a dados em branco
            self.lineEditName_4.setText('Dados Incorretos')
            print(erro)
