# DelimiterCheck
![License: GPLv3](https://img.shields.io/badge/License-GPLv3-blue.svg 'License')

## Delimiters and markup languages

When coding I am used to having matching parentheses indicated by my editor.
In general purpose programming languages this poses no problem.
The syntax never allows unbalanced delimiters.
When I do not get syntax errors I can be sure my editor shows me the proper scope of a pair of braces or parentheses.

Markup languages, however, pose a problem.
If a markup language gives me maximum flexibility, this means I can put unbalanced parentheses in my text.
This can be for aesthetic or notational purposes.
Some examples are:
 * in numbered lists you might want the labels to be `a)`, `b)`, `c)`, etc.
 * a system of equations in a scientific text is often preceded by a single curly brace
 * also in scientific texts, intervals with excluded endpoints are often denoted as `[a,b[` or `[a,b)`.
These examples pose a problem for your text editor because the matching of parentheses gets out of control.

Most of the time, however, there is a solution.
Usually a markup language allows for a simple macro system.
Using these macros you can abstract these common use cases away.
But then you still need a way to check if you've truly removed these special cases.
This script helps with that task.

## Usage

In a command line, simply enter

```
python delimiter_check.py -i textfile.txt
```

Supposing the text file contained

```
[a
(b
{c
}d
)e
(f
]g
```

you will get the following output.

```
Line 1: [ unclosed
Line 6: ( unclosed
Line 7: ] extra
```

The script knows that the two curly braces on lines 3 and 4 cancel.
With them out of the way, the parentheses on lines 2 and 5 can also cancel.
Finally, we are left with the delimiter structure `[(]` and this structure will not be reduced further, generating the three messages.
This is by design. I do not want overlapping hierarchies.

If there is no command line flag given, the script uses stdin for input and can be used in a pipeline.

## How do I break the rules?

### LaTeX

LaTeX includes by default the commands `\lbrace`, `\rbrace`, `\lbrack` and `\rbrack` for braces and square brackets.
Similar commands `\lparen` and `\rparen` exist in the package `mathtools`.
This package extends the classic `amsmath` and is now something I load by default.
Using these six commands with a package like `enumitem` allows you to elegantly solve the problem of numbered lists.
You can also define your own macro's for intervals etc.

## How do I extend the rules of the script?

It is possible to add your own set of delimiters to the program.
To do so you need to edit the code in one place.
Suppose I want the script to also check if every `\langle` has a matching `\rangle`.
To this end I need to add them to `DEFAULT_DELIMITERS` (which matches opening delimiters to their closing counterpart).
It will now look like this:

```
DEFAULT_DELIMITERS = [(r'(', r')'),
                      (r'{', r'}'),
                      (r'[', r']'),
					  (r'\langle', r'\rangle')]

```

The use of raw strings is simply to make it less painful to get LaTeX-commands right
