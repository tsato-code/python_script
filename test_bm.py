"""
ref.: https://stats.stackexchange.com/questions/7257/learning-weights-in-a-boltzmann-machine/132555#132555
"""
import numpy as np


def extract_patches(im,SZ,n):
    imsize,imsize=im.shape;
    X=np.zeros((n,SZ**2),dtype=np.int8);
    startsx= np.random.randint(imsize-SZ,size=n)
    startsy=np.random.randint(imsize-SZ,size=n)
    for i,stx,sty in zip(xrange(n), startsx,startsy):
        P=im[sty:sty+SZ, stx:stx+SZ];
        X[i]=2*P.flat[:]-1;
    return X.T


def sample(T,b,n,num_init_samples):
    """
    sample.m - sample states from model distribution

    function S = sample(T,b,n, num_init_samples)

    T:                weight matrix
    b:                bias
    n:                number of samples
    num_init_samples: number of initial Gibbs sweeps
    """
    N=T.shape[0]

    # initialize state vector for sampling
    s=2*(np.random.rand(N)<sigmoid(b))-1

    for k in xrange(num_init_samples):
        s=draw(s,T,b)

    # sample states
    S=np.zeros((N,n))
    S[:,0]=s
    for i in xrange(1,n):
        S[:,i]=draw(S[:,i-1],T,b)

    return S

def sigmoid(u):
    """
    sigmoid.m - sigmoid function

    function s = sigmoid(u)
    """
    return 1./(1.+np.exp(-u));

def draw(Sin,T,b):
    """
    draw.m - perform single Gibbs sweep to draw a sample from distribution

    function S = draw(Sin,T,b)

    Sin:      initial state
    T:        weight matrix
    b:        bias
    """
    N=Sin.shape[0]
    S=Sin.copy()
    rand = np.random.rand(N,1)
    for i in xrange(N):
        h=np.dot(T[i,:],S)+b[i];
        S[i]=2*(rand[i]<sigmoid(h))-1;

    return S

def run(im, T=None, b=None, display=True,N=4,num_trials=100,batch_size=100,num_init_samples=10,eta=0.1):
    SZ=np.sqrt(N);
    if T is None: T=np.zeros((N,N)); # weight matrix
    if b is None: b=np.zeros(N); # bias

    for t in xrange(num_trials):
        print t, num_trials
        # data statistics (clamped)
        X=extract_patches(im,SZ,batch_size).astype(np.float);
        R_data=np.dot(X,X.T)/batch_size;
        mu_data=X.mean(1);

        # prior statistics (unclamped)
        S=sample(T,b,batch_size,num_init_samples);
        R_prior=np.dot(S,S.T)/batch_size;
        mu_prior=S.mean(1);

        # update params
        deltaT=eta*(R_data - R_prior);
        T=T+deltaT;

        deltab=eta*(mu_data - mu_prior);
        b=b+deltab;
    return T, b
    

if __name__ == "__main__": 
    A = np.array([\
    [0.,1.,1.,0],
    [1.,1.,0, 0],
    [1.,1.,1.,0],
    [0, 1.,1.,1.],
    [0, 0, 1.,0]
    ])
    T,b = run(A,display=False)
    print T
    print b