#!/usr/bin/env python3

def ask_ok(prompt : str, retries=4, remainder="Please, try again") -> bool:
    """Esperar respuesta de confirmación"""

    while True:
        ok = input(prompt)

        if ok in ('s', 'si'):
            return True
        if ok in ('n', 'no', 'nope'):
            return False
        
        retries = retries - 1;

        if retries < 0:
            raise ValueError('Respuesta inválida')
        
        print(remainder)

#-- Mensaje al usuario
while True:
  if ask_ok("Quiere terminar?"):
      break

