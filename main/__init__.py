'''
Main Class
Five datasets are provided - simple point data (Iris), Symbolic Data (City and Hardwood) and Three Way Data of Japan Prefectures I and II
Different ACG can be called for datasets

@author: Kadri Umbleja
'''
import numpy as np
from main.Common import Histogram,SymbolicObject,normalize
import main.ACGs as ACGs

def callMethod(X,objects,titles,type,quantiles,line_width,dot_size):
    nre= len(X)
    nrf = len(titles)
    nrq=len(quantiles)
    
    if(type==0): #simple data table
        #notmalize
        Fmin=[float("inf") for x in range( nrf ) ] 
        Fmax=[float("-inf") for x in range( nrf ) ] 
        data=[ [0 for y in range( nrf ) ] for x in range( nre ) ]
        for i in range(nre):
            helper=X[i].split(",")
            for j in range(nrf):
                data[i][j]=float(helper[j])
                if(data[i][j]<Fmin[j]):
                    Fmin[j]=data[i][j]
                if(data[i][j]>Fmax[j]):
                    Fmax[j]=data[i][j]
        for i in range(nre):
            for j in range(nrf):
                data[i][j]=(data[i][j]- Fmin[j])/(Fmax[j]- Fmin[j])
                
        #for simple point data SAGC is enough        
        ACGs.drawSimple_by_points(data,objects,line_width,dot_size)
    elif(type==1): #symbolic data like interval and histogram
        #takes symbolic form of data and produces list of normalized and Fmin/Fmax
        aList2,Fmin,Fmax=normalize(X,objects,titles)
        
        data=[ [ [ 0 for z in range( nrq ) ] for y in range( nrf ) ] for x in range( nre ) ]
       
        #parse data to Nxdxn
        for i in range(nre):
            for j in range(nrf):
                for k in range (nrq):
                    data[i][j][k]=aList2[i].getHistogram(j).get_quantile(quantiles[k])
        
        ACGs.drawSimple_for_quantiles(data,objects,line_width,dot_size)
        ACGs.drawMinMax_for_quantiles(data,objects,line_width,dot_size)
        ACGs.drawUniliteral_for_quantiles(data,objects,line_width,dot_size)
        ACGs.drawBiliteral_for_quantiles(data,objects,line_width,dot_size)
        ACGs.drawQVACG_for_quantiles(data,objects,line_width,dot_size)
    
    elif(type==2): #data table with Nxdxn
        
        nre=len(objects)
        data=[ [ [ 0 for z in range( nrq ) ] for y in range( nrf ) ] for x in range( nre ) ]
        data1=[ [ [ 0 for z in range( nrq ) ] for y in range( nrf ) ] for x in range( nre ) ]
        
        c=0
        e=0
        
        Fmin=[float("inf") for x in range( nrf ) ] 
        Fmax=[float("-inf") for x in range( nrf ) ] 
        
        #parse data
        for i in range(nre*nrq):
            if(c==nrq):
                c=0
                e+=1
            abi=X[i].split(",")
            for j in range(nrf):
                data[e][j][c]=float(abi[j])
            c+=1
        
        
        
        #add the individual values
        for i in range(nre):
            for j in range(nrf):
                for k in range (nrq):
                    if(k==0):
                        data1[i][j][k]=data[i][j][k]
                    else:
                        data1[i][j][k]=data1[i][j][k-1]+data[i][j][k] 
        
        #find min/max values
        for i in range(nre):
            for j in range(nrf):
                for k in range (nrq):
                    if(data1[i][j][k]<Fmin[j]):
                        Fmin[j]=data1[i][j][k]
                    if(data1[i][j][k]>Fmax[j]):
                        Fmax[j]=data1[i][j][k]
        
        #normalize data   
        for i in range(nre):
            for j in range(nrf):
                for k in range (nrq):
                    data1[i][j][k]=(data1[i][j][k]-Fmin[j])/(Fmax[j]-Fmin[j])
        

        ACGs.drawSimple_for_quantiles(data1,objects,line_width,dot_size)
        ACGs.drawMinMax_for_quantiles(data1,objects,line_width,dot_size)
        ACGs.drawUniliteral_for_quantiles(data1,objects,line_width,dot_size)
        ACGs.drawBiliteral_for_quantiles(data1,objects,line_width,dot_size)
        ACGs.drawQVACG_for_quantiles(data1,objects,line_width,dot_size)


if __name__ == '__main__':

#IRIS DATASET
    objects=[str(i * 1) for i in range(150)]
    titles=['sepal length','sepal width','petal length','petal width']
    X = np.loadtxt("data/iris.txt", dtype='str', delimiter='\n') 
    type=0
    line_width=1
    dot_size=5
    quantiles=[]
     
#CITY DATASET
#     objects=['Amsterdam','Athens','Bahrain','Bombay','Cairo','Calcutta','Colombo','Copenhagen','Dubai','Frankfurt','Geneva','Hong_Kong','Kuala_Lumpur','Lisbon','London','Madras','Madrid','Manila','Mauritius','Mexico_City','Moscow','Munich','Nairobi','New_Delhi','New_York','Paris','Rome','San_Francisco','Seoul','Singapore','Stockholm','Sydney','Tehran','Tokyo','Toronto','Vienna','Zurich']
#     titles=['jan','feb','mar','apr','may','jun','jul','aug','sept','oct','nov','dec']
#     X = np.loadtxt("data/city.txt", dtype='str', delimiter='\n')
#     type=1
#     line_width=1
#     dot_size=5
#     quantiles=[0,1]

#HARDWOOD DATASET
#     objects=['ACER_EAST','ACER_WEST','ALNUS_EAST','ALNUS_WEST','FRAXINUS_EAST','FRAXINUS_WEST','JUGLANS_EAST','JUGLANS_WEST','QUERCUS_EAST','QUERCUS_WEST']
#     titles=['ANNT','JANT','JULT','ANNP','JANP','JULP','GDC5','MITM']
#     X = np.loadtxt("data/hardwood.txt", dtype='str', delimiter='\n')
#     type=1
#     line_width=1
#     dot_size=5
#     quantiles=[0,0.1,0.25,0.5,0.75,0.9,1]

#PREFECTURE 1
#     objects=["Hokkaido","Aomori","Iwate","Miyagi","Akita","Yamagata","Fukushima","Ibaraki","Tochigi","Gumma","Saitama","Chiba","Tokyo","Kanagawa","Niigata","Toyama","Ishikawa","Fukui","Yamanashi","Nagano","Gifu","Shizuoka","Aichi","Mie","Shiga","Kyoto","Osaka","Hyogo","Nara","Wakayama","Tottori","Shimane","Okayama","Hiroshima","Yamaguchi","Tokushima","Kagawa","Ehime","Kochi","Fukuoka","Saga","Nagasaki","Kumamoto","Oita","Miyazaki","Kagoshima","Okinawa"]
#     titles=["Agriculture_and_forestry","Fisheries","Mining_and_quarrying_of_stone_and_gravel","Construction","Manufacturing","Electricity,_gas,_heat_supply_and_water","Information_and_communications","Transport_and_postal_activities","Wholesale_and_retail_trade","Finance_and_insurance","Real_estate_and_goods_rental_and_leasing","Scientific_research,_professional_and_technical_services","Accommodations,_eating_and_drinking_services","Living-related_and_personal_services_and_amusement_services","Education,_learning_support","Medical,_health_care_and_welfare","Compound_services","Services_(not_elsewhere_classified)","Government,_except_elsewhere_classified","Nominal_GDP(10billion_yen)","Temperature_min","Temperature_max","Area_in_squre_kilometres","0-4years_old,Unit_1000_persons","5-9","10-14","15-19","20-24","25-29","30-34","35-39","40-44","45-49","50-54","55-59","60-64","65-69","t0-74","75-79","80-84","85and_over","Birth","Death","Marriage","Devorce","Private_households_Number_of_households","Private_households_Household_members","Industrial_housholds_Number_of_households","Industrial_houleholds_Household_members"]
#     X = np.loadtxt("data/prefecture.txt", dtype='str', delimiter='\n')
#     type=0
#     line_width=0.2
#     dot_size=1
#     quantiles=[]

#PREFECTURE 2 - jobs
#     objects=["Aichi","Akita","Aomori","Chiba","Ehime","Fukui","Fukuoka","Fukushima","Gifu","Gunma","Hiroshima","Hokkaido","Hyogo","Ibaraki","Ishikawa","Iwate","Kagawa","Kagoshima","Kanagawa","Kochi","Kumamoto","Kyoto","Mie","Miyagi","Miyazaki","Nagano","Nagasaki","Nara","Niigata","Oita","Okayama","Okinawa","Osaka","Saga","Saitama","Shiga","Shimane","Shizuoka","Tochigi","Tokushima","Tokyo","Tottori","Toyama","Wakayama","Yamagata","Yamaguchi","Yamanashi"]
#     titles=["Professional skills","Management jobs","Office works","Sales jobs","Service jobs","Security jobs","Agricultural forestry and fisheries","Transportation and communication","Industrial process work","Unclassified jobs"]
#     X = np.loadtxt("data/jobs.txt", dtype='str', delimiter='\n')
#     type=2
#     line_width=0.2
#     dot_size=1
#     quantiles=[1,2,3,4,5,6] #6 different time periods are used

    callMethod(X,objects,titles,type,quantiles,line_width,dot_size)