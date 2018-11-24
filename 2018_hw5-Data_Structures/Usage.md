# Usage
## Requirements
- `python3`
- `numpy`
- `colordiff`

***
To install:  
```
sudo apt install python3
sudo apt install colordiff
pip3 install numpy
```
## How to run test
1. Put the following files in the same folder:
    - Your executable (eg. `adtTest.bst`)
    - The reference program (eg. `adtTest-linux16.bst`)
    - Bash script file `check`
    - Test case generator `gen.py`
2. Go to the folder, on the terminal type:
    ```
    $ ./check [data structure] [Number of test cases] [platform]
    ```
    For example:
    ```
    $ ./check bst 1000 linux16
    ```
    This would generate a test case file `mydo` of 1000 lines, run your program `adtTest.bst`, run the reference program `adtTest-linux16.bst`, and compare the results.
    
    Output files are `out.mine` and `out.ref` for your reference.
3. Data structure flag names:
    - Dynamic array: `array`
    - Doubly linked list: `dlist`
    - Binary Search Tree: `bst`
