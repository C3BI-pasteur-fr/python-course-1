import os

def average(input_filename):
    """
    compute the average of data contains in file input_filename
    and write the result in file results/monscript.out

    :param input_filename: the path to the file containing data
    :type input_filename: string
    """
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
                ave = sum(numbers) / float(len(numbers))
                output.write(str(ave) + "\n")

average('average_inputs')
