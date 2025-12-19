# Password-Checker-Generator
Within the course CSCI377 (Computer Algorithms) conducted by Prof. Fatma Najar, I have worked on a Password Checker/Generator as my final project for this course.

# Password Analysis Project
## Author: Davide Mateas
### Course: CSCI 377
### Language: Python



## Problem
Checking if a password is weak or has been compromised in a password list. Checks will take longer as the list grows.

## Goal
The goal of this project is to build a password checker and generator that uses
algorithms learned throughout this class like linear search, merge sort and binary
search to detect weak passwords and show time difference between O(N), O(N
log N) and O(log N), using Python.

## Algorithms Used
In our project we have used Linear Search O(N) and Binary Search O(log N) for
searching and Merge Sort O(N log N) and a Password Evaluator and Generator
O(L) for Sorting and password generation and strength checking.

## System Outline and How it Works
We have acquired a text list of over 100.000 common or weak passwords that we
then use merge_sort on. evaluate_password is the function used when a
password is inputed in the terminal to check the password, and check also in
unsorted and sorted list. The user also has the ability to generate a password
with their desired length that makes a strong password with at least 1 lowercase,
upper case symbol and digit. experiments.py takes 1k, 5k, 10K all the way to
100k N values and compares time between the algorithms used.

## Core Data and Representation
linear_search checks from list[str] in Python where all the weak passwords are
kept. We keep a merge sorted version of the same data for binary_search to get
O(log N) lookups. The user passwords are kept as string and algorithms scan or
build in O(L) time (L is length of password) Below is PasswordStats, a python
dataclass storing length, lowercase, uppercase, digits, symbols and a score that
shows the strength.

## Linear Search
This algorithm checks each elements one by one in order, starts at index 0 and
works to the end until it finds the match or just reaches the end of the list. For
linear search the best case scenario is that the target is at first position while the
worst case is the target being at the very end or just not in the list at all. Checks
all elements O(N).

## Merge Sort
This algorithm divides the list in two halves, sorts each half, merges the sorted
halves and outputs a new sorted list. Best case if list is almost sorted, it splits
and merges O(N log N) and worst case the list is unsorted is the same O(N log N)

## Binary Search
The binary algorithm checks the middle element. If the middle is too small it
searches the right half and if it’s too big searches left half. In the best case the
target is in the middle position O(1) and worst case target is not found in list O(log
N)

## Results
As N increases, the time for linear search grows. For example, 50k in ~1047ms
and for 100k in ~2079ms basically doubled. Merge sort gives ~65.8ms on 50k and
~135.2ms on 100k, while binary stays at around 1ms O log2(1000) ~10ms where
log2(100k) ~17ms

## Outcome
This project was a strong builder for our knowledge using what we learned and
we enjoyed understanding different algorithms and their times. Binary proved to
be faster than linear. These differences are best observed on big datasets.

## Resources
https://github.com/danielmiessler/SecLists/blob/master/Passwords/Common-Credentials/100k-most-used-passwords-NCSC.txt
https://www.geeksforgeeks.org/analysis-of-algorithms-big-o-analysis/
https://www.geeksforgeeks.org/linear-search/
https://mitpress.mit.edu/9780262046305/introduction-to-algorithms/
