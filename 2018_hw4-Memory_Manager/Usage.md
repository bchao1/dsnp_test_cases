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
    - Your executable (eg. `memTest`)
    - The reference program (eg. `memTest-linux16`)
    - Bash script file `check`
    - Test case generator `gen.py`
2. Go to the folder, on the terminal type:
    ```
    $ ./check [platform] [Number of test cases]
    ```
    For example:
    ```
    $ ./check linux16 1000
    ```
    This would generate a test case file `mydo` of 1000 lines, run your code, run the reference code, and compare the results.
      
    Output files are `out.mine` and `out.ref` for your reference.

## Customize your test cases (modify gen.py)

- *Normal testing*: Should contain a balanced amount of `new, delete, print, reset` commands and some illegal commands. 

- *Extensive testing of error messages*: The probability of illegal commands should be high.

- *Extensive testing of recycle list*: A majority of `mtnew` commands should allocate small number of arrays of varying size (in order to create recyclce list of different indices), and `mtdelete` randomly deletes large number of arrays.
