#seequential_nn_model_relu_droput01_lr001_sigmoid_40_epochs_2019-03-30-1
sequential_nn_model = None
#del sequential_nn_model
if sequential_nn_model:
    del sequential_nn_model
sequential_nn_model = Sequential()
sequential_nn_model.add(Dense(batch_size, input_dim=200, kernel_initializer='normal', activation='relu'))
#sequential_nn_model.add(Dense(batch_size, input_shape=(100, 200), kernel_initializer='normal', activation='sigmoid'))
#sequential_nn_model.add(Dropout(0.76))
sequential_nn_model.add(Dropout(0.1))
sequential_nn_model.add(Dense(1, kernel_initializer='normal', activation='sigmoid'))

sequential_nn_model.compile(loss='binary_crossentropy', optimizer=Adam(lr=0.001), metrics=['accuracy', auc])


#sequential_nn_model_relu_droput024_lr001_sigmoid_40_epochs_2019-03-30-1
sequential_nn_model = None
#del sequential_nn_model
if sequential_nn_model:
    del sequential_nn_model
sequential_nn_model = Sequential()
sequential_nn_model.add(Dense(batch_size, input_dim=200, kernel_initializer='normal', activation='relu'))
#sequential_nn_model.add(Dense(batch_size, input_shape=(100, 200), kernel_initializer='normal', activation='sigmoid'))
#sequential_nn_model.add(Dropout(0.76))
sequential_nn_model.add(Dropout(0.24))
sequential_nn_model.add(Dense(1, kernel_initializer='normal', activation='sigmoid'))

sequential_nn_model.compile(loss='binary_crossentropy', optimizer=Adam(lr=0.001), metrics=['accuracy', auc])


#sequential_nn_model_relu_droput024_lr001_sigmoid_batchnorm_40_epochs_2019-03-31
sequential_nn_model.add(Dense(batch_size, input_dim=200, kernel_initializer='normal', activation='relu'))
sequential_nn_model.add(Dropout(0.1))
sequential_nn_model.add(BatchNormalization())
sequential_nn_model.add(Dense(batch_size, input_dim=100, kernel_initializer='normal', activation='sigmoid'))
sequential_nn_model.add(Dropout(0.1))
sequential_nn_model.add(BatchNormalization())
sequential_nn_model.add(Dense(batch_size, input_dim=50, kernel_initializer='normal', activation='relu'))
sequential_nn_model.add(Dropout(0.1))
sequential_nn_model.add(BatchNormalization())
sequential_nn_model.add(Dense(batch_size, input_dim=50, kernel_initializer='normal', activation='sigmoid'))
#sequential_nn_model.add(Dense(batch_size, input_shape=(100, 200), kernel_initializer='normal', activation='sigmoid'))
#sequential_nn_model.add(Dropout(0.76))
#sequential_nn_model.add(Dropout(0.24))
sequential_nn_model.add(Dropout(0.1))
sequential_nn_model.add(BatchNormalization())
sequential_nn_model.add(Dense(batch_size, input_dim=10, kernel_initializer='normal', activation='relu'))
sequential_nn_model.add(Dropout(0.1))
sequential_nn_model.add(BatchNormalization())
sequential_nn_model.add(Dense(batch_size, input_dim=10, kernel_initializer='normal', activation='sigmoid'))
sequential_nn_model.add(Dropout(0.1))
sequential_nn_model.add(BatchNormalization())
sequential_nn_model.add(Dense(1, kernel_initializer='normal', activation='sigmoid'))

sequential_nn_model.compile(loss='binary_crossentropy', optimizer=Adam(lr=0.001), metrics=['accuracy', auc])
