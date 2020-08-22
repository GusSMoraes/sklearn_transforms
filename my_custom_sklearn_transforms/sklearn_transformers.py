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
    
class Limite(BaseEstimator, TransformerMixin):
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
    
class NotaNan(BaseEstimator, TransformerMixin):
    def __init__(self):
        return

    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        data = X.copy()
        
        for index, row in data.iterrows():
            if(pd.isna(row['NOTA_DE']) & (row['REPROVACOES_DE'] > 0)):
                data.loc[data.index == index, 'NOTA_DE'] = 0
            if(pd.isna(row['NOTA_EM']) & (row['REPROVACOES_EM'] > 0)):
                data.loc[data.index == index, 'NOTA_EM'] = 0
            if(pd.isna(row['NOTA_MF']) & (row['REPROVACOES_MF'] > 0)):
                data.loc[data.index == index, 'NOTA_MF'] = 0
            if(pd.isna(row['NOTA_GO']) & (row['REPROVACOES_GO'] > 0)):
                data.loc[data.index == index, 'NOTA_GO'] = 0
                
        for index, row in data.iterrows():
            if(pd.isna(row['NOTA_DE']) & (row['REPROVACOES_DE'] == 0)):
                data.loc[data.index == index, 'NOTA_DE'] = data.loc[data.index == index , ["NOTA_GO","NOTA_EM","NOTA_MF"]].mean(axis=1)
            if(pd.isna(row['NOTA_EM']) & (row['REPROVACOES_EM'] == 0)):
                data.loc[data.index == index, 'NOTA_EM'] = data.loc[data.index == index , ["NOTA_GO","NOTA_DE","NOTA_MF"]].mean(axis=1)
            if(pd.isna(row['NOTA_MF']) & (row['REPROVACOES_MF'] == 0)):
                data.loc[data.index == index, 'NOTA_MF'] = data.loc[data.index == index , ["NOTA_GO","NOTA_EM","NOTA_DE"]].mean(axis=1)
            if(pd.isna(row['NOTA_GO']) & (row['REPROVACOES_GO'] == 0)):
                data.loc[data.index == index, 'NOTA_GO'] = data.loc[data.index == index , ["NOTA_DE","NOTA_EM","NOTA_MF"]].mean(axis=1)
                
        return data
