# Barrier Option Pricing – Binomial Tree Model

This project implements the **Binomial Tree method** to calculate the theoretical price of barrier **call and put options** using Python.

It uses a discrete-time lattice to simulate possible paths of the underlying asset price and applies backward induction to derive the fair value of the option.

---

## 📌 Model Assumptions

- Markets are frictionless and arbitrage-free  
- The stock does not pay dividends  
- Volatility and interest rates remain constant over the option's life  
- The underlying follows a multiplicative binomial process 
- Supports both European (exercisable only at expiration) and American (exercisable any time) style options

---

## 🧮 Methodology

- Accepts the following input parameters:
  - **So**: Current stock price  
  - **K**: Strike price  
  - **T**: Time to maturity (in years)  
  - **Rf**: Risk-free rate of return  
  - **vol**: Annualized volatility
  - **opt_type**: Option type – `"c"` for call, `"p"` for put  
- Steps:
  - Computes time step size dt, up (u) and down (d) factors
  - Derives the risk-neutral probability p and discount factor
  - Initializes asset prices at maturity and computes terminal option payoffs
  - Uses backward induction to calculate the option price at time zero

---

## 📦 Dependencies

- `numpy`

You can install the dependencies using:

```bash
pip install numpy
