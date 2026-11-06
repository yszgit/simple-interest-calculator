# Copyright 2026 yszgit
# SPDX-License-Identifier: Apache-2.0
"""Calculate simple interest from principal, annual percentage rate, and years."""

import argparse
from decimal import Decimal, InvalidOperation, localcontext


def nonnegative_number(value):
    try:
        number = Decimal(value)
    except InvalidOperation as exc:
        raise argparse.ArgumentTypeError("enter a valid number") from exc
    if not number.is_finite() or number < 0:
        raise argparse.ArgumentTypeError("enter a finite, nonnegative number")
    return number


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("principal", type=nonnegative_number)
    parser.add_argument("rate", type=nonnegative_number, help="annual rate as a percentage")
    parser.add_argument("years", type=nonnegative_number)
    args = parser.parse_args()
    with localcontext() as context:
        context.prec = 50
        interest = args.principal * args.rate * args.years / Decimal(100)
        total = args.principal + interest
        print(f"Simple interest: {interest:.2f}")
        print(f"Total amount: {total:.2f}")


if __name__ == "__main__":
    main()
