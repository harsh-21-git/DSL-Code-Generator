
# DSL Code Generator & Validator Tool

This project is a simplified developer tool that parses a mini Domain-Specific Language (DSL) and generates corresponding Java class boilerplate code. It simulates how internal tools in real-world development environments help automate repetitive tasks, such as writing data models or classes.

## 🔍 Project Purpose

The tool demonstrates:
- Parsing a custom DSL syntax
- Validating input and generating object-oriented Java code
- Mapping data types from DSL to Java types
- Automated unit testing
- Real-world tool design principles like modularity, testing, and code generation

## 💡 DSL Example

Input DSL:
```
class Book:
    title: string
    price: float
    pages: int
```

Generated Java Output:
```java
public class Book {
    private String title;
    private float price;
    private int pages;

    public String getTitle() { return title; }
    public void setTitle(String title) { this.title = title; }

    public float getPrice() { return price; }
    public void setPrice(float price) { this.price = price; }

    public int getPages() { return pages; }
    public void setPages(int pages) { this.pages = pages; }
}
```

## 📁 Files Included
- `dsl_parser.py`: Parses the DSL input
- `code_generator.py`: Generates Java class code
- `test_dsl_tool.py`: Unit tests for the parser and generator
- `main.py`: Example script for running the tool with custom input
- `README.md`: Project overview and usage guide

## ▶️ How to Run

### 1. Run the Unit Tests
```bash
python test_dsl_tool.py
```

### 2. Generate Java Code from Custom DSL
```bash
python main.py
```

## 📌 Requirements
- Python 3.x

## ✅ Ideal For
- Demonstrating code parsing, generation, and testing
- Building tools with real-world utility for developer workflows
- Applying OOP, regex, and automation skills

## 🧑‍💻 Created by
Harsh Arora  
[LinkedIn](https://www.linkedin.com/) | [GitHub](https://github.com/)
