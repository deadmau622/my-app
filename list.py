motorcycles = []
motorcycles.append('yava')
motorcycles.append('honda')  # добавляет элемент в конец списка
print(motorcycles)
motorcycles.insert(0, 'ducati')
# вставка элемента по индексу в список, все остальные
# значения сдвигаются.
print(motorcycles)
popped_motorcycles = motorcycles.pop(0)
# удаляет элемент и сохраняет в переменной
# del motorcycles[-1]
# удаляет элемент по индексу
print(motorcycles)
motorcycles.remove('honda')
# удаляет первое вхождение элемента по значению
print(motorcycles)
