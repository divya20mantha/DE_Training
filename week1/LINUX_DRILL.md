1. How many lines does the file have?
wc -l LINUX_DRILL.md
       6 LINUX_DRILL.md
wc pipeline.log [Lines]   [Words]   [Bytes]
       5000   35000  355982 pipeline.log

2. What do the first 3 lines look like? What does each part of a line mean? 
    2026-11-01 00:00:21 INFO step=transform city=Pune order_id=10000 ms=248
    2026-11-01 00:00:26 INFO step=ingest city=Bengaluru order_id=10001 ms=452
    2026-11-01 00:00:28 INFO step=store city=Pune order_id=10002 ms=537
Pipeline logs of Orders data across multiple cities with timestamps.

3. What is the Order_ID on the last line?
    tail -1  pipeline.log
    2026-11-01 21:38:58 WARN step=ingest city=Pune order_id=14999 ms=865

4. How many lines are errors?
    grep -c ERROR pipeline.log
    160

5. How many errors happened in Pune?
    grep ERROR app.log | grep -c "city=Pune"
    grep -Ec 'ERROR.*city=Pune|city=Pune.*ERROR' pipeline.log
    25

6. Save all the error lines to erros.log file, 
    grep ERROR pipeline.log > errors.log
then count the lines in that file.
     wc errors.log
        160    1120   11595 errors.log

7. How many lines are there for each log level?
    cut -d' ' -f3 errors.log | sort | uniq -c | sort -rn
        160 ERROR

8. Which city has the most errors?
    awk '$3=="ERROR" {count[$5]++} END {for (city in count) print city, count[city]}' pipeline.log | sort -k2,2nr
city=Bengaluru 42
city=Mumbai 37
city=Delhi 29
city=Kanpur 27
city=Pune 25