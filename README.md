# Lab 2: Graph Traversal and Analysis

This project provides Python implementations for reading, transforming, and analyzing graph data using adjacency and incidence matrices. The code includes methods for performing Depth First Search (DFS), Breadth First Search (BFS), and calculating graph properties such as radius. Additionally, it provides flexible utilities to work with graph data in various formats, making it a comprehensive toolkit for graph analysis tasks.

## Features

### Graph Input and Transformation

1. **Adjacency Matrix Transformation**
   - Converts an adjacency matrix into an adjacency list (dictionary format).
   - Enables easier traversal and manipulation of graph data using dictionary-based representations.

2. **Reading Graphs**
   - Reads graph data from a file in incidence or adjacency matrix format.
   - Supports parsing graph definitions from structured text files.

3. **Flexible Input Formats**
   - Handles both adjacency and incidence matrix formats.
   - Allows easy conversion between representations.

### Graph Traversal

1. **Depth First Search (DFS)**
   - Supports both iterative and recursive implementations.
   - Handles adjacency matrices and dictionaries.
   - Provides an efficient way to explore all vertices connected to a start node.

2. **Breadth First Search (BFS)**
   - Iterative implementation for both adjacency matrices and dictionaries.
   - Ensures layer-by-layer traversal of the graph.
   - Suitable for finding the shortest path in unweighted graphs.

### Graph Properties

1. **Graph Radius**
   - Computes the radius of the graph using adjacency matrices or dictionaries.
   - Helps analyze the compactness of the graph.

2. **Eccentricity Calculations**
   - Determines the eccentricity of each node to identify central and peripheral nodes.
   - Supports further analysis like diameter and center of the graph.

## How to Use

### Dependencies

- Python 3.7 or later
- No external libraries are required.

### Running the Code

1. **Prepare Your Graph Data**
   - Place your graph data in a text file formatted as either an adjacency or incidence matrix. Ensure the file follows the expected format with proper delimiters for rows and columns.

2. **Run the Script**
   - Execute the script directly or import its functions into another Python file. For example:

```bash
python traversals.py
```

3. **Graph Processing Functions**
   - Use the following functions to read and process the graph data:
     - `read_adjacency_matrix(filename)`
     - `read_incidence_matrix(filename)`
     - `read_adjacency_dict(filename)`

4. **Run Analysis or Traversals**
   - Call the desired traversal or analysis functions, providing the graph data and start node as arguments:
     - `iterative_adjacency_dict_dfs(graph, start)`
     - `iterative_adjacency_matrix_bfs(graph, start)`
     - `adjacency_matrix_radius(graph)`

5. **Visualize Results**
   - Print or save the traversal or analysis results for further use or visualization:

```python
print("Graph Traversal Results:", results)
```

### Example Usage

#### BFS Traversal Example

```python
from traversals import read_adjacency_matrix, iterative_adjacency_matrix_bfs

# Load graph from a file
graph = read_adjacency_matrix("graph_data.txt")

# Perform BFS
result = iterative_adjacency_matrix_bfs(graph, 0)
print("BFS Traversal:", result)
```

#### Radius Calculation Example

```python
from traversals import read_adjacency_matrix, adjacency_matrix_radius

# Load graph from a file
graph = read_adjacency_matrix("graph_data.txt")

# Compute radius
radius = adjacency_matrix_radius(graph)
print("Graph Radius:", radius)
```

### Advanced Usage

- You can extend the provided functions to incorporate weighted graphs or additional graph properties.
- The library is modular, allowing easy integration with larger projects.

### Testing

The script includes test cases for most functions. Run the following command to verify functionality:

```bash
python traversals.py
```

### Debugging Tips

- Use Python's built-in `doctest` module to run embedded tests.
- Ensure that input graph files follow the expected format to avoid parsing errors.
- Review function documentation for expected inputs and outputs.

## File Structure

- **traversals.py**: Contains all the graph-related functions and doctests. Includes:
  - Graph input readers.
  - Transformation utilities.
  - Traversal algorithms (DFS, BFS).
  - Graph property calculators (radius, eccentricity).

## Author

- Nazar Mykhailyshchuk
- Anton Deputat

## License

This project is licensed under the MIT License. See the LICENSE file for details. The permissive license allows for both academic and commercial use.

## Acknowledgments

- Python documentation for `doctest` and graph traversal algorithms.
- Educational resources on graph theory and algorithms.

