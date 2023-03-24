# DFA Tokenizer in Python

This is a practice project for CSC257 - Theory of Computation subject in my course, implemented by Bhaskar Rijal.

## Overview

This project implements a Deterministic Finite Automata (DFA) tokenizer in Python. The tokenizer extracts tokens from a given string of characters using a set of states for different types of tokens and transition between them based on the current character.

## Installation

To install the DFA tokenizer, clone this repository and run the following command:

pip install -e

This will install the required dependencies and make the `tokenizer` module available for import.

## Usage

To use the DFA tokenizer, import the `tokenizer` module and create a `Tokenizer` object with a string of characters:

```python
from tokenizer import Tokenizer

input_string = "3 + 4 * 2 / (1 - 5)"
tokenizer = Tokenizer(input_string)
tokens = tokenizer.tokenize()
```

The tokenize method returns a list of Token objects, each with a type and a lexeme.

## License

This project is licensed under the MIT License. 
Feel free to modify this template as per your needs.