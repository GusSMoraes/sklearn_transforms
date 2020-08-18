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
    
class TiraNota(BaseEstimator, TransformerMixin):
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
    
class MediaNA(BaseEstimator, TransformerMixin):
    def __init__(self, df_data_1):
		self.df_data_1 = df_data_1
        return

    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        data = X.copy()
        
        media = df_data_1['NOTA_GO'][(df_data_1.PERFIL == "EXCELENTE")].mean()
        for index, row in df_data_1[(df_data_1.PERFIL == "EXCELENTE")].iterrows():
          if(type(row['NOTA_GO']) == float and pd.isna(row['NOTA_GO'])):
            df_data_1.loc[df_data_1.index == index, 'NOTA_GO'] = media

        media = df_data_1['NOTA_GO'][(df_data_1.PERFIL == "MUITO_BOM")].mean()
        for index, row in df_data_1[(df_data_1.PERFIL == "MUITO_BOM")].iterrows():
          if(type(row['NOTA_GO']) == float and pd.isna(row['NOTA_GO'])):
            df_data_1.loc[df_data_1.index == index, 'NOTA_GO'] = media
        
        media = df_data_1['NOTA_GO'][(df_data_1.PERFIL == "EXATAS")].mean()
        for index, row in df_data_1[(df_data_1.PERFIL == "EXATAS")].iterrows():
          if(type(row['NOTA_GO']) == float and pd.isna(row['NOTA_GO'])):
            df_data_1.loc[df_data_1.index == index, 'NOTA_GO'] = media  

        media = df_data_1['NOTA_GO'][(df_data_1.PERFIL == "HUMANAS")].mean()
        for index, row in df_data_1[(df_data_1.PERFIL == "HUMANAS")].iterrows():
          if(type(row['NOTA_GO']) == float and pd.isna(row['NOTA_GO'])):
            df_data_1.loc[df_data_1.index == index, 'NOTA_GO'] = media

        media = df_data_1['NOTA_GO'][(df_data_1.PERFIL == "DIFICULDADE")].mean()
        for index, row in df_data_1[(df_data_1.PERFIL == "DIFICULDADE")].iterrows():
          if(type(row['NOTA_GO']) == float and pd.isna(row['NOTA_GO'])):
            df_data_1.loc[df_data_1.index == index, 'NOTA_GO'] = media

        # Retornamos um novo df_dataframe sem as colunas indesejadas
        return df_data_1    
    
class MediaZero(BaseEstimator, TransformerMixin):
    def __init__(self):
        return

    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        data = X.copy()
        
        media_de = data['NOTA_DE'][(data.PERFIL == "EXCELENTE")].mean()
        media_em = data['NOTA_EM'][(data.PERFIL == "EXCELENTE")].mean()
        media_mf = data['NOTA_MF'][(data.PERFIL == "EXCELENTE")].mean()
        media_go = data['NOTA_GO'][(data.PERFIL == "EXCELENTE")].mean()
        for index, row in data[(data.PERFIL == "EXCELENTE")].iterrows():
          if(row['NOTA_DE'] == 0):
            data.loc[data.index == index, 'NOTA_DE'] = media_de
          if(row['NOTA_EM'] == 0):
            data.loc[data.index == index, 'NOTA_EM'] = media_em
          if(row['NOTA_MF'] == 0):
            data.loc[data.index == index, 'NOTA_MF'] = media_mf
          if(row['NOTA_GO'] == 0):
            data.loc[data.index == index, 'NOTA_GO'] = media_go

        media_de = data['NOTA_DE'][(data.PERFIL == "MUITO_BOM")].mean()
        media_em = data['NOTA_EM'][(data.PERFIL == "MUITO_BOM")].mean()
        media_mf = data['NOTA_MF'][(data.PERFIL == "MUITO_BOM")].mean()
        media_go = data['NOTA_GO'][(data.PERFIL == "MUITO_BOM")].mean()
        for index, row in data[(data.PERFIL == "MUITO_BOM")].iterrows():
          if(row['NOTA_DE'] == 0):
            data.loc[data.index == index, 'NOTA_DE'] = media_de
          if(row['NOTA_EM'] == 0):
            data.loc[data.index == index, 'NOTA_EM'] = media_em
          if(row['NOTA_MF'] == 0):
            data.loc[data.index == index, 'NOTA_MF'] = media_mf
          if(row['NOTA_GO'] == 0):
            data.loc[data.index == index, 'NOTA_GO'] = media_go
        
        media_de = data['NOTA_DE'][(data.PERFIL == "EXATAS")].mean()
        media_em = data['NOTA_EM'][(data.PERFIL == "EXATAS")].mean()
        media_mf = data['NOTA_MF'][(data.PERFIL == "EXATAS")].mean()
        media_go = data['NOTA_GO'][(data.PERFIL == "EXATAS")].mean()
        for index, row in data[(data.PERFIL == "EXATAS")].iterrows():
          if(row['NOTA_DE'] == 0):
            data.loc[data.index == index, 'NOTA_DE'] = media_de
          if(row['NOTA_EM'] == 0):
            data.loc[data.index == index, 'NOTA_EM'] = media_em
          if(row['NOTA_MF'] == 0):
            data.loc[data.index == index, 'NOTA_MF'] = media_mf
          if(row['NOTA_GO'] == 0):
            data.loc[data.index == index, 'NOTA_GO'] = media_go 

        media_de = data['NOTA_DE'][(data.PERFIL == "HUMANAS")].mean()
        media_em = data['NOTA_EM'][(data.PERFIL == "HUMANAS")].mean()
        media_mf = data['NOTA_MF'][(data.PERFIL == "HUMANAS")].mean()
        media_go = data['NOTA_GO'][(data.PERFIL == "HUMANAS")].mean()
        for index, row in data[(data.PERFIL == "HUMANAS")].iterrows():
          if(row['NOTA_DE'] == 0):
            data.loc[data.index == index, 'NOTA_DE'] = media_de
          if(row['NOTA_EM'] == 0):
            data.loc[data.index == index, 'NOTA_EM'] = media_em
          if(row['NOTA_MF'] == 0):
            data.loc[data.index == index, 'NOTA_MF'] = media_mf
          if(row['NOTA_GO'] == 0):
            data.loc[data.index == index, 'NOTA_GO'] = media_go

        media_de = data['NOTA_DE'][(data.PERFIL == "DIFICULDADE")].mean()
        media_em = data['NOTA_EM'][(data.PERFIL == "DIFICULDADE")].mean()
        media_mf = data['NOTA_MF'][(data.PERFIL == "DIFICULDADE")].mean()
        media_go = data['NOTA_GO'][(data.PERFIL == "DIFICULDADE")].mean()
        for index, row in data[(data.PERFIL == "DIFICULDADE")].iterrows():
          if(row['NOTA_DE'] == 0):
            data.loc[data.index == index, 'NOTA_DE'] = media_de
          if(row['NOTA_EM'] == 0):
            data.loc[data.index == index, 'NOTA_EM'] = media_em
          if(row['NOTA_MF'] == 0):
            data.loc[data.index == index, 'NOTA_MF'] = media_mf
          if(row['NOTA_GO'] == 0):
            data.loc[data.index == index, 'NOTA_GO'] = media_go

        # Retornamos um novo dataframe sem as colunas indesejadas
        return data
    
class QRemove(BaseEstimator, TransformerMixin):
    def __init__(self):
        return

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        data = X.copy()

        Q1 = data['NOTA_DE'][(data.PERFIL == "EXCELENTE")].quantile(0.25)
        Q3 = data['NOTA_DE'][(data.PERFIL == "EXCELENTE")].quantile(0.75)
        IQR = Q3-Q1
        Lower = Q1-1.5*IQR
        Upper = Q3+1.5*IQR

        for index, row in data[(data.PERFIL == "EXCELENTE")].iterrows():
          if(row['NOTA_DE'] < Lower):
            data.drop(index, inplace=True)
          if(row['NOTA_DE'] > Upper):
            data.drop(index, inplace=True)

        Q1 = data['NOTA_EM'][(data.PERFIL == "EXCELENTE")].quantile(0.25)
        Q3 = data['NOTA_EM'][(data.PERFIL == "EXCELENTE")].quantile(0.75)
        IQR = Q3-Q1
        Lower = Q1-1.5*IQR
        Upper = Q3+1.5*IQR

        for index, row in data[(data.PERFIL == "EXCELENTE")].iterrows():
          if(row['NOTA_EM'] < Lower):
            data.drop(index, inplace=True)
          if(row['NOTA_EM'] > Upper):
            data.drop(index, inplace=True)

        Q1 = data['NOTA_MF'][(data.PERFIL == "EXCELENTE")].quantile(0.25)
        Q3 = data['NOTA_MF'][(data.PERFIL == "EXCELENTE")].quantile(0.75)
        IQR = Q3-Q1
        Lower = Q1-1.5*IQR
        Upper = Q3+1.5*IQR

        for index, row in data[(data.PERFIL == "EXCELENTE")].iterrows():
          if(row['NOTA_MF'] < Lower):
            data.drop(index, inplace=True)
          if(row['NOTA_MF'] > Upper):
            data.drop(index, inplace=True)

        Q1 = data['NOTA_GO'][(data.PERFIL == "EXCELENTE")].quantile(0.25)
        Q3 = data['NOTA_GO'][(data.PERFIL == "EXCELENTE")].quantile(0.75)
        IQR = Q3-Q1
        Lower = Q1-1.5*IQR
        Upper = Q3+1.5*IQR

        for index, row in data[(data.PERFIL == "EXCELENTE")].iterrows():
          if(row['NOTA_GO'] < Lower):
            data.drop(index, inplace=True)
          if(row['NOTA_GO'] > Upper):
            data.drop(index, inplace=True)

        Q1 = data['NOTA_DE'][(data.PERFIL == "MUITO_BOM")].quantile(0.25)
        Q3 = data['NOTA_DE'][(data.PERFIL == "MUITO_BOM")].quantile(0.75)
        IQR = Q3-Q1
        Lower = Q1-1.5*IQR
        Upper = Q3+1.5*IQR

        for index, row in data[(data.PERFIL == "MUITO_BOM")].iterrows():
          if(row['NOTA_DE'] < Lower):
            data.drop(index, inplace=True)
          if(row['NOTA_DE'] > Upper):
            data.drop(index, inplace=True)

        Q1 = data['NOTA_EM'][(data.PERFIL == "MUITO_BOM")].quantile(0.25)
        Q3 = data['NOTA_EM'][(data.PERFIL == "MUITO_BOM")].quantile(0.75)
        IQR = Q3-Q1
        Lower = Q1-1.5*IQR
        Upper = Q3+1.5*IQR

        for index, row in data[(data.PERFIL == "MUITO_BOM")].iterrows():
          if(row['NOTA_EM'] < Lower):
            data.drop(index, inplace=True)
          if(row['NOTA_EM'] > Upper):
            data.drop(index, inplace=True)

        Q1 = data['NOTA_MF'][(data.PERFIL == "MUITO_BOM")].quantile(0.25)
        Q3 = data['NOTA_MF'][(data.PERFIL == "MUITO_BOM")].quantile(0.75)
        IQR = Q3-Q1
        Lower = Q1-1.5*IQR
        Upper = Q3+1.5*IQR

        for index, row in data[(data.PERFIL == "MUITO_BOM")].iterrows():
          if(row['NOTA_MF'] < Lower):
            data.drop(index, inplace=True)
          if(row['NOTA_MF'] > Upper):
            data.drop(index, inplace=True)

        Q1 = data['NOTA_GO'][(data.PERFIL == "MUITO_BOM")].quantile(0.25)
        Q3 = data['NOTA_GO'][(data.PERFIL == "MUITO_BOM")].quantile(0.75)
        IQR = Q3-Q1
        Lower = Q1-1.5*IQR
        Upper = Q3+1.5*IQR

        for index, row in data[(data.PERFIL == "MUITO_BOM")].iterrows():
          if(row['NOTA_GO'] < Lower):
            data.drop(index, inplace=True)
          if(row['NOTA_GO'] > Upper):
            data.drop(index, inplace=True)

        Q1 = data['NOTA_DE'][(data.PERFIL == "EXATAS")].quantile(0.25)
        Q3 = data['NOTA_DE'][(data.PERFIL == "EXATAS")].quantile(0.75)
        IQR = Q3-Q1
        Lower = Q1-1.5*IQR
        Upper = Q3+1.5*IQR

        for index, row in data[(data.PERFIL == "EXATAS")].iterrows():
          if(row['NOTA_DE'] < Lower):
            data.drop(index, inplace=True)
          if(row['NOTA_DE'] > Upper):
            data.drop(index, inplace=True)

        Q1 = data['NOTA_EM'][(data.PERFIL == "EXATAS")].quantile(0.25)
        Q3 = data['NOTA_EM'][(data.PERFIL == "EXATAS")].quantile(0.75)
        IQR = Q3-Q1
        Lower = Q1-1.5*IQR
        Upper = Q3+1.5*IQR

        for index, row in data[(data.PERFIL == "EXATAS")].iterrows():
          if(row['NOTA_EM'] < Lower):
            data.drop(index, inplace=True)
          if(row['NOTA_EM'] > Upper):
            data.drop(index, inplace=True)

        Q1 = data['NOTA_MF'][(data.PERFIL == "EXATAS")].quantile(0.25)
        Q3 = data['NOTA_MF'][(data.PERFIL == "EXATAS")].quantile(0.75)
        IQR = Q3-Q1
        Lower = Q1-1.5*IQR
        Upper = Q3+1.5*IQR

        for index, row in data[(data.PERFIL == "EXATAS")].iterrows():
          if(row['NOTA_MF'] < Lower):
            data.drop(index, inplace=True)
          if(row['NOTA_MF'] > Upper):
            data.drop(index, inplace=True)

        Q1 = data['NOTA_GO'][(data.PERFIL == "EXATAS")].quantile(0.25)
        Q3 = data['NOTA_GO'][(data.PERFIL == "EXATAS")].quantile(0.75)
        IQR = Q3-Q1
        Lower = Q1-1.5*IQR
        Upper = Q3+1.5*IQR

        for index, row in data[(data.PERFIL == "EXATAS")].iterrows():
          if(row['NOTA_GO'] < Lower):
            data.drop(index, inplace=True)
          if(row['NOTA_GO'] > Upper):
            data.drop(index, inplace=True)

        Q1 = data['NOTA_DE'][(data.PERFIL == "HUMANAS")].quantile(0.25)
        Q3 = data['NOTA_DE'][(data.PERFIL == "HUMANAS")].quantile(0.75)
        IQR = Q3-Q1
        Lower = Q1-1.5*IQR
        Upper = Q3+1.5*IQR

        for index, row in data[(data.PERFIL == "HUMANAS")].iterrows():
          if(row['NOTA_DE'] < Lower):
            data.drop(index, inplace=True)
          if(row['NOTA_DE'] > Upper):
            data.drop(index, inplace=True)

        Q1 = data['NOTA_EM'][(data.PERFIL == "HUMANAS")].quantile(0.25)
        Q3 = data['NOTA_EM'][(data.PERFIL == "HUMANAS")].quantile(0.75)
        IQR = Q3-Q1
        Lower = Q1-1.5*IQR
        Upper = Q3+1.5*IQR

        for index, row in data[(data.PERFIL == "HUMANAS")].iterrows():
          if(row['NOTA_EM'] < Lower):
            data.drop(index, inplace=True)
          if(row['NOTA_EM'] > Upper):
            data.drop(index, inplace=True)

        Q1 = data['NOTA_MF'][(data.PERFIL == "HUMANAS")].quantile(0.25)
        Q3 = data['NOTA_MF'][(data.PERFIL == "HUMANAS")].quantile(0.75)
        IQR = Q3-Q1
        Lower = Q1-1.5*IQR
        Upper = Q3+1.5*IQR

        for index, row in data[(data.PERFIL == "HUMANAS")].iterrows():
          if(row['NOTA_MF'] < Lower):
            data.drop(index, inplace=True)
          if(row['NOTA_MF'] > Upper):
            data.drop(index, inplace=True)

        Q1 = data['NOTA_GO'][(data.PERFIL == "HUMANAS")].quantile(0.25)
        Q3 = data['NOTA_GO'][(data.PERFIL == "HUMANAS")].quantile(0.75)
        IQR = Q3-Q1
        Lower = Q1-1.5*IQR
        Upper = Q3+1.5*IQR

        for index, row in data[(data.PERFIL == "HUMANAS")].iterrows():
          if(row['NOTA_GO'] < Lower):
            data.drop(index, inplace=True)
          if(row['NOTA_GO'] > Upper):
            data.drop(index, inplace=True)

        Q1 = data['NOTA_DE'][(data.PERFIL == "DIFICULDADE")].quantile(0.25)
        Q3 = data['NOTA_DE'][(data.PERFIL == "DIFICULDADE")].quantile(0.75)
        IQR = Q3-Q1
        Lower = Q1-1.5*IQR
        Upper = Q3+1.5*IQR

        for index, row in data[(data.PERFIL == "DIFICULDADE")].iterrows():
          if(row['NOTA_DE'] < Lower):
            data.drop(index, inplace=True)
          if(row['NOTA_DE'] > Upper):
            data.drop(index, inplace=True)

        Q1 = data['NOTA_EM'][(data.PERFIL == "DIFICULDADE")].quantile(0.25)
        Q3 = data['NOTA_EM'][(data.PERFIL == "DIFICULDADE")].quantile(0.75)
        IQR = Q3-Q1
        Lower = Q1-1.5*IQR
        Upper = Q3+1.5*IQR

        for index, row in data[(data.PERFIL == "DIFICULDADE")].iterrows():
          if(row['NOTA_EM'] < Lower):
            data.drop(index, inplace=True)
          if(row['NOTA_EM'] > Upper):
            data.drop(index, inplace=True)

        Q1 = data['NOTA_MF'][(data.PERFIL == "DIFICULDADE")].quantile(0.25)
        Q3 = data['NOTA_MF'][(data.PERFIL == "DIFICULDADE")].quantile(0.75)
        IQR = Q3-Q1
        Lower = Q1-1.5*IQR
        Upper = Q3+1.5*IQR

        for index, row in data[(data.PERFIL == "DIFICULDADE")].iterrows():
          if(row['NOTA_MF'] < Lower):
            data.drop(index, inplace=True)
          if(row['NOTA_MF'] > Upper):
            data.drop(index, inplace=True)

        Q1 = data['NOTA_GO'][(data.PERFIL == "DIFICULDADE")].quantile(0.25)
        Q3 = data['NOTA_GO'][(data.PERFIL == "DIFICULDADE")].quantile(0.75)
        IQR = Q3-Q1
        Lower = Q1-1.5*IQR
        Upper = Q3+1.5*IQR

        for index, row in data[(data.PERFIL == "DIFICULDADE")].iterrows():
          if(row['NOTA_GO'] < Lower):
            data.drop(index, inplace=True)
          if(row['NOTA_GO'] > Upper):
            data.drop(index, inplace=True)                    

        # Retornamos um novo dataframe sem as colunas indesejadas
        return data
    
class ImplementaSmote(BaseEstimator, TransformerMixin):
    def __init__(self, features, target):
        self.features = features
        self.target = target

    def fit(self, A, B, y=None):
        return self

    def transform(self, A, B):
        from imblearn.over_sampling import SMOTE

        self.features = ["NOTA_DE", "NOTA_EM", "NOTA_MF", "NOTA_GO"]
        features = self.features

        X = data[self.features]
        y = data[self.target]
        
        X_resampled, y_resampled = SMOTE().fit_resample(X, y.values.ravel())
        X = X_resampled
        y = y_resampled 

        return X, y
