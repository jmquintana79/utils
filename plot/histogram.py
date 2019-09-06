#!/usr/bin/python

## plot histogram from df
def plot_hist_df(df, title, cumulative = False):
    import matplotlib.pyplot as plt
    import seaborn as sns
    plt.figure(figsize=(8,4))
    if cumulative: g = sns.distplot(df,hist_kws=dict(cumulative=True),kde_kws=dict(cumulative=True))
    else: g = sns.distplot(df, bins = 100)
    g.set_title(title, fontsize=18)
    g.set_xlabel("x")
    g.set_ylabel("Probability", fontsize=15)
    plt.show()
