# sjFs4py
sjFs4py is FileSystem utilities for python, it will contain several tools, such as logcat_rename.

# logcat_rename
logcat_rename is tools for rename logcat.log\.([0-9]+) files to logcat.%02d.log.
On Letv TV devices, the logcat files redirected from system will be named like logcat.log.2 logcat.log.1 logcat.log, as earlier as No is bigger.
```
DMS/GRACE-89/03/Log.2$ tree
.
├── logcat.log
├── logcat.log.1
├── logcat.log.10
├── logcat.log.11
├── logcat.log.12
├── logcat.log.13
├── logcat.log.14
├── logcat.log.15
├── logcat.log.16
├── logcat.log.17
├── logcat.log.18
├── logcat.log.19
├── logcat.log.2
├── logcat.log.20
├── logcat.log.3
├── logcat.log.4
├── logcat.log.5
├── logcat.log.6
├── logcat.log.7
├── logcat.log.8
└── logcat.log.9

0 directories, 21 files
```
if we search something, the result will not be time ascending or descending.
```
Search "ActivityManager-Killer: stopBackgroundIfNeeded()"  (34 hits in 5 files of 21 searched)
  \\XancL03\sjPBP\DMS\GRACE-89\03\Log.2\logcat.log.1  (7 hits)
	Line 77: 07-15 18:55:52.050  4464  4508 D ActivityManager-Killer: stopBackgroundIfNeeded()
...
	Line 39237: 07-15 18:58:55.446  4464  4508 D ActivityManager-Killer: stopBackgroundIfNeeded()
	Line 42615: 07-15 18:59:02.666  4464  4508 D ActivityManager-Killer: stopBackgroundIfNeeded()
  \\XancL03\sjPBP\DMS\GRACE-89\03\Log.2\logcat.log.2  (12 hits)
	Line 2076: 07-15 18:53:14.485  4464  4508 D ActivityManager-Killer: stopBackgroundIfNeeded()
	Line 7348: 07-15 18:53:40.146  4464  4508 D ActivityManager-Killer: stopBackgroundIfNeeded()
...
	Line 37160: 07-15 18:55:30.751  4464  4508 D ActivityManager-Killer: stopBackgroundIfNeeded()
	Line 41966: 07-15 18:55:44.716  4464  4508 D ActivityManager-Killer: stopBackgroundIfNeeded()
```
internal of the file, line is ascending, but the files is descending. so we need to rename files by time ascending.
The expection like these, assumption 3 files.
```
logcat.log -> logcat.03.log
logcat.log.1 -> logcat.02.log
logcat.log.2 -> logcat.01.log
```
## usage
```
  578  python logcat_rename.py --logcat-dir=/disk2/thomas/sjPBP/DMS/GRACE-89/03/Log.2/
```
After that the filenames will be these:
```
$ tree /disk2/thomas/sjPBP/DMS/GRACE-89/03/Log.2
/disk2/thomas/sjPBP/DMS/GRACE-89/03/Log.2
├── logcat.01.log
├── logcat.02.log
├── logcat.03.log
├── logcat.04.log
├── logcat.05.log
├── logcat.06.log
├── logcat.07.log
├── logcat.08.log
├── logcat.09.log
├── logcat.10.log
├── logcat.11.log
├── logcat.12.log
├── logcat.13.log
├── logcat.14.log
├── logcat.15.log
├── logcat.16.log
├── logcat.17.log
├── logcat.18.log
├── logcat.19.log
├── logcat.20.log
└── logcat.21.log
```
The search result:
```
  \\XancL03\sjPBP\DMS\GRACE-89\03\Log.2\logcat.19.log  (12 hits)
	Line 2076: 07-15 18:53:14.485  4464  4508 D ActivityManager-Killer: stopBackgroundIfNeeded()
	Line 7348: 07-15 18:53:40.146  4464  4508 D ActivityManager-Killer: stopBackgroundIfNeeded()
...
	Line 37160: 07-15 18:55:30.751  4464  4508 D ActivityManager-Killer: stopBackgroundIfNeeded()
	Line 41966: 07-15 18:55:44.716  4464  4508 D ActivityManager-Killer: stopBackgroundIfNeeded()
  \\XancL03\sjPBP\DMS\GRACE-89\03\Log.2\logcat.20.log  (7 hits)
	Line 77: 07-15 18:55:52.050  4464  4508 D ActivityManager-Killer: stopBackgroundIfNeeded()
	Line 10081: 07-15 18:56:25.371  4464  4508 D ActivityManager-Killer: stopBackgroundIfNeeded()
...
	Line 39237: 07-15 18:58:55.446  4464  4508 D ActivityManager-Killer: stopBackgroundIfNeeded()
	Line 42615: 07-15 18:59:02.666  4464  4508 D ActivityManager-Killer: stopBackgroundIfNeeded()	
```
