from contextlib import redirect_stdout
from functools import wraps
from inspect import cleandoc, signature, Parameter
import sys
import os

def verbose(func=None, default=False):
    '''
    Decorate a function to turn on/off the print commands inside of it.
    
    This decorator modifies a function by adding the keyword argument `verbose`
    with the default value of `default`.  It updates the docstring and the 
    function signature to reflect the change.
    
    When the function is called with `verbose=False`, any `print` commands or
    calls to `stdout` are redirected and not displayed.  Using `verbose=True` 
    turns on displaying of `print` commands.
    
    Examples:
    ---------
    This function can be used in the following ways:
    
    1.) as a direct decorator to turn off printing
        
        @verbose
        def test(hello='world'):
            """
            Test function to print any input
            """
            print(hello)
            
    >>> help(test)           # inspect function docstring and signature
    
    test(hello='world', *, verbose=False)
        Test function to print any input
    
        Option:
        -------
        verbose : bool
            Turns on/off print lines in the function.
            
    >>> test()               # prints nothing
    >>> test(verbose=True)
    world
    >>>
            
    2.) as a decorator with a keyword argument
    
        @verbose(default=True)
        def test(hello='world'):
            """
            Test function to print any input
            """
            print(hello)
            
    >>> help(test)           # inspect function docstring and signature
    
    test(hello='world', *, verbose=False)
        Test function to print any input
    
        Option:
        -------
        verbose : bool
            Turns on/off print lines in the function.
            
    >>> test()               # printing turned on by default
    world
    >>> test(verbose=False)  # prints nothing
    >>>
    
    3.) as a decorator factory to create a default printing option
    
    Note that using @echo_off has the same result as using @verbose
    
        echo_off = verbose(default=False)
        @echo_off
        def test(hello='world'):
            """
            Test function to print any input
            """
            print(hello)
            
    >>> test(verbose=True)
    world
    >>> test()               # prints nothing
    >>>
    
        echo_on = verbose(default=True)
        @echo_on
        def test(hello='world'):
            """
            Test function to print any input
            """
            print(hello)
            
    >>> test()
    world
    >>> test(verbose=False)  # prints nothing
    >>>
    
    '''
    if func is not None:
        return _verbose(default)(func)
    else:
        return _verbose(default)
    
def _verbose(default):
    def decorator(func):
        @wraps(func)
        def func_wrapper(*args, verbose=default, **kwargs):
            if verbose:
                _stdout = sys.stdout 
            else:
                _stdout = open(os.devnull, 'w')
            with redirect_stdout(_stdout):
                return func(*args, **kwargs)
        # update the docstring
        doc = '\n\nOption:\n-------\nverbose : bool\n    '
        doc += 'Turns on/off print lines in the function.\n '
        func_wrapper.__doc__ = cleandoc(func_wrapper.__doc__) + doc
        # update the function signature to include the verbose keyword
        sig = signature(func)
        param_verbose = Parameter('verbose', Parameter.KEYWORD_ONLY, 
            default=default)
        sig_params = tuple(sig.parameters.values()) + (param_verbose,)
        sig = sig.replace(parameters=sig_params)
        func_wrapper.__signature__ = sig
        return func_wrapper
    return decorator
    