# 🛡️ WebShell Compressor & Obfuscator

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

A powerful, professional-grade tool for compressing and obfuscating web shells and exploit code. Designed for security researchers, penetration testers, and red teams.

## ⚠️ LEGAL DISCLAIMER

**This tool is intended for authorized security testing and educational purposes only.**
- Only use on systems you own or have explicit written permission to test
- Unauthorized use is illegal and unethical
- The authors assume no liability for misuse

## Features

- **Multi-Language Support**: PHP, Python, JavaScript, ASP, JSP
- **Advanced Compression**: 70-90% size reduction
- **Multiple Obfuscation Layers**: Base64, ROT13, XOR, custom encoding
- **Self-Extracting Payloads**: Creates standalone compressed executables
- **Signature Evasion**: Bypass common AV/IDS signatures
- **Comment & Whitespace Removal**: Minify code aggressively
- **Variable/Function Renaming**: Shorten identifiers
- **String Extraction & Compression**: Optimize string literals
- **Multi-Layer Compression**: Apply multiple compression passes
- **REST API**: Compress/decompress remotely
- **CLI Interface**: Easy command-line usage
- **Full Decompression**: Restore original code perfectly

## Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/webshell-compressor.git
cd webshell-compressor

# Install dependencies
pip install -r requirements.txt

# Install the package
python setup.py install




# Code Compressor & Security Analyzer

A safe educational project for compressing/minifying **benign source code** and
analyzing source text for potentially dangerous constructs.

This reconstruction intentionally does **not** implement web-shell generation,
self-executing payloads, AV/IDS signature evasion, or execution of decoded payloads.

## Supported operations

- Text/source-code compression with zlib + Base64
- Source minification for common whitespace/comments
- SHA-256 integrity verification
- Suspicious-pattern analysis
- JSON reports
- CLI and Python API

## Installation

```bash
python -m pip install -r requirements.txt
pip install -e .
```

## Usage

```bash
code-compressor compress examples/sample.py -o sample.compressed.json
code-compressor decompress sample.compressed.json -o sample.restored.py
code-compressor analyze examples/sample.py
```

## Integrity

The compressed package contains a SHA-256 digest of the original source and
decompression verifies it before returning the restored content.
