# Importing libraries
import numpy as np
from scipy.stats import norm

# Defining the input variables
St= 526.41            # Current stock price
K= 500                # Strike price
T= 0.169863014        # Time to maturity in years
Rf= 0.02              # Risk-free rate of return
vol= 0.1742           # Annualized volatility
opttype= "c"          # Option type

# Defining the function to calculate the option price
def black_scholes(St, K, T, Rf, vol, opttype="c"):
    d1= (np.log(St/K) + (Rf + 0.5 * vol**2) * T)/(vol * np.sqrt(T))
    d2= d1 - vol * np.sqrt(T)

    try:
        if opttype=="c":
            price= St * norm.cdf(d1) - K * np.exp(-Rf * T) * norm.cdf(d2)
        elif opttype=="p":
            price= -St * norm.cdf(-d1) + K * np.exp(-Rf * T) * norm.cdf(-d2)
        return price
    except:
        print("Please confirm all the parameters!!!!!!!!!!!!!!")

print(f"The call option price is ${black_scholes(St, K, T, Rf, vol, opttype="c").round(2)}.")
print(f"The put option price is ${black_scholes(St, K, T, Rf, vol, opttype="p").round(2)}.")
