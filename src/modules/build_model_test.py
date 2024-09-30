from sklearn.ensemble import ExtraTreesRegressor
from util import print_metrics

def train_model(train_x, train_y):
    model = ExtraTreesRegressor(n_estimators=100, 
                                max_depth=12,
                              bootstrap=True, 
                                random_state=42, 
                               ) #verbose=2

    model = model.fit(train_x, train_y)
    return model

#  from util import print_metrics

# Evaluate
def predict_evaluate(model, test_x, test_y):
    # predict test data
    test_prediction = model.predict(test_x)

    # Evaluate model performance
    metrics = print_metrics(test_y, test_prediction)
    return test_prediction, metrics