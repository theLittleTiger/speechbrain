#!/usr/bin/env python3
import setuptools
from distutils.core import setup

with open("README.md") as f:
    long_description = f.read()

setup(
    name="speechbrain",
    version="0.5.0",
    description="All-in-one speech toolkit in pure Python and Pytorch",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Mirco Ravanelli & Others",
    author_email="speechbrain@gmail.com",
    packages=setuptools.find_packages(),
    install_requires=[
        "hyperpyyaml",
        "joblib",
        "numpy",
        "packaging",
        "scipy",
        "sentencepiece",
        "torch",
        "torchaudio",
        "tqdm",
        "huggingface_hub",
    ],
    python_requires=">=3.7",
    url="https://speechbrain.github.io/",
)
