![image](https://user-images.githubusercontent.com/84010474/152429739-8dbd5f08-3011-4f6d-a950-d7cc4dcd4b15.png)
R2M-MODEL Instruction
==


## Overview
There are several steps to use the main functions of model.  
* Upload the PV irradiation data.  
* Upload the consumption data of consumers.  
* Set the parameters of model(eg, battery capacity, PV panel efficiency .etc).  
...  

## How to upload the PV irradiation data?
1- First, you need go to the websit(https://re.jrc.ec.europa.eu/pvg_tools/es/#PVP) to download the irradiation data of a certain location, the data has to be hourly in a year.   
2- After downloading the data, you have to process the data and calcuate the global irradiation, this process can be done in Excel.(Note1: in this process, you may have to choose slope, azimuth .etc. Note2: in this process, the result is a colume of `global irradiation` data over a year, like `Figue 1`)  

<div align=center>
<img src="https://user-images.githubusercontent.com/84010474/152431749-a1874a4b-7336-45dd-86bf-cfbc943cd197.png" >
</div>
<p align="center">
Figure 1. Irradiation data over a year(8760 hours)
</p>  

3- Then, you put the data file in folder `irradiation` (Input_data->irradiation).  
4- Finally, the name of the file has to be `irradiation_file.csv`, otherwise the program cannot find the file.(The recommended way is to paste the data in exist csv file)  

## How to upload the consumption data of consumers?
There are two ways to do it.  
But before doing it, make sure you use a csv file and the format of data is hourly consumption over a year, `Figure 2` is a example.  
<div align=center>
<img src="https://user-images.githubusercontent.com/84010474/152434505-cf5369ff-280a-4e4c-9105-575131ee77a3.png" >
</div>
<p align="center">
Figure 2. Consumption data over a year(8760 hours)
</p> 
`The first way`: This way is simply paste a csv file in folder `customer_consumption`(Input_data->customer_consumption), But plesae make sure the name of the file is like `consumption_data0.csv`,`consumption_data1.csv`,`consumption_data2.csv`,the number represent the index of your customer, and the number must be consecutive if you have multiple consumers.  
`The second way`: In case you do not have consumption data, you can go to folder `Some_tools`,opening file named `Annual_consumption.py`. The program is like `Figure 3`. What you need to do is simply assume a annual consumption of a customer(total consumption in a year), the you will get a file named `consumption_data.csv`, data in this file is simulated consumption data which you can use in `The first way`.  
<div align=center>
<img src="https://user-images.githubusercontent.com/84010474/152436421-76808dd9-6ec7-487c-9883-cb31c5b93164.png" >
</div>
<p align="center">
Figure 3. Annual_consumption file
</p>  
