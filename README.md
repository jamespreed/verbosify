# verbosify
Python decorator for turning on/off print statements in a function.  

## Why verbosify?
Because `logging` is for suckers!  Just kidding.  This is simply a quick and dirty decorator that is useful for debugging code without having to comment out print statements.  It also allows you to rapidly add in on/off functionality for printing output (looking at you `statsmodels` ಠ_ಠ)

## Usage
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
```

`verbose` can also be used as a factory to create decorators for turning print on/off by default
```
echo_off = verbose(default=False)  
echo_on = verbose(default=True)

# equivalent to @verbose or @verbose(default=False)
@echo_off
def test(x):
    print(x)
    
# equivalent to @verbose(default=True)
@echo_on
def test(x):
    print(x)
```

## To do list:
- add argument to change the name of the keyword argument added to the decorated function (default: `verbose`)
- add argument to turn change the style of the appended docstring, possible styles:
  - `'none'`
  - `'numpy'`
  - `'sphinx'`
  - `'google'`
  - custom maybe?
