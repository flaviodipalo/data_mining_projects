from sklearn.preprocessing import PolynomialFeatures
from sklearn import linear_model
import models.sklearn.setbuilder as sb
import models.sklearn.evaluator as eval

# LINEAR REGRESSOR, DEG = 2
# TRAINING SET = mean_var_pre_imputed.csv
# PREDICTION OF SALES (with customers as input) : R2 = 0.934850052142
# PREDICTION OF CUSTOMERS : R2 = 0.875309426178


# Build training & test sets
data = sb.SetBuilder(target='NumberOfCustomers').exclude('NumberOfSales').build()

poly_degree = 2

# Performs simple linear regression
print("Linear regression started, polynomial degree = %s" % poly_degree)

poly = PolynomialFeatures(degree=poly_degree)
xtr_ = poly.fit_transform(data.xtr)
xts_ = poly.fit_transform(data.xts)

clf = linear_model.LinearRegression()
clf.fit(xtr_, data.ytr)
ypred = clf.predict(xts_)

print('R2 = %s' % eval.evaluate(data.yts, ypred))