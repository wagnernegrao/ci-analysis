def plot_df():
    df = pd.DataFrame([('Java', commit_project[0]),
                       ('Ruby', commit_project[1]),
                       ('Javascript', commit_project[2])], columns=['Language', 'commit']).set_index('Language')
    df['commit'].apply(lambda x: pd.Series(x)).T.boxplot(figsize=(10,10),rot=0)