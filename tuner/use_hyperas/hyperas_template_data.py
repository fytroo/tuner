def data():
    train_dir = '{train_dir}'
    test_dir = '{validation_dir}'
    resize = '{resize}'
    rescale = '{rescale}'
    df = load_data.df_fromdir_classed(train_dir)
    sampling_size = min(df.label.value_counts()) * 4
    df = load_data.oversampling_df(df, sampling_size)
    x_train, y_train = load_data.load_fromdf(df, resize=resize, rescale=rescale)
    df = load_data.df_fromdir_classed(test_dir)
    x_test, y_test = load_data.load_fromdf(df, resize=resize, rescale=rescale)

    y_train = to_categorical(y_train)
    y_test = to_categorical(y_test)

    return x_train, y_train, x_test, y_test
