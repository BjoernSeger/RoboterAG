# import PyLidar3
import time
import math
import numpy as np
import pygame


class PyLidar3:
    class YdLidarG4:
        running: bool
        lidar_values: dict

        def __init__(self, connection):
            self.connection = connection
            self.running = True
            self.lidar_values = {0: 476, 1: 45, 2: 272, 3: 269, 4: 269, 5: 268, 6: 269, 7: 272, 8: 271, 9: 270, 10: 269,
                                 11: 271, 12: 270, 13: 270, 14: 271, 15: 271, 16: 271, 17: 272, 18: 272, 19: 269,
                                 20: 276, 21: 94, 22: 0, 23: 0, 24: 0, 25: 225, 26: 441, 27: 510, 28: 505, 29: 502,
                                 30: 413, 31: 255, 32: 449, 33: 455, 34: 461, 35: 466, 36: 472, 37: 473, 38: 477,
                                 39: 482, 40: 276, 41: 194, 42: 629, 43: 581, 44: 652, 45: 838, 46: 983, 47: 991,
                                 48: 996, 49: 981, 50: 1020, 51: 1036, 52: 1042, 53: 1057, 54: 1064, 55: 1086, 56: 1107,
                                 57: 1122, 58: 1138, 59: 1153, 60: 1171, 61: 1189, 62: 1207, 63: 670, 64: 0, 65: 558,
                                 66: 1012, 67: 923, 68: 0, 69: 527, 70: 1067, 71: 649, 72: 1103, 73: 1122, 74: 1141,
                                 75: 1156, 76: 1169, 77: 1180, 78: 1204, 79: 1232, 80: 1262, 81: 850, 82: 646, 83: 0,
                                 84: 0, 85: 0, 86: 0, 87: 0, 88: 450, 89: 901, 90: 0, 91: 0, 92: 0, 93: 0, 94: 563,
                                 95: 1172, 96: 1011, 97: 1186, 98: 1021, 99: 1154, 100: 1531, 101: 1545, 102: 1549,
                                 103: 1561, 104: 1568, 105: 1578, 106: 1337, 107: 1291, 108: 1823, 109: 1850, 110: 1848,
                                 111: 1850, 112: 1851, 113: 1852, 114: 1854, 115: 1857, 116: 1861, 117: 1863, 118: 1868,
                                 119: 1874, 120: 1880, 121: 1888, 122: 1894, 123: 843, 124: 178, 125: 682, 126: 0,
                                 127: 431, 128: 272, 129: 0, 130: 0, 131: 450, 132: 443, 133: 435, 134: 374, 135: 402,
                                 136: 432, 137: 430, 138: 428, 139: 428, 140: 428, 141: 431, 142: 434, 143: 438,
                                 144: 445, 145: 458, 146: 380, 147: 448, 148: 397, 149: 553, 150: 399, 151: 175, 152: 0,
                                 153: 0, 154: 2473, 155: 1655, 156: 971, 157: 929, 158: 542, 159: 1440, 160: 1185,
                                 161: 841, 162: 917, 163: 883, 164: 856, 165: 819, 166: 799, 167: 775, 168: 754,
                                 169: 735, 170: 719, 171: 590, 172: 442, 173: 370, 174: 186, 175: 114, 176: 1594,
                                 177: 3701, 178: 3643, 179: 3583, 180: 3518, 181: 3458, 182: 2909, 183: 2153, 184: 3026,
                                 185: 3682, 186: 3658, 187: 3625, 188: 3282, 189: 2980, 190: 3725, 191: 3041, 192: 2749,
                                 193: 3336, 194: 2264, 195: 3104, 196: 2813, 197: 1474, 198: 1905, 199: 2467, 200: 2456,
                                 201: 2468, 202: 2453, 203: 1062, 204: 0, 205: 1735, 206: 2483, 207: 2486, 208: 2491,
                                 209: 2499, 210: 2507, 211: 2514, 212: 2522, 213: 2531, 214: 2543, 215: 556, 216: 801,
                                 217: 1789, 218: 2292, 219: 2320, 220: 2363, 221: 2384, 222: 2384, 223: 1869, 224: 0,
                                 225: 764, 226: 0, 227: 831, 228: 2512, 229: 1681, 230: 1083, 231: 2377, 232: 2332,
                                 233: 2273, 234: 2218, 235: 2158, 236: 2101, 237: 2048, 238: 1998, 239: 1955, 240: 1914,
                                 241: 1877, 242: 1842, 243: 1807, 244: 1774, 245: 1742, 246: 1712, 247: 1680, 248: 1655,
                                 249: 1630, 250: 1604, 251: 1581, 252: 1562, 253: 1541, 254: 1522, 255: 1506, 256: 1492,
                                 257: 1473, 258: 1456, 259: 1445, 260: 1433, 261: 1418, 262: 1405, 263: 1392, 264: 1378,
                                 265: 1366, 266: 1356, 267: 1346, 268: 1336, 269: 1328, 270: 1318, 271: 1309, 272: 1301,
                                 273: 1294, 274: 1287, 275: 1281, 276: 1276, 277: 1270, 278: 1266, 279: 1262, 280: 1258,
                                 281: 1254, 282: 1251, 283: 1249, 284: 1247, 285: 1245, 286: 1244, 287: 1242, 288: 1241,
                                 289: 1241, 290: 1249, 291: 1253, 292: 1236, 293: 1231, 294: 1232, 295: 1234, 296: 1236,
                                 297: 1237, 298: 1239, 299: 1245, 300: 1249, 301: 1252, 302: 1255, 303: 1262, 304: 1267,
                                 305: 1257, 306: 1278, 307: 1300, 308: 1307, 309: 1314, 310: 1321, 311: 1330, 312: 1337,
                                 313: 1347, 314: 1358, 315: 1369, 316: 1380, 317: 1392, 318: 1406, 319: 1408, 320: 1423,
                                 321: 1376, 322: 1340, 323: 1307, 324: 1274, 325: 1244, 326: 1214, 327: 1187, 328: 1159,
                                 329: 759, 330: 678, 331: 885, 332: 1066, 333: 1047, 334: 1028, 335: 1011, 336: 992,
                                 337: 980, 338: 971, 339: 955, 340: 941, 341: 926, 342: 913, 343: 905, 344: 892,
                                 345: 880, 346: 870, 347: 860, 348: 851, 349: 859, 350: 884, 351: 913, 352: 944,
                                 353: 976, 354: 824, 355: 496, 356: 812, 357: 969, 358: 960, 359: 955}

        def Connect(self):
            return self.running

        def StartScanning(self):
            while self.running:
                yield self.lidar_values.copy()

        def StopScanning(self):
            self.running = False

        def Disconnect(self):
            pass


def filter_values(values, distance):
    for winkel, wert in values.items():
        if winkel is None or wert is None:
            continue
        ang_last = (winkel - 1) % 360
        ang_next = (winkel + 1) % 360

        current = values.get(winkel)
        dist_last = values.get(ang_last)
        dist_next = values.get(ang_next)

        # wenn irgenein wert None
        if any([not current, not dist_last, not dist_next]):
            continue

        # x und y aktueller wert
        xc = math.cos(math.radians(winkel)) * wert
        yc = math.sin(math.radians(winkel)) * wert

        # x und y letzter wert
        xl = math.cos(math.radians(ang_last)) * dist_last
        yl = math.sin(math.radians(ang_last)) * dist_last

        # x und y nächster wert
        xn = math.cos(math.radians(ang_next)) * dist_next
        yn = math.sin(math.radians(ang_next)) * dist_next

        dl = math.sqrt((xc - xl) ** 2 + (yc - yl) ** 2)
        dn = math.sqrt((xc - xn) ** 2 + (yc - yn) ** 2)

        if dl > distance and dn > distance:
            values[winkel] = None

    return values


def draw_values(screen, values):
    points = []
    sx, sy = screen.get_size()
    for angle, distance in values.items():
        winkel = math.radians(angle)
        if values[angle] is not None:
            x = math.cos(winkel) * distance
            y = math.sin(winkel) * distance
            points.append((x / 10 + sx / 2, y / 10 + sy / 2))
    screen.fill((0, 0, 0))
    for point in points:
        pygame.draw.circle(screen, (170, 170, 170), point, 5)
    pygame.draw.circle(screen, (255, 0, 0), (sx / 2, sy / 2), 10)
    pygame.display.flip()


def main():
    lidar = PyLidar3.YdLidarG4("com15")
    pygame.init()
    pygame.display.set_caption("Shenzhen Lidar")
    screen = pygame.display.set_mode((1000, 1000))

    try:
        if lidar.Connect():
            print("verbunden")
            gen = lidar.StartScanning()
            t = time.time()
            filter_dist = 100
            while (time.time() - t) < 30:
                rendering = {}
                data = next(gen)
                filtered = filter_values(data, filter_dist)

                draw_values(screen, filtered)

                # selbes wie time.sleep(1) nur mit pygame event handler
                tw = time.time() + 1
                while (time.time() - tw) < 0:
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_ESCAPE:
                                raise KeyboardInterrupt
                            elif event.key == pygame.K_UP:
                                filter_dist += 10
                                print("Filter Value:", filter_dist)
                            elif event.key == pygame.K_DOWN:
                                filter_dist -= 10
                                print("Filter Value:", filter_dist)
                        if event.type == pygame.QUIT:
                            raise KeyboardInterrupt

    except KeyboardInterrupt:
        lidar.StartScanning()
        lidar.Disconnect()


if __name__ == "__main__":
    main()
