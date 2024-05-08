import matplotlib.pyplot as plt
from matplotlib.markers import MarkerStyle

fig, ax = plt.subplots()

# Zeige den ursprünglichen "d"-Marker
plt.scatter([1, 2, 3], [1, 2, 3], s=225, marker="v")

# Erstelle einen neuen "D"-Marker und skaliere ihn
m = MarkerStyle("v")
m._transform.scale(1.0, 0.6)
plt.scatter([1, 2, 3], [2, 3, 4], s=225, marker=m, color="crimson")

# Drehe den "d"-Marker um 60 Grad
m = MarkerStyle("v")
m._transform.rotate_deg(60)
plt.scatter([1, 2, 3], [3, 4, 5], s=225, marker=m, color="limegreen")

plt.margins(0.5)
plt.show()
