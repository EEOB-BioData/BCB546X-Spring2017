##Example of Using a _For Loop_

Within this folder you will find files labeled 'file1', 'file2' and 'file3'.  These files each contain two unsorted columns.  The syntax below uses a for loop to pull out the lines of each of these files matching a regular expression in awk and then pipe this to a sort on both columns.  The standard output of sort is then sent to a new file with '.output' appended to the file name.

Take a look at the initial files, run the code below, and see if the .output files make sense to you.

```
for i in file*; do awk '$1 ~ /1|2/' $i \
| sort -k1,1n -k2,2n > $i.output; done
```