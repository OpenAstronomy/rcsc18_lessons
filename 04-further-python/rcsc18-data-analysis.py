import glob

import analysis_tools


filenames = sorted(glob.glob('inflammation*.csv'))

for f in filenames[:3]:
    print(f)
    analysis_tools.analyse(f)
    analysis_tools.detect_problems(f)
