import unittest

from translator import englishToFrench, frenchToEnglish

class TestE2F(unittest.TestCase):
    def testTranslation(self):
        self.assertEqual(englishToFrench("Hello"),"Bonjour")
    
    def testNullInput(self):
        self.assertIsNone(englishToFrench(""),"")

class TestF2E(unittest.TestCase):
    def testTranslation(self):
        self.assertEqual(frenchToEnglish("Bonjour"),"Hello")

    def testNullInput(self):
        self.assertIsNone(frenchToEnglish(""),"")

unittest.main()