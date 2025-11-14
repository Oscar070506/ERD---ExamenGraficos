import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

notes = np.random.randint(0, 11, 30)
df = {'x': notes}

sns.histplot(x = notes, kde = True,
             line_kws = {'linestyle':'dashed',
                         'linewidth':'2'}).lines[0].set_color('red') 

plt.title('Distribució de les notes de l\'exàmen', fontsize=16)
plt.xlabel('Nota', fontsize=14)
plt.ylabel('Cuantitat', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.5)

plt.show()
