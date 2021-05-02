import matplotlib.pyplot as plt
labels='USA','India','Brazil','Russia','UK'
sizes=29862124,11285561,11205972,4360823,4234924
colors='lightgreen','gold','lightskyblue','lightcoral','purple'
explode=0,0,0,0,0
plt.pie(sizes,explode=explode.labels=labels,
        colors=colors,autopct='%1.1f%%',shadow=True,startangle=50)
plt.axis('equal')
plt.show()
