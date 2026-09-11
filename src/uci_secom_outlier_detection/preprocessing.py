import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler


class Preprocessor:
    def __init__(self):
        self.imputer_ = None
        self.scaler_ = None
        self.kept_columns_ = None
    
    
    def fit(self, X: pd.DataFrame):
        missing_pct = X.isna().mean()
        variances = X.var()
        self.kept_columns_ = X.loc[:,(missing_pct <= 0.20) & (variances > 1e-6)].columns
        
        X_kept = X[self.kept_columns_]
        
        self.imputer_ = SimpleImputer(strategy="median")
        X_imputed = self.imputer_.fit_transform(X_kept)
        
        self.scaler_ = StandardScaler()
        self.scaler_.fit(X_imputed)
        
        return self
    
    
    def transform(self, X):
        X_kept = X[self.kept_columns_]
        X_imputed = self.imputer_.transform(X_kept)
        X_scaled = self.scaler_.transform(X_imputed)
        
        return X_scaled
    
    
    def fit_transform(self, X):
        return self.fit(X).transform(X)