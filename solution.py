import pandas as pd
import numpy as np


chat_id = 1119068275 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    t = 51;
    a = 2 * np.median(x) / (t ** 2)
    
    return a # Ваш ответ
