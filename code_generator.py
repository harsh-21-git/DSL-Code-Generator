
class CodeGenerator:
    def __init__(self, class_name, attributes):
        self.class_name = class_name
        self.attributes = attributes

    def generate_java_code(self):
        lines = [f"public class {self.class_name} {{"]
        for attr, typ in self.attributes:
            java_type = self.map_type(typ)
            lines.append(f"    private {java_type} {attr};")
        
        lines.append("")
        for attr, typ in self.attributes:
            java_type = self.map_type(typ)
            lines.append(f"    public {java_type} get{attr.capitalize()}() {{ return {attr}; }}")
            lines.append(f"    public void set{attr.capitalize()}({java_type} {attr}) {{ this.{attr} = {attr}; }}")
        
        lines.append("}")
        return '\n'.join(lines)

    def map_type(self, dsl_type):
        return {
            'int': 'int',
            'string': 'String',
            'float': 'float',
            'bool': 'boolean'
        }.get(dsl_type.lower(), 'Object')
