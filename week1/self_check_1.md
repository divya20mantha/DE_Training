1. An e-commerce app's   table: OLTP or OLAP? Why?
    OLTP system because, it handles multiple types of transactions at single a time.

2. Why does columnar storage make faster?
    Similar data with multiple values are stored in columns and querying/aggregation makes this faster as, searching is not done at row level.

3. Where would you keep 5 years of raw website logs cheaply?
    In a data lake, as transformation/processing of data is not required. 

4. Which uses schema-on-write: a warehouse or a lake?
    schema-on-write is used in data warehouse as schema is checked when data is being loaded.

5. Raw data is loaded into Snowflake, then cleaned with SQL inside Snowflake. Is that ETL orELT?
    ELT.

6. A bank must flag suspicious card payments within 2 seconds. Batch or streaming?
    Streaming.

7. Name the five pipeline stages, in order.
    Source --> Ingest --> Store --> Transform --> Serve.

8. What does Delta add on top of Parquet? --

9. Give one reason CSV causes bugs in pipelines. 
    CSV stores data in plain and has no data types, it can cause schema mis matches in any of the pipeline stages.

10. In one sentence, what does a data engineer do?
    A data engineer builds automated pipelines that collect raw data and transforms it and stores data in a place , so that this data can be used for analytical purposes by data analysts, data scientists.
