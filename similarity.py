import numpy as np


def levenshtein_distance_ratio(first, second): #levenshtein distance algoritmasını uygulayan fonksiyon tanımı

    # Matrisin yaratılması
    rows = len(first)+1
    cols = len(second)+1
    distance = np.zeros((rows,cols),dtype = int)

    # ilk satır ve ilk sütunun ayarlanması
    for i in range(1, rows):
        distance[i][0] = i
        for j in range(1,cols):
            distance[0][j] = j

    # matris üzerinde uzaklığın bulunması için gerekli hesaplamaların yapılması     
    for col in range(1, cols):
        for row in range(1, rows):
            if first[row-1] == second[col-1]: # iki karakter eşit. bir alt problemin sonucunu aynen yaz
                distance[row][col] = distance[row-1][col-1]
            else: # karakterler eşit değil. komşulardan en küçüğüne bir ekle ve yaz.
                distance[row][col] = min(distance[row-1][col] + 1,distance[row][col-1] + 1,distance[row-1][col-1] + 1)
    
    ratio = ((len(first)+len(second)) - distance[row][col]) / (len(first)+len(second)) #benzerlik oranının hesaplanması
    return ratio

def return_the_most_similar(sickness,questions): # üstteki fonksiyonu kullanarak en benzer sorunun indexini döndüren fonksiyon

    max = levenshtein_distance_ratio(sickness,questions[0])
    index = 0
    index_counter = 1
    for i in questions:
        temp = levenshtein_distance_ratio(sickness,i)
        if(temp > max):
            max = temp
            index = index_counter
        index_counter = index_counter + 1 
    
    return index
