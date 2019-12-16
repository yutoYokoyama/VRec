from sklearn.neighbors import KNeighborsClassifier
import sys
import pandas as pd
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
FileName = str(sys.argv[1])
cluster = int(sys.argv[3]) if len(sys.argv) > 3 else 3
cluster = 10 if cluster > 10 else cluster
imageType = str(sys.argv[2])

pd.set_option('display.max_rows', 10000)

data = pd.read_csv(FileName+".csv", header=None)
data = data.drop(data.columns[[0, 1]], axis=1)

clustering = KNeighborsClassifier(cluster, random_state=10).fit_predict(data)
print(clustering)

colorSet = ["red", "green", "blue", "cyan", "magenta", "navy", "black", "orange", "silver", "pink"]#"rgbcmyk"
pca = PCA(n_components=2)
pca.fit_transform(data)

if imageType == "1":
    data_pca = pca.fit_transform(data)
    # 図として表示します
    for i in range(len(data_pca)):
        plt.scatter(data_pca[i][0], data_pca[i][1], c=colorSet[clustering[i]])
    plt.savefig(FileName + "_k_nn_pca.png")
elif imageType == "2":
    t_sne = TSNE()
    t_sne_data = t_sne.fit_transform(data)
    for i in range(len(t_sne_data)):
        plt.scatter(t_sne_data[i, 0], t_sne_data[i, 1], c=colorSet[clustering[i]])
    plt.savefig(FileName + "_k_nn_t_sne.png")

