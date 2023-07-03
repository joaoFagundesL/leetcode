# Solution

- Each node has a min value. There is also a global min that i can access directly just with the obj pointer.

- If I remove the node "4" then I go to the node "2" and get the min value. After that, I update the "red min".

- If I remove the node "2" then I go tot the node "3" and its min is "3". Afterward, I update the "red min" from "2" to "3".

 If all nodes of my stack are removed then I have to set the "red min" to INT_MAX because the current value is 3, so I have to reset it

<a href="https://ibb.co/5vPtQhq"><img src="https://i.ibb.co/DkZsBf3/image.png" alt="image" border="0" /></a>

## Setting the node->min

<a href="https://ibb.co/my91M6j"><img src="https://i.ibb.co/2Mvmfg9/image.png" alt="image" border="0" /></a>
