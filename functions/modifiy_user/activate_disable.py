class AtivaDesativa:
    def activate_disable(self):
        results = self.cursor.execute(f'UPDATE dados SET situacao = "{self.situacao_modificacao}" WHERE '
                                      f'prontuario = {self.lineEditPront_2.text()}')
        self.conn.commit()
        self.pushButtonADDUser_2.setText('SUCESSO!')
        self.lineEditName_2.setPlaceholderText('')
        self.lineEditCad_2.setPlaceholderText('')
        self.lineEditPront_2.setPlaceholderText('')
        self.lineEditUBS_2.setPlaceholderText('')
        self.lineEditReg_2.setPlaceholderText('')
        self.lineEditRef_2.setPlaceholderText('')
        self.lineEditMed_2.setPlaceholderText('')