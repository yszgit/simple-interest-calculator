# Simple Interest Calculator

A small command-line calculator that computes simple interest from a principal amount, an annual interest rate, and a time period in years. Simple interest is calculated on the original principal only; interest does not compound.

## Formula

```text
Simple interest = principal × annual rate (%) × time (years) / 100
Total amount = principal + simple interest
```

## Inputs and outputs

- **Principal (P):** the initial amount of money.
- **Annual interest rate (R):** a percentage, such as `5` for 5% per year.
- **Time (T):** the duration in years; fractional years are supported.
- **Outputs:** the simple interest and total amount, displayed to two decimal places.

All inputs must be finite, nonnegative numbers. Use the same currency for the principal and the resulting amounts.

## Requirements

Python 3. No third-party packages are required.

## Usage

Clone this repository, open its directory, and run:

```sh
python simple_interest.py 1000 5 2
```

On systems where Python 3 is named `python3`, use `python3` instead of `python`.

Expected output:

```text
Simple interest: 100.00
Total amount: 1100.00
```

For this example, `1000 × 5 × 2 / 100 = 100` in interest over two years.

To see argument help:

```sh
python simple_interest.py --help
```

## Contributing and community

Suggestions and improvements are welcome through issues and pull requests. Please follow the [Code of Conduct](CODE_OF_CONDUCT.md).

## License

Copyright 2026 yszgit. Licensed under the [Apache License, Version 2.0](LICENSE).
