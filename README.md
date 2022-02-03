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
3- Then, you put the data file in folder `irradiation`(Input_data->irradiation).  
4- Finally, the name of the file has to be `irradiation_file.csv`, otherwise the program cannot find the file.


