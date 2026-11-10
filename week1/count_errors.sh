 #!/bin/bash
 # Prints how many ERROR lines a log file has
 echo "ERROR lines: $(grep -c ERROR "$1")"

#  ls -l
# total 48
# -rw-r--r--@ 1 divyamantha  staff  1436 Nov 10 13:36 LINUX_DRILL.md
# -rw-r--r--@ 1 divyamantha  staff   101 Nov 10 13:37 count_errors.sh
# -rw-r--r--@ 1 divyamantha  staff  1227 Nov  4 16:16 lab_s1_formats.py

#  ./count_errors.sh pipeline.log
# bash: ./count_errors.sh: Permission denied
# chmod +x count_errors.sh
# (.venv) Divyas-MacBook-Pro:week1 divyamantha$ ls -

# (.venv) Divyas-MacBook-Pro:week1 divyamantha$ ls -l
# total 48
# -rw-r--r--@ 1 divyamantha  staff  1436 Nov 10 13:36 LINUX_DRILL.md
# -rwxr-xr-x@ 1 divyamantha  staff   101 Nov 10 13:37 count_errors.sh
# -rw-r--r--@ 1 divyamantha  staff  1227 Nov  4 16:16 lab_s1_formats.py
# -rw-r--r--@ 1 divyamantha  staff   705 Nov 10 12:35 make_log.py
# -rw-r--r--@ 1 divyamantha  staff  1385 Nov  4 16:10 self_check_1.md
# -rw-r--r--@ 1 divyamantha  staff   907 Nov  4 16:16 week1_Results.md