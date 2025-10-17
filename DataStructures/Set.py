

fruits_set = {"Apple", "Banana", "Mango", "Apple"}
fruits_set.add("Orange")
fruits_set.discard("Banana")
for fruit in fruits_set:
    print(fruit)
print("Mango" in fruits_set)
print("Final Set:", fruits_set)
