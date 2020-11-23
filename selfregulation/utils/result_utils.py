from glob import glob
import os
from dimensional_structure.results_mv import Results
from selfregulation.utils.utils import get_info

def load_results(datafile, name=None, results_dir=None, verbose = True, solution = None):
    if results_dir is None:
        results_dir = get_info('results_directory')
    results = {}
    if solution is not None:
        result_files = glob(os.path.join(results_dir, 'dimensional_structure/%s/Output/*results_nfactor_master.pkl' % (datafile)))
    else:
        result_files = glob(os.path.join(results_dir, 'dimensional_structure/%s/Output/*results.pkl' % (datafile)))
    if name is not None:
        result_files = [i for i in result_files if name in i]
    for filey in result_files:
        name = os.path.basename(filey).split('_')[0]
        results[name] = Results(saved_obj_file=filey)
    if verbose:
        print('Getting result file: %s...:\n'  % (result_files))
    return results
