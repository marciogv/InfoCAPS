class ModificaBotao:
    # Função para ativar algum botão específico - argumento: botão
    def activate_button(self, botao):
        if botao == self.pushButtonInsert:
            botao.setStyleSheet("QPushButton {\n"
                                "    color: rgb(255, 255, 255);\n"
                                "    background-color: rgb(80,80,80);\n"
                                "    border: 0px solid; border-top-right-radius: 15px\n"
                                "}\n"
                                "QPushButton:hover {\n"
                                "    background-color: rgb(80,80,80); \n"
                                "}")
        else:
            botao.setStyleSheet("QPushButton {\n"
                                            "    color: rgb(255, 255, 255);\n"
                                            "    background-color: rgb(80,80,80);\n"
                                            "    border: 0px solid;\n"
                                            "}\n"
                                            "QPushButton:hover {\n"
                                            "    background-color: rgb(80,80,80);\n"
                                            "}")

    # Função para desativar algum botão específico - argumento: botão
    def disable_button(self, botao, tipo=0):
        if tipo == 1:
            botao.setStyleSheet("QPushButton {color: rgb(255, 255, 255);"
                                            "    background-color: rgb(94,94,94);\n"
                                            "    border: 0px solid;\n"
                                            "}\n"
                                            "QPushButton:hover {\n"
                                            "    background-color: rgb(80,80,80);\n"
                                            "}")
        elif tipo == 2:
            botao.setStyleSheet("QPushButton {\n"
                                "    color: rgb(255, 255, 255);\n"
                                "    background-color: rgb(94,94,94);\n"
                                "    border: 0px solid;\n"
                                "}\n"
                                "QPushButton:hover {\n"
                                "    background-color: rgb(80,80,80); border-top-right-radius: 15px; "
                                "border-top-left-radius: 15px}")
        else:
            botao.setStyleSheet("QPushButton {\n"
                                "    color: rgb(255, 255, 255);\n"
                                "    background-color: rgb(94,94,94);\n"
                                "    border: 0px solid;\n"
                                "}\n"
                                "QPushButton:hover {\n"
                                "    background-color: rgb(80,80,80); border-top-right-radius: 15px;\n"
                                "}")

    # Função para desativar todos os botões
    def disable_all_buttons(self):
        botoes_padrao = [self.pushButton_Search, self.pushButton_InsConsPsiq,
                         self.pushButtonInsAtendRef, self.pushButtonInsHalDec, self.pushButton_Search,
                         self.pushButton_COVID, self.pushButton_Inf, self.pushButton_COVID_3]
        botoes_bordas_superior = [self.pushButton_AtivarPront, self.pushButton_InsUser, self.pushButtonGrafico,
                                  self.pushButton_COVID_2]
        self.disable_button(self.pushButtonInsert)
        for botao in botoes_padrao:
            tipo = 1
            self.disable_button(botao, tipo)
        for botao in botoes_bordas_superior:
            tipo = 2
            self.disable_button(botao, tipo)
        self.pushButtonInsAtendRef.setCheckable(False)
