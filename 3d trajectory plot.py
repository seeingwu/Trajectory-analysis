%matplotlib notebook
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data =pd.read_csv('data.csv')

# calculate the time 
data['time'] = pd.to_datetime(data['time'])
data['z']= 0
for i in range(len(data['time'])):
    data['z'][i] = (data['time'][i]-data['time'][0]).seconds
    
fig = plt.figure()
fig.set_size_inches(15,15)
ax = plt.axes(projection='3d')
# Data for a three-dimensional line
zline = data['z']
xline = data['y']
yline = data['x']
for i in range(len(xline)):
    x = [xline[i]]
    y = [yline[i]]
    z = [0]
    x.append(xline[i])
    y.append(yline[i])
    z.append(zline[i])
    ax.plot3D(x, y, z, 'gray')
    
ax.plot3D(xline, yline, zline, 'black')
ax.scatter3D(xline, yline, zline, c='Orange',s=20)

# set the aixs
ax.zaxis.set_ticks([data['z'][0],data['z'][1000],data['z'][1900]])
ax.zaxis.set_ticklabels([data['time'][0],data['time'][1000],data['time'][1900]])
plt.show()

''' 
fig = plt.figure()
fig.set_size_inches(50,50)
ax = plt.axes(projection='3d')
# Data for a three-dimensional line
zline = data['z']
xline = data['x']
yline = data['y']
wifix = data_wifi['x']
wifiy = data_wifi['y']
wifiz = data_wifi['z']
bley = data_ble['y']
blex = data_ble['x']
blez = data_ble['z']
bty = data_bt['y']
btx = data_bt['x']
btz = data_bt['z']
celly = data_gsm['y']
cellx = data_gsm['x']
cellz = data_gsm['z']
ax.plot3D(xline, yline, zline, 'black',label = 'trajectory')
ax.scatter3D(wifix, wifiy, wifiz, c='red',s=500, alpha = 0.4, label = 'WiFi')
ax.scatter3D(blex, bley, blez, c='blue',s=200, label = 'BLE')
ax.scatter3D(btx, bty, btz, c='royalblue',s=200, label = 'BT')
ax.scatter3D(cellx,celly,cellz,c='orange',s=600,alpha = 0.4, label = 'GSM')
ax.legend(loc=1, shadow=True, fontsize='x-large',prop={'size': 36})
ax.set_xlabel('longitude',fontsize = 40)     
ax.yaxis.set_label_text('latitude',fontsize =40)
ax.zaxis.set_label_text('time/s',fontsize = 40)
ax.azim = -75
ax.dist = 10
ax.elev = 5
plt.savefig('3dplot.png')
plt.show()

'''
