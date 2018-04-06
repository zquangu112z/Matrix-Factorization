import matplotlib.pyplot as plt


def draw_graph(R):
    for i in xrange(len(R)):
        for j in xrange(len(R[0])):
            plt.plot(R[i][j], 'ro')
            print(R[i][j])
    plt.show()
