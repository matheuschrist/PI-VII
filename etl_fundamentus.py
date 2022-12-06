import pandas as pd
from sqlalchemy import create_engine


balanco_cogn3 = 'BaseDados/balanco_COGNA.xlsx'
balanco_azul4='BaseDados/balanco_AZUL4.xlsx'
balanco_cielo='BaseDados/balanco_CIELO.xlsx'
balanco_mglu3='BaseDados/balanco_MGLU3.xlsx'
balanco_lwsa3='BaseDados/balanco_LWSA3.xlsx'
balanco_viia3='BaseDados/balanco_VIIA3.xlsx'
balanco_petz3='BaseDados/balanco_PETZ3.xlsx'
balanco_itub4='BaseDados/balanco_ITUB4.xlsx'
balanco_engie='BaseDados/balanco_ENGIE.xlsx'
balanco_crfb3='BaseDados/balanco_CRFB3.xlsx'



COGN3 = pd.read_excel(balanco_cogn3,sheet_name="Bal. Patrim.")
COGN3_result = pd.read_excel(balanco_cogn3,sheet_name="Dem. Result.")
AZUL4= pd.read_excel(balanco_azul4,sheet_name="Bal. Patrim.")
AZUL4_result = pd.read_excel(balanco_azul4,sheet_name="Dem. Result.")
MGLU3 = pd.read_excel(balanco_mglu3,sheet_name="Bal. Patrim.")
MGLU3_result = pd.read_excel(balanco_mglu3,sheet_name="Dem. Result.")
CIEL3 = pd.read_excel(balanco_cielo,sheet_name="Bal. Patrim.")
CIEL3_result = pd.read_excel(balanco_cielo,sheet_name="Dem. Result.")
LWSA3 = pd.read_excel(balanco_lwsa3,sheet_name="Bal. Patrim.")
LWSA3_result = pd.read_excel(balanco_lwsa3,sheet_name="Dem. Result.")
PETZ3 = pd.read_excel(balanco_petz3,sheet_name="Bal. Patrim.")
PETZ3_result = pd.read_excel(balanco_petz3,sheet_name="Dem. Result.")
ITUB4 = pd.read_excel(balanco_itub4,sheet_name="Bal. Patrim.")
ITUB4_result = pd.read_excel(balanco_itub4,sheet_name="Dem. Result.")
EGIE3 = pd.read_excel(balanco_engie,sheet_name="Bal. Patrim.")
EGIE3_result = pd.read_excel(balanco_engie,sheet_name="Dem. Result.")
CRFB3 = pd.read_excel(balanco_crfb3,sheet_name="Bal. Patrim.")
CRFB3_result = pd.read_excel(balanco_crfb3,sheet_name="Dem. Result.")
VIIA3 = pd.read_excel(balanco_viia3,sheet_name="Bal. Patrim.")
VIIA3_result = pd.read_excel(balanco_viia3,sheet_name="Dem. Result.")

#Tratamento Padrão 
def Tratamento(balanco,result):
  #tratamento balanço 
  balanco=balanco.transpose()
  balanco.loc['XLSWrite 1.34 Copyright(c) 1999,2000 Axolot Data', 0] = "Data"
  balanco=balanco.reset_index()
  balanco=balanco.drop(['index'],axis=1)
  balanco.columns=balanco.loc[0]
  balanco=balanco.drop(0)
   #tratamento resultado  
  result=result.transpose()
  result.loc['XLSWrite 1.34 Copyright(c) 1999,2000 Axolot Data', 0] = "Data"
  result=result.reset_index()
  result=result.drop(['index'],axis=1)
  result.columns=result.loc[0]
  result=result.drop(0)

  return  balanco , result 

def CriarBase(base1,base2):
  base1,base2=Tratamento(base1,base2)
  #Selecionando as colunas que serão utilizadas 
  base1=base1.loc[:,['Patrimônio Líquido','Ativo Total','Data']]
  base2=base2.loc[:,['Receita Líquida de Vendas e/ou Serviços','Resultado Bruto','Despesas Com Vendas'
  ,'Despesas Gerais e Administrativas','Lucro/Prejuízo do Período','Data']]
  base=pd.merge(base1,base2,how="inner",on="Data")

  return base

#Criando A base COGN3

BaseCOGN3=CriarBase(COGN3,COGN3_result)

BaseCOGN3['id_acao']='COGN3'
BaseCOGN3['qtd_acoes']=1876610.000

#Criando A base LWSA3

BaseLWSA3=CriarBase(LWSA3,LWSA3_result)
BaseLWSA3['id_acao']='LWSA3'
BaseLWSA3['qtd_acoes']=592510.000

#Criando A base AZUL4

BaseAZUL4=CriarBase(AZUL4,AZUL4_result)
BaseAZUL4['id_acao']='AZUL4'
BaseAZUL4['qtd_acoes']=347999.000

#Criando A base CIELO

BaseCIEL3=CriarBase(CIEL3,CIEL3_result)
BaseCIEL3['id_acao']='CIEL3'
BaseCIEL3['qtd_acoes']=2716820.000

#Criando A base CRFB3 

BaseCRFB3=CriarBase(CRFB3,CRFB3_result)
BaseCRFB3['id_acao']='CRFB3'
BaseCRFB3['qtd_acoes']=2103610.000

#Criando A base EGIE3

BaseEGIE3=CriarBase(EGIE3,EGIE3_result)
BaseEGIE3['id_acao']='EGIE3'
BaseEGIE3['qtd_acoes']=815928.000

#Criando A base ITUB4

BaseITUB4=CriarBase(ITUB4,ITUB4_result)
BaseITUB4['id_acao']='ITUB4'
BaseITUB4['qtd_acoes']=9804140.000

#Criando A base MGLU3

BaseMGLU3=CriarBase(MGLU3,MGLU3_result)
BaseMGLU3['id_acao']='MGLU3'
BaseMGLU3['qtd_acoes']=6748930.000

#Criando A base PETZ3

BasePETZ3=CriarBase(PETZ3,PETZ3_result)
BasePETZ3['id_acao']='PETZ3'
BasePETZ3['qtd_acoes']=461643.000

#Criando A base VIIA3

BaseVIIA3=CriarBase(VIIA3,VIIA3_result)
BaseVIIA3['id_acao']='VIIA3'
BaseVIIA3['qtd_acoes']=1598430.000

#Concatenção de Base
Fact_balanco=pd.DataFrame()
Fact_balanco = pd.concat([BaseCOGN3,BaseLWSA3,BaseCRFB3,BasePETZ3,BaseVIIA3,BaseCIEL3,BaseEGIE3,
                        BaseITUB4,BaseMGLU3,BaseAZUL4])

#Criar a Dim Empresa

Dim_empresa  = pd.DataFrame({'id_acao':['COGN3','CRFB3','PETZ3','VIIA3','CIEL3','EGIE3',
                                            'ITUB4','MGLU3','AZUL4','LWSA3'],
                             'nome_empresa':['Cogna Educação S.A.','ATACADÃO S.A.',
                                         'Pet Center Comércio e Participações S.A.',
                                         'VIA Varejo S.A.','Bb Elo Cartões Participações S.A.',
                                         'Engie Brasil Energia S.A.','ITAÚ UNIBANCO HOLDING S.A.',
                                         'MAGAZINE LUIZA S.A','AZUL',' Locaweb Serviços de Internet S.A.']
})



def get_calendar(dt_start, dt_end):
    dim_calendar = pd.DataFrame()
    dim_calendar["data"] = pd.date_range(start=dt_start, end=dt_end)
    dim_calendar["Ano"] = dim_calendar.data.apply(lambda x: x.strftime("%Y"))
    dim_calendar["Mes"] = dim_calendar.data.apply(lambda x: x.strftime("%m"))
    dim_calendar["Dia"] = dim_calendar.data.apply(lambda x: x.strftime("%d"))
    #dim_calendar["dia_semana"] = dim_calendar.data.apply(lambda x: week_day[x.weekday()])
    dim_calendar['id_date'] = dim_calendar['Dia'].astype(str)+'/'+dim_calendar['Mes'].astype(str)+'/'+dim_calendar['Ano'].astype(str)
    return dim_calendar
Dim_date= get_calendar('01/01/2002','07/11/2022')

#Criar o Fact Cotação 

Fact_cotacao =pd.read_csv('BaseDados/Cotacoes.csv')

Fact_cotacao.loc[0, 'Unnamed: 1'] = "id_acao"
Fact_cotacao.columns=Fact_cotacao.loc[0]
Fact_cotacao=Fact_cotacao.drop(0)
Fact_cotacao=Fact_cotacao.dropna()

#Renomear nomes das colunas da tabela cotações

Fact_cotacao.rename(columns={'Data': 'id_date'},inplace=True)
Fact_cotacao.rename(columns={'Fechamento': 'valor_abertura'},inplace=True)
Fact_cotacao.rename(columns={'Abertura': 'valor_fechamento'},inplace=True)

Fact_cotacao['id_date'] = pd.to_datetime(Fact_cotacao['id_date'])
Fact_cotacao['id_date'] = Fact_cotacao['id_date'].dt.strftime('%d/%m/%Y')

#Renomear nomes das colunas Base proventos
Fact_proventos=pd.read_excel('BaseDados/BaseProventos.xlsx')
Fact_proventos=Fact_proventos.dropna()
Fact_proventos.rename(columns={'TIPO': 'tipo'},inplace=True)
Fact_proventos.rename(columns={'DATACOM': 'data_com'},inplace=True)
Fact_proventos.rename(columns={'PAGAMENTO': 'data_pagamento'},inplace=True)
Fact_proventos.rename(columns={'VALOR': 'valor'},inplace=True)
Fact_proventos.rename(columns={'Ação': 'id_acao'},inplace=True)
Fact_proventos = Fact_proventos.replace({',': '.'}, regex=True)
Fact_proventos['valor'] = Fact_proventos['valor'].astype(float)
Fact_proventos['id_date'] = Fact_proventos['data_pagamento'].dt.strftime('%d/%m/%Y')

#Renomear nomes das colunas

Fact_balanco.rename(columns={'Patrimônio Líquido': 'patrimonio_liquido'},inplace=True)
Fact_balanco.rename(columns={'Ativo Total': 'ativo_total'},inplace=True)
Fact_balanco.rename(columns={'Data': 'id_date'},inplace=True)
Fact_balanco.rename(columns={'Receita Líquida de Vendas e/ou Serviços': 'receita_liquida'},inplace=True)
Fact_balanco.rename(columns={'Resultado Bruto': 'resultado_bruto'},inplace=True)
Fact_balanco.rename(columns={'Despesas Com Vendas': 'despesas_vendas'},inplace=True)
Fact_balanco.rename(columns={'Despesas Gerais e Administrativas': 'despesas_adiministrativas'},inplace=True)
Fact_balanco.rename(columns={'Lucro/Prejuízo do Período': 'lucro_liquido'},inplace=True)

"""#Criando o data warehouse"""


#Carregamento no DW"""

engine = create_engine("postgresql://ETL:ETL1234@localhost/DW_Fundamentus", echo=True)        
conn=engine.connect()
print("Connection established")

conn.execute("""

CREATE TABLE "dim_date" (
	"data" DATE ,
	"id_date" Varchar NOT NULL,
	"Ano" varchar(255) ,
	"Mes" varchar(255) ,
	"Dia" varchar(255),
	CONSTRAINT "dim_date_pk" PRIMARY KEY ("id_date")
) ;



CREATE TABLE "dim_empresa" (
	"id_acao" Varchar NOT NULL,
	"nome_empresa" varchar(255) ,

	CONSTRAINT "dim_empresa_pk" PRIMARY KEY ("id_acao")
) ;

CREATE TABLE "fact_balanco" (
	"id_acao" Varchar NOT NULL,
	"id_date" Varchar NOT NULL,
	"patrimonio_liquido" float8,
	"ativo_total" float8,
	"receita_liquida" float8,
  "resultado_bruto" float8,
  "despesas_vendas" float8,
  "despesas_adiministrativas" float8,
  "lucro_liquido" float8,
  "qtd_acoes" float8,
	 FOREIGN KEY(id_date) 
	  REFERENCES Dim_date(id_date),
     FOREIGN KEY(id_acao) 
	  REFERENCES dim_empresa(id_acao)
) ;


CREATE TABLE "fact_cotacao" (
	"id_acao" Varchar NOT NULL,
	"id_date" Varchar NOT NULL,
	"valor_abertura" float8,
	"valor_fechamento" float8,

	 FOREIGN KEY(id_date) 
	  REFERENCES dim_date(id_date),
     FOREIGN KEY(id_acao) 
	  REFERENCES dim_empresa(id_acao)
) ;

CREATE TABLE "fact_proventos" (
	"id_acao" Varchar NOT NULL,
	"id_date" Varchar NOT NULL,
  "tipo" Varchar ,
	"data_com" date,
	"data_pagamento" date,
  "valor" float8,

	 FOREIGN KEY(id_date) 
	  REFERENCES dim_date(id_date),
     FOREIGN KEY(id_acao) 
	  REFERENCES dim_empresa(id_acao)
) ;


 """)

#insere os dados da DataFrame no banco de dados 
Dim_date.to_sql(name='dim_date' , con=conn , schema = None , if_exists = 'append' , index = None, index_label = None,chunksize = None , dtype = None , method = None )
print('Executado')

Dim_empresa.to_sql(name='dim_empresa' , con=conn , schema = None , if_exists='append' , index = None, index_label = None,chunksize = None , dtype = None , method = None)
print('Executado')

Fact_balanco.to_sql(name='fact_balanco' , con=conn , schema = None , if_exists = 'append', index = None , index_label = None ,chunksize = None, dtype = None , method = None )
print('Executado')

Fact_cotacao.to_sql(name='fact_cotacao' , con=conn , schema = None , if_exists = 'append', index = None , index_label = None ,chunksize = None , dtype = None , method = None )
print('Executado')

Fact_proventos.to_sql(name='fact_proventos' , con=conn , schema = None , if_exists ='append', index = None , index_label = None ,chunksize = None , dtype = None , method = None )

