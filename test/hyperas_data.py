def data():
    train_dir = 'standard_datasets/5a4e3a66b037cb9b8e2ef254/auged' 
    test_dir = 'standard_datasets/5a4e3a66b037cb9b8e2ef254/validation'
    resize = 96 
    rescale = 1 
    df = utils.df_fromdir(train_dir)
    x_train, y_train = utils.load_fromdf(df, resize=resize, rescale=rescale)
    df = utils.df_fromdir(test_dir)
    x_test, y_test = utils.load_fromdf(df, resize=resize, rescale=rescale)

    y_train = to_categorical(y_train)
    y_test = to_categorical(y_test)

    return x_train, y_train, x_test, y_test
