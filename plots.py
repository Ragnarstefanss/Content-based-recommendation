import seaborn as sns
import pandas as pd
import matplotlib as mpl
import numpy as np
 
import matplotlib.pyplot as plt

def plot_photo(title, dataframe):
    df = pd.DataFrame(dataframe, columns=["x", "y", "category"])

    ax = sns.lineplot('x', 'y', data=df, hue='category', style='category', markers={'Content Based': 'X', 'Collaborative filtering': 's', 'Hybrid recommendation': 'o'},  dashes=False,)
    ax.set_title(title)
    ax.set_ylabel(title)
    ax.set_xlabel("Number of inputs")

    #ax.legend(ax.get_lines(), df.columns, loc='best')
    plt.show()

    
accuracy = [
      [60, 0.71,"Content Based"],
      [80, 0.68,"Content Based"],
      [100, 0.64,"Content Based"],
      [120, 0.63,"Content Based"],
      [160, 0.59,"Content Based"],
      [200, 0.51,"Content Based"],
      [250, 0.49,"Content Based"],

      [60, 0.82,"Collaborative filtering"],
      [80, 0.83,"Collaborative filtering"],
      [100, 0.84,"Collaborative filtering"],
      [120, 0.81,"Collaborative filtering"],
      [160, 0.79,"Collaborative filtering"],
      [200, 0.71,"Collaborative filtering"],
      [250, 0.69,"Collaborative filtering"],

      [60, 0.94,"Hybrid recommendation"],
      [80, 0.91,"Hybrid recommendation"],
      [100, 0.87,"Hybrid recommendation"],
      [120, 0.85,"Hybrid recommendation"],
      [160, 0.81,"Hybrid recommendation"],
      [200, 0.73,"Hybrid recommendation"],
      [250, 0.72,"Hybrid recommendation"],
]



precision = [
    [60, 0.68, "Content Based"],
    [80, 0.65, "Content Based"],
    [100, 0.61, "Content Based"],
    [120, 0.59, "Content Based"],
    [160, 0.55, "Content Based"],
    [200, 0.48, "Content Based"],
    [250, 0.46, "Content Based"],

    [60, 0.85, "Collaborative filtering"],
    [80, 0.84, "Collaborative filtering"],
    [100, 0.83, "Collaborative filtering"],
    [120, 0.80, "Collaborative filtering"],
    [160, 0.76, "Collaborative filtering"],
    [200, 0.68, "Collaborative filtering"],
    [250, 0.68, "Collaborative filtering"],

    [60, 0.89, "Hybrid recommendation"],
    [80, 0.88, "Hybrid recommendation"],
    [100, 0.83, "Hybrid recommendation"],
    [120, 0.82, "Hybrid recommendation"],
    [160, 0.78, "Hybrid recommendation"],
    [200, 0.71, "Hybrid recommendation"],
    [250, 0.70, "Hybrid recommendation"],
]


recall = [
    [60, 0.55, "Content Based"],
    [80, 0.55, "Content Based"],
    [100, 0.52, "Content Based"],
    [120, 0.47, "Content Based"],
    [160, 0.43, "Content Based"],
    [200, 0.35, "Content Based"],
    [250, 0.34, "Content Based"],

    [60, 0.84, "Collaborative filtering"],
    [80, 0.81, "Collaborative filtering"],
    [100, 0.78, "Collaborative filtering"],
    [120, 0.76, "Collaborative filtering"],
    [160, 0.70, "Collaborative filtering"],
    [200, 0.63, "Collaborative filtering"],
    [250, 0.62, "Collaborative filtering"],

    [60, 0.88, "Hybrid recommendation"],
    [80, 0.85, "Hybrid recommendation"],
    [100, 0.85, "Hybrid recommendation"],
    [120, 0.81, "Hybrid recommendation"],
    [160, 0.77, "Hybrid recommendation"],
    [200, 0.69, "Hybrid recommendation"],
    [250, 0.70, "Hybrid recommendation"],
]

f_measure = [
    [60, 0.608, "Content Based"],
    [80, 0.596, "Content Based"],
    [100, 0.561, "Content Based"],
    [120, 0.523, "Content Based"],
    [160, 0.483, "Content Based"],
    [200, 0.405, "Content Based"],
    [250, 0.391, "Content Based"],

    [60, 0.845, "Collaborative filtering"],
    [80, 0.825, "Collaborative filtering"],
    [100, 0.804, "Collaborative filtering"],
    [120, 0.779, "Collaborative filtering"],
    [160, 0.729, "Collaborative filtering"],
    [200, 0.654, "Collaborative filtering"],
    [250, 0.649, "Collaborative filtering"],

    [60, 0.885, "Hybrid recommendation"],
    [80, 0.865, "Hybrid recommendation"],
    [100, 0.840, "Hybrid recommendation"],
    [120, 0.815, "Hybrid recommendation"],
    [160, 0.775, "Hybrid recommendation"],
    [200, 0.700, "Hybrid recommendation"],
    [250, 0.700, "Hybrid recommendation"],
]



plot_photo("Accuracy", accuracy)
#plot_photo("Precision", precision)
#plot_photo("Recall", recall)
#plot_photo("F-Measure", f_measure)