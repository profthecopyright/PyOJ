import signal
# import resource

from RestrictedPython import compile_restricted
from RestrictedPython import safe_globals
from RestrictedPython import utility_builtins
from RestrictedPython.PrintCollector import PrintCollector
from RestrictedPython import Eval
from RestrictedPython import Guards

def time_exceeded(signo, frame):
    raise SystemExit('Time\'s up!')

"""
def set_max_runtime(seconds):
    _, hard = resource.getrlimit(resource.RLIMIT_CPU)
    resource.setrlimit(resource.RLIMIT_CPU, (seconds, hard))
    signal.signal(signal.SIGXCPU, time_exceeded)
    print('CPU time limit: soft = ', seconds, ' hard = ', hard)


def limit_memory(maxsize):
    soft, hard = resource.getrlimit(resource.RLIMIT_AS)
    resource.setrlimit(resource.RLIMIT_AS, (maxsize, hard))
    print('memory limit: soft = ', maxsize, ' hard = ', hard)
"""

source_code = """
# import os
class Foo:
    def __init__(self):
        pass

def add(a, b):
    for i in range(4):
        pass
    
    return other_function(a, b)

def other_function(a, b):
    # print('other function called') # disable print function
    # os.listdir('/')
    d = [1, 2, 3];
    d[1] = 4;
    del d[0]
    return a + b + math.sin(a)
    

"""

suffix = '\noutput = add(5, 8)'
policy_builtins = {**safe_globals, **utility_builtins}
policy_builtins['__builtins__']['__metaclass__'] = type
policy_builtins['__builtins__']['__name__'] = type

policy_builtins['_getattr_'] = Guards.safer_getattr
policy_builtins['_write_'] = Guards.full_write_guard
policy_builtins['_getiter_'] = Eval.default_guarded_getiter
policy_builtins['_getitem_'] = Eval.default_guarded_getitem
policy_builtins['_iter_unpack_sequence_'] = Guards.guarded_iter_unpack_sequence
# policy_builtins['__import__'] = None


byte_code = compile_restricted(source_code + suffix, '<inline>', 'exec')
exec(byte_code, policy_builtins)  # Do not pass locals!
print(policy_builtins['output'])

#print(safe_globals['output'])


"""
set_max_runtime(5)
while True:
    pass
"""



