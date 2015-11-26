'''
Notes:

1. pass by objects 
2. mutable vs immutable
   - Reference: https://www.jeffknupp.com/blog/2013/02/14/drastically-improve-your-python-understanding-pythons-execution-model/
   - mutable: lists, set, dictionaries
   - immutable: string, integer, float, tuple
   - When you "change" a string, you're actually rebinding it to a newly created string object. The original object remains unchanged, even though its possible that nothing refers to it anymore
   - "string concatenation is slow.". It's because concatenating strings must allocate memory for a new string and copy the contents, while appending to a list (in most cases) requires no allocation. 
   - Immutable objects are fundamentally expensive to "change", because doing so involves creating a copy. 
   - Changing mutable objects is cheap
3. PEP8
   coding guidelines, use space
4. python v3 
   - strings are unicode
5. "decorators allow you to wrap a function or class method call and execute some code before 
    or after the execution of the original code",
6. "with keyword is used when working with unmanaged resources (like file streams). 
    It allows you to ensure that a resource is "cleaned up" when the code that uses it finishes running, 
    even if exceptions are thrown",
7.  "Unicode was a brave effort to create a single character set that included every reasonable 
    writing system on the planet"
'''  

