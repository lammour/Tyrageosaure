# TYRAGEOSAURE

import random

def tyrageosaure(dinos):
  emojis = ['🎄', '🎁', '🦌' , '⛄']
  adjectifs = ['surprenant', 'magnifique', 'somptueux', 'admirable', 'brillant', 'remarquable', 'flamboyant', 'étonnant']
  random.shuffle(dinos)
  result = f"{dinos[0]} offre un {random.choice(adjectifs)} tyracadeau à "
  for tyrapseudo in dinos[1:]:
    result += f"{tyrapseudo} {random.choice(emojis)} !\n{tyrapseudo} offre un {random.choice(adjectifs)} tyracadeau à "
  result += f"{dinos[0]} {random.choice(emojis)} !"
  return result

tyras = ["Gabausore", "Cléacératops", "Vincentimétrus",
         "Marionex", "Chemamosaure", "Doritosaure", "Volbecktus", "Yourassic",
         "Archaeopérette", "Godziluis", "Le Viktor", "FedEx", "Dominator",
         "Iva na", "Antoine", "Ugo", "Maud"]
tyrage = tyrageosaure(tyras)
print(tyrage)
