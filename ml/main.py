import pickle
import pandas as pd

from sklearn.model_selection import train_test_split as tts
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

# data
df = pd.read_csv("./stroke.csv")

# drop bugged rows
df = df.dropna()

# labels and features
labels = df['stroke']
features = df.drop(columns=['stroke'], axis=0)
features = pd.get_dummies(features) # one-hot encoding

# train test split operation
Xtrain, Xtest, Ytrain, Ytest = tts(features, labels, test_size=0.20, random_state=42)

# classifier is a support vector machine
clf = make_pipeline(StandardScaler(), SVC(gamma='auto'))
clf.fit(Xtrain, Ytrain)

print(clf.score(Xtest, Ytest))

# save model
pkl_filename = "support_vector_stoke.pkl"
with open(pkl_filename, "wb") as f:
    pickle.dump(clf, f)
