import pandas as pd
import numpy as np

from scipy.stats import norm, chi2


chat_id = 124625853 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 1 - p
    n = len(x)

    x_bar = np.mean(x)

    s = np.std(x, ddof=1)

    df = n - 1

    lower_bound = (n-1)*s**2/chi2.ppf(1-alpha/2,df)
    upper_bound = (n-1)*s**2/chi2.ppf(alpha/2, df)

    # Return the result as a tuple
    return (np.sqrt(lower_bound/39), np.sqrt(upper_bound/39))
