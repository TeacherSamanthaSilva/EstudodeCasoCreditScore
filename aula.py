# Importação da "dupla dinânica": Numpy e Pandas
import pandas as pd
import numpy as np
#Importação das bibliotecas gráficas
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
import matplotlib.pyplot as plt
import seaborn as sns
#definição de um template de fundo branco para plotagem dos gráficos
pio.templates.default = "plotly_white"
#Importação dos pacotes para criação do modelo
# Importação da função train_test_split do pacote Sklearn
from sklearn.model_selection import train_test_split
# Importanto o Algoritmo Random Forest para fazer a Classificação
from sklearn.ensemble import RandomForestClassifier
# Importando accuracy_score para calcular a Acurácia do modelo
from sklearn.metrics import accuracy_score

#importação do dataset
data = pd.read_csv("train.csv")
#Exibição das primeiras linhas do dataset
print(data.head())