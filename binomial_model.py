import numpy as np

# Defining the input variables
So= 526.41            # Current stock price
K= 500                # Strike price
T= 0.169863014        # Time to maturity in years
Rf= 0.02              # Risk-free rate of return
vol= 0.1742           # Annualized volatility
N= 4                  # No. of time steps
opt_style= "e"        # Option style- American or European
opt_type= "p"         # Option type- call or put

# Defining the model
def binomial_tree(So, K, T, Rf, vol, N, opt_style= "e", opt_type="p"):
    dt= T/N                           # Length of a time step

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
        if opt_type=="c":
            O[j]= np.maximum(S[j]-K,0)
        elif opt_type=="p":
            O[j]= np.maximum(K-S[j],0)
        else:
            print("Please confirm all the parameters!!!!!!!!!!!!!!")
            return None

    # Backward induction
    if opt_style== "e":
        for i in range(N-1, -1, -1):
            for j in range(0,i+1):
                O[j]= disc_factor * (O[j+1] * p + O[j] * (1-p))
    
    elif opt_style== "a":
        for i in range(N-1, -1, -1):
            for j in range(0,i+1):
                St= So * (u**j) * (d**(i-j))
                O[j]= disc_factor * (O[j+1] * p + O[j] * (1-p))
                if opt_type=="c":
                    O[j]= np.maximum(St-K, O[j])
                else:
                    O[j]= np.maximum(K-St, O[j])
    else:
        print("Please confirm all the parameters!!!!!!!!!!!!!!")
        return None
            
    return O[0]

print(f"The price of the option is: ${binomial_tree(So, K, T, Rf, vol, N, opt_style="e", opt_type="p").round(2)}")
