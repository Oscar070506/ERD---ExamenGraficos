import pandas as pd
import matplotlib.pyplot as plt

dies = ["Dl", "Dt", "Dc", "Dj", "Dv", "Ds", "Dg"]
temperatures = [14, 15, 17, 18, 19, 20, 16]

plt.figure(figsize=(10,5))
plt.plot(dies, temperatures, marker='o', linestyle='-', color='orange', linewidth=2, markersize=8, label="Temperatura")
plt.title("Temperatura de la Semana", fontsize=16, fontweight='bold')
plt.xlabel("Días", fontsize=12)
plt.ylabel("Temperatura (°C)", fontsize=12)
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend(fontsize=12)

for i, temp in enumerate(temperatures):
    plt.text(i, temp + 2, str(temp), ha='center', fontsize=10)


plt.show()
