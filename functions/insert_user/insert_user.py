from datetime import datetime


class InsereUsuario:
    def inserir_usuario(self):  # Inserir novo usuário ao banco de dados
        try:
            nome = self.lineEditName.text()
            cadastro = self.lineEditCad.text()
            prontuario = self.lineEditPront.text()
            ubs = self.lineEditUBS.text()
            regional = self.lineEditRegional.text()
            referencia = self.lineEditRef.text()
            origem = self.lineEditOrigem.text()
            cid_inicial = self.lineEditCID.text()
            naturalidade_estado = self.lineEditNaturalidadeEst.text()
            naturalidade_cidade = self.lineEditNaturalidadeCid.text()
            escolaridade = self.lineEditescolaridade.text()
            religiao = self.lineEditReligiao.text()
            profissao = self.lineEditProfissao.text()
            interditado = self.lineEditInterditado.text()
            cuidador = self.lineEditCuidador.text()
            origem = self.lineEditOrigem.text()

            # Exceção para o caso de não ser colocado nenhum none - tratada ai final da função
            if nome == '' or prontuario == '' or ubs == '' or regional == '' or referencia == '':
                raise Exception

            #  Listas RadioButton Raça, laços 'for' para preencher definir a variável sexo
            botao_raca = [self.radioButton_43, self.radioButton_44, self.radioButton_45, self.radioButton_46,
                          self.radioButton_47]
            for botao in botao_raca:
                if botao.isChecked():
                    raca = botao.text().lower()
                    break

            #  Listas RadioButton Sexo, laços 'for' para preencher definir a variável sexo
            botao_sexo = [self.radioButton_41, self.radioButton_42]
            for botao in botao_sexo:
                if botao.isChecked():
                    sexo = botao.text()
                    sexo = sexo[0]
                    break

            #  Listas RadioButton Estado Civil, laços 'for' para preencher definir a variável sexo
            botao_ec = [self.radioButton_50, self.radioButton_51, self.radioButton_52, self.radioButton_53]
            for botao in botao_ec:
                if botao.isChecked():
                    estado_civil = botao.text()
                    break

            #  Listas RadioButton Situação Ocupacional, laços 'for' para preencher definir a variável sexo
            botao_so = [self.radioButton_54, self.radioButton_55, self.radioButton_56, self.radioButton_57,
                        self.radioButton_58, self.radioButton_59]
            for botao in botao_so:
                if botao.isChecked():
                    situacao_ocupacional = botao.text()
                    break

            data_nascimento = self.dateEdit.text()
            data = f'{data_nascimento[6:]}-{data_nascimento[3:5]}-{data_nascimento[:2]}'  # Alterando DN - formato EUA
            hj = datetime.now()
            dia_inicio = int(hj.strftime('%d'))  # Dividindo data atual em dia, mês, ano para add em colunas diferentes
            mes_inicio = int(hj.strftime('%m'))
            ano_inicio = int(hj.strftime('%Y'))
            consulta = 'INSERT INTO dados (nome, cadastro, prontuario, ubs, regional, referencia, dia_inicio, ' \
                       'mes_inicio, ano_inicio, sexo, cid_inicial, data_nascimento, raca, estado_civil, ' \
                       'naturalidade_cidade, naturalidade_estado, escolaridade, religiao, profissao, ' \
                       'situacao_ocupacional, curador, cuidador, origem) VALUES ' \
                       '(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'  # Código SQL para add todos dados
            self.cursor.execute(consulta, (nome, cadastro, prontuario, ubs, regional, referencia, dia_inicio,
                                           mes_inicio, ano_inicio, sexo, cid_inicial, data, raca, estado_civil,
                                           naturalidade_cidade, naturalidade_estado, escolaridade, religiao, profissao,
                                           situacao_ocupacional, interditado, cuidador, origem))  # Execução SQL
            self.conn.commit()
            self.lineEditName.setText('Usuário inserido com sucesso')  # Feedback para usuário de sucesso
            linhas = [self.lineEditCad, self.lineEditPront, self.lineEditCID, self.lineEditName, self.lineEditUBS,
                      self.lineEditRegional, self.lineEditReligiao, self.lineEditOrigem, self.lineEditNaturalidadeCid,
                      self.lineEditNaturalidadeEst, self.lineEditescolaridade, self.lineEditReligiao,
                      self.lineEditProfissao, self.lineEditInterditado, self.lineEditCuidador, self.lineEditRef]
            for line in linhas:  # Laço para retirar o que foi escrito nas linhas editáveis
                line.clear()

        except Exception as erro:  # Tratando exceções de erros referentes a dados em branco
            self.lineEditName.setText('Dados Incorretos')
            print(erro)
