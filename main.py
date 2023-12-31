import tehnovideo39
import coxo
import uima
import time
import baltmaximus
import rozetka
import tehnobaza

"""
print(f'Обычное сравнение {fuzz.ratio(str1, str2)}')
print(f'Частичное сравнение {fuzz.partial_ratio(str1, str2)}')
print(f'Сравнение по токену {fuzz.token_sort_ratio(str1, str2)}')
print(f'Продвинутое обычное сравнение {fuzz.WRatio(str1, str2)}')
"""

def main():
    
    start_tehnovideo = time.perf_counter()
    tehnovideo39.main()
    end_tehnovideo = time.perf_counter()
        
    start_coxo = time.perf_counter()
    coxo.main()
    end_coxo = time.perf_counter()
    
    start_uima = time.perf_counter()
    uima.main()
    end_uima = time.perf_counter()
   
    start_baltmaximus = time.perf_counter()
    baltmaximus.main()
    end_baltmaximus = time.perf_counter()
     
    start_rozetka = time.perf_counter()
    rozetka.main()
    end_rozetka = time.perf_counter()
    
    start_tehnobaza = time.perf_counter()
    tehnobaza.main()
    end_tehnobaza = time.perf_counter()
    
    
    print('Время выполнения парсинга tehnovideo39:', round((float(end_tehnovideo - start_tehnovideo) / 60), 1), ' минут!')
    print('Время выполнения парсинга coxo:', round((float(end_coxo - start_coxo) / 60), 1), ' минут!')
    print('Время выполнения парсинга uima:', round((float(end_uima - start_uima) / 60), 1), ' минут!')
    print('Время выполнения парсинга baltmaximus:', round((float(end_baltmaximus - start_baltmaximus) / 60), 1), ' минут!')
    print('Время выполнения парсинга rozetka:', round((float(end_rozetka - start_rozetka) / 60), 1), ' минут!')
    print('Время выполнения парсинга tehno-video:', round((float(end_tehnobaza - start_tehnobaza) / 60), 1), ' минут!')

if __name__ == '__main__':
    main()
