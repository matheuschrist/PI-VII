# Projeto-Integrador-VII


Desenvolvimento de uma pipeline de dados para análise Governamental das
localidades com a maior carência de inscrições no Cadastro único.
Alyson Vargas¹
Carlos Freitas¹
Diogo dos Santos Freires¹
João Victor Fritoli¹
Matheus Christ de Andrade¹
Patrick Robert da Silva Gomes¹
Rafael da Silva Lopes¹
James Alves Junior²
¹ Acadêmicos do Curso de Sistemas de informação 6ª período do Centro
Universitário Salesiano.
² Orientador do Projeto Integrador.




# 1. METODOLOGIA
Para realizar este trabalho foi abordado uma metodologia colaborativa, sendo
feito reuniões para avaliações e ajustes dos detalhes da pipeline com o responsável
da Prefeitura de Vila Velha buscando entender e resolver todos os desafios
propostos para trazer o resultado esperado para o cliente, serão utilizados os
conceitos de ETL para extrair os dados brutos fornecidos pelo solicitante através de
csv(Comma-separated values), e realizar todas as etapas para transformação e
criação de um Data Warehouse buscando trazer o melhor desempenho e
performance para a consulta dos dados, utilizando conceitos de estatísticas e
desenvolvimentos de Dashboards analíticos sendo possível que através deles o
solicitante possa usar como apoio a tomada de decisão para resolver o problema
proposto.
Para confecção da modelagem lógica foi utilizado o programa dbdiagram.io
que é uma ferramenta para desenhar diagramas de ER através da escrita de
códigos.
Como ferramenta de ETL foi utilizado a linguagem de programação Python
juntamente com a biblioteca Pandas que pode ser considerada a mais importante
dentro do mundo da análise de dados para o Python. É a ferramenta principal para
construção de estrutura, manipulação e limpeza de dados, sendo também utilizada
com bibliotecas de processamento numérico e construção de gráficos.
Para confecção do Dashboard analítico foi utilizado Power BI que é um
software de Business Intelligence, ou seja, transforma dados em informação
gerando inteligência de negócios. Ele permite que o usuário conecte diferentes
fontes de dados (txt, Excel, CSV, banco de dados, dados de internet, etc) para
extraí-los, tratá-los, gerar indicadores de desempenho e criar dashboards.


# 2. RESULTADOS E DISCUSSÃO
Seguindo a metodologia indicada quanto a construção de todo o projeto foram
utilizados os dados obtidos através das entrevistas com os responsáveis escolhidos
pela prefeitura, foram elaborados uma série de protótipos do sistema para uma
pré-visualização dos usuários finais com o intuito de receber feedbacks e propostas
de melhorias ao dashboard a fim de mostrar as visualizações e funcionalidades do
produto final. Utilizando esses protótipos como guia fomos capazes de desenvolver
uma versão funcional do ETL dessa base fornecida, restando apenas os dados
essenciais que foram imprescindíveis para o desenvolvimento das visualizações
propostas pelos solicitantes, em um primeiro momento. Essa versão do sistema vai
ser demonstrada nas Figuras a seguir.
## 2.1. MODELAGEM DIMENSIONAL
A modelagem dimensional deu-se na criação de três tabelas dimensões e
uma tabela fato, as tabelas dimensões são ligadas a tabela fato por um
relacionamento com cardinalidade 1 para muitos, conforme imagem abaixo.

![image](https://user-images.githubusercontent.com/62062407/205998709-b708e77f-4d86-48aa-be6e-9b2c84444bca.png)

## 2.2. DASHBOARD
O município de vila velha é dividido por regiões, cada região contém diversos
bairros, em vista disso, foi criado um filtro por regiões. Também podemos ver a
quantidade de cadastros que foram aprovados e não aprovados, bem como
informações de cadastros por faixa de renda e faixa etária por gênero.

![image](https://user-images.githubusercontent.com/62062407/205998812-deac864a-050f-43f2-9aa1-4e88b5382205.png)



Posicionando o mouse sobre a região 5, por exemplo, temos a exibição de
informações sobre a região selecionada sendo exibidas em um formato de tabela.
Essas informações exibidas podem ser parametrizadas acessando a área
“campos” no power bi, desta forma, é possível escolher os dados que serão exibidos
na grid de resultado “tabela”.

![image](https://user-images.githubusercontent.com/62062407/205998887-17e0a36c-e009-489c-af4d-ab02dc3d7179.png)

No exemplo mostrado na figura foi selecionado o
bairro, nome da pessoa, quantidade de membros na casa, renda familiar, renda per
capita e status podendo ser aprovado ou não aprovado no cadastro único.

![image](https://user-images.githubusercontent.com/62062407/205999014-b1fdce32-ba70-4a03-a707-57dfe85d62e2.png)



Todo o dashboard segue esse padrão de funcionamento, ao posicionar o
mouse sobre o campo cadastros por faixa de renda outro gráfico é exibido
mostrando um resumo por cada região.
O dashboard funciona de forma completamente interativa de forma que a
ação de clicar em um área, região 5 por exemplo, mude o resultado de praticamente
todos os campos no dashboard.

![image](https://user-images.githubusercontent.com/62062407/205999054-87cc511a-1518-463b-9c48-14f6b0a55907.png)




## 3. CONCLUSÕES (OU CONSIDERAÇÕES FINAIS)
O desenvolvimento desse projeto possibilitou uma análise geral de como um
projeto de BI pode ser feito e de como ele pode melhorar a visão do usuário final
com suas tomadas de decisões.
Para o grupo o desenvolvimento deste projeto foi muito importante, pois foi,
para a maioria dos integrantes do grupo, a primeira experiência com ferramentas de
BI como Power BI, Python junto com a biblioteca pandas e o dbdiagrama que foi
usado para criação da modelagem dimensional.
Também, durante o desenvolvimento, a ferramenta Power BI foi melhor
compreendida, facilitando o seu futuro uso em outras ocasiões.






![4aea0de172d83451d80b770aa3d317eb-Modelo de banner VII Mostra PIE _page-0001](https://user-images.githubusercontent.com/62062407/205998048-9ec64cf7-e2a6-467b-994c-a14f71018427.jpg)
