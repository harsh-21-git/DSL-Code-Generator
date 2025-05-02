
from dsl_parser import DSLParser
from code_generator import CodeGenerator

dsl_code = """class Book:
    title: string
    price: float
    pages: int"""

parser = DSLParser(dsl_code)
parser.parse()

generator = CodeGenerator(parser.get_class_name(), parser.get_attributes())
java_code = generator.generate_java_code()

print("Generated Java Class:")
print(java_code)
