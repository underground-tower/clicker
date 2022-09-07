this is a cool clicker written in python in one evening. at the start of the program, a choice appears to download a preset or create it (f/n).
press the 'n' key and set the value to 1. the logic of the program is presented as a node.
each node has trigger pixel colors, mouse positions for clicks, and a time delay between clicks.

detailed guide:
 run the program, select 'n',
 press 1 or any other number.

 after that, the console will read the clicks anywhere and it can be collapsed.
 next, press 'n' to create a new node. to set the colors of the triggers,
 you need to focus using mouse on the desired pixel and press the 'c' button,
 after which the index of this color in RGB will be displayed in the console,
 you can add an unlimited number of trigger colors in each node.

 now to create a click, you need to move the mouse to the right place for the click 
 and press 'm' while the console displays the location of this click and the delay
 in seconds relative to the previous click (the node remembers the interval between clicks),
 the number of clicks is also limited.

 to create a new node, press 'n' again and repeat the procedure as much as you like.
 to save the preset, press 's', go to the console and press inter in the console to continue.
 next, you need to give the file a name and click inter. your file will be saved in the json format.
 
 to download a preset, open the program,
 select 'f' and enter "file name.json" and click inter,
 the program will wait 4 seconds and start doing work

 to take control, move the mouse and the program will shut down

===================brief management summary=======================
'n'(new) - create new node
'd'(delete) - delete this node
's'(save) - save preset
'c'(color) - create color trigger
'm'(mouse) - create click event