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
- Whenever you are planning to refer to an array element by its index (e.g. array[0]), make sure that the array is **sorted** in the first place. If you plug in directly from the API, the indices will mess up.

## Networking
- For checking networks, always use exception handling to check the network.

## Variables 
- Global Variable should never be used unless there is no other way, because the code with global variables is not modular

## Web
- If something does not work upon deploy, check if the deployment is on https

<hr>

## Docker
- using -qq in dockerfile run commands run the commands quietly, and assume yes to all installation prompts

## Embedded Systems
- For multithreading on Arduino, use [SoftTimers](https://github.com/end2endzone/SoftTimers)
- Return value for millis() is of type unsigned long, logic errors may occur if a programmer tries to do arithmetic with smaller data types such as int.

## CUDA
- If the CUDA does not work, it may be due to secureboot.

## Electron
- For windows build, when using `electron-builder`, remember to set `powershell Set-ExecutionPolicy RemoteSigned` to run the scripts.

## Node/NPM
- If the builds doesn't work, it is likely that the software/dependency versions are not compatible with each other.
- [Node, deploying on heroku and running out of memory](https://stackoverflow.com/questions/59205530/heroku-server-crashes-with-javascript-heap-out-of-memory-when-deploying-react). Use the following to increase maximum heap size of heroku node.
```
heroku config:set NODE_OPTIONS='--max_old_space_size=2560 [app-name]'
```
- [Handling CORS with Node JS](https://stackabuse.com/handling-cors-with-node-js/)

## JavaScript
- Leaftlet JS Multiple Map Instances- [tutorial](https://programmierfrage.com/items/how-to-implement-multiple-leaflet-js-maps)

## Python
- Force to run on python 3
```
python3 -m [command]
```
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
- PIL remove Alpha Channel
```python
from os.path import isfile, join
from os import listdir
from PIL import Image

# Replace the following with your path
folder_path = "/Users/pi/Desktop/Dataset Structured/Sherifa/"
# Replace with any of the following - brick,cementitious_debris,PVC,rebar,wires
object_type = "rebar"

onlyfiles = [f for f in listdir(folder_path) if isfile(join(folder_path, f))]
for x in onlyfiles:
    if(object_type in x):
        try:
            png = Image.open(
                folder_path+x)
            png.load()  # required for png.split()

            background = Image.new("RGB", png.size, (255, 255, 255))
            # 3 is the alpha channel
            background.paste(png, mask=png.split()[3])
            background.save(
                folder_path+x, 'JPEG', quality=80)
            print("Converted "+x+" to RGB.")
        except:
            print("Cannot convert "+x+" to RGB, skipping...")
```

- Mass Rename Files
```python
from os.path import isfile, join
from os import listdir
import os
from PIL import Image

# Replace the following with your path
folder_path = "/Users/pi/Desktop/Drone Data/outdoor_drone"

onlyfiles = [f for f in listdir(folder_path) if isfile(join(folder_path, f))]
for x in onlyfiles:
    if(".JPG" in x):
        old_name = folder_path+"/"+x
        new_name = folder_path+"/"+x.replace(".JPG", ".jpg")
        os.rename(old_name, new_name)
```

## Markdown
- Syntax highlighting can be done in code blocks by adding the name of the language after the triple quotes.

## JavaScript
- For O(1) JS, use [Qwik](https://qwik.builder.io/)
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

## Remote Access
- Use [NoMachine](https://www.nomachine.com/)

## React
- If you need to pass data from child to parent, follow [this](https://javascript.plainenglish.io/how-to-pass-props-from-child-to-parent-component-in-react-d90752ff4d01).
- Prevent double loading of useEffect - [Link](https://dev.to/ag-grid/react-18-avoiding-use-effect-getting-called-twice-4i9e).

## React Native
- As of 2022, [React Native Paper](https://callstack.github.io/react-native-paper) is the only UI library which works out of the box without any dependency issues.
- ``npm audit fix --force`` is very dangerous, and can break the dependencies
- If the app icon is not working on iOS, restart the device.

## C++
- Segmentation faults cannot be caught via ``try...catch``.
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

## VR/AR
- Don't forget to install the XR Plugin in 
during setup.

## C# (Unity)
- If build fails with the error - [The type or namespace name ‘Editor’ could not be found](https://qa.fmod.com/t/unity-2020-3-8f-build-fails-because-fmod-2-01-09/17751)- put the plugin folder in the Assets/Editor folder
- Use [Unity Photon](https://www.photonengine.com/pun) for multiplayer games.
- For Physics based calculations (e.g. Forces on RigidBodies), put them in FixedUpdate() function instead of Update() - because Update() is called once per frame only, and FixedUpdate() can be called as many times as the physics engine needs.
- For LineRenderer, if it is lagging for ``lineRenderer.SetPosition``, use delegate like in this [tutorial](https://answers.unity.com/questions/1742489/linerenderer-lagging-behind.html).
```csharp
 private void OnEnable()
 {
     Application.onBeforeRender += UpdateRoute;
 }
 
 private void OnDisable()
 {
     Application.onBeforeRender -= UpdateRoute;
 }

```
- Draw Bounding Boxes around objects for computer vision like [this](https://answers.unity.com/questions/292031/how-to-display-a-rectangle-around-a-player.html)
```csharp
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class DrawRect : MonoBehaviour
{
    public GameObject player;

    public float margin = 0;

    private Vector3[] pts = new Vector3[8];

    public void OnGUI()
    {
        Bounds b = player.GetComponent<Renderer>().bounds;
        Camera cam = Camera.main;

        //The object is behind us
        if (cam.WorldToScreenPoint(b.center).z < 0) return;

        //All 8 vertices of the bounds
        pts[0] =
            cam
                .WorldToScreenPoint(new Vector3(b.center.x + b.extents.x,
                    b.center.y + b.extents.y,
                    b.center.z + b.extents.z));
        pts[1] =
            cam
                .WorldToScreenPoint(new Vector3(b.center.x + b.extents.x,
                    b.center.y + b.extents.y,
                    b.center.z - b.extents.z));
        pts[2] =
            cam
                .WorldToScreenPoint(new Vector3(b.center.x + b.extents.x,
                    b.center.y - b.extents.y,
                    b.center.z + b.extents.z));
        pts[3] =
            cam
                .WorldToScreenPoint(new Vector3(b.center.x + b.extents.x,
                    b.center.y - b.extents.y,
                    b.center.z - b.extents.z));
        pts[4] =
            cam
                .WorldToScreenPoint(new Vector3(b.center.x - b.extents.x,
                    b.center.y + b.extents.y,
                    b.center.z + b.extents.z));
        pts[5] =
            cam
                .WorldToScreenPoint(new Vector3(b.center.x - b.extents.x,
                    b.center.y + b.extents.y,
                    b.center.z - b.extents.z));
        pts[6] =
            cam
                .WorldToScreenPoint(new Vector3(b.center.x - b.extents.x,
                    b.center.y - b.extents.y,
                    b.center.z + b.extents.z));
        pts[7] =
            cam
                .WorldToScreenPoint(new Vector3(b.center.x - b.extents.x,
                    b.center.y - b.extents.y,
                    b.center.z - b.extents.z));

        //Get them in GUI space
        for (int i = 0; i < pts.Length; i++)
        pts[i].y = Screen.height - pts[i].y;

        //Calculate the min and max positions
        Vector3 min = pts[0];
        Vector3 max = pts[0];
        for (int i = 1; i < pts.Length; i++)
        {
            min = Vector3.Min(min, pts[i]);
            max = Vector3.Max(max, pts[i]);
        }

        //Construct a rect of the min and max positions and apply some margin
        Rect r = Rect.MinMaxRect(min.x, min.y, max.x, max.y);
        r.xMin -= margin;
        r.xMax += margin;
        r.yMin -= margin;
        r.yMax += margin;

        //Render the box
        GUI.Box(r, "This is a box covering the player");
    }
}

```

## Unity (Playmaker)

# Optimizing and Piping

```bash
objdump -d CPUBenchmark | grep mul | wc -l
```

```bash
sudo perf stat ./lin
```


## C and Assembly
- Never never use ```goto```.

## macOS
- [How to add shortcut for Terminal](https://clay-atlas.com/us/blog/2020/12/14/mac-os-en-open-terminal-by-shortcut-key/)

## Ubuntu/Linux
- [Get Quick Look with Gnome Sushi](https://www.omgubuntu.co.uk/gnome-sushi-mac-quick-for-ubuntu)
