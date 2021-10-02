# InfoCAPS

Programa desenvolvido para serviços de saúde, mais especificamente em CAPS (Centro de Atenção Psicossocial - serviço do Sistema Único de Saúde), com o intuito de ser um centro de informações/dados sobre os usuários daquela instituição. É um programa que armazena desde informações básicas dos usuários - nome, data de nascimento, número de prontuário etc - até as ações que são realizadas pelos trabalhadores para aqueles usuários - consultas psiquiátricas, atendimentos em grupo, medicações ministradas, atendimentos de psicoterapia.

 

## Linguagens e bibliotecas utilizadas

O programa foi desenvolvido em Python com o uso da biblioteca PyQt5 para criação da interface gráfica.  Nesta sua primeira versão foi utilizado como biblioteca de banco de dados o SQLite e o sqlite3 para implementação em Python. 



## Objetivos

Os objetivos para utilização do programa dentro do serviço foram divididos em três módulos que trazem maior eficiência para processos distintos: relacionados aos usuários do serviço, relacionados ao serviço em si e relacionados ao conjunto de serviços (neste caso chamado de RAPS - Rede de Atenção Psicossocial):

### Relacionados ao usuário

1. **Centralização de informações de dados básicos dos usuários do CAPS**: nome, cadastro, prontuário, data de nascimento, idade, UBS, regional, referência, médico, início no CAPS, CID, telefone, endereço, situação (ativo, inativo, falecido), encaminhado por qual serviço – renda, benefício (BPC), raça, situação laboral.
2. **Centralização de informações de dados complementares dos usuários do CAPS**: toma haldol decanoato, toma medicações de alto custo, está em medicação assistida, qual o seu PTS no CAPS?, últimos atendimentos (referência, psiquiatra), rede de apoio.
3. **Centralização de informações de ações em saúde oferecidas ao usuário durante o seu acompanhamento no serviço (com datas de cada ação)**: haldol decanoato, medicação assistida, atendimentos diversos (referência, psiquiatra, familiares, grupos diversos, grupos de família, visita domiciliar), atendimentos na atenção básica (intrasetorial).
4. **Alertas de ações com usuários**: próximo haldol decanoato, próxima retirada de medicação de alto custo, próxima retirada de medicação assistida.
5. **Produção de “relatórios” para auxiliar em análises sobre o acompanhamento do usuário no CAPS/ relação de força com cada ação em Saúde Mental (utilização de gráficos diversos)**: quantidade de atendimentos de cada tipo por ano, mês, semana; porcentagem de cada tipo de atendimento também por período.

### Relacionados ao serviço

1. **Centralização de dados de acolhimentos realizados no CAPS por dia, mês e ano**: utilização facilitada destes dados para inserção na RAAS; relatórios de porcentagem de acolhimentos por UBS, regional etc.
2. **Centralização de dados de ações setoriais do CAPS**: planilha de usuários em haldol decanoato (enfermagem), medicação assistida (enfermagem/farmácia), medicação de alto custo (farmácia)
3. **Centralização de dados de ações em saúde relacionados a indicadores internos, municipais e federais**: produção de relatórios mensais por usuário e profissionais responsáveis de ações diversas evitando dados duplicados (RAAS)
4. **Produção de “relatórios” por períodos para auxiliar na gestão do CAPS**: quantidade total, porcentagem de atendimentos, porcentagem de inserções no CAPS a partir de acolhimentos, entre outros
5. **Produção de dados para utilização em indicadores de Saúde Mental**

### Relacionados a rede (RAPS)

1. **Centralização de dados do usuário para encaminhamento a outros serviços da RAPS e continuidade do cuidado/ PTS**: produção de relatório com dados específicos que podem auxiliar no outro serviço conhecer o usuário a partir de sua relação com o CAPS;
2. **Produção de “relatórios” para apoiar ações de matriciamento**: a partir de dados de acolhimentos e acompanhamento por período (UBS, quem encaminhou), visualizar a relação dos usuários de determinada UBS com o CAPS – ambulatorial, crise, HN etc – para problematizar questões referentes ao apoio de Saúde Mental necessário àquele território.
3. ***Produção de dados para utilização em indicadores de Saúde Mental municipais:*** com a centralização de dados a partir de programa único será possível visualizar semelhanças e diferenças entre os serviços de Saúde Mental do município e indicadores municipais de Saúde Mental.