import PyLidar3
import time
import math
import numpy as np
import pygame
import pyplot

def LidarFilter(data, distance):
    skip = False
    for winkel, werte in data.items():
        if winkel == None:
            skip = True
        elif winkel == 0:
            ang1 = 359
            ang2 = 1
        elif winkel == 359:
            ang1 = 358
            ang2 = 0
        else:
            ang1= winkel - 1
            ang2= winkel + 1
        if skip == False:
            SA = data[winkel]
            S1 = data[ang1]
            S2 = data[ang2]
            # Abst1= math.sqrt((Xang-Xang1)**2 + (Yang-Yang1)**2)
            # Abst2= math.sqrt((Xang-Xang2)**2 + (Yang-Yang2)**2)
            if S1 is not None:
                Xang = math.cos(winkel)*werte
                Yang = math.sin(winkel)*werte
                Xang1 = math.cos(ang1)*data[ang1]
                Yang1 = math.sin(ang1)*data[ang1]
                resP1 = int(math.sqrt((Xang-Xang1)**2+(Yang-Yang1)**2)) #resP1 = int(math.sqrt((SA**2)+(S1**2)+2*SA*S1*0.99985))

            if S2 is not None:
                Xang = math.cos(winkel)*werte
                Yang = math.sin(winkel)*werte
                Xang2 = math.cos(ang2)*data[ang2]
                Yang2 = math.sin(ang2)*data[ang2]
                resP2 = int(math.sqrt((Xang-Xang2)**2+(Yang-Yang2)**2))  #resP2 = int(math.sqrt((SA**2)+(S2**2)+2*SA*S2*0.99985))

            print("resP1", resP1)
            print("resP2", resP2)
            if resP1 > distance and resP2 > distance:
                data[winkel] = None
    return data

        







winkel_dict = {i: {'x': None, 'y': None} for i in range(360)}

lidar = PyLidar3.YdLidarG4("com15") # Hier "/dev/ttyUSB0" ist der Port, an dem Ihr Lidar angeschlossen ist. Ändern Sie dies entsprechend.
try:  

    if(lidar.Connect()):
        print("Lidar G4 verbunden!")
        gen = lidar.StartScanning()
        t = time.time() # Startzeit
        while (time.time() - t) < 30: # für 30 Sekunden scannen
            data = next(gen) # Ausgabe der gescannten Werte
            print(data)
            data = LidarFilter(data, 1500)
            pyplot.main(data)
            for winkel, wert in data.items():

                winkelR = math.radians(winkel)
                if wert is not None:
                    x = math.cos(winkelR)*wert
                    y = math.sin(winkelR)*wert
                    winkel_dict[winkel]['x'] = x
                    winkel_dict[winkel]['y'] = y
                    wiRangeStart = 0
                    wiRangeStop = 20
                    winkelInRangeX = (winkel_dict[i]['x'] for i in range(wiRangeStart, wiRangeStop) if winkel_dict[i]['x'] is not None)
                    winkelInRangeX = np.array(list(winkelInRangeX))
                    winkelInRangeY = (winkel_dict[i]['y'] for i in range(wiRangeStart, wiRangeStop) if winkel_dict[i]['y'] is not None)
                    winkelInRangeY = np.array(list(winkelInRangeY))

                    print("X:",winkelInRangeX)
                    print("Y:", winkelInRangeY)
                
                if winkelInRangeX is not None:  
                    if(np.corrcoef(winkelInRangeX, winkelInRangeY)[0, 1]>=0.9 or np.corrcoef(winkelInRangeX, winkelInRangeY)[0, 1] <= -0.9):
                        print("TRUE Korrelationskoeffizient größer als 0.8", np.corrcoef(winkelInRangeX, winkelInRangeY)[0, 1])
                        x = list((winkel_dict[i]['x'] for i in range(wiRangeStart, wiRangeStop) if winkel_dict[i]['x'] is not None))
                        y = list((winkel_dict[i]['y'] for i in range(wiRangeStart, wiRangeStop) if winkel_dict[i]['y'] is not None))
                        # m, b = np.polyfit(x, y, 1)
                        # # Create a sequence of x values spanning the range of x (for the line)
                        # x_line = np.linspace(min(x), max(x))
                        # # Calculate the corresponding y values for the line
                        # y_line = m*x_line + b
                        # plt.plot(x_line, y_line, color='red')
                    else:
                        print("FALSE Korrelationskoeffizient kleiner als 0.8", np.corrcoef(winkelInRangeX, winkelInRangeY)[0, 1])

            
                
            print(winkel_dict)   

        lidar.StopScanning()
        lidar.Disconnect()
    else:
        print("Fehler beim Verbinden mit Lidar G4.")

except KeyboardInterrupt:
    lidar.StopScanning()
    lidar.Disconnect()
    pygame.quit()