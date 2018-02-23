#!/bin/bash
getCompanies() {
	cat companies.csv | cut -d',' -f2
}


while read -r line; do
	python act3.py $line &
done <<< "$(getCompanies)"
