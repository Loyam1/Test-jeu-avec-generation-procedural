import pygame
def take_key_and_actualise(key_wanted):
  if not hasattr(take_key_and_actualise,"old_keys"):
    take_key_and_actualise.old_keys={}
  if not key_wanted in take_key_and_actualise.old_keys:
    take_key_and_actualise.old_keys[key_wanted]=False
  keys=pygame.key.get_pressed()
  if (not take_key_and_actualise.old_keys[key_wanted]) and keys[key_wanted]:
    retuned_key=True
    take_key_and_actualise.old_keys[key_wanted]=True
  else:
    retuned_key=False
  for i in take_key_and_actualise.old_keys:
    if take_key_and_actualise.old_keys[i] and not keys[i]:
      take_key_and_actualise.old_keys[i]=False
  return retuned_key