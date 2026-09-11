import pandas as pd
from src.uci_secom_outlier_detection.data_loader import load_dataset
from src.uci_secom_outlier_detection.preprocessing import Preprocessor

X, y = load_dataset()

preprocessor = Preprocessor()
X_scaled = preprocessor.fit_transform(X)

print(f"Original shape: {X.shape}")
print(f"After preprocessing: {X_scaled.shape}")
print(f"Kept {len(preprocessor.kept_columns_)} columns")
print(f"Any NaNs remaining? {pd.isna(X_scaled).any()}")
print(f"Column means (should be ~0): {X_scaled.mean(axis=0)[:5]}")
print(f"Column stds (should be ~1): {X_scaled.std(axis=0)[:5]}")