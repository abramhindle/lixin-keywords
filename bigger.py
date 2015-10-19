import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt(file("bigger.csv"), delimiter=",",dtype=str)
rownames = data[1:,0]
colnames = data[0,1:]
rows = data[1:,1:].astype(int)

# now normalize it
rowsum = 1.0/np.sum(rows,axis=1)
rowsum = rowsum.reshape((rowsum.shape[0],1))
norm_rows = np.nan_to_num(rowsum * rows)


def plotit(prefix, rownames, colnames, rows):
    fig, ax = plt.subplots()
    n = len(rownames)
    data = rows
    masked_array = np.ma.array (data, mask=np.isnan(data))

    ax.set_yticks(np.arange(data.shape[0])+0.5, minor=False)
    ax.xaxis.tick_top()
    ax.set_xticks(np.arange(data.shape[1])+0.5, minor=False)
    #ax.imshow(data, interpolation='none')
    heatmap = ax.pcolor(data, cmap=plt.cm.Blues)
    ax.set_yticklabels(rownames.tolist())
    ax.set_xticklabels(colnames.tolist(), rotation=40, ha='left')
    ax.invert_yaxis()
    #ax.set_xticklabels(x_labels)
    fig.set_size_inches(20, 20)
    plt.savefig('%s-matrix.png' % prefix)
    plt.savefig('%s-matrix.pdf' % prefix)
    # plt.show()

plotit("bigger",rownames, colnames, rows)
plotit("bigger-norm",rownames, colnames, norm_rows)