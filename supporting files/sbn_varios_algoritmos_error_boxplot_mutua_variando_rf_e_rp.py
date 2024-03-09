# Gera o boxplot do erro das previsões para cada WTG e calcula o erro absoluto medio
# obtido com o uso do algoritmo de regressão LGBM
# Grupo com 30 aerogeradores do Complexo Eólico São Bento do Norte
# Variacao de -30 a 150% de Rf - distribuicao uniforme

'''

range =[2.5,0.7].Rf and [2.5,0.7].Rp and k=1

5447 samples
Mean Absolute Percentage Error =  20.711 %
Percentual de previsões com erro absoluto > 10% =  53.986 %
Mean Absolute Percentage Error =  8.586 %
Percentual de previsões com erro absoluto > 10% =  24.254 %

_______________________________________________________________


range =[1.5,0.7].Rf and [1.5,0.7].Rp and k=0,6

300 samples:
30-67
Mean Absolute Percentage Error =  20.234 %
Percentual de previsões com erro absoluto > 10% =  59.32 %
30-30
Mean Absolute Percentage Error =  13.478 %
Percentual de previsões com erro absoluto > 10% =  40.778 %

800 samples:
Mean Absolute Percentage Error =  18.981 %
Percentual de previsões com erro absoluto > 10% =  57.002 %
Mean Absolute Percentage Error =  12.517 %
Percentual de previsões com erro absoluto > 10% =  37.681 %

1300
Mean Absolute Percentage Error =  16.87 %
Percentual de previsões com erro absoluto > 10% =  53.819 %
Mean Absolute Percentage Error =  11.382 %
Percentual de previsões com erro absoluto > 10% =  35.632 %

1800
Mean Absolute Percentage Error =  15.81 %
Percentual de previsões com erro absoluto > 10% =  52.247 %
Mean Absolute Percentage Error =  10.65 %
Percentual de previsões com erro absoluto > 10% =  34.093 %

2300
Mean Absolute Percentage Error =  9.323 %
Percentual de previsões com erro absoluto > 10% =  30.546 %

2800
Mean Absolute Percentage Error =  8.274 %
Percentual de previsões com erro absoluto > 10% =  26.762 %

3300
Mean Absolute Percentage Error =  7.774 %
Percentual de previsões com erro absoluto > 10% =  25.098 %

3800
Mean Absolute Percentage Error =  4.512 %
Percentual de previsões com erro absoluto > 10% =  14.294 %

____________________________________________________________________

range =[1.5,0.7].Rf and [1.5,0.7].Rp and [0.3,1].k

1000 samples
Mean Absolute Percentage Error =  7.91 %
Percentual de previsões com erro absoluto > 10% =  31.542 %
Mean Absolute Percentage Error =  5.723 %
Percentual de previsões com erro absoluto > 10% =  18.333 %

2000 samples
MP Mean Absolute Percentage Error =  5.501 %
Percentual de previsões com erro absoluto do MP> 10% =  16.889 %




____________________________________________________________________

range =[2.5,0.7].Rf and [2.5,0.7].Rp and k=0,6

Samples 1000
Mean Absolute Percentage Error =  22.976 %
Percentual de previsões com erro absoluto > 10% =  60.199 %
Mean Absolute Percentage Error =  14.146 %
Percentual de previsões com erro absoluto > 10% =  38.978 %

Samples 1500
Mean Absolute Percentage Error =  22.453 %
Percentual de previsões com erro absoluto > 10% =  59.254 %
Mean Absolute Percentage Error =  13.526 %
Percentual de previsões com erro absoluto > 10% =  37.526 %

Samples 2500
Mean Absolute Percentage Error =  22.136 %
Percentual de previsões com erro absoluto > 10% =  58.726 %
Mean Absolute Percentage Error =  13.128 %
Percentual de previsões com erro absoluto > 10% =  36.662 %

Samples 3000
Mean Absolute Percentage Error =  21.933 %
Percentual de previsões com erro absoluto > 10% =  58.504 %
Mean Absolute Percentage Error =  13.023 %
Percentual de previsões com erro absoluto > 10% =  36.581 %


__________________________________________________________________
range = all - Mix

12785 samples
Mean Absolute Percentage Error =  17.261 %
Percentual de previsões com erro absoluto > 10% =  50.2 %
Mean Absolute Percentage Error =  9.35 %
Percentual de previsões com erro absoluto > 10% =  28.385 %


__________________________________________________________________

range =[2.5,0.7].Rf and [2.5,0.7].Rp and [0.3,1].k

500 samples
Mean Absolute Percentage Error =  24.911 %
Percentual de previsões com erro absoluto > 10% =  65.775 %
Mean Absolute Percentage Error =  16.635 %
Percentual de previsões com erro absoluto > 10% =  51.067 %

1250 samples
Mean Absolute Percentage Error =  16.096 %
Percentual de previsões com erro absoluto > 10% =  47.411 %

2250 samples
MP Mean Absolute Percentage Error =  15.387 %
Percentual de previsões com erro absoluto do MP> 10% =  46.114 %


__________________________________________________________________

range = varmix - atenção

2000 samples
MP Mean Absolute Percentage Error =  10.79 %
Percentual de previsões com erro absoluto do MP> 10% =  32.96 %

MP Mean Absolute Percentage Error =  9.711 %
Percentual de previsões com erro absoluto do MP> 10% =  30.26 %

MP Mean Absolute Percentage Error =  9.147 %
Percentual de previsões com erro absoluto do MP> 10% =  28.573 %

MP Mean Absolute Percentage Error =  8.657 %
Percentual de previsões com erro absoluto do MP> 10% =  26.728 %

MP Mean Absolute Percentage Error =  8.119 %
Percentual de previsões com erro absoluto do MP> 10% =  25.148 %
MP Mean Absolute Percentage Error =  7.866 %
Percentual de previsões com erro absoluto do MP> 10% =  24.317 %
MP Mean Absolute Percentage Error =  7.634 %
Percentual de previsões com erro absoluto do MP> 10% =  23.773 %

mix2
MP Mean Absolute Percentage Error =  7.173 %
Percentual de previsões com erro absoluto do MP> 10% =  22.46 %
MP Mean Absolute Percentage Error =  6.907 %
Percentual de previsões com erro absoluto do MP> 10% =  21.504 %
MP Mean Absolute Percentage Error =  6.777 % - random 2
Percentual de previsões com erro absoluto do MP> 10% =  21.19 %
MP Mean Absolute Percentage Error =  6.664 % -random 9
Percentual de previsões com erro absoluto do MP> 10% =  20.872 %


MP Mean Absolute Percentage Error =  6.275 %
Percentual de previsões com erro absoluto do MP> 10% =  19.492 %



Var-mir-3
MP Mean Absolute Percentage Error =  6.199 %
Percentual de previsões com erro absoluto do MP> 10% =  19.148 %
...
CGM Mean Absolute Percentage Error =  251.818 %
Percentual de previsões com erro absoluto do CGM > 10% =  88.664 %

'''




import warnings
warnings.filterwarnings('ignore')
from lightgbm import LGBMRegressor
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_percentage_error
import statistics

from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso
from sklearn.linear_model import ElasticNet
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from sklearn.linear_model import RANSACRegressor
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import DotProduct, WhiteKernel, RBF
import xgboost as xgb
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import ElasticNet

 
arquivo = pd.read_excel('C:/Users/Alexa/OneDrive/Área de Trabalho/Rec_Padroes/parque_eolico_SBN/dataframe_sbn_mutua_varia_rf_e_rp.xlsx', sheet_name = 'var-mix-3')#2,5-0,7-k=var
X = arquivo.iloc[:,68:] #68 to mix and 69 to variable k
Y = arquivo.iloc[:,1:31]

#Normalizando as variaveis preditoras
normalizador = MinMaxScaler(feature_range=(0,1))
X_norm = pd.DataFrame(normalizador.fit_transform(X))


X_norm_teste = pd.DataFrame()
Y_teste = pd.DataFrame()
Y_pred = pd.DataFrame()


for item in Y:
    y = Y[item]
    print('oi')
    x_norm_treino, x_norm_teste, y_treino, y_teste = train_test_split(X_norm , y, test_size = 0.30, random_state = 12)#12
    modelo = LGBMRegressor(n_estimators=177, learning_rate=0.062)
    #modelo = LinearRegression()
    #modelo = Ridge(alpha=0.001)
    #modelo = Lasso(alpha=0.001)
    #modelo = DecisionTreeRegressor(min_samples_split=5, max_depth=3, criterion='mse')
    #modelo = RandomForestRegressor(min_samples_split=5, max_depth=11, min_samples_leaf=4)
    #modelo = SVR(kernel='rbf', degree=2, gamma='auto', C=60, epsilon=0.01)
    #modelo = RANSACRegressor(LinearRegression(), max_trials=100, min_samples=50, loss='absolute_loss', residual_threshold=5.0)
    #kernel = DotProduct()
    #modelo = GaussianProcessRegressor(kernel=kernel)
    #modelo = xgb.XGBRegressor(use_label_encoder=False)
    
    modelo.fit(x_norm_treino, y_treino)
    X_norm_teste = pd.concat([X_norm_teste,x_norm_teste], axis=1, ignore_index=True)
    Y_teste = pd.concat([Y_teste,y_teste], axis=1, ignore_index=True)
    
    y_pred = modelo.predict(x_norm_teste)
    Y_pred = pd.concat([Y_pred,pd.Series(y_pred)], axis=1, ignore_index=True)

from sklearn.metrics import mean_absolute_percentage_error  
erro_brut=  (Y_teste.values-Y_pred.values)/Y_teste.values*100
Erro = abs((Y_teste.values-Y_pred.values)/Y_teste.values*100)
mape = mean_absolute_percentage_error(Y_teste , Y_pred)


#%% Contando os outliers > 10%

ERRO = pd.DataFrame(Erro)
outliers= 0
l=0
while l<Erro.shape[0]:
    for i in ERRO.iloc[l,:]:
        if i > 10: 
            outliers=outliers+1
        else:
                pass
    l=l+1


print('MP Mean Absolute Percentage Error = ', round(mape*100,3), '%') 
print('Percentual de previsões com erro absoluto do MP> 10% = ', round(outliers/(ERRO.shape[0]*ERRO.shape[1])*100,3), '%')


#%% CGM ERRORS - Erros da aplicação direta do método do alicate terrometro

x_teste=pd.DataFrame(normalizador.inverse_transform(x_norm_teste))
mape_cgm = mean_absolute_percentage_error(Y_teste , x_teste)
erro_brut_cgm=  (Y_teste.values-x_teste.values)/Y_teste.values*100
Erro_cgm = abs((Y_teste.values-x_teste.values)/Y_teste.values*100)

ERRO_cgm = pd.DataFrame(Erro_cgm)
outliers_cgm= 0
l=0
while l<Erro_cgm.shape[0]:
    for i in ERRO_cgm.iloc[l,:]:
        if i > 10: 
            outliers_cgm=outliers_cgm+1
        else:
                pass
    l=l+1

print('...')
print('CGM Mean Absolute Percentage Error = ', round(mape_cgm*100,3), '%') 
print('Percentual de previsões com erro absoluto do CGM > 10% = ', round(outliers_cgm/(ERRO_cgm.shape[0]*ERRO_cgm.shape[1])*100,3), '%')


#%% Boxplot do APE das previsões por aerogerador
 
ERRO.columns = Y.columns

plt.boxplot(ERRO, labels=ERRO.columns)
plt.gcf().set_size_inches(40, 20)#tamanho do grafico
plt.xlabel('Wind turbine generator', fontsize=40)
plt.ylabel('APE(%)', fontsize=40)
plt.xticks(fontsize=30)#tamanho da letra dos eixos
plt.xticks(rotation=45)
plt.yticks(fontsize=30)
plt.semilogy()
plt.grid(True)
plt.title('Boxplot of APEs between the real and LGBM estimated ground resistances', fontsize=40)
plt.annotate("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _  _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ", xy=(10, 12), xycoords='data', xytext=(0.7, 10.3), textcoords='data', color='red')
plt.show()
plt.close()

#%%
import matplotlib.pyplot as plt

plt.hist(-erro_brut[:,4], bins=20)
plt.title("Histograma do erro do método proposto com LGBM")
plt.xlabel("Erro Absoluto (%)")
plt.ylabel("Ocorrência")
plt.grid()
plt.show()
plt.close()

#%%
import matplotlib.pyplot as plt

plt.hist(-erro_brut_cgm[:,4], bins=20)
plt.title("Histograma do erro do metodo direto do alicate terrômetro com LGBM")
plt.xlabel("Erro Absoluto (%)")
plt.ylabel("Ocorrência")
plt.grid()
plt.show()
plt.close()


#%%
'''
# libraries & dataset
import seaborn as sns
import matplotlib.pyplot as plt
# set a grey background (use sns.set_theme() if seaborn version 0.11.0 or above) 
sns.set(style="darkgrid")
df = ERRO['SB03']
 
# Grouped violinplot
sns.violinplot(data=df, palette="Pastel1")
plt.show()'''



