# to be integrated for automatic problem generation with an algorithm function
import json

inputs = [(1, 1), (-1, 1), (100, 100), (-100, 98), (102318274832593274, -23187493265108369)]

def add(a, b):
    return a + b

problem_test_points = [(args, add(*args)) for args in inputs]

problem_str = json.dumps(problem_test_points)

filename = 'sample_problem.txt'

with open(filename, 'w+') as f:
    f.write(problem_str)