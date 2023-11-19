import matplotlib.pyplot as plt
from matplotlib.ticker import StrMethodFormatter
import math

x1=12
x2=61
y1=30
y2=-45

naire=1.00
ndiamante=2.42

velLuz=3.00*pow(10,8)
velEnDiamante=velLuz/ndiamante
angulo1=[]
angulo2=[]
tiempo=[]

for x in range (70):
    t=((math.sqrt(pow(x1-x,2)+pow(y1,2))/velLuz)+(math.sqrt(pow(x2-x,2)+pow(y2,2))/velEnDiamante))
    angulo1.append(abs(math.degrees(math.atan((x1-x)/y1))))
    angulo2.append(abs(math.degrees(math.atan((x2-x)/y2))))   
    tiempo.append(t)


#SNELL: n1 sen1 = n2 sen 2
for i in range(70):
    if(tiempo[i]==min(tiempo)):
        print(f'angulo 1: {angulo1[i]}')
        print(f'angulo 2: {angulo2[i]}')
        print(f'tiempo minimo: {tiempo[i]}')
        print(f'sin/sin: {math.sin(angulo1[i])/math.sin(angulo2[i])}')

x=range(70)

# Crear la gráfica
plt.figure(figsize=(8, 6))  # Tamaño de la figura

# Agregar los datos a la gráfica
plt.plot(x, tiempo, marker='o')
plt.gca().xaxis.set_major_formatter(StrMethodFormatter('{x:.1f}'))


# Etiquetas de los ejes
plt.xlabel('x (m)')
plt.ylabel('t (s)')

# Título de la gráfica
plt.title('Gráfica x vs t')

# Mostrar la gráfica
plt.grid(True)  # Mostrar cuadrícula
plt.show()
