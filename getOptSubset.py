import numpy as np

def getOptSubset(a=np.array([0.39655862, 0.89264548, 0.45199725, 0.42657046, 0.39709303,
       0.7272395 , 0.09417599, 0.78766142, 0.45848148, 0.08820034]),b=np.array([0.70287222, 0.47727187, 0.25146845, 0.67415466, 0.83229899,
       0.66127568, 0.5832867 , 0.34142671, 0.4345677 , 0.75122681]),M=5, maxmin='max'):
    """
    This function computes the subset S of size M which optimizes the
    ratio of the sums of a(S) and b(S)
    :param a: vector of positive numbers
    :param b: vector of positive numbers
    :param M: size of the subset S
    :return: A subset of size M.
    """

    N = len(a)

    if(maxmin=='min'):
        t = np.array(a)
        a = np.array(b)
        b = np.array(t)

    if((a<=0).any() or (b<=0).any()):
        print('Only positive numbers allowed!')
        return
    if(len(a)!=len(b)):
        print('Length of vectors a and b are different!')
        return
    if (M>len(a)):
        print('Size of subset cannot exceed the size of the set!')
        return

    l = 0
    r = np.sum(np.sort(a)[-M:])/np.sum(np.sort(b)[:M])

    for k in range(N):
        xl = r - 0.618*(r-l)
        xr = l + 0.618*(r - l)
        fl, tmp = getVal(a,b,xl,M)
        fl = fl**2
        fr, tmp = getVal(a, b, xr, M)
        fr = fr**2
        if(fl>=fr):
            l = xl
        else:
            r = xr

    f, subs = getVal(a,b,0.5*(l+r),M)
    print('The optimal subset consists of the ' + str(np.sort(subs)) + ' elements.')
    print('The optimal value is: ' + str(np.sum(a[subs])/np.sum(b[subs])))

def getVal(a,b,x,M):
    """
    :param a: Array of positive numbers.
    :param b: Array of positive numbers.
    :param x: A float at which SUM(a[k]-xb[k]) needs to be calculated.
    :param M: An integer between 1 and len(a).
    :return: A float value equal to SUM(a[k]-xb[k]).
    """
    N = len(a)
    allvals = np.zeros(N)
    for k in range(N):
        allvals[k] = a[k] - x*b[k]

    return np.sum(np.sort(allvals)[-M:]), np.argsort(allvals)[-M:]