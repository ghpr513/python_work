motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)

motorcycles[0] = 'ducati' 
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

motorcycles = []
motorcycles.append('ducati')
motorcycles.append('honda')
print(motorcycles)

motorcycles = ['honda','yamaha','suzuki']
motorcycles.insert(2,'ducati')
print(motorcycles)

motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)

del motorcycles[1]
print(motorcycles)

motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)

poped_motorcycle = motorcycles.pop()
print(motorcycles)
print(poped_motorcycle)

motorcycles = ['honda','yamaha','suzuki']

last_owned = motorcycles.pop(0)
print(f"The last motorcycle I owned was a {last_owned.title()}")

motorcycles = ['honda','yamaha','suzuki','ducati']
print(motorcycles)

too_expensive = motorcycles[3]
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")

motorcycles = ['honda','yamaha','suzuki','ducati']
print(motorcycles[-1])
