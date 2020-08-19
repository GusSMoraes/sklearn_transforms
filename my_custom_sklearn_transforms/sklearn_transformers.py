from sklearn.base import BaseEstimator, TransformerMixin

# All sklearn Transforms must have the `transform` and `fit` methods
class DropColumns(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
        data = X.copy()
        # Retornamos um novo dataframe sem as colunas indesejadas
        return data.drop(labels=self.columns, axis='columns')
    
class MaiorDez(BaseEstimator, TransformerMixin):
    def __init__(self):
        return

    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        data = X.copy()
        
        for index, row in data.iterrows():
            if(row['NOTA_EM'] > 10):
                data.loc[data.index == index, 'NOTA_EM'] = 10
            if(row['NOTA_DE'] > 10):
                data.loc[data.index == index, 'NOTA_DE'] = 10
            if(row['NOTA_MF'] > 10):
                data.loc[data.index == index, 'NOTA_MF'] = 10
            if(row['NOTA_GO'] > 10):
                data.loc[data.index == index, 'NOTA_GO'] = 10
                
        return data
    
class MenorZero(BaseEstimator, TransformerMixin):
    def __init__(self):
        return

    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        data = X.copy()
        
        for index, row in data.iterrows():
            if(row['NOTA_EM'] < 0):
                data.loc[data.index == index, 'NOTA_EM'] = 0
            if(row['NOTA_DE'] < 0):
                data.loc[data.index == index, 'NOTA_DE'] = 0
            if(row['NOTA_MF'] < 0):
                data.loc[data.index == index, 'NOTA_MF'] = 0
            if(row['NOTA_GO'] < 0):
                data.loc[data.index == index, 'NOTA_GO'] = 0
                
        return data

class MediaNan(BaseEstimator, TransformerMixin):
    def __init__(self):
        return

    def fit(self, X, y=None):
        return self
    
    def transform(self, X):

        data = X.copy()

        media = data.loc[data['NOTA_GO'] > 0, 'NOTA_GO'].mean()
        for index, row in data.iterrows():
            if(type(row['NOTA_GO']) == float and pd.isna(row['NOTA_GO'])):
                data.loc[data.index == index, 'NOTA_GO'] = media    

        return data     

class ImplementaSmote(BaseEstimator, TransformerMixin):
    def __init__(self, features, target):
        self.features = features
        self.target = target

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        from imblearn.over_sampling import SMOTE
        data = X.copy()

        self.features = ["NOTA_DE", "NOTA_EM", "NOTA_MF", "NOTA_GO"]

        X = data[self.features]
        y = data[self.target]
        
        X, y = SMOTE().fit_resample(X, y.values.ravel())
        
        X = pd.DataFrame(data=X, index=None, columns=self.features)
        y = pd.DataFrame(data=y, index=None, columns=self.target)

        return X, y
