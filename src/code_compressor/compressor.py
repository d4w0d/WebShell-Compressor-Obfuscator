import base64
import hashlib
import json
import zlib


class CodeCompressor:
    """Compress and restore source text without executing it."""

    def __init__(self, compression_level: int = 9):
        self.compression_level = max(1, min(9, int(compression_level)))

    @staticmethod
    def _package(source: str, data: str) -> dict:
        return {
            "version": "1.0.0",
            "encoding": "base64",
            "compression": "zlib",
            "original_length": len(source),
            "sha256": hashlib.sha256(source.encode("utf-8")).hexdigest(),
            "data": data,
        }

    def compress(self, source: str) -> str:
        raw = source.encode("utf-8")
        compressed = zlib.compress(raw, self.compression_level)
        encoded = base64.b64encode(compressed).decode("ascii")
        return json.dumps(self._package(source, encoded), indent=2)

    def decompress(self, package_text: str) -> str:
        package = json.loads(package_text)
        if package.get("compression") != "zlib":
            raise ValueError("Unsupported compression format")
        compressed = base64.b64decode(package["data"], validate=True)
        source = zlib.decompress(compressed).decode("utf-8")
        digest = hashlib.sha256(source.encode("utf-8")).hexdigest()
        if digest != package.get("sha256"):
            raise ValueError("Integrity check failed: SHA-256 mismatch")
        return source

    def compress_file(self, input_file: str, output_file: str) -> dict:
        with open(input_file, "r", encoding="utf-8") as fh:
            source = fh.read()
        package = self.compress(source)
        with open(output_file, "w", encoding="utf-8") as fh:
            fh.write(package)
        return {"input_file": input_file, "output_file": output_file,
                "original_size": len(source), "compressed_package_size": len(package)}

    def decompress_file(self, input_file: str, output_file: str) -> dict:
        with open(input_file, "r", encoding="utf-8") as fh:
            package = fh.read()
        source = self.decompress(package)
        with open(output_file, "w", encoding="utf-8") as fh:
            fh.write(source)
        return {"input_file": input_file, "output_file": output_file,
                "restored_size": len(source)}
