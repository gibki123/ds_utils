import matplotlib as plt


def annotate_bars(ax=None, fmt='.5g', **kwargs):
    ax = plt.gca() if ax is None else ax
    for p in ax.patches:
        ax.annotate('{{:{:s}}}'.format(fmt).format(p.get_height()), (p.get_x() + p.get_width() / 2., p.get_height()),
                    xytext=(0, 20), textcoords='offset points',
                    ha='center', va='center', **kwargs)
