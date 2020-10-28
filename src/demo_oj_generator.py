import OJGenerator
import OJTemplate
"""
text_file = '../OJ/seed_text.txt'
tp_file = '../OJ/seed_testpoints.txt'
output_file = '../OJ/Problems/Problem1.plm'

OJGenerator.generate_from_file(text_file, tp_file, output_file)
OJGenerator.load_oj_file(output_file)
"""

text_file = '../OJ/seed_text.txt'
output_file='../OJ/Problems/Problem2.plm'
tp = OJGenerator.generate_test_points(OJTemplate.standard_answer, OJTemplate.test_inputs)
with open(text_file, encoding='utf-8') as f:
    txt = f.read()

OJGenerator.generate_from_memory(txt, tp, output_file)
OJGenerator.load_oj_file(output_file)