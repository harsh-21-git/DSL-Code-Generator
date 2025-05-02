
import unittest
from dsl_parser import DSLParser
from code_generator import CodeGenerator

class TestDSLTool(unittest.TestCase):
    def test_parser_and_generator(self):
        dsl_code = """class Person:
    name: string
    age: int
    isStudent: bool"""
        
        parser = DSLParser(dsl_code)
        parser.parse()

        self.assertEqual(parser.get_class_name(), "Person")
        self.assertEqual(parser.get_attributes(), [("name", "string"), ("age", "int"), ("isStudent", "bool")])

        generator = CodeGenerator(parser.get_class_name(), parser.get_attributes())
        java_code = generator.generate_java_code()
        self.assertIn("public class Person", java_code)
        self.assertIn("private String name;", java_code)
        self.assertIn("public int getAge()", java_code)

if __name__ == "__main__":
    unittest.main()
