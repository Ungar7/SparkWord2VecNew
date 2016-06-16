import numpy as np
import matplotlib.pylab as pl
import sys
from sklearn.manifold import TSNE
from tempfile import TemporaryFile

data = np.loadtxt("vec.txt")
print(data.shape)
data = data[:100]
label=map(lambda s:s.strip(), open("word.txt").readlines())

model = TSNE(n_components=2, random_state=0)
x, y = model.fit_transform(data).T

fig, ax = pl.subplots(figsize=(15, 15))

# nice points
#scatter = ax.scatter(x, y, alpha=0.2, color='k', facecolor='none', s=100)

# invisible points
scatter = ax.scatter(x, y, alpha=0.)

for i in range(0, 5):
	ax.text(x[i], y[i], label[i], color='r', fontsize=14)



ax.set_xticks([])
ax.set_yticks([])

pl.tight_layout()

pl.show()


for i in range(50, 100):
	ax.text(x[i], y[i], label[i], color='g', fontsize=14)

