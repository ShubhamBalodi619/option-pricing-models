# Option Pricing – Black-Scholes Model

This project implements the **Black-Scholes formula** to calculate the theoretical price of European-style **call and put options** using Python.

It assumes log-normally distributed stock prices and uses an analytical approach based on market inputs like volatility, time to maturity, and risk-free rate.

---

## 📌 Model Assumptions

- Markets are frictionless and arbitrage-free  
- The stock does not pay dividends  
- Volatility and interest rates are constant  
- Stock returns are normally distributed  
- European-style options (exercisable only at expiration)

---

## 🧮 Methodology

- Accepts the following input parameters:
  - **St**: Current stock price  
  - **K**: Strike price  
  - **T**: Time to maturity (in years)  
  - **Rf**: Risk-free rate of return  
  - **vol**: Annualized volatility  
  - **opttype**: Option type – `"c"` for call, `"p"` for put  
- Computes intermediate variables `d1` and `d2`  
- Calculates the option price using the Black-Scholes formula:
  - Call Option: `C = S·N(d1) − K·e^(−rT)·N(d2)`  
  - Put Option: `P = K·e^(−rT)·N(−d2) − S·N(−d1)`

---

## 📦 Dependencies

- `numpy`
- `scipy.stats`

You can install the dependencies using:

```bash
pip install numpy scipy
