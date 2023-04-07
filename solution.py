import pandas as pd
import numpy as np

from scipy.stats import norm, chi2


chat_id = 124625853 # Ваш chat ID, не меняйте название переменной
def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 1 - p
    n_2 = 2*len(x)

    # Calculate the sample standard deviation

    df = n_2

    lower_bound = sum(x**2)/chi2.ppf(1-alpha/2,df)
    upper_bound = sum(x**2)/chi2.ppf(alpha/2, df)


    return (np.sqrt(lower_bound/39), np.sqrt(upper_bound/39))
