'''
ACGs are drawn in this cass
@author: Kadri Umbleja
'''
import matplotlib.pyplot as plt
from matplotlib.pyplot import cm

width=1

#help functions for plotting
def addPoint(i,v1,ax,colors,dot_size,j=None):
    if j is None:
        j=i
    v=[v1]
    y=[(i)*width]
    ax.plot(y, v, 'ro',color=colors[j],markersize=dot_size)
    
def addLineUniliteral(j,i,v1,v2,ax,colors,line_width,dot_size):
    v=[v1,v2]
    y=[(i)*width,(i+1)*width]
    ax.plot(y, v, 'ro-',color=colors[j],linewidth=line_width,markersize=dot_size)


#MAIN VISUALIZATION FOR SINGLE POINT DATA          
def drawSimple_by_points(data,objects,line_width,dot_size):
    

    fig, axes = plt.subplots(1, 1, sharey=False,figsize=(16, 8)) 
    nrf=len(data[0])
    nre=len(data)
    #diffrence between objects
    m=nrf+3 
    
    #color shades are produced
    colors=[0 for x in range(nrf)]
    cmap = plt.cm.get_cmap('Greys')
    start=0.5
    end=1
    for i in range(nrf):
        colors[i] = cmap(start+((end-start)/(nrf+1))*(i+1))
    
    #lines are drawn
    for i in range(nre):
        so_far=0;
        for j in range(nrf):
                if(j==0):
                    so_far=data[i][0] 
                else:
                    addLineUniliteral(j,(i)*m+j,so_far,so_far+(data[i][j] ),axes,colors,line_width,dot_size)
                    so_far=so_far+(data[i][j])
        
        #add name    
        axes.text((i+1)*m-(round(m/2)), so_far+0.2, objects[i],{'ha': 'left', 'va': 'bottom'}, rotation=90)
    
    

    axes.set_xlim([0,nre*m])
    axes.set_ylim([0, nrf])
    
    plt.savefig('graphs/SACG.jpg', format='jpg', dpi=300)
    plt.show()
    plt.close()
    
 
    
    
    
#METHODS FOR THREE WAY DATA
def drawSimple_for_quantiles(data,objects,line_width,dot_size):
    
    fig, axes = plt.subplots(1, 1, sharey=False,figsize=(16, 8)) 
    nrf=len(data[0])
    nre=len(data)
    nrq=len(data[0][0])
    
    #diffrence between objects
    m=nrf+3 
    
    #color shades are produced
    colors=[0 for x in range(nrf)]
    cmap = plt.cm.get_cmap('Greys')
    start=0.5
    end=1
    for i in range(nrf):
        colors[i] = cmap(start+((end-start)/(nrf+1))*(i+1))
    
    #for adequate limits
    max=0
    #lines are drawn
    for i in range(nre):
        so_far=0;
        for j in range(nrf):
            if(i>=0):
                if(j==0):
                    so_far=data[i][j][0] 
                else:
                    addLineUniliteral(j,(i)*m+j,so_far,so_far+(data[i][j][nrq-1] -data[i][j][0] ),axes,colors,line_width,dot_size)
                    so_far=so_far+(data[i][j][nrq-1] -data[i][j][0] )
        if(so_far>max):
            max=so_far
        
        #add name    
        axes.text((i+1)*m-(round(nrf/2)), so_far+0.1, objects[i],{'ha': 'left', 'va': 'bottom'}, rotation=90)
    
    

    axes.set_xlim([0,nre*m])
    axes.set_ylim([0, max*1.1])
    
    plt.savefig('graphs/SACG.jpg', format='jpg', dpi=300)
    plt.show()
    plt.close()
    
def drawMinMax_for_quantiles(data,objects,line_width,dot_size):
  
    fig, axes = plt.subplots(1, 1, sharey=False,figsize=(16, 8)) 
    nrf=len(data[0])
    nre=len(data)
    nrq=len(data[0][0])
    #diffrence between objects
    m1=2
    m2=4
    m=nrf+m1+nrf+m2
    
    #color shades are produced, one for min, other to max
    colors=[0 for x in range(nrf)]
    cmap = plt.cm.get_cmap('Blues')
    start=0.5
    end=1
    for i in range(nrf):
        colors[i] = cmap(start+((end-start)/(nrf+1))*(i+1))
        
    colors2=[0 for x in range(nrf)]
    cmap = plt.cm.get_cmap('Reds')
    start=0.5
    end=1
    for i in range(nrf):
        colors2[i] = cmap(start+((end-start)/(nrf+1))*(i+1))
    
    #lines are drawn
    for i in range(nre):
        so_far=0;
        for j in range(nrf):
            if(j==0):
                so_far=data[i][j][0]
            else:
                addLineUniliteral(j,(i)*m+j,so_far,so_far+(data[i][j][0]),axes,colors,line_width,dot_size)
                so_far=so_far+(data[i][j][0])
                
        so_far=0;
        for j in range(nrf):
            if(j==0):
                so_far=data[i][j][nrq-1]  
            else:
                addLineUniliteral(j,(i)*m+nrf+m1+j,so_far,so_far+(data[i][j][nrq-1] ),axes,colors2,line_width,dot_size)
                so_far=so_far+(data[i][j][nrq-1] )
                    
        #add name    
        axes.text((i+1)*m-(nrf), so_far+0.1, objects[i],{'ha': 'left', 'va': 'bottom'}, rotation=90)


    axes.set_xlim([0,nre*m])
    axes.set_ylim([0, nrf])
    
        
        
    
    plt.savefig('graphs/MinMaxACG.jpg', format='jpg', dpi=300)
    plt.show()
    plt.close()
    
    
def drawUniliteral_for_quantiles(data,objects,line_width,dot_size):
    fig, axes = plt.subplots(1, 1, sharey=False,figsize=(16, 8))
    nrf=len(data[0])
    nre=len(data)
    nrq=len(data[0][0])
    #diffrence between objects
    m1=3
    m=2*nrf+m1
     
     #color shades are produced
    colors=[0 for x in range(nrf)]
    cmap = plt.cm.get_cmap('Greys')
    start=0.5
    end=1
    for i in range(nrf):
        colors[i] = cmap(start+((end-start)/(nrf+1))*(i+1))
    
    
    #for adequate limits
    max=0 
    #lines are drawn
    for i in range(nre):
        so_far=0;
        for j in range(nrf):
            if(j==0):
                so_far=data[i][j][0]
                addLineUniliteral(j,(i*m)+j+1,so_far,data[i][j][0],axes,colors,line_width,dot_size)
                so_far=data[i][j][0]
            else:
                addLineUniliteral(j,(i*m)+j*2,so_far,so_far+data[i][j][0],axes,colors,line_width,dot_size)
                addPoint((i*m)+j*2,so_far,axes,colors,dot_size,j-1)
                so_far=so_far+data[i][j][0]
                addLineUniliteral(j,(i*m)+j*2+1,so_far,so_far+data[i][j][nrq-1]-data[i][j][0],axes,colors,line_width,dot_size)
                so_far=so_far+data[i][j][nrq-1]-data[i][j][0]
        if(so_far>max):
            max=so_far
 
         
        axes.text((i+1)*m-(round(nrf/2)), so_far+0.1, objects[i],{'ha': 'left', 'va': 'bottom'}, rotation=90)
     
 
    axes.set_xlim([0,nre*m])
    axes.set_ylim([0, max*1.1])
    
    
    plt.savefig('graphs/uniliteral.jpg', format='jpg', dpi=300)
    plt.show()
    plt.close()
    
def drawBiliteral_for_quantiles(data,objects,line_width,dot_size):
    fig, axes = plt.subplots(1, 1, sharey=False,figsize=(16, 8))
    nrf=len(data[0])
    nre=len(data)
    nrq=len(data[0][0])
    #diffrence between objects
    m1=3
    m=2*nrf+m1
     
     #color shades are produced
    colors=[0 for x in range(nrf)]
    cmap = plt.cm.get_cmap('Greys')
    start=0.5
    end=1
    for i in range(nrf):
        colors[i] = cmap(start+((end-start)/(nrf+1))*(i+1))
    
    
    #for adequate limits
    max=0 
    #lines are drawn
    for i in range(nre):
        so_far=0;
        for j in range(nrf):
            if(j==0):
                so_far=data[i][j][0]
                addLineUniliteral(j,(i*m)+j+1,so_far,data[i][j][nrq-1],axes,colors,line_width,dot_size)
                so_far+=data[i][j][nrq-1]
            else:
                addLineUniliteral(j,(i*m)+j*2,so_far,so_far+data[i][j][0],axes,colors,line_width,dot_size)
                addPoint((i*m)+j*2,so_far,axes,colors,dot_size,j-1)
                so_far=so_far+data[i][j][0]
                addLineUniliteral(j,(i*m)+j*2+1,so_far,so_far+data[i][j][nrq-1],axes,colors,line_width,dot_size)
                so_far=so_far+data[i][j][nrq-1]
        if(so_far>max):
            max=so_far
 
         
        axes.text((i+1)*m-(round(nrf/2)), so_far+0.1, objects[i],{'ha': 'left', 'va': 'bottom'}, rotation=90)
     
 
    axes.set_xlim([0,nre*m])
    axes.set_ylim([0, max*1.1])
    
    
    plt.savefig('graphs/biliteral.jpg', format='jpg', dpi=300)
    plt.show()
    plt.close()
    
    
def drawQVACG_for_quantiles(data,objects,line_width,dot_size):

    fig, axes = plt.subplots(1, 1, sharey=False,figsize=(16, 8)) 
    nrf=len(data[0])
    nre=len(data)
    nrq=len(data[0][0])
    
    #diffrence between features
    m1=1
    #diffrence between objects
    m2=3
    m=(m1+nrq)*nrf+m2
    
    #for adequate limits
    max=0 
     #color shades are produced
    colors=[0 for x in range(nrf)]
    cmap = plt.cm.get_cmap('Greys')
    start=0.5
    end=1
    for i in range(nrf):
        colors[i] = cmap(start+((end-start)/(nrf+1))*(i+1))
        
    #lines are drawn    
    for i in range(nre):
          
        for k in range(nrq):
            so_far2=[0 for x in range(nrq)]
            for j in range(nrf-1):
                if(j==0):
                    v1=so_far2[k]+data[i][j][k]
                    so_far2[k]=v1
                    v2=so_far2[k]+data[i][j+1][k]
                    so_far2[k]=v2
                else:
                    v1=so_far2[k]
                    v2=so_far2[k]+data[i][j+1][k]
                    so_far2[k]=v2
                addLineUniliteral(j,(i*m)+nrf*k+j,v1,v2,axes,colors,line_width,dot_size)
            addPoint((i*m)+nrf*(k+1),so_far2[k],axes,colors,dot_size,nrf-1)
        
            if(so_far2[nrq-1]>max):
                max=so_far2[nrq-1]
               

        axes.text(i*m+round(m/2), so_far2[nrq-1]+0.2, objects[i],{'ha': 'left', 'va': 'bottom'}, rotation=90)
    
    axes.set_xlim([0,nre*m])
    axes.set_ylim([0, max*1.1])
    
    
    plt.savefig('graphs/QV_ACG.jpg', format='jpg', dpi=300)
    plt.show()
    plt.close()