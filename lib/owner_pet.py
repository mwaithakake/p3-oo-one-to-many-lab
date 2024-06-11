class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in Pet.PET_TYPES:
            raise Exception("Invalid pet type")
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)  # Add the pet to the list of all pets
        if owner:  # If the pet has an owner, add it to the owner's list of pets
            owner.add_pet(self)

class Owner:
    def __init__(self, name):
        self.name = name
        self._pets = []

    def pets(self):
        return self._pets

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("The pet must be an instance of Pet")
        pet.owner = self
        self._pets.append(pet)  # Add the pet to the owner's list of pets

    def get_sorted_pets(self):
        return sorted(self._pets, key=lambda pet: pet.name)


