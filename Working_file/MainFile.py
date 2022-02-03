from PV import *
from Consumption import *
from Energy_flux import *
import pandas as pd
import numpy as np
import os
import csv

"The Main file is the only file you need to run"

"The parameters you can change"
"————————————————————————————————————————————"
"Adjusting PV parameters"
area = 2.576 # m^2
panel_efficiency = 0.203
loss = 0.8
number_panels = 40

"Adjusting battery parameters"
capacity_battery = 30000  #Wh batter's capacity_batterycapacity_battery = 30000,  #Wh batter's capacity_battery
deep_battery = 0.05  #batter discharge at most to capacity_battery*deep_battery of its capacity_battery
bat_charge_speed = 1400 #w charging speed

"Adjusting charging time"
char_time_start = 3  #charging start time
char_time_stop = 4   #charging stop time

"Spliting PV generation"
pv_allocation=[0, 0.2, 0, 0.8]  # The number of components have to match the number of customers
"————————————————————————————————————————————"

"The parameters you do not need to change"
n_coustomer = number_customers() # number of customers, depend on number of consumptions files you upload
pv = PV(area,panel_efficiency,loss,number_panels)
parameters_consumption = [1,capacity_battery,deep_battery,bat_charge_speed,char_time_start,char_time_stop]

"Creating Energy flux data file"
for i in range(n_coustomer):
    in_file_prefix = r'..\Input_Data\customer_consumption\consumption_data'
    in_file_name = in_file_prefix + str(i) + '.csv' 
    out_file_prefix = r'..\Output_Data\EnergyFlux_data\consumption_data'
    out_file_name = out_file_prefix + str(i) + '.csv' 
    parameters_consumption[0] =  pv_allocation[i]
    with open(out_file_name,'w') as file:
        writer = csv.writer(file)
        writer.writerows(consumer_profile(in_file_name,pv,parameters_consumption))
        

