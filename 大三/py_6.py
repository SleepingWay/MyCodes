import sklearn
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans

A = np.random.randint(0, 30, (100, 2))
data = pd.DataFrame(A)

writer = pd.ExcelWriter('E01914008.xlsx')
data.to_excel(writer, 'page_1', float_format='%.5f')
writer.save()
writer.close()

data = pd.read_csv(r"D:\Pycharm\pythoncode\pythonProject1\E01914008.xlsx")
data.dropna(inplace=True)
data.head()

see = []
for k in range(1,20):
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(data[['0','1']])
    see.append(kmeans.inertia_)
fig = plt.figure(figsize=(20, 6))
plt.xlabel("Number of clusters")
plt.ylabel("Distortion")
plt.plot(range(1,20),see)
plt.show()

kmeans = KMeans(n_clusters = 4)

kmeans.fit(data[['0','1']])

data['label'] = kmeans.labels_
data.groupby('label').size()
from sklearn.preprocessing import StandardScaler
while True:
    odd = kmeans.labels_
    data_scaled = StandardScaler().fit_transform(data[['0','1']])

    kmeans.fit(data_scaled)
    if odd.all() == kmeans.labels_.all():
        break
data['label_standarer'] = kmeans.labels_
print(data)
