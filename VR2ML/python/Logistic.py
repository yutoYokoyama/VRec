import pandas as pd
from sklearn.linear_model import LogisticRegression
import pickle
import sys
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE

FileName = str(sys.argv[1])
imageType = str(sys.argv[2])
makeModel = int(sys.argv[3])
saveFileName = str(sys.argv[4]) if len(sys.argv) > 4 else FileName
df = pd.read_csv(FileName+".csv", header=None)
dataCount = df[1][0]

if makeModel == 0:
    x = df.drop(df.columns[[0, 1, dataCount + 2]], axis=1).values
    model = LogisticRegression()
    y = df[dataCount+2]
    model.fit(x, y)
    pickle.dump(model, open(saveFileName+".sav", 'wb'))
    print("LogisticRegressionModelMakeSuccessed")
else:
    if len(df.columns) > dataCount+2:
        x = df.drop(df.columns[[0, 1, dataCount + 2]], axis=1).values
    else:
        x = df.drop(df.columns[[0, 1]], axis=1).values
    loaded_model = pickle.load(open(saveFileName+".sav", 'rb'))
    y = loaded_model.predict(x)
    print(y)


colorSet = ["red", "green", "blue", "cyan", "magenta", "navy", "black", "orange", "silver", "pink"]#"rgbcmyk"
if imageType == "1":
    pca = PCA(n_components=2)
    pca.fit_transform(x)
    data_pca = pca.fit_transform(x)
    # 図として表示します
    for i in range(len(data_pca)):
        plt.scatter(data_pca[i][0], data_pca[i][1], c=colorSet[y[i]])
    plt.savefig(FileName + "_LogisticRegression_pca.png")
elif imageType == "2":
    t_sne = TSNE()
    t_sne_data = t_sne.fit_transform(x)
    for i in range(len(t_sne_data)):
        plt.scatter(t_sne_data[i, 0], t_sne_data[i, 1], c=colorSet[y[i]])
    plt.savefig(FileName + "_LogisticRegression_t_sne.png")

