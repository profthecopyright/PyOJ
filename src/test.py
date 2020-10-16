import signal
# import resource

from RestrictedPython import compile_restricted
from RestrictedPython import safe_globals


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
def add(a, b):
    return other_function(a, b)

def other_function(a, b):
    # print('other function called')
    return a + b
"""

byte_code = compile_restricted(source_code, '<inline>', 'exec')
exec(byte_code, globals())  # Do not pass locals!
print(add(4, 4))
"""
set_max_runtime(5)
while True:
    pass
"""



