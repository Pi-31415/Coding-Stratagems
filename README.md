# Coding-Stratagems
My personal accumulation of best pratices and strategies in software development

<hr>

## Essential
- Always, always, always use exception handling. It can cost you your life.
- In interviews, don't be a hot-headed person. In design problems, the solution depends on the application. Try to have a conversation with the interviewer to explore all the possibilities.
- Always refactor, and reduce [code bloat](https://en.wikipedia.org/wiki/Code_bloat) using iterators.
- Never use multiple inheritance. There is always a way to avoid it.
- If the build doesn't work, the dependencies are most likely the culprit.
- Whenever you write code, write in the standard way and not in unconventional ways. This is because if you write it in unconventional ways, and visit the same code a year later and do not understand and have to google it, google will not show results.
- Always check the limits of data types to make sure maximum value can be stored. Otherwise, overflow will caluse unexpected errors, which are runtime. (e.g. int data type cannot hold 14 factorial)

## Networking
- For checking networks, always use exception handling to check the network.

## Variables 
- Global Variable should never be used unless there is no other way, because the code with global variables is not modular

## Web
- If something does not work upon deploy, check if the deployment is on https

<hr>

## Docker
- using -qq in dockerfile run commands run the commands quietly, and assume yes to all installation prompts

## NPM
- If the builds doesn't work, it is likely that the software/dependency versions are not compatible with each other.

## Python
- Quick setup virtual environment and set up packages
```
python3 -m venv packenv
call packenv\scripts\activate.bat (Windows)
source packenv/bin/activate (Linux/OSX)
pip list
```
- PIL Convert Image from Array
```python
from numpy import genfromtxt
import numpy as np
from PIL import Image as im
my_data = genfromtxt('datamatrix1.txt', delimiter=',')
my_data = np.delete(my_data, np.s_[-1:], axis=1)


data = im.fromarray((my_data * 20).astype(np.uint8))

data.save('aaaa16.png')

```

## Markdown
- Syntax highlighting can be done in code blocks by adding the name of the language after the triple quotes.

## JavaScript
- For d3.js, if you want to get the parent node from the data, use the following.
```javascript
function node_mouseover(d) {
  //Get the parent node
  var g = d3.select(this);
  }
}
```

- For d3.js, to get data from d, get with
```javascript
.on("mouseover", function (d) {
          d3.select(this).style("cursor", "pointer");
          var g = d3.select(this);
          console.log(d.target.__data__);
        })
```
- Javascript event listener function only takes event as a parameter. Get the data within that event.

## React
- If you need to pass data from child to parent, follow [this](https://javascript.plainenglish.io/how-to-pass-props-from-child-to-parent-component-in-react-d90752ff4d01).

## React Native
- As of 2022, [React Native Paper](https://callstack.github.io/react-native-paper) is the only UI library which works out of the box without any dependency issues.
- ``npm audit fix --force`` is very dangerous, and can break the dependencies
- If the app icon is not working on iOS, restart the device.

## C++
- Getter functions must have ``const``.
- Optimize memory with pass by reference, but use ``const`` to prevent accidental changes.
- Use of inline functions is more efficient
- Use '\n' instead of endl. \n does not call a flushing output buffer everytime it is called, so it is more efficient.
- Pass by reference does not create a new variable, so it saves memory.
- Use ``nullptr`` instead of ``NULL``. Because ``NULL`` is a macro for the 0 literal, and it can be ambigious with int data type.
- Don't use ``friend`` unless you really need to, because it might accidentally change the data.
- C++ is one of the two languages which supports **Multiple inheritance**. Never use it unless you have a really really good reason.
- C++ supports multiple inheritance and Java doesn't.
- For big projects, use smart pointers.

## C# (Unity)
- For Physics based calculations (e.g. Forces on RigidBodies), put them in FixedUpdate() function instead of Update() - because Update() is called once per frame only, and FixedUpdate() can be called as many times as the physics engine needs.
