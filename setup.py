from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="chadgpt",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A natural language terminal interface powered by GPT-3.5",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/chadgpt",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=[
        "openai>=1.12.0",
        "python-dotenv>=1.0.1",
        "rich>=13.7.0",
    ],
    entry_points={
        "console_scripts": [
            "chadgpt=chadgpt.cli:main",
        ],
    },
) 