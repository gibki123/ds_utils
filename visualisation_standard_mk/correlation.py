import pandas as pd
from dython.nominal import associations
from dython.nominal import identify_nominal_columns, identify_numeric_columns
import matplotlib.pyplot as plt


def visualise_correlation(df: pd.DataFrame, graph_type="full", nom_nom_assoc='cramer', num_num_assoc='pearson',
                          nom_num_assoc='correlation_ratio'):
    if graph_type == 'full':
        associations(df, figsize=(12, 12), nominal_columns='auto', numerical_columns=identify_numeric_columns(df),
                     nom_nom_assoc=nom_nom_assoc, num_num_assoc=num_num_assoc, nom_num_assoc=nom_num_assoc,
                     nan_strategy='drop_features', cramers_v_bias_correction=False,
                     title=f'Heatmap corr all data types: {nom_nom_assoc, num_num_assoc, nom_num_assoc}')
    if graph_type == 'numerical':
        df = df[identify_numeric_columns(df)]
        associations(df, figsize=(12, 12), nominal_columns=None, numerical_columns=identify_numeric_columns(df),
                     num_num_assoc=num_num_assoc,
                     nan_strategy='drop_features', title=f'Heatmap corr numerical: {num_num_assoc}')
    if graph_type == 'nominal':
        df = df[identify_nominal_columns(df)]
        associations(df, figsize=(12, 12), nominal_columns='auto', numerical_columns=None,
                     nom_nom_assoc=nom_nom_assoc, nan_strategy='drop_features', cramers_v_bias_correction=False,
                     title=f'Heatmap corr all nominal: {nom_nom_assoc}')
    plt.show()



