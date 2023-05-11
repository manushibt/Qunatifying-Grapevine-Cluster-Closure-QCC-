import pandas as pd
import numpy as np

path = ".../"
dfc = pd.read_csv(path+"result.csv")

#Calculate mean and median
dfc.groupby("Date").mean()
dfc.groupby("Date").median()

#Calculate minimum, maximum and standard deviation
np.min(dfc["Clust_Clos"])
np.std(dfc["Clust_Clos"])
np.max(dfc["Clust_Clos"])
