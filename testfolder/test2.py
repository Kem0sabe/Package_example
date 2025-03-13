from ctab_xtra_dp import CTAB_XTRA_DP, load_demo
import pandas as pd

# Load your data
df = load_demo()

# Initialize the model
synthesizer = CTAB_XTRA_DP(
    df=df,
    categorical_columns=['workclass', 'education', 'marital-status', 'occupation', 
                         'relationship', 'race', 'gender', 'native-country'],
    mixed_columns={'capital-loss': [0],'capital-gain': [0]},
    integer_columns=['age', 'hours-per-week']
)

# Train the model
synthesizer.fit(epochs=5)