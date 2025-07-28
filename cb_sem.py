"""
CB-SEM analysis (covariance-based SEM) using semopy.
Assumes Data/pls_data.csv with columns:
    srv1,srv2,srv3,val1,val2,sat1,sat2,loy1
"""

import pandas as pd
from semopy import Model, inspect, calc_stats

# 1. Load data
df = pd.read_csv("Data/pls_data.csv")

# 2. Specify model in lavaan-style syntax
model_desc = """
# Measurement model (reflective)
Service     =~ srv1 + srv2 + srv3
Value       =~ val1 + val2
Satisfaction =~ sat1 + sat2
Loyalty     =~ loy1

# Structural model
Value        ~ Service
Satisfaction ~ Service + Value
Loyalty      ~ Satisfaction
"""

# 3. Build and fit
sem_model = Model(model_desc)
res = sem_model.fit(df)

# 4. Inspect estimates
print("\n=== Parameter Estimates ===\n")
print(inspect(sem_model))

# 5. Goodness‑of‑fit indices
stats = calc_stats(sem_model)
print("\n=== Fit Statistics ===\n")
for k, v in stats.items():
    print(f"{k}: {v:.3f}")
