# CB-SEM and PLS-SEM
covariance-based structural equation modeling (CB-SEM) and partial least squares structural equation modeling (PLS-SEM).
# Structural Equation Modeling Examples

This repository provides two example scripts for conducting structural equation modeling (SEM) in Python:

1. **Covariance‑Based SEM (CB‑SEM)** using **semopy**
2. **Partial Least Squares SEM (PLS‑SEM)** using **plspm**

Both examples use the same sample dataset (`Data/pls_data.csv`) with the following columns:

```
srv1, srv2, srv3,   # Service indicators
val1, val2,         # Value indicators
sat1, sat2,         # Satisfaction indicators
loy1                # Loyalty indicator
```

---

## Contents

```
.
├── Data/
│   └── pls_data.csv      # Example CSV with measured indicators
│
├── cb_sem.py            # CB‑SEM example (semopy)
├── pls_sem.py           # PLS‑SEM example (plspm)
└── README.md            # This file
```

---

## 1. CB‑SEM (`cb_sem.py`)

A covariance‑based SEM example in `lavaan`-style syntax:

* **Measurement model** (reflective):

  ```
  Service     =~ srv1 + srv2 + srv3
  Value       =~ val1 + val2
  Satisfaction =~ sat1 + sat2
  Loyalty     =~ loy1
  ```
* **Structural model**:

  ```
  Value        ~ Service
  Satisfaction ~ Service + Value
  Loyalty      ~ Satisfaction
  ```

### Usage

```bash
pip install semopy pandas
python cb_sem.py
```

---

## 2. PLS‑SEM (`pls_sem.py`)

A partial least squares SEM example:

* **Inner model (paths)**:

  ```
  Service     → Value, Satisfaction
  Value       → Satisfaction
  Satisfaction→ Loyalty
  ```
* **Outer model**: Mode A (reflective) measurement blocks:

  * Service: srv1, srv2, srv3
  * Value: val1, val2
  * Satisfaction: sat1, sat2
  * Loyalty: loy1

### Usage

```bash
pip install pandas plspm
python pls_sem.py
```

---

## Dataset

Place your `pls_data.csv` under `Data/` with the columns described above. Your working directory should be the repository root.

---

## Credits

* **CB‑SEM** powered by [semopy](https://pypi.org/project/semopy/)
* **PLS‑SEM** powered by [plspm](https://pypi.org/project/plspm/) (Python port of [pylspm](https://github.com/lseman/pylspm))

Feel free to adapt these examples for your own SEM workflows!
