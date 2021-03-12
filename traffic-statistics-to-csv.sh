#!/usr/bin/env bash

CSVHEADER="Date, CurrentConnectTime, CurrentUpload, CurrentDownload, CurrentDownloadRate, CurrentUploadRate, TotalUpload, TotalDownload, TotalConnectTime"
OUTFILE=./traffic-statistics.csv

if [ ! -f $OUTFILE ]; then
    echo "$CSVHEADER"  > $OUTFILE
fi

python3 ./traffic-statistics-to-csv.py >> $OUTFILE
