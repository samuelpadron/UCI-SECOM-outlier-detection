from sklearn.metrics import DistanceMetric 
from sklearn.covariance import MinCovDet


class MahalanobisOutlierDetector:
    def __init__(self):
        self.mean_ = None
        self.inv_cov_ = None 
        
    def fit(self, X_scaled):
        pass 
    
    def score(self, X_scaled):
        pass 
    
    def detect(self, X_scaled, contamination=0.05):
        pass
        
        