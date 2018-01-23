def data():
    train_dir = '/home/fytroo/Tuner/test/standard_datasets/5a6708dbb037cb59496d1265/auged'
    test_dir = '/home/fytroo/Tuner/test/standard_datasets/5a6708dbb037cb59496d1265/validation'
    resize = '96'
    rescale = '0.00392156862745098'
    df = load_data.df_fromdir_classed(train_dir)
    x_train, y_train = load_data.load_fromdf(df, resize=resize, rescale=rescale)
    df = load_data.df_fromdir_classed(test_dir)
    x_test, y_test = load_data.load_fromdf(df, resize=resize, rescale=rescale)

    y_train = to_categorical(y_train)
    y_test = to_categorical(y_test)

    return x_train, y_train, x_test, y_test