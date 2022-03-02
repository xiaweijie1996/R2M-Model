![image](https://user-images.githubusercontent.com/84010474/152429739-8dbd5f08-3011-4f6d-a950-d7cc4dcd4b15.png)
R2M-MODEL Instruction
==


## Overview
There are several steps to use the main functions of the model.  
* Upload the PV irradiation data.  
* Upload the consumption data of consumers.  
* Set the parameters of model (eg, battery capacity, PV panel efficiency,...etc).  
* Find the output.  
...  

## How to upload the PV irradiation data?
**1-** First, the irradiation data of a certain location has to be downloaded from the website (https://re.jrc.ec.europa.eu/pvg_tools/es/#PVP). The data has to be hourly in a year.   
**2-** After downloading the data, it has to be processed and the global irradiation calculated, this process can be done in Excel. (Note1: in this process, you may have to choose slope, azimuth .etc. Note2: in this process, the result is a column of `global irradiation` data over a year, like `Figue 1`)  

<div align=center>
<img src="https://user-images.githubusercontent.com/84010474/152431749-a1874a4b-7336-45dd-86bf-cfbc943cd197.png" >
</div>
<p align="center">
Figure 1. Irradiation data over a year(8760 hours)
</p>  

**3-** Then, the data file has to be placed in the folder `irradiation` (Input_data->irradiation).  
**4-** Finally, the name of the file has to be `irradiation_file.csv`, otherwise the program will not be able to find the file. (The recommendeded way is to paste the data in exist csv file)  

## How to upload the consumption data of consumers?
There are two ways to do it.  
But before doing it, make sure you use a csv file and the format of data is hourly consumption over a year, `Figure 2` is an example.  
<div align=center>
<img src="https://user-images.githubusercontent.com/84010474/152434505-cf5369ff-280a-4e4c-9105-575131ee77a3.png" >
</div>
<p align="center">
Figure 2. Consumption data over a year(8760 hours)
</p> 

**The first way**: This way is simply paste a csv file in folder `customer_consumption`(Input_data->customer_consumption), But plesae make sure the name of the file is like `consumption_data0.csv`,`consumption_data1.csv`,`consumption_data2.csv`,the number represent the index of your customer, and the number must be consecutive if you have multiple consumers.  

**The second way**: In case you do not have consumption data, you can go to folder `Some_tools`,opening file named `Annual_consumption.py`. The program is like `Figure 3`. What you need to do is simply assume a annual consumption of a customer(total consumption in a year), the you will get a file named `consumption_data.csv`, data in this file is simulated consumption data which you can use in `The first way`.  

<div align=center>
<img src="https://user-images.githubusercontent.com/84010474/153673712-747ab19d-1d10-4796-8ba1-bdd9f2e776dc.png" >
</div>
<p align="center">
Figure 3. Annual_consumption file
</p>  

## How to set the parameters of model?
After finishing steps before (Uploading PV irradiation data and consumption data of consumers), you can open the `Mainfile.py`(Working_file->Working_file.py). The program is like `Figure 4`, Here, all parameters that you are allowed to adjust is within red rectangle.

<div align=center>
<img src="https://user-images.githubusercontent.com/84010474/152438045-fbd171ad-47a7-434f-b9e7-98cee14619a0.png" >
</div>
<p align="center">
Figure 4. MainFile
</p>  

## How to see my output?
After setting the parameters of `MainFile`, you can runn this file, the output is the simulated data of your customers, you can find the output file in `EnergyFlux_data`(Output_data->EnergyFlux_data).

## How to use visualization tool?
Following the path:(smalltools->Visualization). you will find a file name `Visualization.py`, open it and choose the data sources you want visualized by change te file_name, as show in Fig 5. The 'file_name' is the name of file in (Output_data->EnergyFlux_data). Aftering changing the file_name, you can run the file, the program will then generate several figures in the folder.

<div align=center>
<img src="https://user-images.githubusercontent.com/84010474/153673015-3a43a358-ef09-480c-a880-b31f22d74e22.png" >
<img src="https://user-images.githubusercontent.com/84010474/153673384-988e6d79-fed9-4690-a3f6-ab3711429ad3.png">

</div>
 
<p align="center">
Figure 5. Visualization tool
</p>  

## The explanation of input data.

**PV parameters**  
area: the area of PV panel, m^2.    
panel_efficiency: the efficiency of panel.    
loss: 1-loss indicate the energy loss.   
number_panels: the number of PV panels.  

**Battery parameters**  
capacity_battery: batter's capacity_battery, Wh.  
deep_battery: the maximum allowed deepth of charging.  
bat_charge_speed: charging speed, Wh.  

**Charging time**  
char_time_start: charging start time.  
char_time_stop: charging stop time.  

**Spliting PV generation**  
pv_allocation: pv_allocation is a list, the number of components have to match the number of customers, the sum of components has to be 1.  

## The explanation of output data of EnergyFlux_data.
`generation_pv`: the generation of PV in this hour.  
`consumption`: the consumption of customer in this hour.  
`surplus`: the energy surplus in this hour, if consumption<=generation_pv, then, surplus=generation_pv-consumption, otherwise surplus=0.  
`grid consumption`: grid consumption is the power consumption supporting by gird in this hour in the scenario **without battery**.   
`use_power_pv1`: use_power_pv1 is the power consumption supporting by PV panel in this hour.  
`use_power_grid1`: use_power_grid1 is the power consumption supporting by gird in this hour in the scenario **with the battery**.  
`en_battery_grid1`: en_battery_grid1 is the enegy absorbed by battery from the grid.  
`en_battery_pv1`: en_battery_pv1 is the enegy absorbed by battery from the PV panel.  
`en_dump1`: en_dump 1 is the energy left after consumption and charging of the battery, this part of energy can be sold.   

## Calculation distance between panels accounting for possible shadowing
**Input data**  
The input data needed is:
Height of the panel (m): 1.134
Width of the panel (m): 2.279
The power of the panel is 0.36 kW

The data of the panel selected corresponds to a policristaline PERC Canadian Solar and is taken from: https://drive.google.com/drive/folders/1V6A4QYkpaBNFW43knFr8O-DXwlMuXWdd

Latitude of the location (degrees): 41.38
Inclination (degrees): 10


With these values the minimum distance is given following Figure 5, and an extra 5% added to give the recommended distance between panels.

<div align=center>
<img src="https://user-images.githubusercontent.com/60061119/153641804-638aca0b-b4e4-4df6-8143-8b3191ae955d.png" >
</div>
 
<p align="center">
Figure 6. Calculation of minimum distance between panels
</p>  

Other inputs are:
The total surface (m): 62
The "flat surface"; if installed directly with the slope of the roof (m): 160

**Output data** 
The outputs are:

* The area of a matrix, number of matrices and finally the installed power (kW)
* The area of a matrix, number of matrices and finally the installable power (kW)

**Other remarks** 

The following also have to be taken into account: 
The minimum distance from chimneys is: 0.9 m
The distance from other panels (horizontal) shall be: 0.5m

For an inclined surface use the following website can be used: https://www.monsolar.com/separacion-paneles-solares


## Explanation for the Billing part

**Variables that the user have to change for the given case**

**Updating Tariffs**

the tariffs can be updated from the utility company's website. in the tool, two types of customers with two different tariffs are considered for the case study.

Following the Spanish Tariff scheme, for Customers with a connection point of 15kW or above, the type of tariff used is "3.0 TD". To keep it simple, customers under this tariff are considered to be `Business` in nature becuase of larger connection point. There are 3 different components to this tariffs which will be explained in short. 3.0TD tariffs contains 6 price periods distributed across 24 hours (a day).

`Energy_term_3`: This component signifies the cost of using the electricity for each of the 6 periods given per unit MWh consumed.
`Power_term_3`: This component signifies the cost of having the power connection for a period of time, which in this case is kW per day.
`Billed_power_3`: This componnet signifies the amount of power being supplied by the DSO at any given time, in this case denoted in kW.

"2.0 TD"

The customers who are connected less than 15kW or below are considered to be `Homeowners` or `Residential` customers. There can be several other possibilities but are neglected to keep the tool simple and accessable to the majority. the tariff assigned consists of 3 periods distributed across 24 hours (a day).

`Energy_term_2`: Same as `Energy_term_3` for 2.0 TD that contains only 3 periods.
`Power_term_2`: Same as `Power_term_3` for 2.0 TD. 
`Billed_power_2`: Same as `Billed_power_3` for 2.0 TD.

**Furthurmore, there are few variables that are independent of the Utility company that the customer has to change.**

`tax_electricity` -  Electricity tax.
`meter_rent` - Metered equipment rental in Euro per month. 
`em_service`   -  Electrical Emergancy service in Euro per month.
`IVA = 0.21`   - 21 Percent, equivalent to VAT (Value Added Tax).
`pv_energy_terms` - Power purchase agreement in EUR/KWh. 


Once you have done changing these variables according to your requirements, you have to save the `MainFile.py`file(`MainFile_0SX.py` if your using macOS).

Now, before running the file you need to make sure you have all the python packages required to run the tool. you can do this by installing the requirement.txt located in the same folder. You can do this by typing the following command in your `CLI` (Command Prompt/Terminal).
<p align="center">
<img width="333" alt="Screenshot 2022-02-26 at 5 41 16 PM" src="https://user-images.githubusercontent.com/89131947/156340255-0352f333-8baa-44b1-89ae-02d32ea9a08d.png">
 </p>

Once you have installed the packages, now you can run the `MainFile.py`file(`MainFile_0SX.py` if your using macOS).


