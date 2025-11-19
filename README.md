# Nitrogen Purging Estimator
## Project Overview
This project aims to build a machine learning model that predicts the volume of nitrogen required to purge pipelines in oil and gas operations. Nitrogen purging is a critical safety and operational step used to displace hazardous gases before maintenance or commissioning. Traditional estimation methods rely on engineering heuristics, which may be conservative or inconsistent. By leveraging historical, simulated, or expert-driven data, this project provides a data-driven approach to optimize nitrogen usage, reduce costs, and improve planning accuracy.

## Problem Statement
Given pipeline specifications and operating conditions, estimate the volume of nitrogen required for purging. The model considers features such as:
- Pipeline length, diameter, and volume
- Target residual concentration
- Operating and ambient temperature
- Pressure, Safety factor, purge cycle, and number of bends/valves
- Purge method (displacement or dilution)

The target variable is the volume of nitrogen needed, calculated or measured from past operations. The assumed/fixed variables are:
- Purge method (displacement)
- Initial gas Type (Natural gas)

## Tech Stack
- Python 3.13.3
- Pandas, Numpy for data handling
- Scikit-learn, XGBoost for modeling
- Matplotlib, Seaborn for visualization
- FastAPI for deployment
- Docker for containerization

## How to Run the Project
1. Clone the Repository
```bash
git clone https://github.com/Abasi-ifreke/nitrogen-purging.git
cd nitrogen-purging
```

2. Set Up the Environment
Create a virtual environment and install dependencies:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows:  .venv\Scripts\activate
pip install -r requirements.txt
```