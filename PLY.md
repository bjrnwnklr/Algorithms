# PLY (Python Lex-Yacc)

PLY is a 100% Python implementation of the lex and yacc tools commonly used to write parsers and compilers. Parsing is based on the same LALR(1) algorithm used by many yacc tools.

[Homepage](https://www.dabeaz.com/ply/)
[GitHub](https://github.com/dabeaz/ply)
[Documentation](https://ply.readthedocs.io/en/latest/)

## Installation

This package can only be installed by cloning the GitHub repo:

To use PLY, simply copy the ply directory to your project and import lex and yacc from the associated ply package. For example:

```python
from ply import lex
from ply import yacc
```

See the example implementation in AoC 2020, day 18 for a very simple calculation grammar including changing the operator precedence by making PLUS a higher precedence than TIMES.
