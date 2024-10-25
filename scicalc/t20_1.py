import numpy as np
import matplotlib.pyplot as plt


def sequance_a_n(n):
    s = 0
    z = 1
    for i in range(n):
        s += z 
        z *= -2/3
    return s


def verify(e, a, b):
    c = abs(a - b) < e
    k = - 1
    for i in range(c.size):
        if c[i] == True:
            k = i
            break
    if k != -1:
        cc = c[k:c.size]
        if np.all(cc):
            print('sequence convergence, number of convergenced sequence is', k)
            return k
        else:
            print('sequence do not convergent')
    else:
        print('sequence do not convergent')
        return -1


def movespinesticks():
    '''Move axes
    '''
    ax = plt.gca()  # отримати поточний об'єкт класу axes
    # зробити праву та верхню осі невидимими:
    ax.spines['top'].set_color('none')
    ax.spines['right'].set_color('none')
    # перенести нижню вісь у позицію y=0:
    ax.xaxis.set_ticks_position('bottom')
    ax.spines['bottom'].set_position(('data', 0))
    # перенести ліву вісь у позицію x == 0:
    ax.yaxis.set_ticks_position('left')
    ax.spines['left'].set_position(('data', 0))


if __name__ == '__main__':
    e = 0.01
    b = 3/5
    n = int(input('Number of elements: '))

    a = np.array([sequance_a_n(i) for i in range(1, n)])
    nn = np.array([i for i in range(1, n)])

    k = verify(e, a, b)

    bb = np.ones(nn.size) * b
    movespinesticks()
    plt.plot(nn, a, ':b')  # створити графік
    plt.xlabel('n')
    plt.ylabel('a_n')
    plt.title('sequance а_n')
    plt.plot(nn, bb, 'r')
    plt.plot(nn, bb - e, '--g')
    plt.plot(nn, bb + e, '--g')
    plt.grid(True)
    plt.show()
