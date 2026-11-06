#!/usr/bin/env bash
# Copyright 2026 yszgit
# SPDX-License-Identifier: Apache-2.0
# Calculate simple interest using a principal, annual percentage rate, and years.

set -euo pipefail

read -r -p "Enter the principal amount: " principal
read -r -p "Enter the annual rate of interest (%): " rate
read -r -p "Enter the time period in years: " years

number_pattern='^([0-9]+([.][0-9]*)?|[.][0-9]+)$'
for value in "$principal" "$rate" "$years"; do
    if [[ ! "$value" =~ $number_pattern ]]; then
        echo "Error: all inputs must be nonnegative numbers." >&2
        exit 1
    fi
done

awk -v p="$principal" -v r="$rate" -v t="$years" 'BEGIN {
    interest = p * r * t / 100
    printf "The simple interest is: %.2f\n", interest
    printf "The total amount is: %.2f\n", p + interest
}'
