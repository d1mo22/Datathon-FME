def undersample_partition(df, target_col="buyer_d7", majority=0, minority=1, ratio=4.0):
    pos = df[df[target_col] == minority]
    neg = df[df[target_col] == majority]

    n_pos = len(pos)
    n_keep_neg = int(n_pos * ratio)

    neg_sampled = neg.sample(n=n_keep_neg, random_state=42) if len(
        neg) > n_keep_neg else neg

    return dd.concat([pos, neg_sampled])
