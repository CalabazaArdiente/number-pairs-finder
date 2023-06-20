# Number Pairs Finder

This program finds pairs of integers from a given list that sum to a target value. The algorithm is implemented to be more efficient than O(n^2) and returns the correct results for all possible inputs.

## Usage

The program is executed from the command line and takes two arguments: a comma-separated list of integers and the target sum.

```shell
python app.py 1,9,5,0,20,-4,12,16,7 12

The output will display the pairs of numbers that sum up to the target value:
+ 12, 0
+ 5, 7
+ 16, -4

