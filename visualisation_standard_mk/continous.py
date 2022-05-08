from operator import mul
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import missingno as msno
from dython.nominal import identify_numeric_columns
from html_utils import print_blank_line, print_header, print_paragraph, print_horizontal_line


def visualise_cont_cat(df: pd.DataFrame, variable_col: str, target_col: str) -> None:
    config = {
        'fontsize': 16,
        'fontsize_html': 16,
        'sns_font_scale': 1.3,
        'figsize_single_plot': (8, 6),
        'figsize_tuple_multiplier': (2, 1),
        'facet_height': 5,
        'facet_aspect': 2,
        'tight_layout_padding': 1.8,
        'fontweight_plot_title': 'bold',
    }
    sns.set(font_scale=config['sns_font_scale'])
    sns.set_style('white')

    print_header(f'Variable: {variable_col}')

    fig, axs = plt.subplots(1, 2,
                            figsize=tuple(map(mul, config['figsize_single_plot'], config['figsize_tuple_multiplier'])))
    fig.set_constrained_layout(True)
    fig.set_constrained_layout_pads(wspace=0.1)

    sns.boxplot(data=df, x=target_col, y=variable_col, ax=axs[0])
    axs[0].set_title(f'BoxPlot: {variable_col} to {target_col}', fontweight=config['fontweight_plot_title'])
    sns.kdeplot(data=df, x=variable_col, hue=target_col, shade='fill', ax=axs[1])
    axs[1].set_title(f'DensityPlot: {variable_col} to {target_col}', fontweight=config['fontweight_plot_title'])
    plt.show()
    print_blank_line()

    plt.figure(figsize=config['figsize_single_plot'])
    sns.violinplot(data=df, x=target_col, y=variable_col, constrained_layout=True,
                   figsize=config['figsize_single_plot'])
    plt.title(f"ViolinPlot: {variable_col} to {target_col}", fontweight=config['fontweight_plot_title'])
    plt.show()
    print_blank_line()

    msno.matrix(df[[variable_col]], figsize=config['figsize_single_plot'], fontsize=config['fontsize'])
    plt.title(f"Missing values plot of variable {variable_col}", fontweight=config['fontweight_plot_title'])
    plt.show()
    print_paragraph(f'Number of missing values col {variable_col}: {df[variable_col].isna().sum()}',
                    fontsize=config['fontsize_html'])


def visualise_all_cont_cat(df: pd.DataFrame, target_col: str) -> None:
    nom_columns = identify_numeric_columns(df.drop(columns=target_col))
    for column in nom_columns:
        visualise_cont_cat(df, column, target_col)
        print_horizontal_line()
        print_blank_line()
