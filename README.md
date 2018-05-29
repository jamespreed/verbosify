# verbosify
Python decorator for turning on/off print statements in a function.  Useful for debugging code without having to comment out print statements.

### Usage
Simply decorate a function with `@verbose` to do the following:
  + add the keyword-only argument `verbose` to the function
  + update the docstring to include information about the `verbose` option
  + update the function signature to show `verbose` with its default value (also adds completion for IPython)

The default behavior is to turn off printing
```
from verbosify import verbose

@verbose
def test(hello='world'):
    '''
    Test function to print an input.

    Parameters:
    -----------
    hello : <any>
        Any input.

    Returns:
    --------
    None
    '''
    print(hello)
```

Bringing up the help for `test` shows the modified docstring and arguments
```
help(test)
# prints
Help on function test in module __main__:

test(hello='world', *, verbose=False)
    Test function to print an input.

    Parameters:
    -----------
    hello : <any>
        Any input.

    Returns:
    --------
    None

    Option:
    -------
    verbose : bool
        Turns on/off print lines in the function.
```

Calling the function `test` prints nothing, unless `verbose` is set to `True`:
```
test()   # prints nothing
test(verbose=True)
# prints:
world
