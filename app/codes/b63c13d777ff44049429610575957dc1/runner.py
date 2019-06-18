import sys

def load_module(module):

    # module_path = "mypackage.%s" % module
    module_path = module

    if module_path in sys.modules:
        return sys.modules[module_path]

    return __import__(module_path, fromlist=[module])

# Main script here... Could be your for loop or anything else
# `m` is a reference to the imported module that contains the functions
m = load_module("test")
asd = m.ex()

print(asd)