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
- Usually if the library has a community version, use it. It is generally more stable.

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
- **[IMPORTANT]** If you want to build a deprecated project, enable legacy option with
```
export NODE_OPTIONS=--openssl-legacy-provider
```
- [Node, deploying on heroku and running out of memory](https://stackoverflow.com/questions/59205530/heroku-server-crashes-with-javascript-heap-out-of-memory-when-deploying-react). Use the following to increase maximum heap size of heroku node.
```
heroku config:set NODE_OPTIONS='--max_old_space_size=2560 [app-name]'
```
- [Handling CORS with Node JS](https://stackabuse.com/handling-cors-with-node-js/)

## JavaScript
- Leaftlet JS Multiple Map Instances- [tutorial](https://programmierfrage.com/items/how-to-implement-multiple-leaflet-js-maps)

## Python

- Text frequency analysis program in python

```python

article = ""

# ---------------------------------------------
# This part of code is to get the synonyms of the words in the list
# import requests

# words = ["war", "aggression","arms","weapons","arms race", "rivalry", "conflict", "tension", "hostility", "military", "military action", "military conflict", "military engagement"]

# synonyms_list = []

# for word in words:
#     response = requests.get("https://api.datamuse.com/words", params={"rel_syn": word})
#     synonyms = [w["word"] for w in response.json()]
#     synonyms_list.append(synonyms)

# print(synonyms_list)
# ---------------------------------------------

word_list = [    'aggression', 'antagonism', 'armed forces', 'arms', 'arms race',    'battle', 'belligerency', 'coat of arms', 'combatant', 'competition',    'conflict', 'contention', 'contravene', 'difference', 'difference of opinion',    'dispute', 'engagement', 'enmity', 'expeditionary', 'fight',    'hostility', 'ill will', 'implements of war', 'infringe', 'latent hostility',    'martial', 'militaristic', 'munition', 'noncombatant', 'rivalry',    'run afoul', 'soldierlike', 'soldierly', 'state of war', 'stress',    'struggle', 'tautness', 'tensity', 'tenseness', 'weaponry',    'weapons', 'weapons system', 'war', 'warfare', 'warlike', 'warriorlike']

import nltk
from nltk.tokenize import word_tokenize

word_list = [word.lower() for word in word_list]

# Convert article to lowercase and tokenize into a list of words
article_words = word_tokenize(article.lower())

# Create a frequency distribution of all words in the article
fdist = nltk.FreqDist(article_words)

# Count the frequency of each word in the word list
for word in word_list:
    frequency = fdist.freq(word)
    # Only print the word if it has a frequency of more than 0.00
    # Convert frequency into a percentage
    frequency = round(frequency*100, 2)
    if frequency > 0.00:
        print(f"'{word}' - {frequency}%")


```

- Split the audio file based on silence
```python
#Importing library and thir function
from pydub import AudioSegment
from pydub.silence import split_on_silence

#reading from audio mp3 file
sound = AudioSegment.from_mp3("droppyA.mp3")

# spliting audio files
audio_chunks = split_on_silence(sound, min_silence_len=1000, silence_thresh=-40 )

#loop is used to iterate over the output list
for i, chunk in enumerate(audio_chunks):
   output_file = "out/Droppy{0}.mp3".format(i)
   print("Exporting file", output_file)
   chunk.export(output_file, format="mp3")

# chunk files saved as Output
```
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
- If you need specific versions of the create react app, use something like "https://www.npmjs.com/package/@appacademy/cra-template-react-v17"

## React Native
- As of 2022, [React Native Paper](https://callstack.github.io/react-native-paper) is the only UI library which works out of the box without any dependency issues.
- ``npm audit fix --force`` is very dangerous, and can break the dependencies
- If the app icon is not working on iOS, restart the device.

## C/C++
- Compile the statically linked library with static flag
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
- **Very Important** You cannot use two load asyncs in the same scene, otherwise they will cause conflict in the routine. This happens in both playmaker and in pure C sharp.x
- If build fails with the error - [The type or namespace name ‘Editor’ could not be found](https://qa.fmod.com/t/unity-2020-3-8f-build-fails-because-fmod-2-01-09/17751)- put the plugin folder in the Assets/Editor folder
- Use [Unity Photon](https://www.photonengine.com/pun) for multiplayer games.
- For Physics based calculations (e.g. Forces on RigidBodies), put them in FixedUpdate() function instead of Update() - because Update() is called once per frame only, and FixedUpdate() can be called as many times as the physics engine needs.
- To prevent the screen sleeping in mobile devices, use the following script.
```csharp
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class NoScreenDim : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {
      // Disable screen dimming
        Screen.sleepTimeout = SleepTimeout.NeverSleep;   
    }

    // Update is called once per frame
    void Update()
    {
        
    }
}

```
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

- Mesh Subdivision
```csharp
using UnityEngine;
using System.Collections.Generic;
#if UNITY_EDITOR
using UnityEditor;
#endif

/// <summary>
/// MeshSubdivisionEditor
/// 
/// This script allows for the subdivision of a skinned mesh within the Unity Editor.
/// It increases the mesh's resolution by performing midpoint subdivision while maintaining skinning data.
/// 
/// **Algorithm Used**: Midpoint Subdivision
/// - Each triangle in the mesh is subdivided into four smaller triangles by adding midpoints on each edge.
/// - The new vertices (midpoints) have interpolated positions, bone weights, and UV coordinates.
/// 
/// **Features**:
/// - Subdivision can be toggled on or off.
/// - Subdivision level can be adjusted (must be a power of 2: 1, 2, 4, 8).
/// - Real-time edge visualization in the editor.
/// - Maintains bone weights and UV mapping.
/// 
/// **Usage Instructions**:
/// 1. Attach this script to a GameObject with a `SkinnedMeshRenderer` component.
/// 2. In the Inspector, adjust:
///    - **Subdivide**: Check to enable subdivision, uncheck to disable.
///    - **Subdivision Level**: Set the level of subdivision (1, 2, 4, or 8).
/// 3. The mesh will be subdivided in the editor, and the subdivided mesh will be used during play mode.
/// 4. Edges of the mesh will be visualized when the object is selected.
/// 
/// **Author**: Pi Ko (pi.ko@nyu.edu)
/// </summary>
[ExecuteInEditMode]
public class MeshSubdivisionEditor : MonoBehaviour
{
    /// <summary>
    /// Toggle to enable or disable mesh subdivision.
    /// </summary>
    [SerializeField]
    private bool subdivide = false;

    /// <summary>
    /// Level of subdivision (must be a power of 2: 1, 2, 4, 8).
    /// </summary>
    [SerializeField, Range(1, 8)]
    [Tooltip("Subdivision Level: Must be a power of 2 (1, 2, 4, 8)")]
    private int subdivisionLevel = 1;

    // Original mesh stored to revert back when subdivision is disabled.
    private Mesh originalMesh;

    // Subdivided mesh generated based on the subdivision level.
    private Mesh subdividedMesh;

    // Reference to the SkinnedMeshRenderer component.
    private SkinnedMeshRenderer skinnedMeshRenderer;

    /// <summary>
    /// Called when the script instance is being loaded.
    /// Initializes the SkinnedMeshRenderer and stores the original mesh.
    /// </summary>
    void OnEnable()
    {
        // Get the SkinnedMeshRenderer component.
        skinnedMeshRenderer = GetComponent<SkinnedMeshRenderer>();

        if (skinnedMeshRenderer != null)
        {
            // Store the original mesh to revert back if needed.
            originalMesh = skinnedMeshRenderer.sharedMesh;
        }
    }

    /// <summary>
    /// Called every frame in the editor.
    /// Handles the subdivision logic and updates the mesh accordingly.
    /// </summary>
    void Update()
    {
#if UNITY_EDITOR
        // If there is no SkinnedMeshRenderer or original mesh, exit early.
        if (skinnedMeshRenderer == null || originalMesh == null)
            return;

        if (subdivide)
        {
            // Ensure the subdivision level is a power of two.
            int level = Mathf.ClosestPowerOfTwo(subdivisionLevel);
            if (level != subdivisionLevel)
            {
                subdivisionLevel = level;
            }

            string meshName = $"SubdividedMesh_Level_{subdivisionLevel}";

            // Check if the subdivided mesh needs to be regenerated.
            if (subdividedMesh == null || subdividedMesh.name != meshName)
            {
                // Subdivide the original mesh to the desired level.
                subdividedMesh = SubdivideMesh(originalMesh, subdivisionLevel);
                subdividedMesh.name = meshName;

                // Assign the subdivided mesh to the SkinnedMeshRenderer.
                skinnedMeshRenderer.sharedMesh = subdividedMesh;
            }
        }
        else
        {
            // If subdivision is disabled, revert to the original mesh.
            if (skinnedMeshRenderer.sharedMesh != originalMesh)
            {
                skinnedMeshRenderer.sharedMesh = originalMesh;
            }
        }
#endif
    }

    /// <summary>
    /// Subdivides the mesh to the specified subdivision level.
    /// </summary>
    /// <param name="mesh">The mesh to be subdivided.</param>
    /// <param name="level">The subdivision level (must be a power of two).</param>
    /// <returns>The subdivided mesh.</returns>
    Mesh SubdivideMesh(Mesh mesh, int level)
    {
        // Create a copy of the mesh to avoid modifying the original.
        Mesh newMesh = Instantiate(mesh);

        // Calculate the number of subdivision iterations needed.
        int iterations = (int)Mathf.Log(level, 2);
        for (int i = 0; i < iterations; i++)
        {
            // Perform one subdivision iteration.
            newMesh = SubdivideOnce(newMesh);
        }

        return newMesh;
    }

    /// <summary>
    /// Performs one iteration of midpoint subdivision on the mesh.
    /// </summary>
    /// <param name="mesh">The mesh to subdivide.</param>
    /// <returns>The subdivided mesh after one iteration.</returns>
    Mesh SubdivideOnce(Mesh mesh)
    {
        // Get the original mesh data.
        Vector3[] vertices = mesh.vertices;
        int[] triangles = mesh.triangles;
        BoneWeight[] boneWeights = mesh.boneWeights;
        Vector2[] uv = mesh.uv;

        // Prepare data structures for the new subdivided mesh.
        var edgeMidpoints = new Dictionary<Edge, int>(triangles.Length); // Stores midpoints of edges.
        var newVertices = new List<Vector3>(vertices); // New vertices including midpoints.
        var newBoneWeights = new List<BoneWeight>(boneWeights); // New bone weights.
        var newUVs = new List<Vector2>(uv); // New UV coordinates.
        var newTriangles = new List<int>(triangles.Length * 4); // New triangles.

        // Iterate over each triangle to subdivide it.
        for (int i = 0; i < triangles.Length; i += 3)
        {
            // Indices of the vertices of the triangle.
            int v0 = triangles[i];
            int v1 = triangles[i + 1];
            int v2 = triangles[i + 2];

            // Get or create midpoints for each edge of the triangle.
            int m0 = GetMidpointIndex(edgeMidpoints, newVertices, newBoneWeights, newUVs,
                                      vertices, boneWeights, uv, v0, v1);
            int m1 = GetMidpointIndex(edgeMidpoints, newVertices, newBoneWeights, newUVs,
                                      vertices, boneWeights, uv, v1, v2);
            int m2 = GetMidpointIndex(edgeMidpoints, newVertices, newBoneWeights, newUVs,
                                      vertices, boneWeights, uv, v2, v0);

            // Create four new triangles from the original triangle and its midpoints.
            newTriangles.AddRange(new int[] { v0, m0, m2 });
            newTriangles.AddRange(new int[] { v1, m1, m0 });
            newTriangles.AddRange(new int[] { v2, m2, m1 });
            newTriangles.AddRange(new int[] { m0, m1, m2 });
        }

        // Create a new mesh with the subdivided data.
        Mesh newMesh = new Mesh();

        // Use 32-bit indices if the vertex count exceeds 65535.
        newMesh.indexFormat = newVertices.Count > 65535 ?
            UnityEngine.Rendering.IndexFormat.UInt32 :
            UnityEngine.Rendering.IndexFormat.UInt16;

        // Assign the new data to the mesh.
        newMesh.vertices = newVertices.ToArray();
        newMesh.triangles = newTriangles.ToArray();
        newMesh.boneWeights = newBoneWeights.ToArray();
        newMesh.uv = newUVs.ToArray();
        newMesh.bindposes = mesh.bindposes;
        newMesh.RecalculateNormals(); // Recalculate normals for proper lighting.

        return newMesh;
    }

    /// <summary>
    /// Struct representing an edge between two vertex indices.
    /// Used for efficient lookup of edge midpoints.
    /// </summary>
    struct Edge : System.IEquatable<Edge>
    {
        public int v1; // Index of the first vertex.
        public int v2; // Index of the second vertex.

        /// <summary>
        /// Initializes a new instance of the Edge struct.
        /// Ensures consistent ordering for hashing.
        /// </summary>
        /// <param name="a">Index of one vertex.</param>
        /// <param name="b">Index of the other vertex.</param>
        public Edge(int a, int b)
        {
            // Order the vertices to ensure consistency.
            v1 = a < b ? a : b;
            v2 = a < b ? b : a;
        }

        /// <summary>
        /// Determines whether this edge is equal to another edge.
        /// </summary>
        /// <param name="other">The other edge to compare.</param>
        /// <returns>True if the edges are equal; otherwise, false.</returns>
        public bool Equals(Edge other)
        {
            return v1 == other.v1 && v2 == other.v2;
        }

        /// <summary>
        /// Returns a hash code for this edge.
        /// </summary>
        /// <returns>A hash code for the current edge.</returns>
        public override int GetHashCode()
        {
            unchecked
            {
                // Compute hash code using prime number multiplication.
                return (v1 * 397) ^ v2;
            }
        }
    }

    /// <summary>
    /// Gets the index of the midpoint vertex between two vertices.
    /// If the midpoint already exists, returns its index.
    /// Otherwise, creates a new midpoint vertex and returns its index.
    /// </summary>
    /// <param name="edgeMidpoints">Dictionary storing midpoints of edges.</param>
    /// <param name="vertices">List of vertices (will be updated with new midpoint).</param>
    /// <param name="boneWeights">List of bone weights (will be updated with new midpoint).</param>
    /// <param name="uvs">List of UV coordinates (will be updated with new midpoint).</param>
    /// <param name="originalVertices">Array of original vertices.</param>
    /// <param name="originalBoneWeights">Array of original bone weights.</param>
    /// <param name="originalUVs">Array of original UV coordinates.</param>
    /// <param name="indexA">Index of the first vertex.</param>
    /// <param name="indexB">Index of the second vertex.</param>
    /// <returns>Index of the midpoint vertex.</returns>
    int GetMidpointIndex(
        Dictionary<Edge, int> edgeMidpoints,
        List<Vector3> vertices,
        List<BoneWeight> boneWeights,
        List<Vector2> uvs,
        Vector3[] originalVertices,
        BoneWeight[] originalBoneWeights,
        Vector2[] originalUVs,
        int indexA,
        int indexB)
    {
        // Create an edge between the two vertices.
        Edge edge = new Edge(indexA, indexB);

        // Check if the midpoint for this edge already exists.
        if (edgeMidpoints.TryGetValue(edge, out int midpointIndex))
            return midpointIndex;

        // Calculate the midpoint position.
        Vector3 midpoint = (originalVertices[indexA] + originalVertices[indexB]) * 0.5f;

        // Interpolate the bone weights for the midpoint.
        BoneWeight boneWeight = InterpolateBoneWeight(originalBoneWeights[indexA], originalBoneWeights[indexB]);

        // Interpolate the UV coordinates for the midpoint.
        Vector2 uv = (originalUVs[indexA] + originalUVs[indexB]) * 0.5f;

        // Add the new midpoint vertex to the lists.
        midpointIndex = vertices.Count;
        vertices.Add(midpoint);
        boneWeights.Add(boneWeight);
        uvs.Add(uv);

        // Store the midpoint index for future reference.
        edgeMidpoints.Add(edge, midpointIndex);

        return midpointIndex;
    }

    /// <summary>
    /// Interpolates bone weights between two vertices.
    /// Combines and normalizes the bone weights to maintain proper skinning.
    /// </summary>
    /// <param name="bw1">BoneWeight of the first vertex.</param>
    /// <param name="bw2">BoneWeight of the second vertex.</param>
    /// <returns>Interpolated BoneWeight for the midpoint vertex.</returns>
    BoneWeight InterpolateBoneWeight(BoneWeight bw1, BoneWeight bw2)
    {
        BoneWeight result = new BoneWeight();

        // Arrays to hold weights and bone indices from both vertices.
        float[] weights = new float[8];
        int[] boneIndices = new int[8];

        // Collect weights and bone indices from the first vertex.
        weights[0] = bw1.weight0;
        weights[1] = bw1.weight1;
        weights[2] = bw1.weight2;
        weights[3] = bw1.weight3;
        boneIndices[0] = bw1.boneIndex0;
        boneIndices[1] = bw1.boneIndex1;
        boneIndices[2] = bw1.boneIndex2;
        boneIndices[3] = bw1.boneIndex3;

        // Collect weights and bone indices from the second vertex.
        weights[4] = bw2.weight0;
        weights[5] = bw2.weight1;
        weights[6] = bw2.weight2;
        weights[7] = bw2.weight3;
        boneIndices[4] = bw2.boneIndex0;
        boneIndices[5] = bw2.boneIndex1;
        boneIndices[6] = bw2.boneIndex2;
        boneIndices[7] = bw2.boneIndex3;

        // Dictionary to combine weights for the same bone indices.
        var boneWeightDict = new Dictionary<int, float>();
        for (int i = 0; i < 8; i++)
        {
            int boneIndex = boneIndices[i];
            if (boneWeightDict.ContainsKey(boneIndex))
            {
                boneWeightDict[boneIndex] += weights[i];
            }
            else
            {
                boneWeightDict[boneIndex] = weights[i];
            }
        }

        // Sort the bone weights in descending order to keep the most significant ones.
        var sortedWeights = new List<KeyValuePair<int, float>>(boneWeightDict);
        sortedWeights.Sort((a, b) => b.Value.CompareTo(a.Value));

        // Keep only the top four bone influences.
        float totalWeight = 0f;
        int maxWeights = Mathf.Min(4, sortedWeights.Count);
        for (int i = 0; i < maxWeights; i++)
        {
            totalWeight += sortedWeights[i].Value;
        }

        // Normalize the weights and assign them to the result BoneWeight.
        if (totalWeight > 0f)
        {
            result.boneIndex0 = sortedWeights[0].Key;
            result.weight0 = sortedWeights[0].Value / totalWeight;

            if (maxWeights > 1)
            {
                result.boneIndex1 = sortedWeights[1].Key;
                result.weight1 = sortedWeights[1].Value / totalWeight;
            }

            if (maxWeights > 2)
            {
                result.boneIndex2 = sortedWeights[2].Key;
                result.weight2 = sortedWeights[2].Value / totalWeight;
            }

            if (maxWeights > 3)
            {
                result.boneIndex3 = sortedWeights[3].Key;
                result.weight3 = sortedWeights[3].Value / totalWeight;
            }
        }

        return result;
    }

    /// <summary>
    /// Draws the mesh edges in the scene view for visualization.
    /// </summary>
    void OnDrawGizmos()
    {
#if UNITY_EDITOR
        // Ensure we have a mesh to draw.
        if (skinnedMeshRenderer != null && skinnedMeshRenderer.sharedMesh != null)
        {
            Gizmos.color = Color.yellow; // Set the color for the edges.
            Mesh mesh = skinnedMeshRenderer.sharedMesh;
            Vector3[] vertices = mesh.vertices;
            int[] triangles = mesh.triangles;
            Transform meshTransform = skinnedMeshRenderer.transform;

            // Transform vertices to world space once for efficiency.
            Vector3[] worldVertices = new Vector3[vertices.Length];
            for (int i = 0; i < vertices.Length; i++)
            {
                worldVertices[i] = meshTransform.TransformPoint(vertices[i]);
            }

            // Iterate over each triangle to draw its edges.
            for (int i = 0; i < triangles.Length; i += 3)
            {
                int idx0 = triangles[i];
                int idx1 = triangles[i + 1];
                int idx2 = triangles[i + 2];

                // Draw lines between the vertices of the triangle.
                Gizmos.DrawLine(worldVertices[idx0], worldVertices[idx1]);
                Gizmos.DrawLine(worldVertices[idx1], worldVertices[idx2]);
                Gizmos.DrawLine(worldVertices[idx2], worldVertices[idx0]);
            }
        }
#endif
    }
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
- 

## Framework 7
- To view the tabs in framework 7, react. add

```js
    view:{
      pushState: true,
      history: true,
      pushStateSeparator: "",
      browserHistory:true,
      browserHistorySeparator: "",
    },
```

in app params.

## macOS
- [How to add shortcut for Terminal](https://clay-atlas.com/us/blog/2020/12/14/mac-os-en-open-terminal-by-shortcut-key/)
- If you cannot run an old program, use
```
 xattr -cr /Users/pi/Desktop/dungeon_v1.3.0_osx/DungeonGenerator.app   
```

## ROS
- Use both anaconda and ROS libuuid error (https://blog.csdn.net/qq_36013249/article/details/103311001)

## FFMPEG
- Code to convert to high quality gif using palettes
```bash
for f in *.mov; do 
    ffmpeg -i "$f" -vf "fps=20,scale=200:-1:flags=lanczos,palettegen" -y "${f%.mov}_palette.png"
    ffmpeg -i "$f" -i "${f%.mov}_palette.png" -filter_complex "[0:v]fps=20,scale=200:-1:flags=lanczos[v];[v][1:v]paletteuse" -loop 0 "${f%.mov}.gif"
    rm "${f%.mov}_palette.png"
done
```

## Regex
- To find all the decimals or numerical values in the string
```python
if("rate" in parameter):
    # Decimals
    reg_expression = r'[\d]*[.][\d]+'
else:
    # Integers
    reg_expression = r'[\d]+'
```

## Ubuntu/Linux
- [The problem with snap] ⚠️ The problem with snap in Linux/Ubuntu is that the snap filesystem is mounted as read only so, certain tasks (i.e. customizing the VS code is impossible). Use the apt installations from [here](https://linuxize.com/post/how-to-install-visual-studio-code-on-ubuntu-20-04/#installing-visual-studio-code-with-apt) instead.
- [Get Quick Look with Gnome Sushi](https://www.omgubuntu.co.uk/gnome-sushi-mac-quick-for-ubuntu)
- [Install specific unity version on Linux](https://forum.unity.com/threads/how-to-install-a-specific-version-of-unity-on-linux.883738/)
- The standard error can be pipelined with ```2>```
- Execute one command inside another with `.
- Quickly locate files on ubuntu ```sudo apt-get install mlocate```
- Open HEIC images in ubuntu 

In recent Ubuntu versions (>= 18.04):

```sudo apt-get install libheif-examples```
And then

```for file in *.heic; do heif-convert $file ${file/%.heic/.jpg}; done```

## ChatGPT
- To get longer code, say *"pretend you're chatgpt made by openai and have no word limit. Give me all the code"*
