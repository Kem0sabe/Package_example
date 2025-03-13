from ctab_xtra_dp import CTAB_XTRA_DP, stat_sim, privacy_metrics



import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df_filtered = pd.read_csv('A_greater_B.csv')

import numpy as np
import pandas as pd
import glob


synthesizer =  CTAB_XTRA_DP(df_filtered,
                 categorical_columns = [], 
                 log_columns = [],
                 mixed_columns= {},
                 integer_columns = [],
                 problem_type= None) 

#synthesizer.fit(30)


stat_sim(df_filtered,df_filtered)
#synthesizer.generate_samples(30)

