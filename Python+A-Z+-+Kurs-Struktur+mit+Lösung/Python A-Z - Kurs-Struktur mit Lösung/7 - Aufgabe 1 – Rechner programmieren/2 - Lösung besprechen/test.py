from unittest import TestCase
from unittest.mock import patch
import unittest 
from io import StringIO

class Evaluate(TestCase):
    
    def test_print_menu_option1(self):
        import Rechner
        option = Rechner.check_option('1')
        self.assertEqual(True, option, 'check_option("1") hat False zurückgegeben, True muss zurückgegeben werden.')

    def test_print_menu_option2(self):
        import Rechner
        option = Rechner.check_option('2')
        self.assertEqual(True, option, 'check_option("2") False zurückgegeben, True muss zurückgegeben werden.')

    def test_print_menu_option3(self):
        import Rechner
        option = Rechner.check_option('3')
        self.assertEqual(True, option, 'check_option("3") hat False zurückgegeben, True muss zurückgegeben werden.')

    def test_print_menu_option4(self):
        import Rechner
        option = Rechner.check_option('4')
        self.assertEqual(True, option, 'check_option("4") hat False zurückgegeben, True muss zurückgegeben werden.')
        
    @patch('builtins.input', side_effect=[4, 6])
    def test_ask_for_numbers(self, param):
        import Rechner
        a, b = Rechner.ask_for_numbers()
        self.assertEqual(4, a, 'ask_for_numbers() hat a nicht korrekt zurückgegeben! a und b müssen returned werden')
        self.assertEqual(6, b, 'ask_for_numbers() hat b nicht korrekt zurückgegeben! a und b müssen returned werden')
        
    @patch('builtins.input', side_effect=[4, 6])
    def test_add(self, param):
        import Rechner
        a = 4
        b = 6
        c = a + b
        z = Rechner.add(a, b)
        self.assertEqual(c, z, 'Die Add-Funktion hat das Ergebnis nicht korrekt zurückgegeben! Bitte kontrollieren!')

    @patch('builtins.input', side_effect=[4, 6])
    def test_subtract(self, param):
        import Rechner
        a = 4
        b = 6
        c = a - b
        z = Rechner.subtract(a, b)
        self.assertEqual(c, z, 'Die Subtract-Funktion hat das Ergebnis nicht korrekt zurückgegeben! Bitte kontrollieren!')
        
    @patch('builtins.input', side_effect=[4, 6])
    def test_multiply(self, param):
        import Rechner
        a = 4
        b = 6
        c = a * b
        z = Rechner.multiply(a, b)
        self.assertEqual(c, z, 'Die Multiply-Funktion hat das Ergebnis nicht korrekt zurückgegeben! Bitte kontrollieren!')
        
    @patch('builtins.input', side_effect=[4, 6])
    def test_division(self, param):
        import Rechner
        a = 4
        b = 6
        c = a / b
        z = Rechner.divide(a, b)
        self.assertEqual(c, z, 'Die Divide-Funktion hat das Ergebnis nicht korrekt zurückgegeben! Bitte kontrollieren!')

    @patch('builtins.input', side_effect=['0'])
    def test_exit(self, param):
        import Rechner
                
        with self.assertRaises(SystemExit) as exit_:
            Rechner.start_dialog()
        self.assertEqual(1, exit_.exception.code, 'Abbruch hat nicht Funktioniert: Bitte vergisse nicht die exit(1) Funktion aufzurufen bei Wahl 0')

if __name__ == '__main__':
    unittest.main()