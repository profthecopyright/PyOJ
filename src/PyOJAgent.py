# https://restrictedpython.readthedocs.io/_/downloads/en/stable/pdf/

from RestrictedPython import compile_restricted
from RestrictedPython import Eval
from RestrictedPython import Guards
from RestrictedPython import safe_globals
from RestrictedPython import utility_builtins
from RestrictedPython.PrintCollector import PrintCollector
import signal
import json
# import resource

class PyOJAgent:
    def __init__(self, memory_limit=1048576, time_limit=10, **kwargs):
        self.name = 'default_agent'
        self.memory_limit = memory_limit
        self.time_limit = time_limit
        self.set_limit()
        self.config_restricted_environment()

    def set_limit(self):
        pass
        # use resource module, only available in Unix

    def config_restricted_environment(self):
        self.policy_globals = {**safe_globals, **utility_builtins}
        self.policy_globals['__builtins__']['__metaclass__'] = type
        self.policy_globals['__builtins__']['__name__'] = type

        self.policy_globals['_getattr_'] = Guards.safer_getattr
        self.policy_globals['_write_'] = Guards.full_write_guard
        self.policy_globals['_getiter_'] = Eval.default_guarded_getiter
        self.policy_globals['_getitem_'] = Eval.default_guarded_getitem
        self.policy_globals['_iter_unpack_sequence_'] = Guards.guarded_iter_unpack_sequence

    def load_test_points(self, filename):
        with open(filename) as f:
            self.test_points = json.load(f)

    def test_submission(self, submission_code_str):
        self.result_correctness = []

        for test_point in self.test_points:
            suffix = '\noutput = main_function' + str(tuple(test_point[0]))
            self.policy_globals['output'] = None

            try:
                _getiter_ = Eval.default_guarded_getiter
                _print_ = PrintCollector
                _getattr_ = getattr

                byte_code = compile_restricted(submission_code_str + suffix, '<inline>', 'exec')
                exec(byte_code, self.policy_globals)

            except Exception as e:
                print(e)
                # CE, Runtime Error, TLE, MLE
                print('exception!')
                # more handling here

            if self.policy_globals['output'] == test_point[1]:
                self.result_correctness.append('Correct')
            else:
                self.result_correctness.append('Incorrect') # add error types here maybe

    def process(self, problem_filename, submission_code_str):
        self.load_test_points(problem_filename)
        self.test_submission(submission_code_str)

        for result in self.result_correctness:
            print(result, sep='\n')


    def reset(self):
        pass
        # safe_globals['output'] = None
        # clear temporaries