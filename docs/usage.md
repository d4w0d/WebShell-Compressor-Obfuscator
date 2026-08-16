# Usage Guide

## Compress

`code-compressor compress input.py -o output.json`

The output is a JSON container holding zlib-compressed, Base64-encoded source
and a SHA-256 digest.

## Restore

`code-compressor decompress output.json -o restored.py`

Restoration is data-only: the project never executes decoded or restored code.

## Analyze

`code-compressor analyze input.py`

The analyzer reports selected constructs commonly associated with dynamic code
execution or command execution. Findings are indicators, not proof of a
vulnerability.
