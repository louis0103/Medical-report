#!/bin/bash
counter=0
start=$(date +%s)
for filename in ./report_cxv/*.csv; do
    ((counter++))
    python label.py --reports_path $filename
    echo "$counter : $filename "
done
end=$(date +%s)
duration=$((end - start))
echo -e "$counter : Processing took $duration seconds."