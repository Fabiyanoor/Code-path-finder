# Test Path Finder and Cyclomatic Complexity Analyzer

This Python script provides tools to analyze Python code by generating a **Control Flow Graph (CFG)**, identifying **test paths**, and calculating **Cyclomatic Complexity**. The key components of the script are `TestPathFinder`, `CyclomaticComplexityCalculator`, and `VisualControlFlowGraph`. 

## Features

1. **Control Flow Graph Generation**  
   Parse Python source code to generate a CFG, representing function definitions, loops, conditionals, and other control structures.

2. **Test Path Discovery**  
   Identify all possible execution paths in the generated CFG using **Depth-First Traversal**.

3. **Cyclomatic Complexity Calculation**  
   Measure the Cyclomatic Complexity of Python code, which represents the number of independent paths through the code.

4. **Visualization**  
   Create a graphical representation of the CFG for better understanding of the code's flow.

---

## Components

### 1. **`GraphElements`**
Represents a node (vertex) in the CFG with its description and edges.

### 2. **`TestPathFinder`**
Handles CFG creation and test path discovery:
- **`add_vertex`**: Adds a new vertex to the graph.  
- **`add_edge_between`**: Adds an edge between two vertices.  
- **`depth_first_traversal`**: Performs a depth-first search to find execution paths.  
- **`generate_control_flow_graph`**: Builds the CFG from Python code's abstract syntax tree (AST).  
- **`get_test_paths`**: Returns all discovered test paths.  
- **`find_highest_complexity_path`**: Finds the path with the highest complexity.

### 3. **`CyclomaticComplexityCalculator`**
Calculates Cyclomatic Complexity using AST traversal. It increments decision points for constructs like:
- `if`, `elif`, and `else`
- Loops (`for`, `while`)
- `try` and `except` blocks

### 4. **`VisualControlFlowGraph`**
Creates a graphical representation of the CFG using Graphviz:
- Nodes represent control statements.
- Edges represent flow between these statements.

---

## Usage

### Prerequisites
- **Python 3.9+**
- **Graphviz** (for visualization)
- Install necessary Python modules:
  ```bash
  pip install graphviz
  ```

### Example

```python
import ast

# Source code to analyze
source_code = """
def example_function(x):
    if x > 0:
        print("Positive")
    elif x < 0:
        print("Negative")
    else:
        print("Zero")
"""

# Parse the source code
tree = ast.parse(source_code)

# Generate Control Flow Graph
finder = TestPathFinder()
finder.generate_control_flow_graph(tree)

# Get all test paths
paths = finder.get_test_paths()
print("Test Paths:", paths)

# Calculate Cyclomatic Complexity
calculator = CyclomaticComplexityCalculator(source_code)
complexity = calculator.calculate_cyclomatic_complexity()
print("Cyclomatic Complexity:", complexity)

# Visualize Control Flow Graph
visualizer = VisualControlFlowGraph()
nodes, edges = visualizer.analyze(tree)
print("Nodes:", nodes)
print("Edges:", edges)
```

---

## Output
- **Test Paths**: Lists all possible paths through the code.  
- **Cyclomatic Complexity**: A numerical value indicating code complexity.  
- **CFG Visualization**: Graphviz nodes and edges representing the flow.

---

## Applications
- **Code Optimization**: Identify bottlenecks or overly complex parts of the code.  
- **Testing**: Ensure all possible paths are covered during testing.  
- **Documentation**: Visualize code flow for better understanding and maintenance.

---

## Contributing
Feel free to submit pull requests or issues to improve functionality or fix bugs.

