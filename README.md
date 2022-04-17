# Coding-Stratagems
My personal accumulation of best pratices and strategies in software development

## Essential
- Always check the limits of data types to make sure maximum value can be stored. Otherwise, overflow will caluse unexpected errors, which are runtime. (e.g. int data type cannot hold 14 factorial)

## Variables 
- Global Variable should never be used unless there is no other way, because the code with global variables is not modular


## Object Oriented


## Python
- Quick setup virtual environment and set up packages
```
python3 -m venv packenv
call packenv\scripts\activate.bat (Windows)
source packenv/bin/activate (Linux/OSX)
pip list
```

## C++
- Use of inline functions is more efficient
- Use '\n' instead of endl. \n does not call a flushing output buffer everytime it is called, so it is more efficient.
- Pass by reference does not create a new variable, so it saves memory.
- Use ``nullptr`` instead of ``NULL``. Because ``NULL`` is a macro for the 0 literal, and it can be ambigious with int data type.

## C# (Unity)
- For Physics based calculations (e.g. Forces on RigidBodies), put them in FixedUpdate() function instead of Update() - because Update() is called once per frame only, and FixedUpdate() can be called as many times as the physics engine needs.
