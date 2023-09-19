# Plotting and table-making scripts

This directory contains scripts to create plots and tables from the structured
data in the `/data/` directory. The following is a description of how to use
the scripts.

## Requirements

Our Python code is designed to be used with Python 3.9 or higher and requires
_matplotlib_ and _pandas_ to be installed. If _Poetry_ is available, the
requirements can be installed easily as follows:

```bash
poetry install
```

Otherwise, _matplotlib_ and _pandas_ can be installed using pip:

```bash
pip install pandas==2.1.0 matplotlib==3.8.0
```

## Running

Running the scripts is as easy as running the following command if the Poetry
installation method was used:

```bash
poetry run python make_plots.py
```

Otherwise, it is possible to run:

```bash
python make_plots.py
```

### Running with or without TeX

By default, our plotting scripts use a TeX-based rendering engine to most
accurately match the ACM LaTeX template in order to provide the most
aesthetically pleasing result possible. If LaTeX is not available, our plotting
code can be run without TeX support using the `--no-tex` flag:

```bash
[poetry run] python make_plots.py --no-tex
```
