Sources - 
    1.OrdersDB, Restaurant Menu, Payments.  
    2.Clicks, GPS. 

Ingest - 
    1.OrdersDB, Restaurant Menu, Payments (Not live events, can be     loaded   periodically) - Hence Batch processing.
    2.Clicks, GPS - Live events - Streams- Kafka.

Store - 
AWS -S3 - Data Lake - stores Raw data. (Parquet files) 

Transform - 
    Pipeline 1 - ELT - to transform Orders data - SnowFlake/Big query - (OLAP systems)
    Pipeline 2 - ETL - GPS for Live Delivery.  

     