# Nitrogen Purging Estimator
## Project Overview
This project aims to build a machine learning model that predicts the number of nitrogen bottles required to purge pipelines in oil and gas operations. Nitrogen purging is a critical safety and operational step used to displace hazardous gases before maintenance or commissioning. Traditional estimation methods rely on engineering heuristics, which may be conservative or inconsistent. By leveraging historical, simulated, or expert-driven data, this project provides a data-driven approach to optimize nitrogen usage, reduce costs, and improve planning accuracy.

## Problem Statement
Given pipeline specifications and operating conditions, estimate the number of nitrogen bottles required for purging. The model considers features such as:
- Pipeline length, diameter, and volume
- Initial gas type (crude or natural gas)
- Target residual concentration
- Operating and ambient temperature
- Pressure, elevation change, and number of bends/valves
- Purge method (displacement or dilution)
The target variable is the number of nitrogen bottles needed, calculated or measured from past operations.

## Tech Stack
- Python 3.13.3
- Pandas, Numpy for data handling
- Scikit-learn, XGBoost for modeling
- Matplotlib, Seaborn for visualization
- FastAPI for deployment
- Docker for containerization