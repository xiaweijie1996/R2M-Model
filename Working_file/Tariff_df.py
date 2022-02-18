import os
import pandas as pd
import numpy as np
# User Input 
customer_input = input("Enter Customer number (Index): ")
P1 = r'..\Output_Data\EnergyFlux_data\con_gen_data'
R1 = P1 + str(customer_input) + '.csv'

data_df = pd.read_csv(R1)
tariff_df = pd.read_csv(r'..\Input_Data\Tarifa_demo.csv')
t1 = tariff_df['TARIFA 2.0 TD']    
t1_np = t1.to_numpy()
t1_df = pd.DataFrame(t1_np)
t2 = tariff_df['TARIFA 3.0 TD']
t2_np = t2.to_numpy()
t2_df = pd.DataFrame(t2_np)
data1_df = pd.concat([t1_df, t2_df, data_df], axis=1)

r2 = data_df["consumption"]
r2_np = r2.to_numpy()
r3 = data_df['use_power_grid1']
r3_np = r3.to_numpy()
data_df['instant_consumption'] = data_df["generation_pv"] - data_df["surplus"]
r4 = data_df['en_battery_grid1']
r5 = data_df['grid consumption']
r6 = data_df['instant_consumption']

# Tariffs_3 = np.array(['P1','P2','P3','P4','P5','P6'])
# Energy_term_3  = np.array([0.171, 0.147, 0.117, 0.097, 0.083, 0.077])
# Energy_term_3  = np.array([0.387, 0.350, 0.319, 0.293, 0.266, 0.253])
# cons_p = []
# for i in Tariffs_3:
#     cons_p6 = np.sum(r2[t2_np == i])
#     cons_p.append(cons_p6)
# cons_np = np.array(cons_p)/1000
# tot = (cons_np * Energy_term_3)/12
# print(tot)
# sum1 = np.sum(tot)
# print(sum1)