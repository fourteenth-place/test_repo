import os; 
val = os.environ.get('RUN_ENV')
if val is None:
    raise Exception('VAL IS NONE')
else:
    print(f'python found env var: {val}')