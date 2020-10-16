# https://restrictedpython.readthedocs.io/_/downloads/en/stable/pdf/

from RestrictedPython import compile_restricted
from RestrictedPython import safe_globals
import signal
import json
# import resource

class PyOJAgent:
    def __init__(self, memory_limit=1048576, time_limit=10, **kwargs):
        self.name = 'default_agent'
        self.memory_limit = memory_limit
        self.time_limit = time_limit
        self.set_limit()


    def set_limit(self):
        pass
        # use resource module, only available in Unix

    def load_test_points(self, filename):
        with open(filename) as f:
            self.test_points = json.load(f)

    def compile_submission(self, submission_code_str):
        try:
            byte_code = compile_restricted(submission_code_str, '<inline>', 'exec')
            exec(byte_code, globals())
        except Exception as e:
            print('exception in compiling: CE')
            print(e)
            # more handling here
        else:
            print('compiled successfully!')

    def test_submission(self):
        self.result_correctness = []

        for test_point in self.test_points:
            submission_return_value = None
            try:
                submission_return_value = main_function(*test_point[0])
            except Exception as e:
                print(e)
                # Runtime Error, TLE, MLE
                print('exception in Runtime')
                # more handling here

            if submission_return_value == test_point[1]:
                self.result_correctness.append('Correct')
            else:
                self.result_correctness.append('Not Correct') # add error types here maybe

    def process(self, problem_filename, submission_code_str):
        self.load_test_points(problem_filename)
        self.compile_submission(submission_code_str)
        self.test_submission()

        for result in self.result_correctness:
            print(result, sep='\n')