import unittest


class TestL1(unittest.TestCase):

    def test_print(self):
        # -- Esta prueba sólo imprime en la consola
        # -- Realmente no se comprueba nada
        print("══════════════════════════════")
        print("Mensaje 1")
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print("✅ Test 1: OK")

    def test_var(self):
        # -- Asignar un valor a la variable
        a = 1

        # -- Comprobar que la variable es igual a 1
        self.assertEqual(a, 1)
        print("✅ Test 2: OK")

    def test_var_fail(self):
        # -- Este test siempre falla
        self.assertFalse(True)
        print("✅ Test 3: OK")


if __name__ == "__main__":
    unittest.main()
