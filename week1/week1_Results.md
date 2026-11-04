1. What were the two file sizes, and how many times smaller is Parquet?
---- orders.csv: 29.4 MB
---- orders.parquet: 7.2 MB
2. Which format read the 'amount' column faster, and why?
  1st Run
--- CSV read amount: 0.11s
--- Parquet read amount: 0.12s
  2nd Run
--- CSV read amount: 0.16s,0.12s
--- Parquet read amount: 0.01s,0.09s

3. What data type did 'order_date' come back as from CSV, and from Parquet? Why the difference?
-- CSV - plain text
-- Parquet - binary

order_id      int64
city            str
amount        int64
order_date      str
dtype: object
order_id               int64
city                     str
amount                 int64
order_date    datetime64[us]
dtype: object
 

4. If analysts will query this data in Amazon S3 using Athena, which format would you store, and why?
tabular format.(structured data)
-- https://docs.aws.amazon.com/athena/latest/ug/when-should-i-use-ate.html

