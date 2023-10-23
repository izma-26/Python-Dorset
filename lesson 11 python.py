
import numpy as np

temp_mar=[13.8,13.3,13.9,15.0,16.4,20.0,21.9,22.3,22.0,21.2,18.8,16.0]
months=['January','February','March','April','May','June','July','August','September','October',
'November','December']
print(temp_mar)
temp_arr = np.array(temp_mar)
print(temp_arr)


print('Average temperature : '+str(np.mean(temp_arr)) + ' °C')
min = 9999999999999999999999999999999999999999999999999999999
max = -999999999999999999999999999999999999999999999999999999
k=0
p=0
for i in range (0,len(temp_arr)) :
    if(temp_arr[i] > max) :
        max = temp_arr[i]
        k=i
    if (temp_arr[i] < min):
        min = temp_arr[i]
        p=i


print('Minimum temperature : '+str(min) + ' °C  in ' +str(months[p]))
print('Maximum temperature : ' +str(max) + ' °C  in ' +str(months[k]))





