def studentReg(ages_train, net_worths_train):
    ### import the sklearn regression module, create, and train your regression
    ### name your regression reg
 
    ### your code goes here!
    from sklearn import datasets, linear_model   
    reg = linear_model.LinearRegression()

    # Train the model using the training sets
    reg.fit(ages_train, net_worths_train)
    
    return reg