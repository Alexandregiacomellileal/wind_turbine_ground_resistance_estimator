# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 07:12:45 2023

@author: Alexandre Giacomelli Leal

"""
#######################################################################################################################

#%% Module 1 - Algorithm to automate data insertion and removal in ATP software specifically adapted for simulations of clamp-on ground meter measurement circuits.


# This analysis refers to a set of 30 wind turbines located at the São Bento do Norte Wind Complex.
# Grounding parameters range from -30% to 150% and follow a uniform distribution.


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

#Etapa de entrada de parâmetros:
    
# Numero de amostras a serem produzidas
samples_n= 50

# Range para criação de amostras para vetores Rf e Rp 
maximo = 2.5 #+150%
minimo = 0.7 #-30%

#Valores da resistividade aparente no solo
pa_f = np.array([231.1 , 173.3, 594.5 , 25.5 , 37.4 , 76.4 , 325.6 , 60.9 , 180.6 , 60.0 , 307.3 , 1990.3 , 94.8 , 76.4 , 98.9 , 184.4 , 3224.5 , 56.8 , 274.5 , 78.1 , 1119.7 , 28.2 , 110.3 , 2534.6 , 243.2 , 5120.0 , 274.1 , 5120.0 , 5120.0 , 63.2])																																					
pa_p = np.array([1280,640,2560,2560,2000,1280,10240,10240,10240,10240,5120,2560,10240,5120,640,5120,640,5120,5120,10240,10240,10240,5120,5120,10240,640,5120,1280,5120,5120,10240,5120,10240,1280,640,20,10240])


#Dataframe que contera os valores solução para os WTG
Rf_df_float = pd.DataFrame({'OD01':[] , 'SB01':[] ,'SB02':[] ,'SB03':[] , 'SB05':[] , 'SB04':[] , 'OD02':[], 'OD03':[] ,'SB06':[] ,'SB08':[] , 'SB07':[] , 'OD04':[] ,'SB10':[] , 'SB11':[] , 'OD15':[] , 'SB09':[] ,'OD14':[] , 'SB15':[] , 'SB14':[] , 'SB13':[] , 'OD10':[] , 'OD09':[] ,'OD08':[] ,'OD07':[] , 'SB12':[] , 'OD06':[] , 'OD05':[] , 'OD11':[] , 'OD12':[] , 'OD13':[] ,'-OD1':[] , 'OD1-SB1':[] ,'SB01-SB02':[] ,'SB02-SB03':[] , 'SB03-SB05':[] , 'SB05-SB04':[] , 'SB04-OD02':[], 'OD02-OD03':[] ,'OD03-SB06':[] ,'SB06-SB08':[] , 'SB08-SB07':[] , 'SB07-':[]  ,'OD02-OD04':[] ,'OD04-SB10':[] , 'SB10-SB11':[] ,'SB11-':[]  , '-OD15':[] , 'OD15-SB09':[] ,'SB09-OD02':[]  , 'SB09-OD14':[] , 'OD14-SB15':[] , 'SB15-SB14':[] , 'SB14-SB13':[] , 'SB13-':[] , 'SB14-OD10':[] , 'OD10-OD09':[] ,'OD09-OD08':[] ,'OD08-OD07':[] , 'OD07-SB12':[] , 'SB12-OD06':[] , 'OD06-OD05':[] , 'OD05-':[] , 'OD10-OD11':[] , 'OD11-OD12':[] ,'OD12-OD13':[], 'OD13-':[] , 'SB09-SE':[],'k':[], 'OD1_R':[] , 'SB1_R':[] ,'SB02_R':[] ,'SB03_R':[] , 'SB05_R':[] , 'SB04_R':[] , 'OD02_R':[], 'OD03_R':[] ,'SB06_R':[] ,'SB08_R':[] , 'SB7_R':[] , 'OD04_R':[] ,'SB10_R':[] , 'SB11_R':[] , 'OD15_R':[] , 'SB09_R':[] ,'OD14_R':[] , 'SB15_R':[] , 'SB14_R':[] , 'SB13_R':[] , 'OD10_R':[] , 'OD09_R':[] ,'OD08_R':[] ,'OD07_R':[] , 'SB12_R':[] , 'OD06_R':[] , 'OD05_R':[] , 'OD11_R':[] , 'OD12_R':[] , 'OD13_R':[] })

R_df_new_fixed = pd.DataFrame({'OD01':[] , 'SB01':[] ,'SB02':[] ,'SB03':[] , 'SB05':[] , 'SB04':[] , 'OD02':[], 'OD03':[] ,'SB06':[] ,'SB08':[] , 'SB07':[] , 'OD04':[] ,'SB10':[] , 'SB11':[] , 'OD15':[] , 'SB09':[] ,'OD14':[] , 'SB15':[] , 'SB14':[] , 'SB13':[] , 'OD10':[] , 'OD09':[] ,'OD08':[] ,'OD07':[] , 'SB12':[] , 'OD06':[] , 'OD05':[] , 'OD11':[] , 'OD12':[] , 'OD13':[] ,'-OD1':[] , 'OD1-SB1':[] ,'SB01-SB02':[] ,'SB02-SB03':[] , 'SB03-SB05':[] , 'SB05-SB04':[] , 'SB04-OD02':[], 'OD02-OD03':[] ,'OD03-SB06':[] ,'SB06-SB08':[] , 'SB08-SB07':[] , 'SB07-':[]  ,'OD02-OD04':[] ,'OD04-SB10':[] , 'SB10-SB11':[] ,'SB11-':[]  , '-OD15':[] , 'OD15-SB09':[] ,'SB09-OD02':[]  , 'SB09-OD14':[] , 'OD14-SB15':[] , 'SB15-SB14':[] , 'SB14-SB13':[] , 'SB13-':[] , 'SB14-OD10':[] , 'OD10-OD09':[] ,'OD09-OD08':[] ,'OD08-OD07':[] , 'OD07-SB12':[] , 'SB12-OD06':[] , 'OD06-OD05':[] , 'OD05-':[] , 'OD10-OD11':[] , 'OD11-OD12':[] ,'OD12-OD13':[], 'OD13-':[] , 'SB09-SE':[], 'Rm1':[], 'Rm2':[],'Rm3':[],'Rm4':[],'Rm5':[],'Rm6':[],'Rm7':[],'Rm8':[],'Rm9':[],'Rm10':[], 'Rm11':[], 'Rm12':[],'Rm13':[],'Rm14':[],'Rm15':[],'Rm16':[],'Rm17':[],'Rm18':[],'Rm19':[],'Rm20':[], 'Rm21':[], 'Rm22':[],'Rm23':[],'Rm24':[],'Rm25':[],'Rm26':[],'Rm27':[],'Rm28':[],'Rm29':[],'Rm30':[]})


Cf= pd.DataFrame({'Cf_OD01' :[] , 'Cf_SB01' :[] , 'Cf_SB02' :[] , 'Cf_SB03' :[] , 'Cf_SB05' :[] , 'Cf_SB04' :[] , 'Cf_OD02' :[] , 'Cf_OD03' :[] , 'Cf_SB06' :[] , 'Cf_SB08' :[] ,	'Cf_SB07' :[] , 'Cf_OD04'  :[] ,  'Cf_SB10' :[]	, 'Cf_SB11' :[] , 'Cf_OD15' :[] , 'Cf_SB09' :[] , 'Cf_OD14' :[] , 'Cf_SB15' :[] , 'Cf_SB14' :[]	, 'Cf_SB13' :[] , 'Cf_OD10' :[] , 'Cf_OD09' :[] , 'Cf_OD08' :[] , 'Cf_OD07' :[] , 'Cf_SB12' :[] , 'Cf_OD06' :[] , 'Cf_OD05 ':[] , 'Cf_OD11' :[] , 'Cf_OD12' :[] , 'Cf_OD13' :[]})
Cp = pd.DataFrame({'Cp_-OD1':[] , 'Cp_OD1-SB1':[] , 'Cp_SB01-SB02':[] ,  'Cp_SB02-SB03':[] , 'Cp_SB03-SB05':[] , 'Cp_SB05-SB04':[] , 'Cp_SB04-OD02':[] , 'Cp_OD02-OD03':[] , 'Cp_OD03-SB06':[] , 'Cp_SB06-SB08':[] , 'Cp_SB08-SB07':[] , 'Cp_SB07-':[] , 'Cp_OD02-OD04':[] , 'Cp_OD04-SB10':[] , 'Cp_SB10-SB11':[] , 'Cp_SB11-':[] , 'Cp_-OD15':[] , 'Cp_OD15-SB09':[] , 'Cp_SB09-OD02':[] , 'Cp_SB09-OD14':[] , 'Cp_OD14-SB15':[] , 'Cp_SB15-SB14':[] , 'Cp_SB14-SB13':[] , 'Cp_SB13-':[] , 'Cp_SB14-OD10':[] , 'Cp_OD10-OD09':[] , 'Cp_OD09-OD08':[] , 'Cp_OD08-OD07':[] , 'Cp_OD07-SB12':[] , 'Cp_SB12-OD06' : []  ,  'Cp_OD06-OD05':[] , 'Cp_OD05-':[] , 'Cp_OD10-OD11':[] , 'Cp_OD11-OD12':[] , 'Cp_OD12-OD13':[] , 'Cp_OD13-':[] , 'Cp_SB09-SE':[]})
Cm= pd.DataFrame({'Cm_OD01' :[] , 'Cm_SB01' :[] , 'Cm_SB02' :[] , 'Cm_SB03' :[] , 'Cm_SB05' :[] , 'Cm_SB04' :[] , 'Cm_OD02' :[] , 'Cm_OD03' :[] , 'Cm_SB06' :[] , 'Cm_SB08' :[] ,	'Cm_SB07' :[] , 'Cm_OD04'  :[] ,  'Cm_SB10' :[]	, 'Cm_SB11' :[] , 'Cm_OD15' :[] , 'Cm_SB09' :[] , 'Cm_OD14' :[] , 'Cm_SB15' :[] , 'Cm_SB14' :[]	, 'Cm_SB13' :[] , 'Cm_OD10' :[] , 'Cm_OD09' :[] , 'Cm_OD08' :[] , 'Cm_OD07' :[] , 'Cm_SB12' :[] , 'Cm_OD06' :[] , 'Cm_OD05 ':[] , 'Cm_OD11' :[] , 'Cm_OD12' :[] , 'Cm_OD13' :[]})

R_df_new_fixed = pd.concat([R_df_new_fixed,Cf,Cp,Cm])


index_rf=0
while index_rf<(samples_n):
    k=random.uniform(0.3, 1)
    print('Amostra', index_rf+1, 'de', samples_n)
    #converte o arquivo que eu vou utilizar para txt.
    shutil.copyfile('C:/Pl42mat09/sbnallmutuacap.atp','C:/Pl42mat09/sbnallmutuacap.txt')
    arquivo_original = open('C:/Pl42mat09/sbnallmutuacap.txt', 'r')
    arquivo_novo = open('C:/Pl42mat09/sbnallmutuacap_copia.txt', 'a')

    #digitar aqui os Rf e Rp e Rm originais de projeto para propósito posicional
    Rf_list_orig = ['2.392' , '1.8808' , '5.7783', '.2221' , '1.0471', '1.0138', '4.0268' , '.8332' , '3.5515', '.6498' , '3.176', '17.598', '1.3877' , '1.2352' , '3.1659' , '2.4319' , '27.66' , '.7353' , '6.4363' , '1.1123' , '12.139' , '.342' ,'1.422' ,'20.59' , '4.457' , '45.224' , '3.8429' , '12.994' , '15.479' , '.4231']
    Rp_list_orig = ['71.68' , '11.36' , '24.77' , '21.62' , '12.19' , '17.03' , '111.68' , '176.44' , '150.96' , '64.29' , '68.1' , '143.34' , '39.98' , '50.83' , '11.36' , '286.68' , '35.84' , '93.56' , '35.48' , '79.68' , '79.66' , '181.62' ,'136.21' , '286.68' , '54.06' , '17.03' , '88.22' , '20.88' , '70.46' , '64.76' , '192.98' , '286.68', '102.92' , '26.64' , '12.86' , '2.24', '126.96' ] 
    Rm_list_orig = ['10001.','10002.','10003.','10004.','10005.','10006.','10007.','10008.','10009.','10010.','10011.','10012.','10013.','10014.','10015.','10016.','10017.','10018.','10019.','10020.','10021.','10022.','10023.','10024.','10025.','10026.','10027.','10028.','10029.','10030.']
    Cf_list_orig = ['.00011', '.00012', '.00013', '.00014', '.00015', '.00016', '.00017', '.00018', '.00019', '.00021', '.00022', '.00023', '.00024', '.00025', '.00026', '.00027', '.00028', '.00029', '.00031', '.00032', '.00033', '.00034', '.00035', '.00036', '.00037', '.00038', '.00039', '.00041', '.00042', '.00043']
    Cp_list_orig = ['1.1E-5', '1.2E-5', '1.3E-5', '1.4E-5', '1.5E-5', '1.6E-5', '1.7E-5', '1.8E-5', '1.9E-5','2.1E-5', '2.2E-5', '2.3E-5', '2.4E-5', '2.5E-5', '2.6E-5', '2.7E-5', '2.8E-5', '2.9E-5','3.1E-5','3.2E-5', '3.3E-5', '3.4E-5', '3.5E-5', '3.6E-5', '3.7E-5', '3.8E-5', '3.9E-5', '4.1E-5', '4.2E-5', '4.3E-5', '4.4E-5', '4.5E-5', '4.6E-5', '4.7E-5', '4.8E-5', '4.9E-5', '5.1E-5' ]
    Cm_list_orig = ['1.1E-6', '1.2E-6', '1.3E-6', '1.4E-6', '1.5E-6', '1.6E-6', '1.7E-6', '1.8E-6', '1.9E-6','2.1E-5', '2.2E-6', '2.3E-6', '2.4E-6', '2.5E-6', '2.6E-6', '2.7E-6', '2.8E-6', '2.9E-6','3.1E-6','3.2E-6', '3.3E-6', '3.4E-6', '3.5E-6', '3.6E-6', '3.7E-6', '3.8E-6', '3.9E-6', '4.1E-6', '4.2E-6', '4.3E-6']
    
    
    #lista com o  tamanho de cada string Rf
    Rf_list_orig_len = []
    h=0
    while h < len(Rf_list_orig):
        Rf_list_orig_len.append(len(Rf_list_orig[h]))
        h=h+1
        
    #lista com o  tamanho de cada string Cf
    Cf_list_orig_len = []
    h=0
    while h < len(Cf_list_orig):
        Cf_list_orig_len.append(len(Cf_list_orig[h]))
        h=h+1   



    #converte para uma lista com floats para encontrar valores aleatorios para as novas var Rf
    n=0
    lixo=[]
    Rf_list_float_orig = []
    for i in Rf_list_orig:
        Rf_list_float_orig.append(float(Rf_list_orig[n]))
        n=n+1
    Rf_list_float_new = list(map(lambda u: random.uniform(maximo*u, minimo*u),Rf_list_float_orig))
    Rf_list_float_new_fixed = []
    
    ######## NOVO -- CALCULA CF POR RF
    Cf_list_float_new = pa_f/Rf_list_float_new
    Cf_list_float_new = Cf_list_float_new *9/(36*3.141592653589793*10**9)*10**6
    
    
    
    
    #Conversão de float para string - Rf

    Rf_list_new = []
    c=0
    lixo=[]
    for i in Rf_list_float_new:
        Rf_list_new.append((str(round(Rf_list_float_new[c],4))).lstrip('0'))
        c=c+1
        
    #etapa de tratamento para inserção no arquivo txt - para encaixe no atp - Rf
    Rf_list_new_fixed = []
    h=0
    while h < len(Rf_list_orig):
        l=Rf_list_orig_len[h]
        if l==2:
            Rf_list_new_fixed.append('%.2s' % ((Rf_list_new[h]).ljust(2, '0')))#trunca o número
        elif l==3:
            Rf_list_new_fixed.append('%.3s' % ((Rf_list_new[h]).ljust(3, '0')))#trunca o número
        elif l==4:
            Rf_list_new_fixed.append('%.4s' % ((Rf_list_new[h]).ljust(4, '0')))
        elif l==5:
            Rf_list_new_fixed.append('%.5s' % ((Rf_list_new[h]).ljust(5, '0')))
        elif l==6:
            Rf_list_new_fixed.append('%.6s' % ((Rf_list_new[h]).ljust(6, '0')))     
             
        h=h+1
        
        
       
    #Conversão de float para string - Cf
    
    Cf_list_new = []
    c=0
    lixo=[]
    for i in Cf_list_float_new:
        Cf_list_new.append((str(round(Cf_list_float_new[c],4))).lstrip('0'))
        c=c+1
        
    #etapa de tratamento para inserção no arquivo txt - para encaixe no atp - Rf
    Cf_list_new_fixed = []
    h=0
    while h < len(Rf_list_orig):
        l=Rf_list_orig_len[h]
        if l==2:
            Cf_list_new_fixed.append('%.2s' % ((Cf_list_new[h]).ljust(2, '0')))#trunca o número
        elif l==3:
            Cf_list_new_fixed.append('%.3s' % ((Cf_list_new[h]).ljust(3, '0')))#trunca o número
        elif l==4:
            Cf_list_new_fixed.append('%.4s' % ((Cf_list_new[h]).ljust(4, '0')))
        elif l==5:
            Cf_list_new_fixed.append('%.5s' % ((Cf_list_new[h]).ljust(5, '0')))
        elif l==6:
            Cf_list_new_fixed.append('%.6s' % ((Cf_list_new[h]).ljust(6, '0')))     
             
        h=h+1
        
        
        #######################################
        
        
            
    
       
    #lista com o  tamanho de cada  string - Rp
    Rp_list_orig_len = []
    h=0
    while h < len(Rp_list_orig):
        Rp_list_orig_len.append(len(Rp_list_orig[h]))
        h=h+1
    
    #lista com o  tamanho de cada  string - Cp
    Cp_list_orig_len = []
    h=0
    while h < len(Cp_list_orig):
        Cp_list_orig_len.append(len(Cp_list_orig[h]))
        h=h+1        
    

    #converte para uma lista com floats para encontrar valores aleatorios para as novas var - Rp
    n=0
    lixo=[]
    Rp_list_float_orig = []
    for i in Rp_list_orig:
        Rp_list_float_orig.append(float(Rp_list_orig[n]))
        n=n+1
    Rp_list_float_new = list(map(lambda u: random.uniform(maximo*u, minimo*u),Rp_list_float_orig))
    Rp_list_float_new_fixed = []
    
    
    #### NOVO  -- CALCULO DE Cp
    Cp_list_float_new = pa_p/Rp_list_float_new
    Cp_list_float_new = Cp_list_float_new *9/(36*3.141592653589793*10**9)*10**6


    #Conversão de float para string - Rp

    Rp_list_new = []
    c=0
    lixo=[]
    for i in Rp_list_float_new:
        Rp_list_new.append((str(round(Rp_list_float_new[c],4))).lstrip('0'))
        c=c+1
        
    #etapa de tratamento para inserção no arquivo txt - para encaixe no atp - Rp
    Rp_list_new_fixed = []
    h=0
    while h < len(Rp_list_orig):
        l=Rp_list_orig_len[h]
        if l==2:
            Rp_list_new_fixed.append('%.2s' % ((Rp_list_new[h]).ljust(2, '0')))#trunca o número
        elif l==3:
            Rp_list_new_fixed.append('%.3s' % ((Rp_list_new[h]).ljust(3, '0')))#trunca o número
        elif l==4:
            Rp_list_new_fixed.append('%.4s' % ((Rp_list_new[h]).ljust(4, '0')))
        elif l==5:
            Rp_list_new_fixed.append('%.5s' % ((Rp_list_new[h]).ljust(5, '0')))
        elif l==6:
            Rp_list_new_fixed.append('%.6s' % ((Rp_list_new[h]).ljust(6, '0')))     
             
        h=h+1
        
        
    ###########################
     
    #Conversão de float para string - Cp
    Cp_list_new = []
    c=0
    lixo=[]
    for i in Cp_list_float_new:
        Cp_list_new.append((str(round(Cp_list_float_new[c],4))).lstrip('0'))
        c=c+1
         
    #etapa de tratamento para inserção no arquivo txt - para encaixe no atp - Cp
    Cp_list_new_fixed = []
    h=0
    while h < len(Cp_list_orig):
        l=Cp_list_orig_len[h]
        if l==2:
            Cp_list_new_fixed.append('%.2s' % ((Cp_list_new[h]).ljust(2, '0')))#trunca o número
        elif l==3:
            Cp_list_new_fixed.append('%.3s' % ((Cp_list_new[h]).ljust(3, '0')))#trunca o número
        elif l==4:
            Cp_list_new_fixed.append('%.4s' % ((Cp_list_new[h]).ljust(4, '0')))
        elif l==5:
            Cp_list_new_fixed.append('%.5s' % ((Cp_list_new[h]).ljust(5, '0')))
        elif l==6:
            Cp_list_new_fixed.append('%.6s' % ((Cp_list_new[h]).ljust(6, '0')))     
              
        h=h+1
        
   # para cálculo da resistência mútua entre as turninas e os eletrodos horizontais.
    
    #lista com o  tamanho de cada string Rm
    Rm_list_orig_len = []
    h=0
    while h < len(Rm_list_orig):
        Rm_list_orig_len.append(len(Rm_list_orig[h]))
        h=h+1
        
    #lista com o  tamanho de cada string Cm
    Cm_list_orig_len = []
    h=0
    while h < len(Cm_list_orig):
        Cm_list_orig_len.append(len(Cm_list_orig[h]))
        h=h+1
    
    #etapa de calculo da resistência mútua entre a turbinas e os eletrodos horizontais 
    Rm_list_float_new = []
    Rm_list_float_new.append((1/(1/Rp_list_float_new[0]+1/Rp_list_float_new[1])+Rf_list_float_new[0])*k/(1-k))
    Rm_list_float_new.append((1/(1/Rp_list_float_new[1]+1/Rp_list_float_new[2])+Rf_list_float_new[1])*k/(1-k))
    Rm_list_float_new.append((1/(1/Rp_list_float_new[2]+1/Rp_list_float_new[3])+Rf_list_float_new[2])*k/(1-k))
    Rm_list_float_new.append((1/(1/Rp_list_float_new[3]+1/Rp_list_float_new[4])+Rf_list_float_new[3])*k/(1-k))
    Rm_list_float_new.append((1/(1/Rp_list_float_new[4]+1/Rp_list_float_new[5])+Rf_list_float_new[4])*k/(1-k))
    Rm_list_float_new.append((1/(1/Rp_list_float_new[5]+1/Rp_list_float_new[6])+Rf_list_float_new[5])*k/(1-k))
    Rm_list_float_new.append((1/(1/Rp_list_float_new[6]+1/Rp_list_float_new[7]+1/Rp_list_float_new[12]+1/Rp_list_float_new[16])+Rf_list_float_new[6])*k/(1-k))
    Rm_list_float_new.append((1/(1/Rp_list_float_new[7]+1/Rp_list_float_new[8])+Rf_list_float_new[7])*k/(1-k))
    Rm_list_float_new.append((1/(1/Rp_list_float_new[8]+1/Rp_list_float_new[9])+Rf_list_float_new[8])*k/(1-k))
    Rm_list_float_new.append((1/(1/Rp_list_float_new[9]+1/Rp_list_float_new[10])+Rf_list_float_new[9])*k/(1-k))
    Rm_list_float_new.append((1/(1/Rp_list_float_new[10]+1/Rp_list_float_new[11])+Rf_list_float_new[10])*k/(1-k))
    Rm_list_float_new.append((1/(1/Rp_list_float_new[12]+1/Rp_list_float_new[13])+Rf_list_float_new[11])*k/(1-k))
    Rm_list_float_new.append((1/(1/Rp_list_float_new[13]+1/Rp_list_float_new[14])+Rf_list_float_new[12])*k/(1-k))
    Rm_list_float_new.append((1/(1/Rp_list_float_new[14]+1/Rp_list_float_new[15])+Rf_list_float_new[13])*k/(1-k))
    Rm_list_float_new.append((1/(1/Rp_list_float_new[16]+1/Rp_list_float_new[17])+Rf_list_float_new[14])*k/(1-k))
    Rm_list_float_new.append((1/(1/Rp_list_float_new[17]+1/Rp_list_float_new[18])+Rf_list_float_new[15])*k/(1-k))
    Rm_list_float_new.append((1/(1/Rp_list_float_new[19]+1/Rp_list_float_new[20])+Rf_list_float_new[16])*k/(1-k))
    Rm_list_float_new.append((1/(1/Rp_list_float_new[20]+1/Rp_list_float_new[21])+Rf_list_float_new[17])*k/(1-k))
    Rm_list_float_new.append((1/(1/Rp_list_float_new[21]+1/Rp_list_float_new[22]+1/Rp_list_float_new[24]+1/Rp_list_float_new[16])+Rf_list_float_new[18])*k/(1-k))
    Rm_list_float_new.append((1/(1/Rp_list_float_new[22]+1/Rp_list_float_new[23])+Rf_list_float_new[19])*k/(1-k))
    Rm_list_float_new.append((1/(1/Rp_list_float_new[24]+1/Rp_list_float_new[25]+1/Rp_list_float_new[32]+1/Rp_list_float_new[16])+Rf_list_float_new[20])*k/(1-k))
    Rm_list_float_new.append((1/(1/Rp_list_float_new[25]+1/Rp_list_float_new[26])+Rf_list_float_new[21])*k/(1-k))
    Rm_list_float_new.append((1/(1/Rp_list_float_new[26]+1/Rp_list_float_new[27])+Rf_list_float_new[22])*k/(1-k))
    Rm_list_float_new.append((1/(1/Rp_list_float_new[27]+1/Rp_list_float_new[28])+Rf_list_float_new[23])*k/(1-k))
    Rm_list_float_new.append((1/(1/Rp_list_float_new[28]+1/Rp_list_float_new[29])+Rf_list_float_new[24])*k/(1-k))
    Rm_list_float_new.append((1/(1/Rp_list_float_new[29]+1/Rp_list_float_new[30])+Rf_list_float_new[25])*k/(1-k))
    Rm_list_float_new.append((1/(1/Rp_list_float_new[30]+1/Rp_list_float_new[31])+Rf_list_float_new[26])*k/(1-k))
    Rm_list_float_new.append((1/(1/Rp_list_float_new[32]+1/Rp_list_float_new[33])+Rf_list_float_new[27])*k/(1-k))
    Rm_list_float_new.append((1/(1/Rp_list_float_new[33]+1/Rp_list_float_new[34])+Rf_list_float_new[28])*k/(1-k))
    Rm_list_float_new.append((1/(1/Rp_list_float_new[34]+1/Rp_list_float_new[35])+Rf_list_float_new[29])*k/(1-k))


    #etapa de calculo da capacitância mútua entre a turbinas e os eletrodos horizontais 
    Cm_list_float_new = []
    Cm_list_float_new.append(1/(1/(Cp_list_float_new[0]+Cp_list_float_new[1])+1/(Cf_list_float_new[0]))*(1-k)/k)
    Cm_list_float_new.append(1/(1/(Cp_list_float_new[1]+Cp_list_float_new[2])+1/(Cf_list_float_new[1]))*(1-k)/k)
    Cm_list_float_new.append(1/(1/(Cp_list_float_new[2]+Cp_list_float_new[3])+1/(Cf_list_float_new[2]))*(1-k)/k)
    Cm_list_float_new.append(1/(1/(Cp_list_float_new[3]+Cp_list_float_new[4])+1/(Cf_list_float_new[3]))*(1-k)/k)
    Cm_list_float_new.append(1/(1/(Cp_list_float_new[4]+Cp_list_float_new[5])+1/(Cf_list_float_new[4]))*(1-k)/k)
    Cm_list_float_new.append(1/(1/(Cp_list_float_new[5]+Cp_list_float_new[6])+1/(Cf_list_float_new[5]))*(1-k)/k)
    Cm_list_float_new.append(1/(1/(Cp_list_float_new[6]+Cp_list_float_new[7]+Cp_list_float_new[12]+Cp_list_float_new[16])+1/Cf_list_float_new[6])*(1-k)/k)
    Cm_list_float_new.append(1/(1/(Cp_list_float_new[7]+Cp_list_float_new[8])+1/(Cf_list_float_new[7]))*(1-k)/k)
    Cm_list_float_new.append(1/(1/(Cp_list_float_new[8]+Cp_list_float_new[9])+1/(Cf_list_float_new[8]))*(1-k)/k)
    Cm_list_float_new.append(1/(1/(Cp_list_float_new[9]+Cp_list_float_new[10])+1/(Cf_list_float_new[9]))*(1-k)/k)
    Cm_list_float_new.append(1/(1/(Cp_list_float_new[10]+Cp_list_float_new[11])+1/(Cf_list_float_new[10]))*(1-k)/k)
    Cm_list_float_new.append(1/(1/(Cp_list_float_new[12]+Cp_list_float_new[13])+1/(Cf_list_float_new[11]))*(1-k)/k)
    Cm_list_float_new.append(1/(1/(Cp_list_float_new[13]+Cp_list_float_new[14])+1/(Cf_list_float_new[12]))*(1-k)/k)
    Cm_list_float_new.append(1/(1/(Cp_list_float_new[14]+Cp_list_float_new[15])+1/(Cf_list_float_new[13]))*(1-k)/k)
    Cm_list_float_new.append(1/(1/(Cp_list_float_new[16]+Cp_list_float_new[17])+1/(Cf_list_float_new[14]))*(1-k)/k)
    Cm_list_float_new.append(1/(1/(Cp_list_float_new[17]+Cp_list_float_new[18])+1/(Cf_list_float_new[15]))*(1-k)/k)
    Cm_list_float_new.append(1/(1/(Cp_list_float_new[19]+Cp_list_float_new[20])+1/(Cf_list_float_new[16]))*(1-k)/k)
    Cm_list_float_new.append(1/(1/(Cp_list_float_new[20]+Cp_list_float_new[21])+1/(Cf_list_float_new[17]))*(1-k)/k)
    Cm_list_float_new.append(1/(1/(Cp_list_float_new[21]+Cp_list_float_new[22]+Cp_list_float_new[24]+Cp_list_float_new[16])+1/Cf_list_float_new[18])*(1-k)/k)
    Cm_list_float_new.append(1/(1/(Cp_list_float_new[22]+Cp_list_float_new[23])+1/(Cf_list_float_new[19]))*(1-k)/k)
    Cm_list_float_new.append(1/(1/(Cp_list_float_new[24]+Cp_list_float_new[25]+Cp_list_float_new[32]+Cp_list_float_new[16])+1/Cf_list_float_new[20])*(1-k)/k)
    Cm_list_float_new.append(1/(1/(Cp_list_float_new[25]+Cp_list_float_new[26])+1/(Cf_list_float_new[21]))*(1-k)/k)
    Cm_list_float_new.append(1/(1/(Cp_list_float_new[26]+Cp_list_float_new[27])+1/(Cf_list_float_new[22]))*(1-k)/k)
    Cm_list_float_new.append(1/(1/(Cp_list_float_new[27]+Cp_list_float_new[28])+1/(Cf_list_float_new[23]))*(1-k)/k)
    Cm_list_float_new.append(1/(1/(Cp_list_float_new[28]+Cp_list_float_new[29])+1/(Cf_list_float_new[24]))*(1-k)/k)
    Cm_list_float_new.append(1/(1/(Cp_list_float_new[29]+Cp_list_float_new[20])+1/(Cf_list_float_new[25]))*(1-k)/k)
    Cm_list_float_new.append(1/(1/(Cp_list_float_new[30]+Cp_list_float_new[31])+1/(Cf_list_float_new[26]))*(1-k)/k)
    Cm_list_float_new.append(1/(1/(Cp_list_float_new[32]+Cp_list_float_new[33])+1/(Cf_list_float_new[27]))*(1-k)/k)
    Cm_list_float_new.append(1/(1/(Cp_list_float_new[33]+Cp_list_float_new[34])+1/(Cf_list_float_new[28]))*(1-k)/k)
    Cm_list_float_new.append(1/(1/(Cp_list_float_new[34]+Cp_list_float_new[35])+1/(Cf_list_float_new[29]))*(1-k)/k)
    



    #Conversão de float para string - Rm

    Rm_list_new = []
    c=0
    lixo=[]
    for i in Rm_list_float_new:
        Rm_list_new.append((str(round(Rm_list_float_new[c],4))).lstrip('0'))
        c=c+1
        
    #etapa de tratamento para inserção no arquivo txt - para encaixe no atp - Rp
    Rm_list_new_fixed = []
    h=0
    while h < len(Rm_list_orig):
        l=Rm_list_orig_len[h]
        if l==2:
            Rm_list_new_fixed.append('%.2s' % ((Rm_list_new[h]).ljust(2, '0')))#trunca o número
        elif l==3:
            Rm_list_new_fixed.append('%.3s' % ((Rm_list_new[h]).ljust(3, '0')))#trunca o número
        elif l==4:
            Rm_list_new_fixed.append('%.4s' % ((Rm_list_new[h]).ljust(4, '0')))
        elif l==5:
            Rm_list_new_fixed.append('%.5s' % ((Rm_list_new[h]).ljust(5, '0')))
        elif l==6:
            Rm_list_new_fixed.append('%.6s' % ((Rm_list_new[h]).ljust(6, '0')))     
             
        h=h+1
        
        
    #Conversão de float para string - Cm

    Cm_list_new = []
    c=0
    lixo=[]
    for i in Cm_list_float_new:
        Cm_list_new.append((str(round(Cm_list_float_new[c],4))).lstrip('0'))
        c=c+1
        
    #etapa de tratamento para inserção no arquivo txt - para encaixe no atp - Cm
    Cm_list_new_fixed = []
    h=0
    while h < len(Rm_list_orig):
        l=Cm_list_orig_len[h]
        if l==2:
            Cm_list_new_fixed.append('%.2s' % ((Cm_list_new[h]).ljust(2, '0')))#trunca o número
        elif l==3:
            Cm_list_new_fixed.append('%.3s' % ((Cm_list_new[h]).ljust(3, '0')))#trunca o número
        elif l==4:
            Cm_list_new_fixed.append('%.4s' % ((Cm_list_new[h]).ljust(4, '0')))
        elif l==5:
            Cm_list_new_fixed.append('%.5s' % ((Cm_list_new[h]).ljust(5, '0')))
        elif l==6:
            Cm_list_new_fixed.append('%.6s' % ((Cm_list_new[h]).ljust(6, '0')))     
             
        h=h+1       
        
        
        ###############################
    
    #inserção dos dados no programa - Rf e Rp e Rm e Cf e Cp e Cm
    R_list_orig = Rf_list_orig + Rp_list_orig + Rm_list_orig + Cf_list_orig + Cp_list_orig + Cm_list_orig
    R_list_new_fixed = Rf_list_new_fixed + Rp_list_new_fixed + Rm_list_new_fixed + Cf_list_new_fixed + Cp_list_new_fixed + Cm_list_new_fixed

    
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

    os.rename('C:/Pl42mat09/sbnallmutuacap_copia.txt','C:/Pl42mat09/sbnallmutuacap_copia.atp')


    #agora vamos rodar o atp
    if index_rf == 0:
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
    

    pyautogui.write('runATP sbnallmutuacap_copia.atp')
    pyautogui.press('enter')
    pyautogui.PAUSE = 3
    pyautogui.press('enter')

    pyautogui.write('pl42mat sbnallmutuacap_copia.pl4')
    pyautogui.press('enter')
      
    time.sleep(0.5)

    
    mat = scipy.io.loadmat('C:/Pl42mat09/sbnallmutuacap_copia.mat')

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
        
    #armazena valor atual de k dentro do vetor Rp
    Rp_list_float_new.append(k) 
    
    #armazena valores no dataframeRf_df_float
    i=0
    for item in rf:
        Rp_list_float_new.append(rf[i])
        i=i+1
    
           
    Rf_df_float.loc[index_rf] = Rf_list_float_new + Rp_list_float_new
    
    R_df_new_fixed.loc[index_rf] = R_list_new_fixed
         
    os.remove('C:/Pl42mat09/sbnallmutuacap_copia.atp')

     
    index_rf=index_rf+1

pyautogui.write('TASKKILL /F /IM cmd.exe /T')
pyautogui.press('enter')

#Dataframe principal
Rf_df_float.to_excel('C:/Users/alexa/OneDrive/Área de Trabalho/df_current_sbn.xlsx')

R_df_new_fixed.to_excel('C:/Users/alexa/OneDrive/Área de Trabalho/R_df_new_fixed.xlsx')




#######################################################################################################################



#%% Module 2 - Algorithm that incorporates machine learning techniques to predict turbine grounding resistance based on clamp-on meter readings, utilizing data preprocessing, model training, and evaluation metrics to optimize predictive accuracy
#Additionally, it generates a CGM and a Proposed Solution boxplot error graph in the SBC.

# This analysis refers to a set of 30 wind turbines located at the São Bento do Norte Wind Complex.
# Grounding parameters range from -30% to 150% and follow a uniform distribution.
# Generate a boxplot illustrating prediction errors for each Wind Turbine Generator (WTG) and calculate the mean absolute error using various machine learning algorithms.

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
    #modelo = LGBMRegressor(n_estimators=177, learning_rate=0.062)
    #modelo = LinearRegression()
    #modelo = Ridge(alpha=0.001)
    #modelo = Lasso(alpha=0.001)
    #modelo = DecisionTreeRegressor(min_samples_split=5, max_depth=3, criterion='mse')
    #modelo = RandomForestRegressor(min_samples_split=5, max_depth=11, min_samples_leaf=4)
    modelo = SVR(kernel='rbf', degree=2, gamma='auto', C=60, epsilon=0.01)
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

# Contando os outliers > 10%

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

# CGM ERRORS - Erros da aplicação direta do método do alicate terrometro

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

#  Boxplot do APE das previsões por aerogerador
 
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


# Boxplot do APE das previsões por aerogerador PROPOSED SOLUTION

ERRO.columns = Y.columns
desired_order = ['SB03', 'OD09', 'OD13','SB08','SB15',	'OD03'	,'SB04','SB05'	,'SB13'	,'SB11',	'SB10'	,'OD08', 'SB01'	,'OD01',	'SB09',	'OD15'	,'SB07',	'SB06'	,'OD05'	,'OD02'	,'SB12'	,'SB02'	,'SB14',	'OD10', 'OD11',	'OD12',	'OD04',	'OD07'	,'OD14'	,'OD06']
ERRO = ERRO[desired_order]

#ERRO.columns = ['SB03', 'OD09', 'OD13','SB08','SB15',	'OD03'	,'SB04','SB05'	,'SB13'	,'SB11',	'SB10'	,'OD08', 'SB01'	,'OD01',	'SB09',	'OD15'	,'SB07',	'SB06'	,'OD05'	,'OD02'	,'SB12'	,'SB02'	,'SB14',	'OD10', 'OD11',	'OD12',	'OD04',	'OD07'	,'OD14'	,'OD06']

# Set the size of the circles for outliers (adjust as needed)
flierprops = dict(markerfacecolor='gray', markersize=2, linestyle='none', marker='o', alpha=0.7)

plt.boxplot(ERRO[desired_order], flierprops=flierprops, labels=ERRO.columns )
plt.gcf().set_size_inches(15, 8)  # Adjust the size of the plot
plt.xlabel('Wind Turbine Generator', fontsize=16)
plt.ylabel('Absolute Percentage Error (%)', fontsize=16)
plt.xticks(rotation=45, fontsize=12)  # Rotate and resize x-axis labels
plt.yticks(fontsize=12)
plt.semilogy()
plt.grid(True)
#plt.title('Boxplot of APEs between Real and LGBM Estimated Ground Resistances', fontsize=18)


plt.show()
plt.close()

# Boxplot do APE das previsões por aerogerador CGM

ERRO_cgm.columns = Y.columns
desired_order = ['SB03', 'OD09', 'OD13','SB08','SB15',	'OD03'	,'SB04','SB05'	,'SB13'	,'SB11',	'SB10'	,'OD08', 'SB01'	,'OD01',	'SB09',	'OD15'	,'SB07',	'SB06'	,'OD05'	,'OD02'	,'SB12'	,'SB02'	,'SB14',	'OD10', 'OD11',	'OD12',	'OD04',	'OD07'	,'OD14'	,'OD06']
ERRO_cgm = ERRO_cgm[desired_order]

#ERRO.columns = ['SB03', 'OD09', 'OD13','SB08','SB15',	'OD03'	,'SB04','SB05'	,'SB13'	,'SB11',	'SB10'	,'OD08', 'SB01'	,'OD01',	'SB09',	'OD15'	,'SB07',	'SB06'	,'OD05'	,'OD02'	,'SB12'	,'SB02'	,'SB14',	'OD10', 'OD11',	'OD12',	'OD04',	'OD07'	,'OD14'	,'OD06']

# Set the size of the circles for outliers (adjust as needed)
flierprops = dict(markerfacecolor='gray', markersize=1, linestyle='none', marker='o', alpha=0.7)

plt.boxplot(ERRO_cgm[desired_order], flierprops=flierprops, labels=ERRO_cgm.columns )
plt.gcf().set_size_inches(15, 8)  # Adjust the size of the plot
plt.xlabel('Wind Turbine Generator', fontsize=16)
plt.ylabel('Absolute Percentage Error (%)', fontsize=16)
plt.xticks(rotation=45, fontsize=12)  # Rotate and resize x-axis labels
plt.yticks(fontsize=12)
plt.semilogy()
plt.grid(True)
#plt.title('Boxplot of APEs between Real and LGBM Estimated Ground Resistances', fontsize=18)


plt.show()
plt.close()


#######################################################################################################################


#%% Module 3 - Algorithm to automate data insertion and removal in ATP software specifically adapted for simulations of high-frequency ground meter measurement circuits.
#Additionally, it generates an HFM boxplot error graph in the SBC.

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

#ESTAGIO SOMENTE PARA CALCULO DO ERRO DO HFM ---

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

# Boxplot do APE das previsões por aerogerador
 

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

#Boxplot do APE das previsões por aerogerador

erro_hfm.columns = epa1.columns
desired_order = ['SB03', 'OD09', 'OD13','SB08','SB15',	'OD03'	,'SB04','SB05'	,'SB13'	,'SB11',	'SB10'	,'OD08', 'SB01'	,'OD01',	'SB09',	'OD15'	,'SB07',	'SB06'	,'OD05'	,'OD02'	,'SB12'	,'SB02'	,'SB14',	'OD10', 'OD11',	'OD12',	'OD04',	'OD07'	,'OD14'	,'OD06']
erro_hfm = erro_hfm[desired_order]

#ERRO.columns = ['SB03', 'OD09', 'OD13','SB08','SB15',	'OD03'	,'SB04','SB05'	,'SB13'	,'SB11',	'SB10'	,'OD08', 'SB01'	,'OD01',	'SB09',	'OD15'	,'SB07',	'SB06'	,'OD05'	,'OD02'	,'SB12'	,'SB02'	,'SB14',	'OD10', 'OD11',	'OD12',	'OD04',	'OD07'	,'OD14'	,'OD06']

# Set the size of the circles for outliers (adjust as needed)
flierprops = dict(markerfacecolor='gray', markersize=2, linestyle='none', marker='o', alpha=0.7)

plt.boxplot(erro_hfm[desired_order], flierprops=flierprops, labels=erro_hfm.columns )
plt.gcf().set_size_inches(15, 8)  # Adjust the size of the plot
plt.xlabel('Wind Turbine Generator', fontsize=16)
plt.ylabel('Absolute Percentage Error (%)', fontsize=16)
plt.xticks(rotation=45, fontsize=12)  # Rotate and resize x-axis labels
plt.yticks(fontsize=12)
plt.semilogy()
plt.grid(True)
#plt.title('Boxplot of APEs between Real and LGBM Estimated Ground Resistances', fontsize=18)


plt.show()
plt.close()
