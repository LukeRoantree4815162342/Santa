import imp
import os
parent_path = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
script_location = str(parent_path) + '\\Submissions\\TryEval.py'
test = imp.load_source('try_eval_bag', script_location)
test('gloves_123 gloves_134')