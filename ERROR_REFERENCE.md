## When an error occurred while installing packages with pip
#### - `Requirement already satisfied: {package name}` but `ModuleNotFoundError` occurs when executing the code. 
- It's saying that the installation of the package on your computer is succcessfully done. But, the specific location where it's installed might not be as we intended. 
- Please check the path of the python kernel where the program is running and the one where the package is installed. They must be the same.

    ```
    where the program is running
    $ import sys
    $ print(sys.executable)

    where the package is installed
    $ pip show {package name}
    ```