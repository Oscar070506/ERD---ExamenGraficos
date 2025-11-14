import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Categories": ["Menjar", "Transport", "Oci", "Altres"],
    "Despesa": [250, 60, 90, 40]
}

df = pd.DataFrame(data)

plt.pie(df["Despesa"], labels=df["Categories"], autopct="%1.1f%%", startangle=90)
plt.title("Distribución de la despesa mensual", color='red')
plt.show()
