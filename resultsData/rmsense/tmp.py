import numpy as np
import matplotlib.pylab as pl
from sklearn.manifold import TSNE


data = np.random.random((1000,50))

model = TSNE(n_components=2, random_state=0)
x, y = model.fit_transform(data).T

fig, ax = pl.subplots(figsize=(15, 15))

# nice points
#scatter = ax.scatter(x, y, alpha=0.2, color='k', facecolor='none', s=100)

# invisible points
scatter = ax.scatter(x, y, alpha=0.)

for i in range(0, 50):
	ax.text(x[i], y[i], "red"+str(i), color='r', fontsize=14)


for i in range(50, 100):
	ax.text(x[i], y[i], "green"+str(i), color='g', fontsize=14)


ax.set_xticks([])
ax.set_yticks([])


pl.tight_layout()

​

