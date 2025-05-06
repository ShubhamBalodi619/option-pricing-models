# 📈 Option Pricing Models in Python

This repository contains Python & Excel implementations of popular **option pricing models** used in financial mathematics.

The goal is to provide clean, well-documented, and easy-to-understand scripts for each model, along with example use cases and practical insights.

---

## 🚀 Models Implemented

### ✅ Black-Scholes Model  
A closed-form solution for pricing **European call and put options** assuming log-normally distributed stock prices and constant volatility.

- Inputs: Spot price, strike price, time to maturity, risk-free rate, volatility, option type  
- Outputs: Theoretical option price

### ✅ Binomial Option Pricing Model  
A discrete-time lattice-based model that can price **European and American options**. It uses a stepwise approach to model stock price movements and apply backward induction to compute option values.

- Inputs: Spot price, strike price, time to maturity, volatility, risk-free rate, number of steps, option type (call/put), option style (European/American)  
- Outputs: Estimated option price using backward induction
---

## 📅 Coming Soon

These models will be added to the repository soon:

- **Monte Carlo Simulation for Option Pricing**
- **Greeks Calculation (Delta, Gamma, Vega, etc.)**

---
