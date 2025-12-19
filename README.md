# Password-Checker-Generator
Within the course CSCI377 (Computer Algorithms) conducted by Prof. Fatma Najar, I have worked on a Password Checker/Generator as my final project for this course.

Password Analysis Project
Author: Davide Mateas
Course: CSCI 377
Language: Python
Overview
This project focuses on analyzing password strength and detecting compromised or weak passwords using fundamental algorithms. I implemented a password checker and generator to compare algorithmic performance as the dataset scales, while also evaluating password strength based on character composition.
The project demonstrates practical applications of algorithmic complexity concepts such as O(N), O(N log N), and O(log N) in a security-focused context.
Problem Statement
As password datasets grow larger, checking whether a password is weak or compromised becomes increasingly time-consuming. The challenge is to efficiently detect weak passwords while understanding how different algorithms scale with larger inputs.
Project Goals
Build a password checker that identifies weak or commonly used passwords
Compare the performance of:
Linear Search O(N)
Binary Search O(log N)
Merge Sort O(N log N)
Implement a password strength evaluator and generator
Measure and analyze time differences as dataset size increases
Algorithms Used
Linear Search (O(N)) – scans each password sequentially
Merge Sort (O(N log N)) – sorts large password lists efficiently
Binary Search (O(log N)) – performs fast lookups on sorted data
Password Evaluation (O(L)) – analyzes password strength based on length and character diversity
Password Generation (O(L)) – creates strong randomized passwords
System Design
I used a dataset of 100,000 common weak passwords
The list is stored in two forms:
Unsorted (for linear search)
Merge-sorted (for binary search)
User input passwords are evaluated for:
Length
Lowercase characters
Uppercase characters
Digits
Symbols
A Python dataclass (PasswordStats) stores password metrics and a computed strength score
An experiment script benchmarks algorithm performance across datasets ranging from 1,000 to 100,000 entries
Algorithm Explanations
Linear Search
Checks each element in the list sequentially until a match is found or the list ends.
Best case: target at first index
Worst case: target at last index or not present
Time complexity: O(N)
Merge Sort
Divides the list into halves, recursively sorts each half, and merges them into a sorted list.
Best and worst case: O(N log N)
Used to prepare data for binary search
Binary Search
Searches a sorted list by repeatedly dividing the search range in half.
Best case: target at middle index (O(1))
Worst case: target not found (O(log N))
Password Evaluator & Generator
Password Evaluation
Each password is analyzed to determine:
Total length
Count of lowercase, uppercase, digits, and symbols
Overall strength score (0–5)
Password Generation
The generator:
Accepts a user-defined length
Guarantees at least one lowercase letter, uppercase letter, digit, and symbol
Produces a randomized, high-entropy password
Demo Summary
Weak Password Example
Input: password123
Score: 2 / 5
Found using both linear and binary search
Indicates weak and commonly used password
Strong Password Example
Input: WriteItDownOnPaper!333
Score: 5 / 5
Not found in either search method
Demonstrates strong password characteristics
Password Generation Example
Generated a 500-character password
Includes lowercase, uppercase, digits, and symbols
Achieves maximum strength score
Performance Results
As dataset size increased:
Linear search time increased linearly
~1047 ms for 50k passwords
~2079 ms for 100k passwords
Merge sort scaled efficiently
~65.8 ms for 50k
~135.2 ms for 100k
Binary search remained extremely fast
~10–17 ms even for large datasets
These results clearly demonstrate the efficiency advantages of sorting and binary search for large-scale password analysis.
Outcome
This project strengthened my understanding of algorithmic efficiency and demonstrated how foundational computer science concepts directly apply to cybersecurity problems. Binary search proved significantly faster than linear search at scale, especially when paired with efficient sorting.
Resources
SecLists – Common Passwords
https://github.com/danielmiessler/SecLists
GeeksForGeeks – Algorithm Analysis
https://www.geeksforgeeks.org/analysis-of-algorithms-big-o-analysis/
Introduction to Algorithms (MIT Press)
