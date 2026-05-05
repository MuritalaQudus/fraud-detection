import pandas as pd
def load_data(path):
    return pd.read_csv(path )

load_data('data/raw/nova_pay_combined.csv')