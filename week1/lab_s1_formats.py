# DE_Training/week1/lab_s1_formats.py
import os, time
import numpy as np
import pandas as pd


# 1. Create 1 million fake orders
n = 1_000_000
rng = np.random.default_rng(42)
df = pd.DataFrame({
    "order_id": np.arange(n),
    "city": rng.choice(["Kanpur", "Pune", "Delhi", "Mumbai", "Bengaluru"],n),
    "amount": rng.integers(50, 2000, n),
    "order_date": pd.to_datetime("2026-01-01") + pd.to_timedelta(rng.integers(0, 300, n), unit="D"),
})

# 2. Save the same data in both formats
df.to_csv("orders.csv", index=False)
df.to_parquet("orders.parquet", index=False)

# 3. Compare file sizes
for f in ["orders.csv", "orders.parquet"]:
    print(f"{f}: {os.path.getsize(f) / 1e6:.1f} MB")

# 4. Read only one column: Parquet can skip the others
t = time.time(); 
pd.read_csv("orders.csv", usecols=["amount"]); 
print(f"CSV read amount: {time.time() - t:.2f}s")
t = time.time(); 
pd.read_parquet("orders.parquet", columns=["amount"]);
print(f"Parquet read amount: {time.time() - t:.2f}s")

# 5. Check whether data types survive
print(pd.read_csv("orders.csv").dtypes)
print(pd.read_parquet("orders.parquet").dtypes)

# # 5. Read data from parquet file
# df_parquet = pd.read_parquet ("orders.parquet")
# df_parquet.head()



