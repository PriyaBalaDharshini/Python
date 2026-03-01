# NumPy Practice Notes

## 1. Arrays

- **1D Array**: Single row/column of elements
- **2D Array**: Matrix with rows and columns
- **Mixed-Type Array**: If any element is float → dtype becomes `float64`; if any element is boolean → dtype also becomes `float64`
- **3D Array**: Multi-layered structure (layers, rows, columns)

---

## 2. Array Properties

- **Type**: All arrays are of type `numpy.ndarray`
- **Shape**: Returns dimensions (rows, columns, layers)
- **Size**: Total number of elements
- **ndim**: Number of dimensions
- **dtype**: Data type of elements (int64, float64, etc.)

---

## 3. Data Types

- Arrays can be explicitly created with a chosen `dtype`
- Mixed values (int, float, boolean) promote to the most general type (`float64`)

---

## 4. Special Arrays

- **zeros**: Creates an array filled with zeros (default float, can specify dtype)
- **ones**: Creates an array filled with ones
- **full**: Creates an array filled with a specified value
- **empty**: Creates an array with uninitialized values (garbage from memory)

---

## 5. Ranges and Spaced Values

- **linspace**: Generates evenly spaced values between a start and end
- **arange**: Generates values with a defined start, stop, and step

---

## ✅ Summary

- NumPy arrays are powerful structures for numerical data
- Key properties: `shape`, `size`, `ndim`, `dtype`
- Special functions allow quick creation of arrays (`zeros`, `ones`, `full`, `empty`)
- Range functions (`linspace`, `arange`) generate sequences of values

# NumPy Operations and Broadcasting Notes

## 1. Basic Arithmetic Operations

- Arrays support element‑wise operations:
  - **Addition (`+`)** → adds corresponding elements
  - **Subtraction (`-`)** → subtracts corresponding elements
  - **Multiplication (`*`)** → multiplies corresponding elements
  - **Division (`/`)** → divides corresponding elements (float result)
  - **Floor Division (`//`)** → divides and returns integer quotient

---

## 2. Broadcasting

- NumPy automatically expands smaller arrays or scalars to match the shape of larger arrays.
- Example: adding a scalar to an array → scalar is treated as an array of the same shape.
- Broadcasting rules:
  - Dimensions are compared from right to left.
  - If dimensions differ, the smaller one is stretched to match.
  - If they cannot be matched, broadcasting fails.

---

## 3. Aggregation

- Aggregation refers to applying operations that summarize array values.
- Common aggregation functions include:
  - **sum** → total of all elements
  - **min** → smallest element
  - **max** → largest element
  - **mean** → average of elements
  - **prod** → product of all elements

---

## ✅ Summary

- NumPy arrays allow direct arithmetic operations applied element‑wise.
- Broadcasting makes operations between arrays of different shapes possible.
- Aggregation functions provide quick summaries of array data.

# NumPy Aggregation Notes

## 1. Basic Aggregation Functions

- **sum** → Adds all elements in the array
- **mean** → Calculates the average value
- **median** → Finds the middle value when sorted
- **max** → Returns the largest element
- **min** → Returns the smallest element

---

## 2. Variance and Standard Deviation

- **Variance (`var`)** → Measures how far elements spread out from the mean
  - Formula: (1/N) Σ (xi − μ)²
- **Standard Deviation (`std`)** → Square root of variance, shows spread in same units as data

---

## 3. Aggregation on 2D Arrays

- **sum** → Adds all elements in the 2D array
- **sum with axis=0** → Column‑wise addition
- **sum with axis=1** → Row‑wise addition
- **conditional sum** → Sum of elements that satisfy a condition (e.g., values greater than 4)

---

## ✅ Summary

- Aggregation functions provide quick insights into data (total, average, spread, extremes).
- Variance and standard deviation measure variability.
- Axis parameter allows aggregation across rows or columns in multi‑dimensional arrays.
- Conditional aggregation enables selective calculations.

# NumPy Indexing and Slicing Notes

## 1. Indexing

- Access elements directly using their index position.
- Works for both 1D and multi‑dimensional arrays.

---

## 2. Slicing

- Extracts a sub‑array from the main array.
- Syntax: `start:stop:step`
- Variations:
  - From a specific index to the end
  - Entire array (`::`)
  - Reverse order (`[::-1]`)
  - Step slicing (`[::-2]`)
- Works with multi‑dimensional arrays using row and column ranges.

---

## 3. Boolean Indexing

- Create a boolean mask by applying conditions on the array.
- Use the mask to filter elements that satisfy the condition.
- Works for both 1D and 2D arrays.

---

## 4. Filtering

- Apply conditions directly to extract specific elements.
- Examples of conditions:
  - Greater than a value
  - Multiple conditions combined with logical operators (`&`, `|`)
  - Even/odd checks using modulus operator

---

## ✅ Summary

- Indexing retrieves single elements.
- Slicing extracts ranges or patterns of elements.
- Boolean indexing creates masks for conditional selection.
- Filtering allows complex conditions to select subsets of data.

# NumPy Reshaping and Stacking Notes

## 1. Reshaping

- **reshape**: Changes the shape of an array without changing data.
- Reshaped arrays may share memory with the original → modifying reshaped array can affect the original.

---

## 2. Flattening

- **ravel**: Flattens multi‑dimensional array into 1D. Returns a view (changes affect original).
- **flatten**: Flattens multi‑dimensional array into 1D. Returns a copy (changes do not affect original).

---

## 3. Stacking

- **hstack**: Joins arrays horizontally (along axis 1).
- **vstack**: Joins arrays vertically (along axis 0).
- **concatenate**: Joins arrays along any specified axis.

---

## 4. Transpose

- **transpose (`.T`)**: Swaps rows and columns.
- Double transpose (`.T.T`) returns the original array.

---

## ✅ Summary

- Reshaping allows changing array dimensions.
- Flattening converts multi‑dimensional arrays into 1D (view vs copy).
- Stacking combines arrays horizontally, vertically, or along any axis.
- Transpose swaps rows and columns for matrix operations.

# NumPy Random Data Notes

## 1. Random Values

- **rand** → Generates random float values between 0 and 1
- **randint** → Generates random integer values (end value not included)

---

## 2. Distributions

- **normal** → Generates values from a normal distribution
  - `loc` → mean
  - `scale` → standard deviation
  - `size` → number of values
- **uniform** → Generates values from a uniform distribution within a given range
- **binomial** → Generates values from a binomial distribution (important for probability/statistics)

---

## 3. Random Seed

- **seed** → Fixes the random sequence so results are reproducible
- Useful for testing and debugging

---

## ✅ Summary

- NumPy provides functions to generate random numbers and distributions.
- `rand` and `randint` are for simple random values.
- `normal`, `uniform`, and `binomial` are for statistical distributions.
- `seed` ensures reproducibility of random results.

# NumPy Random Data & Matplotlib Notes

## 1. Random Data in NumPy

- **rand** → Generates random float values between 0 and 1
- **randint** → Generates random integer values (end value not included)
- **normal** → Generates values from a normal distribution
  - `loc` → mean
  - `scale` → standard deviation
  - `size` → number of values
- **uniform** → Generates values from a uniform distribution within a given range
- **binomial** → Generates values from a binomial distribution (important for probability/statistics)
- **seed** → Fixes the random sequence so results are reproducible (useful for testing/debugging)

---

## 2. Matplotlib Basics

- **hist** → Plots a histogram (distribution of data)
  - `data` → dataset to plot
  - `bins` → number of intervals (bars). More bins = finer detail
  - `density` → if `True`, normalizes histogram so total area = 1 (probability density)
  - `alpha` → transparency of bars (0 = fully transparent, 1 = opaque)
  - `color` → bar color (`"r"` = red, `"g"` = green, `"b"` = blue, etc.)
- **xlabel** → Label for x‑axis
- **ylabel** → Label for y‑axis
- **title** → Title of the plot
- **show** → Displays the plot window

---

## ✅ Summary

- NumPy can generate random values and statistical distributions (`rand`, `randint`, `normal`, `uniform`, `binomial`).
- `seed` ensures reproducibility of random results.
- Matplotlib is used to visualize data distributions.
- Histogram parameters (`bins`, `density`, `alpha`, `color`) control how the plot looks.
- Labels and titles make plots readable, and `show` renders the final visualization.

# NumPy Linear Algebra Notes

## 1. Matrix Multiplication

- **Operators**:
  - `@` → matrix multiplication operator
  - `np.matmul()` → performs matrix multiplication
  - `np.dot()` → for 2D arrays, also performs matrix multiplication
- **Rule**: Multiply rows of the first matrix with columns of the second.
- **Result Shape**: `(rows of first, columns of second)`

---

## 2. Matrix Inverse

- **Concept**:
  - For a number: reciprocal → `1/n`
  - For a matrix: inverse → `A⁻¹`
  - Property: `A * A⁻¹ = I` (Identity Matrix)
- **Identity Matrix**: Diagonal elements = 1, off-diagonal = 0
- **Function**: `np.linalg.inv(A)` → computes inverse of matrix `A`
- **Note**: Only square matrices with non-zero determinant have an inverse.

---

## 3. Determinant

- **Definition**: Scalar value that indicates whether a matrix is invertible.
- **Function**: `np.linalg.det(A)` → computes determinant of matrix `A`
- **Rules**:
  - If determinant = 0 → matrix is singular (no inverse).
  - If determinant ≠ 0 → matrix is invertible.

---

## 4. Example Workflow

- Compute inverse: `inv(A)`
- Compute determinant: `det(A)`
- Multiply: `B @ inv(A)`
- Flatten result if needed: `X.flatten()` → allows unpacking into variables.

---

## ✅ Summary

- Use `@`, `matmul`, or `dot` for matrix multiplication.
- Inverse is the matrix equivalent of reciprocal.
- Determinant tells if a matrix is invertible.
- Always check shapes and flatten results before unpacking values.

Vectorized NumPy operations mean performing calculations on entire arrays at once instead of looping through elements one by one in Python. NumPy is built on fast C/C++ implementations, so vectorization makes your code both cleaner and much faster
