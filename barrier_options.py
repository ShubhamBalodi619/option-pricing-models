#!/usr/bin/env python
# coding: utf-8

# In[65]:


# Importing libraries

import numpy as np


# In[91]:


# Defining the input variables

So= 526.41            # Current stock price
K= 500                # Strike price
T= 0.169863014        # Time to maturity in years
H= 550                #Barrier price
Rf= 0.02              # Risk-free rate of return
vol= 0.1742           # Annualized volatility
N= 4                  # No. of time steps
opttype= "c"          # Option type


# In[101]:


def binomial_tree_barrier(So, K, T, H, Rf, vol, N, opttype="c"):
    """
    European-style up-and-out barrier option using binomial tree.
    """
    dt= T/N       # Length of a time step

    u= np.exp(vol*np.sqrt(dt))        # Up-move factor
    d=1/u                            # Down-move factor

    p= (np.exp(Rf * dt)-d)/(u-d)     # Probability of an up-move 

    disc_factor= np.exp(-Rf * dt)    # Discount factor

    # Initialising the asset prices at maturity (t= N)
    S= np.zeros(N+1)
    for j in range(0,N+1):
        S[j]= So * (u ** j) * (d**(N-j))

    # Initialising the option values at maturity (t= N)
    O= np.zeros(N+1)
    for j in range(N+1):
        if opttype=="c":
            O[j]= np.maximum(S[j]-K,0)
        elif opttype=="p":
            O[j]= np.maximum(K-S[j],0)
        else:
            print("Please confirm all the parameters!!!!!!!!!!!!!!")
            return None

    # Checking terminal condition payoff
    for i in range(N+1):
        if S[i]>H:
            O[i]=0

    # Backward induction
    for i in range(N-1, -1, -1):
        for j in range(0,i+1):
            St= So * (u ** j) * (d**(i-j))
            if St>=H:
                O[j]=0
            else:
                O[j]= disc_factor * (O[j+1] * p + O[j] * (1-p))

    return O[0]


# In[103]:


binomial_tree_barrier(So, K, T, H, Rf, vol, N, opttype="c").round(2)


# In[ ]:





# In[ ]:





# In[ ]:




