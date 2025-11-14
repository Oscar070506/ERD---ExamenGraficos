import pandas as pd
import matplotlib.pyplot as plt

data = {
    "productes": ["Cafè", "Croissant", "Suc", "Sandvitx", "Pastís"],
    "vendes": [120, 85, 60, 45, 75]
}

df = pd.DataFrame(data)

# Gráfico de barras mejorado
plt.figure(figsize=(8,5))
bars = plt.bar(df['productes'], df['vendes'], color=["#A50101","#00458A","#00A000","#F59C44","#720081"])
plt.title("Productos y Ventas", fontsize=16, fontweight='bold')
plt.xlabel("Producto", fontsize=12)
plt.ylabel("Ventas", fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)

for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 20, f'{yval}', ha='center', fontsize=10)

plt.show()