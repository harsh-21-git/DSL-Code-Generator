
import re

class DSLParser:
    def __init__(self, dsl_code):
        self.dsl_code = dsl_code.strip()
        self.class_name = ""
        self.attributes = []

    def parse(self):
        lines = self.dsl_code.split('\n')
        if not lines or not lines[0].startswith("class"):
            raise SyntaxError("DSL must start with 'class' declaration")
        
        header = lines[0]
        match = re.match(r'class\s+(\w+):', header)
        if not match:
            raise SyntaxError("Invalid class declaration syntax")
        
        self.class_name = match.group(1)
        
        for line in lines[1:]:
            line = line.strip()
            if not line:
                continue
            match = re.match(r'(\w+)\s*:\s*(\w+)', line)
            if not match:
                raise SyntaxError(f"Invalid attribute line: {line}")
            self.attributes.append((match.group(1), match.group(2)))

    def get_class_name(self):
        return self.class_name

    def get_attributes(self):
        return self.attributes
