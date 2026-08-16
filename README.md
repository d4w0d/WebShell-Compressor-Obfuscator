# WebShell Compressor & Security Analyzer

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A security-focused tool for compressing, restoring, and analyzing source code. Designed for authorized security research, penetration-testing labs, and educational environments.

> **Note:** This project operates on source code as data. It does not generate or execute web shells, self-extracting payloads, or payload-evasion mechanisms.

## Legal Disclaimer

**Use this project only on systems and code you own or have explicit permission to test.**

Unauthorized testing may be illegal. The authors assume no responsibility for misuse.

## Features

* **Source-Code Compression** — zlib compression with Base64 encoding
* **Multiple Languages** — Suitable for common text-based source code
* **Integrity Verification** — SHA-256 verification after decompression
* **Security Analysis** — Detects selected suspicious constructs
* **CLI Interface** — Simple command-line workflow
* **Python API** — Use the compressor programmatically
* **JSON Packages** — Stores compressed data and integrity metadata
* **Safe Restoration** — Restores source code without executing it
* **File Operations** — Compress and decompress files directly
* **Testing** — Includes automated tests

## Quick Start

### Installation

```bash
git clone https://github.com/d4w0d/WebShell-Compressor-Obfuscator.git
cd WebShell-Compressor-Obfuscator/

python -m pip install -r requirements.txt
pip install -e .
```

### Compress a File

```bash
code-compressor compress examples/sample.py -o sample.compressed.json
```

### Decompress a File

```bash
code-compressor decompress sample.compressed.json -o sample.restored.py
```

### Analyze Source Code

```bash
code-compressor analyze examples/sample.py
```

### Get Help

```bash
code-compressor --help
```

## Python API

```python
from code_compressor import CodeCompressor
from code_compressor.analyzer import analyze_code

source = """
def greet(name):
    return f"Hello, {name}!"
"""

compressor = CodeCompressor(compression_level=9)

compressed = compressor.compress(source)
restored = compressor.decompress(compressed)

print(restored == source)
# True

results = analyze_code(source)
print(results)
```

## Integrity Verification

Every compressed package contains a SHA-256 hash of the original source.

During decompression:

1. The package is parsed.
2. The compressed data is decoded.
3. The source is restored.
4. SHA-256 is calculated again.
5. The calculated hash is compared with the stored hash.
6. Decompression fails if the hashes do not match.

This helps detect accidental or unauthorized modification of the compressed data.

## 🔎 Security Analysis

The analyzer checks for selected constructs that may warrant manual security review, including:

* `eval()`
* `exec()`
* `system()`
* `shell_exec()`
* `passthru()`
* `proc_open()`
* `base64_decode()`

A finding is an **indicator**, not proof of a vulnerability. Results should always be reviewed in the context of the application.

Example:

```bash
code-compressor analyze examples/sample.py
```

Example output:

```json
{
  "risk_score": 0,
  "suspicious": [],
  "findings": []
}
```

## Project Structure

```text
code-compressor-security-analyzer/
├── README.md
├── LICENSE
├── requirements.txt
├── setup.py
├── config.yaml
├── examples/
│   └── sample.py
├── src/
│   └── code_compressor/
│       ├── __init__.py
│       ├── analyzer.py
│       ├── cli.py
│       └── compressor.py
├── tests/
│   └── test_compressor.py
└── docs/
    └── usage.md
```

## Testing

Run the test suite with:

```bash
pytest
```

## Dependencies

The project uses:

* Python 3.8+
* Click
* Pytest for testing

Install dependencies with:

```bash
python -m pip install -r requirements.txt
```

## Security Considerations

This project intentionally does **not**:

* Execute restored or decoded source code
* Generate self-executing payloads
* Implement AV/IDS signature-evasion mechanisms
* Generate web shells
* Provide remote payload execution

Compressed files should still be treated as untrusted input when received from external sources.

## License

Distributed under the MIT License. See `LICENSE` for details.

## Contributing

Contributions are welcome.

Before submitting changes:

```bash
pytest
```

Please keep security-sensitive functionality focused on defensive analysis, safe transformation, and authorized research.

---

**Use responsibly and only in authorized environments.**
