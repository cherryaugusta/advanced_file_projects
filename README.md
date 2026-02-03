# File Projects – Python File Handling System

## Overview

This repository demonstrates a production-style Python project focused on file handling, data parsing, and clean software architecture.

The project is structured as an installable Python package using the `src/` layout, with clear separation between domain logic, I/O utilities, runtime data, and entry-point scripts.

## Architecture Overview

- `src/` layout to avoid import ambiguity
- Domain modules contain pure logic only
- Centralized file I/O utilities
- `pathlib` used exclusively for path handling
- Scripts act as thin orchestration layers
- Unit tests validate parsing and file behavior
- GitHub Actions CI enforces correctness

## Folder Structure

- `data/` – runtime text files (not imported)
- `src/file_projects/` – application code
- `scripts/` – CLI-style entry points
- `tests/` – pytest test suite

## Key Design Decisions

- `pathlib` over `os.path` for safety and clarity
- Immutable domain models using `dataclass`
- No file access outside `common/io.py`
- Explicit separation between logic and execution

## Running Scripts

````bash
python scripts/diary.py
python scripts/budget.py
python scripts/report.py
Testing
pytest
Disclaimer
This project is for educational and portfolio purposes only. Do not use real personal or financial data.
````
---

## LICENSE
MIT License

Copyright (c) 2026 Cherry Augusta

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND.
