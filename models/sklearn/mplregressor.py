from sklearn import neural_network
import models.sklearn.setbuilder as sb
import models.sklearn.evaluator as eval

# Build training & test sets
data = sb.SetBuilder(target='NumberOfCustomers').exclude('NumberOfSales').build()


nn = neural_network.MLPRegressor(
    hidden_layer_sizes=(100,5),
    activation='relu',
    solver='adam',
    batch_size='auto',
    learning_rate='adaptive',
    learning_rate_init=0.01,
    max_iter=50,
    shuffle=True,
    random_state=9,
    tol=0.000001,
    verbose=True,
    warm_start=False,
    momentum=0.9,
    nesterovs_momentum=True,
    early_stopping=False,
    validation_fraction=0.1,
    beta_1=0.9,
    beta_2=0.999,
    epsilon=1e-08
)

n = nn.fit(data.xtr, data.ytr.ravel())

ypred = nn.predict(data.xts)
print('R2 = %s' % eval.evaluate(data.yts, ypred))