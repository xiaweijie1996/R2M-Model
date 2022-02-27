from Tariff_df import *
import pandas as pd
import numpy as np
import os

user = input("which type of customer are you: ",  )  #This is user input
if user == "Business":
    Tariffs_3      = np.array(['P1','P2','P3','P4','P5','P6'])  # Tariff structure in Spain
    Energy_term_3  = np.array([0.387, 0.350, 0.319, 0.293, 0.266, 0.253]) # EUR/KWh
    Power_term_3   = np.array([0.045671833, 0.033543392, 0.016257762, 0.013830986, 0.009228504, 0.005896482])   # Euro per kw per day
    Billed_power_3 = np.array([18, 18, 18, 18, 18, 18])  ## in KW
    cons_p = []
    for i in Tariffs_3:     # Loop that sums the consumption at each Tariff 'P'
        cons_p6 = np.sum(r2[t2_np == i])
        cons_p.append(cons_p6)
    cons_np = np.array(cons_p)/1000  # converting KWh to MWh 
    tot_energy = np.sum(cons_np * Energy_term_3)/12  # Calculating the Bill in terms of Energy
    tot_power = np.sum(Power_term_3 * Billed_power_3)* 30
    print("Energy Consumption per month in MWh : ", np.sum(cons_np)/12) # Calculating the amount of energy used each month.


elif user == "Residential" or user =="Homeowner":
    Tariffs_2 = np.array(['P1','P2','P3'])
    Energy_term_2  = np.array([0.407, 0.320, 0.262])  #EUR/KWh
    Power_term_2   = np.array([0.081583562, 0.008432877])    # Euro per kw per day
    Billed_power_2 = np.array([4, 4])   ## in KW
    cons_p = []
    for i in Tariffs_2:
        cons_p6 = np.sum(r2[t1_np == i])
        cons_p.append(cons_p6)
    cons_np = np.array(cons_p)/1000
    tot_energy = np.sum(cons_np * Energy_term_2)/(12*19)  # for each household
    tot_power = (2/3)*(Power_term_2[0] * Billed_power_2[0])* 30 + (1/3)*(Power_term_2[1] * Billed_power_2[1])*30
    print("Energy Consumption per month in MWh : ",np.sum(cons_np)/12)
else:
    print("Please enter a valid customer type")

print("Invoiced Energy per month in Euro : ",tot_energy)
print("Invoiced Power per month in Euro : ",tot_power)

tax_electricity = 0.051127  # 5.11 percentage
meter_rent  = 0.81*30      # in Euro per month
em_service  = 2.06      # in Euro per month
IVA = 0.21       # 21 Percent

tot = (tot_energy + tot_power) * (1 + tax_electricity)
bef_iva = tot + em_service + meter_rent
tot_inv = bef_iva * (1 + IVA)
print("Invoice after Electricity tax in Euro: ", tot)
print("Metered Equipment rental: in Euro ",meter_rent)
print("Electrical emergency service in Euro : ",em_service)
print("Invoice before IVA: " ,bef_iva)
print("Total Invoice in Euro: ", tot_inv)