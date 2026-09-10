#screen is the pygame.display.set_mode and instruction is a dictionnary {"text": "str", "coordinates": [x, y], "size": int, "color": rgb or "name"} "text" and "coordinates" are required, but the others are not
import pygame
def print_in_screen (user_instruction, screen):
  intruction = {"text": user_instruction["text"], "coordinates": user_instruction["coordinates"]}
  if user_instruction.get("size",30) != 30:
    intruction["size"] = user_instruction["size"]
  else:
    intruction["size"] = 30
  if user_instruction.get("color","white") != "white":
    intruction["color"] = user_instruction["color"]
  else:
    intruction["color"] = "white"
  pygame.init()
  font = pygame.font.Font(None,intruction["size"])
  screen.blit(font.render(intruction["text"], True, intruction["color"]),intruction["coordinates"])