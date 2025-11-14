import pandas as pd
import matplotlib.pyplot as plt

dades = {
    "Edat": [16, 17, 16, 18, 17, 19, 18, 17],
    "Nota": [6.5, 7.0, 5.5, 8.0, 6.0, 9.0, 7.5, 8.5]
}

df = pd.DataFrame(dades)

plt.figure(figsize=(8,6))
scatter = plt.scatter(df['Edat'], df['Nota'], 
                      color='#1f77b4', 
                      edgecolor='black', 
                      s=100,
                      label='Alumnes')  

plt.title('Gràfic de dispersió de Notes FINALS vs Edats', fontsize=16)
plt.xlabel('Edat', fontsize=14)
plt.ylabel('Nota', fontsize=14)

plt.legend(title='Leyenda')

plt.grid(True, linestyle='--', alpha=0.5)
plt.show()