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
    - Your executable (eg. `taskMgr`)
    - The reference program (eg. `taskMgr-linux16`)
    - Bash script file `check`
    - Test case generator `gen.py`
2. Go to the folder, on the terminal type:
    ```
    $ ./check [platform] 
    ```
    For example:
    ```
    $ ./check linux16
    ```
    This would generate a test case file `mydo`, run your code, run the reference code, and compare the results.
      
    Output files are `out.mine` and `out.ref` for your reference. The compared results can be viewed in the log file `diff`.