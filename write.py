from take_key_and_actualise import *
key_of_chifre={pygame.K_0:0,pygame.K_1:1,pygame.K_2:2,pygame.K_3:3,pygame.K_4:4,pygame.K_5:5,pygame.K_6:6,pygame.K_7:7,pygame.K_8:8,pygame.K_9:9}
key_of_letre={pygame.K_a:"a",pygame.K_z:"z",pygame.K_e:"e",pygame.K_r:"r",pygame.K_t:"t",pygame.K_y:"y",pygame.K_u:"u",pygame.K_i:"i",pygame.K_o:"o",pygame.K_p:"p",pygame.K_q:"q",pygame.K_s:"s",pygame.K_d:"d",pygame.K_f:"f",pygame.K_g:"g",pygame.K_h:"h",pygame.K_j:"j",pygame.K_k:"k",pygame.K_l:"l",pygame.K_m:"m",pygame.K_w:"w",pygame.K_x:"x",pygame.K_c:"c",pygame.K_v:"v",pygame.K_b:"b",pygame.K_n:"n"}
key_of_symbole_up={pygame.K_RIGHTPAREN:"°",pygame.K_ASTERISK:"µ",pygame.K_EQUALS:"+",pygame.K_COLON:"/",pygame.K_SEMICOLON:".",pygame.K_LESS:">",pygame.K_COMMA:"?",pygame.K_EXCLAIM:"§",pygame.K_CARET:"¨",pygame.K_DOLLAR:"£"}
key_of_symbole_down={pygame.K_7:"è",pygame.K_8:"_",pygame.K_9:"ç",pygame.K_0:"à",pygame.K_CARET:"^",pygame.K_COMMA:",",pygame.K_2:"é",pygame.K_EXCLAIM:"!",pygame.K_3:"\"",pygame.K_DOLLAR:"$",pygame.K_1:"&",pygame.K_5:"(",pygame.K_RIGHTPAREN:")",pygame.K_ASTERISK:"*",pygame.K_EQUALS:"=",pygame.K_4:"'",pygame.K_6:"-",pygame.K_SEMICOLON:";",pygame.K_COLON:":",pygame.K_LESS:">"}
key_of_symbole_alt={pygame.K_2:"~",pygame.K_3:"#",pygame.K_4:"{",pygame.K_5:"[",pygame.K_6:"|",pygame.K_7:"`",pygame.K_8:"\\",pygame.K_9:"^",pygame.K_0:"@",pygame.K_RIGHTPAREN:"]",pygame.K_EQUALS:"}",pygame.K_DOLLAR:"¤",pygame.K_e:"€"}
str_to_type_text={"<class 'str'>":str, "<class 'int'>":int}
def write(text,chifre=True,letre=True,symbole=True):
  pygame.event.get()
  type_text=str(type(text))
  text=str(text)
  if not pygame.key.get_pressed()[pygame.K_RALT] and letre:
    for i in key_of_letre:
      if take_key_and_actualise(i):
        if pygame.key.get_pressed()[pygame.K_LSHIFT] or pygame.key.get_pressed()[pygame.K_RSHIFT]:
          text += f"{(chr(ord(key_of_letre[i]) - 32))}"
          return str_to_type_text[type_text](text)
        else:
          text += f"{(key_of_letre[i])}"
          return str_to_type_text[type_text](text)
  if (pygame.key.get_pressed()[pygame.K_LSHIFT] or pygame.key.get_pressed()[pygame.K_RSHIFT]) and not \
  pygame.key.get_pressed()[pygame.K_RALT] and chifre:
    for i in key_of_chifre:
      if take_key_and_actualise(i):
        text += f"{(key_of_chifre[i])}"
        return str_to_type_text[type_text](text)
    for i in key_of_symbole_up:
      if take_key_and_actualise(i):
        text += f"{key_of_symbole_up[i]}"
        return str_to_type_text[type_text](text)
  elif not pygame.key.get_pressed()[pygame.K_RALT] and symbole and not (pygame.key.get_pressed()[pygame.K_LSHIFT] or pygame.key.get_pressed()[pygame.K_RSHIFT]):
    for i in key_of_symbole_down:
      if take_key_and_actualise(i):
        text += f"{(key_of_symbole_down[i])}"
        return str_to_type_text[type_text](text)
  elif symbole and pygame.key.get_pressed()[pygame.K_RALT]:
    for i in key_of_symbole_alt:
      if take_key_and_actualise(i):
        text += f"{(key_of_symbole_alt[i])}"
        return str_to_type_text[type_text](text)
  if take_key_and_actualise(pygame.K_BACKSPACE):
    text=text.removesuffix(text[-1])
    return str_to_type_text[type_text](text)
  return str_to_type_text[type_text](text)