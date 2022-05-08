import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from plot_utils import annotate_bars
from html_utils import print_blank_line, print_header, print_paragraph, print_horizontal_line
import matplotlib.patheffects as path_effects
import missingno as msno
from dython.nominal import identify_nominal_columns


def visualise_cat_cat(df: pd.DataFrame, variable_col: str, target_col: str, only_null_plot=False) -> None:
    config = {
        'fontsize': 16,
        'fontsize_html': 16,
        'figsize_single_plot': (12, 4),
        'sns_font_scale': 1.3,
        'facet_height': 5,
        'facet_aspect': 2,
        'bar_edge_color': "black",
        'bar_edge_width': 1
    }
    sns.set(font_scale=config['sns_font_scale'])
    sns.set_style('white')

    print_header(f'Variable: {variable_col}')
    unique_categories = df[variable_col].unique()
    print_paragraph(f"Number of unique values in column {variable_col}: {len(unique_categories)}",
                    fontsize=config['fontsize_html'])

    if not only_null_plot:
        plt.figure(figsize=config['figsize_single_plot'])
        ax = sns.histplot(df, x=variable_col, discrete=True, edgecolor=config["bar_edge_color"],
                          linewidth=config["bar_edge_width"])
        ax.spines['right'].set_visible(False)
        ax.spines['top'].set_visible(False)
        ax.set_title(f'Number of occurnces: {variable_col}')
        annotate_bars(ax, fontsize=config['fontsize'])
        total = df[variable_col].count()

        texts = ax.bar_label(ax.containers[0], label_type='center',
                             labels=[f'{val / total * 100.0:.1f} %' for val in ax.containers[0].datavalues],
                             color='white', fontsize=config['fontsize'], fontweight='bold')
        for text in texts:
            text.set_path_effects([path_effects.Stroke(linewidth=1, foreground='black'),
                                   path_effects.Normal()])
        plt.tight_layout()
        ax.plot()
        plt.show()
        print_blank_line()

        g = sns.FacetGrid(df, col=target_col, hue=target_col, legend_out=True, palette="Set2",
                          height=config['facet_height'], aspect=config['facet_aspect'])
        g.fig.suptitle(f'Number of occurnces {variable_col} divided by: {target_col}')
        g.map(sns.histplot, variable_col, discrete=True, edgecolor=config["bar_edge_color"],
              linewidth=config["bar_edge_width"])
        for ax in g.axes.ravel():
            sum_facet = 0
            for p in ax.patches:
                sum_facet += p.get_height()
            for p in ax.patches:
                ax.annotate(format(p.get_height(), '.5g'), (p.get_x() + p.get_width() / 2., p.get_height()),
                            ha='center', va='center', xytext=(0, 20), textcoords='offset points',
                            fontsize=config['fontsize'])
                annot = ax.annotate(format(p.get_height() * 100.0 / sum_facet, '.1f') + "%",
                                    (p.get_x() + p.get_width() / 2., p.get_height() / 2.),
                                    ha='center', va='center', xytext=(0, 0), textcoords='offset points', color='white',
                                    fontsize=config['fontsize'], fontweight='bold')
                annot.set_path_effects([path_effects.Stroke(linewidth=1, foreground='black'),
                                        path_effects.Normal()])
        plt.tight_layout()
        plt.show()
        print_blank_line()
    else:
        msno.matrix(df[[variable_col]], figsize=config['figsize_single_plot'], fontsize=config['fontsize'])
        plt.title(f"Missing values plot of variable {variable_col}")
        plt.show()
        print_paragraph(f'Number of missing values col {variable_col}: {df[variable_col].isna().sum()}',
                        config['fontsize_html'])


def visualise_all_cat_cat(df: pd.DataFrame, target_col: str, unique_limit: int = 20) -> None:
    nom_columns = identify_nominal_columns(df.drop(columns=target_col))
    for column in nom_columns:
        unique_categories = df[column].unique()
        if len(unique_categories) <= unique_limit:
            visualise_cat_cat(df, column, target_col=target_col)
        else:
            print_paragraph(f"Too many categories for full visualisation", fontsize=20)
            visualise_cat_cat(df, column, target_col=target_col, only_null_plot=True)
        print_horizontal_line()
        print_blank_line()

