# Password-Checker-Generator
Within the course CSCI377 (Computer Algorithms) conducted by Prof. Fatma Najar, I have worked on a Password Checker/Generator as my final project for this course.

# Password Analysis Project
## Author: Davide Mateas
## Course: CSCI 377
## Language: Python

# Problem
Checking if a password is weak or has been compromised in a password list.
Checks will take longer as the list grows.

# Goal
The goal of this project is to build a password checker and generator that uses
algorithms learned throughout this class like linear search, merge sort and binary
search to detect weak passwords and show time difference between O(N), O(N
log N) and O(log N), using Python.

# Algorithms Used
In our project we have used Linear Search O(N) and Binary Search O(log N) for
searching and Merge Sort O(N log N) and a Password Evaluator and Generator
O(L) for Sorting and password generation and strength checking.

# System Outline and How it Works
We have acquired a text list of over 100.000 common or weak passwords that we
then use merge_sort on. evaluate_password is the function used when a
password is inputed in the terminal to check the password, and check also in
unsorted and sorted list. The user also has the ability to generate a password
with their desired length that makes a strong password with at least 1 lowercase,
upper case symbol and digit. experiments.py takes 1k, 5k, 10K all the way to
100k N values and compares time between the algorithms used.

# Core Data and Representation
linear_search checks from list[str] in Python where all the weak passwords are
kept. We keep a merge sorted version of the same data for binary_search to get
O(log N) lookups. The user passwords are kept as string and algorithms scan or
build in O(L) time (L is length of password) Below is PasswordStats, a python
dataclass storing length, lowercase, uppercase, digits, symbols and a score that
shows the strength.
