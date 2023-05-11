import pandas as pd
import numpy as np

path = ""
dfc = pd.read_csv("F:/Cornell/Cluster_closure/2023/Project_Data/results/CF_PSP_Date.csv")
df1 = pd.read_csv("F:/Cornell/Cluster_closure/2023/Project_Data/results/PGRIS_PSP_Date.csv")

dfr = df1[df1["Cultivar"] == "Riesling"]
dfpg = df1[df1["Cultivar"] == "Pinot gris"]

import seaborn as sns

ax = sns.catplot(
    data=dfr, x="Timestep", y="Clust_Clo",
    zorder=1, color= "Black"
)
ax = sns.regplot(
    data=dfr, x="Timestep", y="Clust_Clo",
    scatter=False, truncate=False, order=2, color=".2",
)
ax.set(ylabel ="% cluster closure", xlabel = "Timestep")
ax.set_ylim(10, 100)
ax1 = sns.catplot(
    data=dfpg, x="Timestep", y="Clust_Clo",
    zorder=1, color= "Black"
)
ax1 = sns.regplot(
    data=dfpg, x="Timestep", y="Clust_Clo",
    scatter=False, truncate=False, order=2, color=".2",
)
ax1.set(ylabel ="% cluster closure", xlabel = "Timestep")
ax1.set_ylim(10, 100)

ax2 = sns.catplot(
    data=dfc, x="Timestep", y="Clust_Clos",
    zorder=1, color= "Black"
)
ax2 = sns.regplot(
    data=dfc, x="Timestep", y="Clust_Clos",
    scatter=False, truncate=False, order=2, color=".2",
)
ax2.set(ylabel ="% cluster closure", xlabel = "Timestep")
ax2.set_ylim(10, 100)

dfc.groupby("Date").median()
dfr.groupby("Date").median()
dfpg.groupby("Date").median()

np.min(dfc["Clust_Clos"])
np.min(dfr["Clust_Clo"])
np.min(dfpg["Clust_Clo"])

np.max(dfc["Clust_Clos"])
np.max(dfr["Clust_Clo"])
np.max(dfpg["Clust_Clo"])