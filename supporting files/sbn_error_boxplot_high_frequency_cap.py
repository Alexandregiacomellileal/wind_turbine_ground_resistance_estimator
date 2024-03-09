# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 10:15:13 2022

@author: alexa
"""

import numpy as np
import os
import random
import pandas as pd
import pyautogui
import time
import scipy.io
import matplotlib.pyplot as plt
from scipy.io import loadmat
import shutil
import time

#Dataframe que conterá os vetores solução para Rf, Rp, Cf, Cp e Rmed.
Rf = pd.DataFrame({'OD01':[] , 'SB01':[] ,'SB02':[] ,'SB03':[] , 'SB05':[] , 'SB04':[] , 'OD02':[], 'OD03':[] ,'SB06':[] ,'SB08':[] , 'SB07':[] , 'OD04':[] ,'SB10':[] , 'SB11':[] , 'OD15':[] , 'SB09':[] ,'OD14':[] , 'SB15':[] , 'SB14':[] , 'SB13':[] , 'OD10':[] , 'OD09':[] ,'OD08':[] ,'OD07':[] , 'SB12':[] , 'OD06':[] , 'OD05':[] , 'OD11':[] , 'OD12':[] , 'OD13':[]})
Rp = pd.DataFrame({'-OD1':[] , 'OD1-SB1':[] ,'SB01-SB02':[] ,'SB02-SB03':[] , 'SB03-SB05':[] , 'SB05-SB04':[] , 'SB04-OD02':[], 'OD02-OD03':[] ,'OD03-SB06':[] ,'SB06-SB08':[] , 'SB08-SB07':[] , 'SB07-':[]  ,'OD02-OD04':[] ,'OD04-SB10':[] , 'SB10-SB11':[] ,'SB11-':[]  , '-OD15':[] , 'OD15-SB09':[] ,'SB09-OD02':[]  , 'SB09-OD14':[] , 'OD14-SB15':[] , 'SB15-SB14':[] , 'SB14-SB13':[] , 'SB13-':[] , 'SB14-OD10':[] , 'OD10-OD09':[] ,'OD09-OD08':[] ,'OD08-OD07':[] , 'OD07-SB12':[] , 'SB12-OD06':[] , 'OD06-OD05':[] , 'OD05-':[] , 'OD10-OD11':[] , 'OD11-OD12':[] ,'OD12-OD13':[], 'OD13-':[] , 'SB09-SE':[]})
Cf= pd.DataFrame({'Cf_OD01' :[] , 'Cf_SB01' :[] , 'Cf_SB02' :[] , 'Cf_SB03' :[] , 'Cf_SB05' :[] , 'Cf_SB04' :[] , 'Cf_OD02' :[] , 'Cf_OD03' :[] , 'Cf_SB06' :[] , 'Cf_SB08' :[] ,	'Cf_SB07' :[] , 'Cf_OD04'  :[] ,  'Cf_SB10' :[]	, 'Cf_SB11' :[] , 'Cf_OD15' :[] , 'Cf_SB09' :[] , 'Cf_OD14' :[] , 'Cf_SB15' :[] , 'Cf_SB14' :[]	, 'Cf_SB13' :[] , 'Cf_OD10' :[] , 'Cf_OD09' :[] , 'Cf_OD08' :[] , 'Cf_OD07' :[] , 'Cf_SB12' :[] , 'Cf_OD06' :[] , 'Cf_OD05 ':[] , 'Cf_OD11' :[] , 'Cf_OD12' :[] , 'Cf_OD13' :[]})
Cp = pd.DataFrame({'Cp_-OD1':[] , 'Cp_OD1-SB1':[] , 'Cp_SB01-SB02':[] ,  'Cp_SB02-SB03':[] , 'Cp_SB03-SB05':[] , 'Cp_SB05-SB04':[] , 'Cp_SB04-OD02':[] , 'Cp_OD02-OD03':[] , 'Cp_OD03-SB06':[] , 'Cp_SB06-SB08':[] , 'Cp_SB08-SB07':[] , 'Cp_SB07-':[] , 'Cp_OD02-OD04':[] , 'Cp_OD04-SB10':[] , 'Cp_SB10-SB11':[] , 'Cp_SB11-':[] , 'Cp_-OD15':[] , 'Cp_OD15-SB09':[] , 'Cp_SB09-OD02':[] , 'Cp_SB09-OD14':[] , 'Cp_OD14-SB15':[] , 'Cp_SB15-SB14':[] , 'Cp_SB14-SB13':[] , 'Cp_SB13-':[] , 'Cp_SB14-OD10':[] , 'Cp_OD10-OD09':[] , 'Cp_OD09-OD08':[] , 'Cp_OD08-OD07':[] , 'Cp_OD07-SB12':[] , 'Cp_SB12-OD06' : []  ,  'Cp_OD06-OD05':[] , 'Cp_OD05-':[] , 'Cp_OD10-OD11':[] , 'Cp_OD11-OD12':[] , 'Cp_OD12-OD13':[] , 'Cp_OD13-':[] , 'Cp_SB09-SE':[]})
Zmed = pd.DataFrame( {'OD1_R':[] , 'SB1_R':[] ,'SB02_R':[] ,'SB03_R':[] , 'SB05_R':[] , 'SB04_R':[] , 'OD02_R':[], 'OD03_R':[] ,'SB06_R':[] ,'SB08_R':[] , 'SB7_R':[] , 'OD04_R':[] ,'SB10_R':[] , 'SB11_R':[] ,'OD15_R':[] , 'SB09_R':[] ,'OD14_R':[] , 'SB15_R':[] , 'SB14_R':[] , 'SB13_R':[] , 'OD10_R':[] , 'OD09_R':[] ,'OD08_R':[] ,'OD07_R':[] , 'SB12_R':[] , 'OD06_R':[] , 'OD05_R':[] , 'OD11_R':[] , 'OD12_R':[] , 'OD13_R':[] })
R_df_float = pd.concat([Rf,Rp,Cf,Cp,Zmed])

#Dataframe que contém o dataset para os testes em HFM
df_high = pd.read_excel('C:/Users/Alexa/OneDrive/Área de Trabalho/dataset_Y_test.xlsx', sheet_name = 'atp')

#Inicio programa - Onde index é o número de vetores solução para Rf+Rp+Cf+Cp
index=2690

while index<3301:
    print('Amostra', index)
    #converte o arquivo que eu vou utilizar para txt.
    shutil.copyfile('C:/Pl42mat09/allat25khzcap.atp','C:/Pl42mat09/allat25khzcap.txt')
    arquivo_original = open('C:/Pl42mat09/allat25khzcap.txt', 'r')
    arquivo_novo = open('C:/Pl42mat09/allat25khzcap_copia.txt', 'a')

    #Lista contendo valores originais para os vetores Rf, Rp, Cf e Cp - Servirá para propósitos posicionais no arquivo original - estes valores serão trocados pelos valores carregados nos vetores de amostra
    Rf_orig = ['2.392' , '1.8808' , '5.7783', '.2221' , '1.0471', '1.0138', '4.0268' , '.8332' , '3.5515', '.6498' , '3.176', '17.598', '1.3877' , '1.2352' , '3.1659' , '2.4319' , '27.66' , '.7353' , '6.4363' , '1.1123' , '12.139' , '.342' ,'1.422' ,'20.59' , '4.457' , '45.224' , '3.8429' , '12.994' , '15.479' , '.4231'] 
    Rp_orig = ['716.8' , '113.6' , '247.7' , '216.2' , '121.9' , '170.3' , '1116.8' , '1764.4' , '1509.6' , '642.9' , '681.0' , '1433.4' , '399.8' , '508.3' , '113.6' , '2866.8' , '358.4' , '935.6' , '354.8' , '796.8' , '796.6' , '1816.2' ,'1362.1' , '2866.8' , '540.6' , '170.3' , '882.2' , '208.8' , '704.6' , '647.6' , '1929.8' , '2866.8', '1029.2' , '266.4' , '128.6' , '22.4', '1269.6']
    Cf_orig = ['.00011', '.00012', '.00013', '.00014', '.00015', '.00016', '.00017', '.00018', '.00019', '.00021', '.00022', '.00023', '.00024', '.00025', '.00026', '.00027', '.00028', '.00029', '.00031', '.00032', '.00033', '.00034', '.00035', '.00036', '.00037', '.00038', '.00039', '.00041', '.00042', '.00043']
    Cp_orig = ['1.1E-5', '1.2E-5', '1.3E-5', '1.4E-5', '1.5E-5', '1.6E-5', '1.7E-5', '1.8E-5', '1.9E-5','2.1E-5', '2.2E-5', '2.3E-5', '2.4E-5', '2.5E-5', '2.6E-5', '2.7E-5', '2.8E-5', '2.9E-5','3.1E-5','3.2E-5', '3.3E-5', '3.4E-5', '3.5E-5', '3.6E-5', '3.7E-5', '3.8E-5', '3.9E-5', '4.1E-5', '4.2E-5', '4.3E-5', '4.4E-5', '4.5E-5', '4.6E-5', '4.7E-5', '4.8E-5', '4.9E-5', '5.1E-5' ]
    R_list_orig = Rf_orig+Rp_orig+Cf_orig+Cp_orig
    
    #lista com o  tamanho de cada string Rf
    R_list_orig_len = []
    h=0
    while h < len(R_list_orig):
        R_list_orig_len.append(len(R_list_orig[h]))
        h=h+1

    #converte para uma lista com floats para novos valores de R_list
    R_list_float_new = df_high.iloc[index,:]
    R_list_float_new_fixed = []


    #Conversão de float para string - Rf+Rp+Cf+Cp
    R_list_new = []
    c=0
    lixo=[]
    for i in R_list_float_new:
        R_list_new.append((str(round(R_list_float_new[c],5))).lstrip('0'))
        c=c+1
        
    #etapa de tratamento para inserção no arquivo txt - para encaixe no atp - Rf+Rp+Cf+Cp
    R_list_new_fixed = []
    h=0
    while h < len(R_list_orig):
        l=R_list_orig_len[h]
        if l==2:
            R_list_new_fixed.append('%.2s' % ((R_list_new[h]).ljust(2, '0')))#trunca o número
        elif l==3:
            R_list_new_fixed.append('%.3s' % ((R_list_new[h]).ljust(3, '0')))#trunca o número
        elif l==4:
            R_list_new_fixed.append('%.4s' % ((R_list_new[h]).ljust(4, '0')))
        elif l==5:
            R_list_new_fixed.append('%.5s' % ((R_list_new[h]).ljust(5, '0')))
        elif l==6:
            R_list_new_fixed.append('%.6s' % ((R_list_new[h]).ljust(6, '0')))     
             
        h=h+1
        
      
    #inserção dos dados no programa - Rf, Rp, Cf e Cp.
    for linha in arquivo_original:
        i=0
        for item in R_list_orig:
            palavra = R_list_orig[i]
            palavra_nova = R_list_new_fixed[i]
            i=i+1
            if (palavra in linha) == True: #and (palavra_check in linha) == True:
                linha = linha.replace(palavra,palavra_nova)
            else:
                pass
        arquivo_novo.write(linha)

             
    arquivo_original.close()
    arquivo_novo.close()

    os.rename('C:/Pl42mat09/allat25khzcap_copia.txt','C:/Pl42mat09/allat25khzcap_copia.atp')


    #agora vamos rodar o atp
    if index == 0:
        pyautogui.PAUSE = 1
        pyautogui.press('winleft')
        pyautogui.PAUSE = 1
        pyautogui.write('cmd')
        pyautogui.press('enter')
        pyautogui.PAUSE = 1

        pyautogui.write('cd..')
        pyautogui.press('enter')
        pyautogui.PAUSE = 1

        pyautogui.write('cd..')
        pyautogui.press('enter')
        pyautogui.PAUSE = 1

        pyautogui.write('cd pl42mat09')
        pyautogui.press('enter')
        pyautogui.PAUSE = 0.5
    

    pyautogui.write('runATP allat25khzcap_copia.atp')
    pyautogui.press('enter')
    pyautogui.PAUSE =10
    pyautogui.press('enter')

    pyautogui.write('pl42mat allat25khzcap_copia.pl4')
    pyautogui.press('enter')
      
    time.sleep(0.5)

    
    mat = scipy.io.loadmat('C:/Pl42mat09/allat25khzcap_copia.mat')

    #plt.plot(mat['t'], mat['t39'])

    t = mat['t']
    t1 = mat['t1']
    t2 = mat['t2']
    t3 = mat['t3']
    t4 = mat['t4']
    t5 = mat['t5']
    t6 = mat['t6']
    t7 = mat['t7']
    t8 = mat['t8']
    t9 = mat['t9']
    t10 = mat['t10']
    t11 = mat['t11']
    t12 = mat['t12']
    t13 = mat['t13']
    t14 = mat['t14']
    t15 = mat['t15']
    t16 = mat['t16']
    t17 = mat['t17']
    t18 = mat['t18']
    t19 = mat['t19']
    t20 = mat['t20']
    t21 = mat['t21']
    t22 = mat['t22']
    t23 = mat['t23']
    t24 = mat['t24']
    t25 = mat['t25']
    t26 = mat['t26']
    t27 = mat['t27']
    t28 = mat['t28']
    t29 = mat['t29']
    t30 = mat['t30']
    tgeral=[t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,t11,t12,t13,t14,t15,t16,t17,t18,t19,t20,t21,t22,t23,t24,t25,t26,t27,t28,t29,t30]

    wtg = np.linspace(5000,305000,30)
    rf=[]   
    i=5000
    cont=0
    for item in wtg:
        rf.append(float(tgeral[cont][i]))
        i=i+10000
        cont=cont+1
        
    #armazena valores no dataframeRf_df_float
    R_list_float_new=list(R_list_float_new)
    i=0
    for item in rf:
        R_list_float_new.append(rf[i])
        i=i+1
    
    #Atualiza aqui !!!
    R_df_float.loc[index] = R_list_float_new #Atualiza o arquivo com os novos dados
    #R_df_new_fixed.loc[index] = R_list_new_fixed
    os.remove('C:/Pl42mat09/allat25khzcap_copia.atp')
    index=index+1

pyautogui.write('TASKKILL /F /IM cmd.exe /T')
pyautogui.press('enter')

#Salvar tudo em uma planilha do EXCEL  !!!!
R_df_float.to_excel('C:/Users/alexa/OneDrive/Área de Trabalho/allat25khzcap_sbn.xlsx')


#%% ESTAGIO SOMENTE PARA CALCULO DO ERRO DO HFM ---

df_hfm = pd.read_excel('C:/Users/Alexa/OneDrive/Área de Trabalho/allat25khzcap_sbn_results.xlsx')#2,5-0,7-k=var
epa1 = df_hfm.loc[:,['OD01' , 'SB01' ,'SB02' ,'SB03' , 'SB05' , 'SB04' , 'OD02', 'OD03' ,'SB06' ,'SB08' , 'SB07' , 'OD04' ,'SB10' , 'SB11' , 'OD15' , 'SB09' ,'OD14' , 'SB15' , 'SB14' , 'SB13' , 'OD10' , 'OD09' ,'OD08' ,'OD07' , 'SB12' , 'OD06' , 'OD05' , 'OD11' , 'OD12' , 'OD13' ]]
epa2 = df_hfm.loc[:,['OD1_R' , 'SB1_R' ,'SB02_R' ,'SB03_R' , 'SB05_R' , 'SB04_R' , 'OD02_R', 'OD03_R' ,'SB06_R' ,'SB08_R' , 'SB7_R' , 'OD04_R' ,'SB10_R' , 'SB11_R' ,'OD15_R' , 'SB09_R' ,'OD14_R' , 'SB15_R' , 'SB14_R' , 'SB13_R' , 'OD10_R' , 'OD09_R' ,'OD08_R' ,'OD07_R' , 'SB12_R' , 'OD06_R' , 'OD05_R' , 'OD11_R' , 'OD12_R' , 'OD13_R' ]]

from sklearn.metrics import mean_absolute_percentage_error
mape_hfm = mean_absolute_percentage_error(epa1, epa2)
erro_brut_hfm=  (epa2.values-epa1.values)/epa1.values*100
erro_hfm = abs((epa2.values-epa1.values)/epa1.values*100)

erro_hfm = pd.DataFrame(erro_hfm)

outliers_hfm= 0
l=0
while l<erro_hfm.shape[0]:
    for i in erro_hfm.iloc[l,:]:
        if i > 10: 
            outliers_hfm=outliers_hfm+1
        else:
                pass
    l=l+1

print('MP Mean Absolute Percentage Error = ', round(mape_hfm*100,3), '%') 
print('...')
print('Percentual de previsões com erro absoluto do HFM > 10% = ', round(outliers_hfm/(erro_hfm.shape[0]*erro_hfm.shape[1])*100,3), '%')


#%% Boxplot do APE das previsões por aerogerador
 

plt.boxplot(erro_hfm, labels=epa1.columns)
plt.gcf().set_size_inches(40, 20)#tamanho do grafico
plt.xlabel('Wind turbine generator', fontsize=30)
plt.ylabel('APE(%)', fontsize=30)
plt.xticks(fontsize=25)#tamanho da letra dos eixos
plt.xticks(rotation=45)
plt.yticks(fontsize=30)
plt.semilogy()
plt.grid(True)
plt.title('Boxplot of APEs between the real and HFM method ground resistances', fontsize=40)
plt.annotate("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _  _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ", xy=(10, 12), xycoords='data', xytext=(0.7, 10.3), textcoords='data', color='red')
plt.show()
plt.close()
