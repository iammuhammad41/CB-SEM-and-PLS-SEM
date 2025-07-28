"""
PLS-SEM analysis using plspm.
Assumes Data/pls_data.csv with columns:
    srv1,srv2,srv3,val1,val2,sat1,sat2,loy1
"""

import pandas as pd
import plspm.config as c
from plspm.plspm import Plspm
from plspm.scheme import Scheme
from plspm.mode import Mode

# 1. Load data
df = pd.read_csv("Data/pls_data.csv")

# 2. Define inner (structural) model
structure = c.Structure()
structure.add_path(["Service"],     ["Value", "Satisfaction"])
structure.add_path(["Value"],       ["Satisfaction"])
structure.add_path(["Satisfaction"],["Loyalty"])

# 3. Configure outer (measurement) model
config = c.Config(structure.path(), scaled=False)
config.add_lv_with_columns_named("Service",     Mode.A, df, ["srv1","srv2","srv3"])
config.add_lv_with_columns_named("Value",       Mode.A, df, ["val1","val2"])
config.add_lv_with_columns_named("Satisfaction",Mode.A, df, ["sat1","sat2"])
config.add_lv_with_columns_named("Loyalty",     Mode.A, df, ["loy1"])

# 4. Run PLS-PM
pls = Plspm(df, config, Scheme.CENTROID)

# 5. Output
print("\n=== Inner Model Summary ===\n")
print(pls.inner_summary())

print("\n=== Path Coefficients ===\n")
print(pls.path_coefficients())
