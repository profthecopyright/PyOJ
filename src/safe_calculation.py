from RestrictedPython import compile_restricted
from RestrictedPython import Eval
from RestrictedPython import Guards
from RestrictedPython import safe_globals
from RestrictedPython import utility_builtins
import os       # os is unavailable in user code scope even we imported os
# import math   # math is available in user code scope even we did not import math

def generate_safe_policy():
    policy_globals = {**safe_globals, **utility_builtins}
    policy_globals['__builtins__']['__metaclass__'] = type
    policy_globals['__builtins__']['__name__'] = type
    policy_globals['_getattr_'] = Guards.safer_getattr
    policy_globals['_write_'] = Guards.full_write_guard
    policy_globals['_getiter_'] = Eval.default_guarded_getiter
    policy_globals['_getitem_'] = Eval.default_guarded_getitem
    policy_globals['_iter_unpack_sequence_'] = Guards.guarded_iter_unpack_sequence

    return policy_globals

def safe_calculate(input_str):
    policy_globals = generate_safe_policy()
    ret = None

    try:
        bytecode = compile_restricted(input_str, '<calc_exp>', 'eval')
        result = eval(bytecode, policy_globals)
    except Exception as e:
        ret = repr(e)
    else:
        ret = str(result)
    finally:
        return ret

teststrs = ['1 + 1', '-.2+.8', '(5+2j) / (5-7j)', '0/0', 'a=1', 'import os', 'math.sin(1)',
            'abs(-8)', '1877 ** 177', "os.listdir('/')",
            '(lambda x, y: [a * b for a in range(x) for b in range(y)])(4, 5)',
            '(lambda x: import os)(1)',
            "(lambda x: open('sample_problem.txt')(2)", '4', 'open', 'math', 'random', 'random.random()']

for input_str in teststrs:
    print(input_str, 'returns: ', safe_calculate(input_str))
