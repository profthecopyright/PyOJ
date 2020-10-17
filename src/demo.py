import PyOJAgent

agent = PyOJAgent.PyOJAgent()

submission = """

def add(a, b):
    for i in range(10):
        pass

    return a + b

def other_function():
    pass
    # print('nonsense')

def main_function(a, b):
    other_function()
    return add(a, b)
"""

agent.process(problem_filename='sample_problem.txt', submission_code_str=submission)