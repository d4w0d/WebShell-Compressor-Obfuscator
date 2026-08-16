from setuptools import setup, find_packages

setup(
    name="code-compressor-security-analyzer",
    version="1.0.0",
    description="Safe source-code compressor and suspicious-pattern analyzer",
    packages=find_packages("src"),
    package_dir={"": "src"},
    python_requires=">=3.9",
    install_requires=["click>=8.1"],
    entry_points={
        "console_scripts": [
            "code-compressor=code_compressor.cli:main",
        ]
    },
)
