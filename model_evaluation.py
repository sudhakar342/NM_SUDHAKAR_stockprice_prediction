import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, mean_absolute_error
import numpy as np

def evaluate_model(y_true, y_pred):
    rmse = np.sqrt(mean_squared_error(y_true, y_pred))
    mae = mean_absolute_error(y_true, y_pred)
    print(f'RMSE: {rmse}, MAE: {mae}')
    
    plt.figure(figsize=(10,6))
    plt.plot(y_true, label='Actual')
    plt.plot(y_pred, label='Predicted')
    plt.title('Actual vs Predicted Prices')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    # Example dummy data
    y_true = np.random.rand(100)
    y_pred = y_true + np.random.normal(0, 0.1, 100)
    evaluate_model(y_true, y_pred)
