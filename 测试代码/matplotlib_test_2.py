# encoding=utf-8
import numpy as np


def main():
    # scatter#散点图
    import matplotlib.pyplot as plt
    fig = plt.figure()
    ax = fig.add_subplot(3, 3, 1)
    n = 128
    X = np.random.normal(0, 1, n)
    Y = np.random.normal(0, 1, n)
    T = np.arctan2(X, Y)
    # plt.axes([0.025,0.025,0.95,0.95])
    ax.scatter(X, Y, s=75, c=T, alpha=.5)
    plt.xlim(-1.5, 1.5), plt.xticks([])
    plt.ylim(-1.5, 1.5), plt.yticks([])
    plt.axis()
    plt.title("scatter")
    plt.xlabel("x")
    plt.ylabel("y")
    # plt.show()
    # bar柱状图
    ax = fig.add_subplot(332)
    n = 10
    X = np.arange(n)
    Y1 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)
    Y2 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)
    ax.bar(X, +Y1, facecolor='#9999ff', edgecolor='white')
    ax.bar(X, -Y2, facecolor='#ff9999', edgecolor='white')
    for x, y in zip(X, Y1):
        plt.text(x + 0.4, y + 0.05, '%.2f' % y, ha='center', va='bottom')
    for x, y in zip(X, Y2):
        plt.text(x + 0.4, -y - 0.05, '%.2f' % y, ha='center', va='top')
    # Pie 饼图
    fig.add_subplot(333)
    n = 20
    Z = np.ones(n)
    Z[-1] *= 2
    plt.pie(Z, explode=Z * .05, colors=['%f' % (i / float(n)) for i in range(n)],
            labels=['%.2f' % (i / float(n)) for i in range(n)])
    plt.gca().set_aspect('equal')
    plt.xticks([]), plt.yticks([])
    #polar 极值图
    fig.add_subplot(334,polar=True)
    n=20
    theta=np.arange(0.0,2*np.pi,2*np.pi/n)
    radii=10*np.random.rand(n)
    # plt.plot(theta,radii)
    plt.polar(theta,radii)
    #heatmap热图
    fig.add_subplot(335)
    from matplotlib import cm
    data=np.random.rand(3,3)
    cmap=cm.Blues
    map=plt.imshow(data,interpolation='nearest',cmap=cmap,aspect='auto',vmin=0,vmax=1)
    #3D图
    from mpl_toolkits.mplot3d import Axes3D
    ax=fig.add_subplot(336,projection="3d")
    ax.scatter(1,1,3,s=100)
    #hot map 热力图
    fig.add_subplot(313)
    def f(x,y):
        return(1-x/2+x**5+y**3)*np.exp(-x**2-y**2)
    n=256
    x=np.linspace(-3,3,n)
    y=np.linspace(-3,3,n)
    X,Y=np.meshgrid(x,y)
    plt.contourf(X,Y,f(X,Y),8,alpha=.75,cmap=plt.cm.hot)
    plt.savefig("./data/fig.png")
    
    plt.show()

if __name__ == "__main__":
    main()
