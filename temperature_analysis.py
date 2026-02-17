#Task 1: Create an Array and Basic Math
import numpy as np
import time
temps_celsius = np.array([22, 25, 28, 24, 26])
fahrenheit = temps_celsius * 1.8 + 32
print("Celsius:", temps_celsius)
print("Fahrenheit:", fahrenheit)
average_fahrenheit = np.mean(fahrenheit)
print("Average Fahrenheit:", average_fahrenheit)

#Task 2: Array Shape and Statistics
test_score = np.array([85, 90, 78, 92, 88, 76, 95, 82, 89, 91, 87, 84])
print("Shape:", test_score.shape)
print("Total elements:", test_score.size)
print("Highest score:", np.max(test_score))
print("Lowest score:", np.min(test_score))
print("Range:", np.max(test_score) - np.min(test_score))

#Task 3: Performance Comparison

# Create NumPy array
numpy_array = np.arange(1, 50001)
# Create Python list
python_list = list(range(1, 50001))
# ----- NumPy Sum -----
start_time = time.time()
numpy_sum = np.sum(numpy_array)
numpy_time = time.time() - start_time
# ----- Python List Sum -----
start_time = time.time()
python_sum = sum(python_list)
python_time = time.time() - start_time
# Results
print("NumPy Sum:", numpy_sum)
print("NumPy Time:", numpy_time)
print("Python List Sum:", python_sum)
print("Python Time:", python_time)
# Speed comparison
faster_times = python_time / numpy_time
print("NumPy is", faster_times, "times faster than Python list.")
