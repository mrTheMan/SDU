global Entity_list
Entity_list = []


class entity():

    name = ""
    attr = []

    def __getattr__(self, key):
        print("Entity: " + key)
        self.name = key
        return entities

class field():

    def __getattr__(self, key):
        print("Field: " + key + "; Parent is: " + entities.current_entity.name)

        entities.current_entity.attr.append(key)
        print(entities.current_entity.attr)
        return entities



class entities():

    Entity = entity()
    current_entity = Entity

    Entity_list.append(Entity)

    Field = field()

'''
{

entities.
        Entity.Batman.
            Field.alex.
        Entity.Cat.
            Field.mikkel.
            Field.Gray

}





print(" ")
print(" ")
print(" ")

print()
'''




