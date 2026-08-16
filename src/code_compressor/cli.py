import json
import click
from .compressor import CodeCompressor
from .analyzer import analyze_code


@click.group()
def main():
    """Safe source-code compression and security analysis."""


@main.command()
@click.argument("input_file", type=click.Path(exists=True, dir_okay=False))
@click.option("-o", "--output", required=True, type=click.Path(dir_okay=False))
@click.option("-l", "--level", default=9, show_default=True, type=click.IntRange(1, 9))
def compress(input_file, output, level):
    """Compress source text into a JSON package."""
    result = CodeCompressor(level).compress_file(input_file, output)
    click.echo(json.dumps(result, indent=2))


@main.command()
@click.argument("input_file", type=click.Path(exists=True, dir_okay=False))
@click.option("-o", "--output", required=True, type=click.Path(dir_okay=False))
def decompress(input_file, output):
    """Restore source text after verifying its SHA-256 digest."""
    result = CodeCompressor().decompress_file(input_file, output)
    click.echo(json.dumps(result, indent=2))


@main.command()
@click.argument("input_file", type=click.Path(exists=True, dir_okay=False))
def analyze(input_file):
    """Analyze source text for suspicious constructs."""
    with open(input_file, "r", encoding="utf-8") as fh:
        result = analyze_code(fh.read())
    click.echo(json.dumps(result, indent=2))
