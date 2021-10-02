from PyQt5.QtChart import QChart, QChartView, QBarSet, QBarCategoryAxis, QBarSeries
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QGridLayout


class Graficos:

    # Função para mostrar no gráfico os atendimentos realizados no CAPS
    def mostrar_grafico(self):
        try:
            set0 = QBarSet("Atendimento de referência")  # Adicionando as colunas
            set1 = QBarSet("Consulta Psiquiátrica")

            for tipo_atendimento in range(2):  # Indo ao SQL para puxar os atendimentos (por tipo) para adicionar no gráfico
                if tipo_atendimento == 0:  # Pegando cada tipo de atendimento
                    atendimento = 'atendimento_referencia'
                else:
                    atendimento = 'consulta_psiquiatra'
                for mes in range(1, 13):  # Pegando cada mês do ano
                    sqlstr = f'SELECT COUNT(*) FROM {atendimento} WHERE usuarios_prontuario = ? AND ano = ? AND ' \
                             f'mes = {mes}'  # Contando a quantidade de atendimento para add no gráfico
                    results = self.cursor.execute(sqlstr,
                                                  (int(self.lineEditInfPront.text()), int(self.lineEditAno.text())))
                    for quantidade in results:  # Adicionando a quantidade de atendimentos ao gráfico
                        if tipo_atendimento == 0:
                            set0.append(quantidade)
                        else:
                            set1.append(quantidade)
            series = QBarSeries()
            series.append(set0)
            series.append(set1)
            chart = QChart()
            chart.addSeries(series)
            chart.setTitle(f'Porcentagem de Atendimentos no CAPS por mês - ano: {self.lineEditAno.text()}')
            chart.setAnimationOptions(QChart.SeriesAnimations)
            categories = ["Jan", "FeV", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"]  # Mês
            axis = QBarCategoryAxis()
            axis.append(categories)
            chart.createDefaultAxes()
            chart.setAxisX(axis, series)

            chart.legend().setVisible(True)
            chart.legend().setAlignment(Qt.AlignBottom)

            chartView = QChartView(chart)
            chartView.setRenderHint(QPainter.Antialiasing)
            gridlayout = QGridLayout(self.widget)
            gridlayout.addWidget(chartView, 50, 50)
        except Exception:
            pass
