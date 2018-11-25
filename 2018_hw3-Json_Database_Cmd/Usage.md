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
    - Your executable (eg. `mydb`)
    - The reference program (eg. `mydb-linux16`)
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
    This would generate a test case file `mydo` of 1000 lines, run your program, run the reference program, and compare the results.
      
    Output files are `out.mine` and `out.ref` for your reference.
3. A folder `tests` will be created after running `./check`. It contains 10 randomly generated json files named `test1.json` ~ `test10.json`for testing purposes.

## Notes
`Tab` command tests are currently not supported. Feel free to submit your `Tab` command test cases.