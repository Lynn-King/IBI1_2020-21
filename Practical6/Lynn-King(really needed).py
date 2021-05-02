# task 1
# the pie chart
import matplotlib.pyplot as plt
labels='USA','India','Brazil','Russia','UK'
sizes=29862124,11285561,11205972,4360823,4234924
colors='lightgreen','gold','lightskyblue','lightcoral','purple'
explode=0,0,0,0,0
plt.pie(sizes,explode=explode,labels=labels,
        colors=colors,autopct='%1.1f%%',shadow=True,startangle=50)
plt.axis('equal')
plt.show()
# the dictionary
countries={'USA':29862124,'India':11285561,'Brazil':11205972,'Russia':4360823,'UK':4234924}
print(countries)

# task 2
# the list
gene_lengths=[9410,394141,4442,105338,19149,76779,126550,36296,842,15981]
print(gene_lengths)
# the boxplot
import matplotlib.pyplot as plt
data=[51,1142,42,216,25.650,32533,57,1,523]
plt.boxplot(x=data)
plt.ylim(0,2500)
plt.show()
