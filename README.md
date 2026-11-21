# golden-vortex

![CI](https://img.shields.io/github/actions/workflow/status/shaxxenoaj/golden-vortex/ci.yml?branch=main&label=CI) ![Python](https://img.shields.io/badge/python-3.10+-blue) ![Jupyter](https://img.shields.io/badge/jupyter-notebook-F37626) ![License](https://img.shields.io/github/license/shaxxenoaj/golden-vortex?color=blue)

golden-vortex provides a statistical modeling and forecasting workflow: load CSV data from a directory, clean and deduplicate rows, compute summary statistics (count, mean, std, min, max), generate time-series and distribution plots, and export results. Includes a Jupyter notebook for interactive exploration and a CLI script for batch processing.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Running Tests](#running-tests)
- [Contributing](#contributing)
- [Changelog](#changelog)
- [License](#license)

## Features

- Summary statistics: count, mean, std, min, max
- Data cleaning pipeline: dedup, dropna, type coercion, timestamp parsing
- Matplotlib time-series plot with configurable figsize and DPI
- Cached intermediate results for reproducible analysis
- CLI entry point: `python scripts/run_analysis.py --data data/ --output results/`
- Automated data loading: concatenate all CSV files from a directory

## Prerequisites

- Python 3.10 or higher
- Jupyter Notebook or JupyterLab
- pip for installing dependencies

## Installation

```bash
git clone https://github.com/shaxxenoaj/golden-vortex.git
cd golden-vortex
pip install -r requirements.txt
jupyter notebook
```

## Usage

```bash
# Run the full analysis pipeline
python scripts/run_analysis.py --data data/raw/ --output results/
# => Loading data from data/raw/...
# => Loaded 10000 rows
# => Stats: count=10000, mean=42.5, std=15.3, min=0.0, max=100.0
# => Plots saved to results/

# Or open the interactive notebook
jupyter notebook notebooks/analysis.ipynb

# View generated plots
ls results/*.png
# results/timeseries.png  results/distribution.png
```

## Project Structure

```
golden-vortex/
├── scripts/run_analysis.py
├── notebooks/analysis.ipynb
├── data/  results/
├── requirements.txt
├── README.md  LICENSE  CHANGELOG.md  CONTRIBUTING.md  CODE_OF_CONDUCT.md
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.md
│   │   └── feature_request.md
│   └── PULL_REQUEST_TEMPLATE.md
└── .gitignore
```

## Running Tests

```bash
# Verify the pipeline runs end-to-end
python scripts/run_analysis.py --data data/ --output results/

# Or run the notebook
jupyter notebook notebooks/analysis.ipynb
```

## Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

Quick start:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/my-feature`
3. Make your changes and run tests (see [Running Tests](#running-tests) above)
4. Commit with a clear message: `git commit -am 'Add: my feature'`
5. Push to your fork: `git push origin feature/my-feature`
6. Open a Pull Request

Please ensure all tests pass before submitting a pull request.

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for a list of changes and version history.

## License

This project is licensed under the GPL-3.0 -- see the [LICENSE](LICENSE) file for details.

Copyright (c) 2026 ella li.

## Acknowledgements

- Built with pandas, NumPy, Matplotlib, Seaborn, and Plotly
- CI/CD powered by [GitHub Actions](https://github.com/features/actions)
- Badges by [shields.io](https://shields.io)
- Inspired by best practices from the open-source community
