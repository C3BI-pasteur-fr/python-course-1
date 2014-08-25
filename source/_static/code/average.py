import os

def average(input_filename):
   here = os.getcwd()
   result_dir = os.path.join(here, 'results')
   if not os.path.exists(result_dir):
      os.mkdir(result_dir)
   result_path = os.path.join(result_dir, 'mon_script.out')
   input_path = os.path.realpath(input_filename)
   with open(input_path, 'r') as inputs:
      with open(result_path, 'w') as output:
         for line in inputs:
            fields = line.split()
            if not fields:
                continue
            numbers = [float(items) for items in fields]
            average = sum(numbers)/ float(len(numbers))
            output.write(str(average) + "\n")

average('average_inputs')
