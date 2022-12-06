
import pandas as pd
from sqlalchemy import create_engine
import numpy as np





import pandas as pd
from datetime import datetime, date

cadunico ="Dados/cadunico.xlsx"
baseCad=pd.read_excel(cadunico)



# This function converts given date to age
def GetIdade(nascimento):
    today = date.today()
    return today.year - nascimento.year - ((today.month, 
                                      today.day) < (nascimento.month, 
                                                    nascimento.day))



#Criando a tabela fato

#Criando a tabela fato

#Mudar a data Nascimento para data CaD
Fact_Cad =baseCad.loc[:,['N° REGIÃO','N° MEMBRO FAM','RENDA RESPONSAVEL','RENDA FAM','RENDA PERCAPTA','DAT NASC','CPF','BAIRRO','DATA DE CADASTRO']]
Fact_Cad.rename(columns={'N° REGIÃO': 'id_regiao'},inplace=True)
Fact_Cad.rename(columns={'CPF': 'sk_pessoa'},inplace=True)
Fact_Cad.rename(columns={'N° MEMBRO FAM': 'qtd_pessoas_dom'},inplace=True)
Fact_Cad.rename(columns={'RENDA RESPONSAVEL': 'rendaResponsavel'},inplace=True)
Fact_Cad.rename(columns={'RENDA FAM': 'rendaFamiliar'},inplace=True)
Fact_Cad.rename(columns={'RENDA PERCAPTA': 'rendaPerCapta'},inplace=True)
Fact_Cad.rename(columns={'BAIRRO': 'bairro'},inplace=True)
Fact_Cad.rename(columns={'DATA DE CADASTRO': 'dataCad'},inplace=True)
Fact_Cad['id_data'] = Fact_Cad['dataCad'].dt.strftime('%d/%m/%Y')
Fact_Cad['idadeRespon'] = Fact_Cad['DAT NASC'].apply(GetIdade)
Fact_Cad=Fact_Cad.dropna()


Fact_Cad=Fact_Cad.drop(columns="DAT NASC")





import pandas as pd

def get_calendar(dt_start, dt_end):
    dim_calendar = pd.DataFrame()
    dim_calendar["data"] = pd.date_range(start=dt_start, end=dt_end)
    dim_calendar["ano"] = dim_calendar.data.apply(lambda x: x.strftime("%Y"))
    dim_calendar["mes"] = dim_calendar.data.apply(lambda x: x.strftime("%m"))
    dim_calendar["dia"] = dim_calendar.data.apply(lambda x: x.strftime("%d"))
    #dim_calendar["dia_semana"] = dim_calendar.data.apply(lambda x: week_day[x.weekday()])
    dim_calendar['id_data'] = dim_calendar['dia'].astype(str)+'/'+dim_calendar['mes'].astype(str)+'/'+dim_calendar['ano'].astype(str)
    return dim_calendar
Dim_date= get_calendar('01/01/2020','31/12/2022')




#Criando a Dimensão Regiao 

Dim_regiao =  pd.DataFrame({'id_regiao':['1.0','2.0','3.0','4.0','5.0'],
                              'nome_regiao':['Região 1','Região 2','Região 3','Região 4','Região 5']
                          
})

#Criando a Dimensão Dim_Responsavel_familiar
import numpy as np
#Criando a Dimensão Dim_Responsavel_familiar

def CalcRenda(rendafam):
    faixa1 = 0
    faixa2 = 606
    faixa3 = 1212
    faixa=''
    if rendafam <=faixa1:

      faixa="Sem renda"
 
    elif rendafam <faixa2:

      faixa="<606"
 
    elif rendafam >faixa2 and rendafam<faixa3:

      faixa=">606 e <1212"
    elif rendafam>faixa3:

      faixa=">1212"
    
    return faixa
    
def CalcFaixaEtaria(idade):
  faixa1 = 0
  faixa2 = 20
  faixa3 = 35
  faixa4 = 50
  faixa5=60
  faixa=''
  if idade >faixa1 and idade<=faixa2:
    faixa="<=20"
  elif idade >faixa2 and idade<=faixa3:
    faixa=">20 e <=35"
  elif idade >faixa3 and idade<=faixa4:
    faixa=">35 e <=50"
  elif  idade >faixa4 and idade<=faixa5:
    faixa=">50 e <=60"
  elif idade >faixa5 :
    faixa=">60"
  
  return faixa

def VerStatus(renda):
  valor=606
  status=''
  if renda<=valor:
    status="Aprovado"
  else:
    status="Não Aprovado"

  return status

  

#Criando a Dimensão Dim_Responsavel_familiar


Dim_Responsavel_familiar =baseCad.loc[:,['NOME','SEXO','CPF','DAT NASC']]
Dim_Responsavel_familiar.rename(columns={'NOME': 'nome'},inplace=True)
Dim_Responsavel_familiar.rename(columns={'SEXO': 'sexo'},inplace=True)
Dim_Responsavel_familiar.rename(columns={'CPF': 'sk_pessoa'},inplace=True)
Dim_Responsavel_familiar.rename(columns={'DAT NASC': 'dataNascimento'},inplace=True)
Dim_Responsavel_familiar['idade'] = Dim_Responsavel_familiar['dataNascimento'].apply(GetIdade)
Dim_Responsavel_familiar=Dim_Responsavel_familiar.dropna()
Dim_Responsavel_familiar['faixa_de_renda']=baseCad['RENDA FAM'].apply(CalcRenda)
Dim_Responsavel_familiar['faixa_etaria']=Dim_Responsavel_familiar['idade'].apply(CalcFaixaEtaria)
Dim_Responsavel_familiar['status']=baseCad['RENDA PERCAPTA'].apply(VerStatus)






#Carregamento no DW"""
#postgres://kumxpccv:VkS0JRbaPAVzMpc5iwRv5CZnkQCszsTm@kesavan.db.elephantsql.com/kumxpccv
engine = create_engine("postgresql://ETL:ETL1234@localhost:5432/DW_PMVV", echo=True)        
conn=engine.connect()
print("Connection established")

conn.execute(""" 


CREATE SCHEMA "dw";

CREATE TABLE "dw"."dim_date" (
  "id_data" varchar(255),
  "data" date,
  "dia" varchar(255),
  "mes" varchar(255),
  "ano" int,

  CONSTRAINT "dim_date_pk" PRIMARY KEY ("id_data")
);

CREATE TABLE "dw"."dim_regiao" (
  "id_regiao" varchar(255),
  "nome_regiao" varchar(255),
   CONSTRAINT "dim_regiao_pk" PRIMARY KEY ("id_regiao")
);

CREATE TABLE "dw"."dim_responsavel_familiar" (
  "sk_pessoa" varchar(255),
  "nome" varchar(255),
  "sexo" varchar(255),
  "idade" varchar(255),
  "faixa_de_renda" varchar(255),
  "faixa_etaria" varchar(255),
  "status" varchar(255),
  "dataNascimento" date,
  CONSTRAINT "dim_responsavel_familiar_pk" PRIMARY KEY ("sk_pessoa")
);

CREATE TABLE "dw"."fact_Cad" (
  "id_regiao" varchar(255),
  "id_data" varchar(255),
  "sk_pessoa" varchar(255),
  "rendaFamiliar" float,
  "rendaPerCapta" float,
  "idadeRespon" varchar(255),
  "qtd_pessoas_dom" int,
  "rendaResponsavel" float,
  "bairro" varchar(255),
  "dataCad" date,

    FOREIGN KEY(id_data) 
	  REFERENCES dw.dim_date(id_data),
     FOREIGN KEY(id_regiao) 
	  REFERENCES dw.dim_regiao(id_regiao),
    FOREIGN KEY(sk_pessoa) 
	  REFERENCES dw.dim_responsavel_familiar(sk_pessoa)

);
""")

#insere os dados da DataFrame no banco de dados 
Dim_date.to_sql(name='dim_date' , con=conn , schema = "dw" , if_exists = 'append' , index = None, index_label = None,chunksize = None , dtype = None , method = None )
print('Executado')

Dim_regiao.to_sql(name='dim_regiao' , con=conn , schema = "dw" , if_exists = 'append' , index = None, index_label = None,chunksize = None , dtype = None , method = None )
print('Executado')

Dim_Responsavel_familiar.to_sql(name='dim_responsavel_familiar' , con=conn , schema = "dw" , if_exists = 'append' , index = None, index_label = None,chunksize = None , dtype = None , method = None )
print('Executado')

Fact_Cad.to_sql(name='fact_Cad' , con=conn , schema = "dw" , if_exists = 'append' , index = None, index_label = None,chunksize = None , dtype = None , method = None )
print('Executado')