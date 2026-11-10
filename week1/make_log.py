 # DE_Training/week1/make_log.py
import random
from datetime import datetime, timedelta
rng = random.Random(42)
t = datetime(2026, 11, 1, 0, 0, 0)
cities = ["Kanpur", "Pune", "Delhi", "Mumbai", "Bengaluru"]
steps = ["ingest", "store", "transform", "serve"]
with open("pipeline.log", "w", newline="\n") as f:
     for i in range(5000):
         t += timedelta(seconds=rng.randint(1, 30))
         level = rng.choices(["INFO", "WARN", "ERROR"], weights=[90, 7, 3])[0]
         f.write(
                f"{t:%Y-%m-%d %H:%M:%S} {level} step={rng.choice(steps)} "
                f"city={rng.choice(cities)} order_id={10000 + i} ms={rng.randint(20, 900)}\n")
            
print("Wrote pipeline.log")

  


  

