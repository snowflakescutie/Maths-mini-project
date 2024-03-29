import numpy as np
import matplotlib.pyplot as plt

# Function to generate 'n' random one-digit numbers
def generate_numbers(n):
    return np.random.randint(0, 10, size=n)

# Function to count the number of even numbers in an array
def count_even_numbers(arr):
    return np.sum(arr % 2 == 0)

# Function to perform trials and record the counts
def perform_trials(trials, numbers_per_trial):
    even_counts = []
    for _ in range(trials):
        numbers = generate_numbers(numbers_per_trial)
        even_counts.append(count_even_numbers(numbers))
    return even_counts

# Function to draw the graph of count vs frequency
def draw_graph(counts):
    unique_counts, frequencies = np.unique(counts, return_counts=True)
    plt.bar(unique_counts, frequencies)
    plt.xlabel('Count of Even Numbers')
    plt.ylabel('Frequency')
    plt.title('Count vs Frequency of Even Numbers')
    plt.show()

# Perform trials for various numbers of trials
trials_list = [10, 20, 30, 40, 50, 100, 200, 1000]
numbers_per_trial = 100

for trials in trials_list:
    print(f"Number of Trials: {trials}")
    even_counts = perform_trials(trials, numbers_per_trial)
    draw_graph(even_counts)
