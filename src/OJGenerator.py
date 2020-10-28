import json

def generate_from_file(text_file, testpoint_file, output_file):
    with open(text_file, encoding='utf-8') as f:
        txt = f.read()

    with open(testpoint_file) as f:
        tp = json.load(f)

    generate_from_memory(txt, tp, output_file)

def load_oj_file(problem_file):
    with open(problem_file, encoding='utf-8') as f:
        oj_dict = json.load(f)
        print(oj_dict['txt'])
        print(oj_dict['tp'])


def generate_test_points(standard_func, test_inputs):
    test_points = [(test_point, standard_func(*test_point)) for test_point in test_inputs]

    return test_points

def generate_from_memory(txt, tp, output_file):

    oj_dict = {'txt': txt, 'tp': tp}

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(oj_dict, f, ensure_ascii=False)

