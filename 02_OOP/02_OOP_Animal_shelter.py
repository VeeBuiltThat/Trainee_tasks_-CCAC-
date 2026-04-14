"""Create a base class Animal:
  - Attributes: name, age, adopted (bool, default False)
  - Method: speak() — returns a generic sound
  - Method: adopt() — marks the animal as adopted

Create two subclasses Dog and Cat:
  - Each overrides speak() with the right sound
  - Dog has an extra attribute: breed

Create a class Shelter:
  - Stores a list of animals
  - add_animal(animal) — adds to the list
  - available() — returns unadopted animals
  - adopt_animal(name) — finds by name and adopts it

Test with at least 3 animals."""