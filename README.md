How to import Assets: Right click bottom left to create 3 folders, one for "Assets", one for "Scripts" and one for "Scenes"
Drag and drop Assets into Assets folder



Nodes:
You put together nodes to create things. Nodes come in many forms, some display an image (sprites), some play a sound (Audio) or add Physics (RigidBody). Making a game in Godot is combining and extending nodes.

Scenes:
We use Scenes to bundle together nodes into reusable packages, a scene can be a character, a weapon, a menu. They can be as small as a single collectible coin, or an entire level. You can put scenes inside of other scenes, this is called nesting. You call the whole structure the scene tree and the node at the very beginning is called the root.

Click 2D Scene in the top left box to create a root node. Rename Node2D to Game. Hit Cntr S go under Scenes and save here. You can hit play in top right, and allow current scene to be main scene.

Create a new scene by hitting the plus sign by the tab above the Game view. Click the plus in the top left and search for CharacterBody2D and hit create. Hit plus in top right again and search for sprite, or animated sprite 2d if you want to add an animated sprite. 
Add a png to the sprite or add a sprite sheet using the animator in the inspector. If doing animation, configure the grid to fit all the sprites, and click the grids in the order that you would like your animation. Hit add frames. Hit F to centre character on the screen, Scroll to zoom in, and click and drag with the middle mouse button to move around. If character is blurry go to project in the top left, project settings, look under rendering to find Textures and make the default texture filter nearest instead of linear. 

Click plus in top left, search collision shape 2d, go to the inspector, define a new shape (circle shape for character) and adjust it to fit the sprite. Rename CharacterBody2d to player and save the scene. 

Go into Game Scene (First tab above the game display) and drag in the player from the files box in bottom left.

Click plus in top left, search camera 2d, if you press F it centres your screen to the camera. Adjust the zoom in the inspector to make it fit to your liking and then drag the camera to be on top of the player.

Click on tab to go into player scene, with player node selected press the add script button (This looks like a scroll next to the + button top left). Here you can choose a template, for now use the basic movement template provided by godot. As for the path make sure it's put inside the scripts folder and name it player movement. If you click play now your player will immediately fall through the screen. 

Click 2d at the middle top to change back, add a node by hitting plus, add a staticbody2d (Make sure tab is on game). While staticbody2d is selected click plus and add a collision shape, in the inspector click to create a new world body shape. This will extend infinitely to the left and right. 

Select staticbody2d, change to move tool by pressing arrows next to cursor in top left of game view. Move the object down under the character. Go back to the select tool now by pressing the cursor. If you click play the player will land on the invisible collider and not fall through. 

Modify the movement script:

You can modify the speed and the Jump_Velocity to 130 and 300 respectively to slow the player down.

World Building:
To build the world delete the StaticBody2D, and add a tilemap node. Press plus and search for tile map. A tile set is a collection of tiles we can use to create our world and a tile map is the node we use to paint these tiles into our world. 

In inspector under tileset click to create a new tileset and and click on it to configure. Set tile size to the correct thing for the asset you have. At the bottom of the screen you have the tileset and tilemap. Go into tileset and drag in tile set asset into square on the left. Automatically create tiles in the atlas? Yes. Make tile portion of screen bigger. Click bottom of the screen to go to tilemap and start painting, make sure your scene has the select tool (Cursor) and that the tile map has the paint tool enabled. Left click to place tiles, right click to remove. 

Add physics layer so player doesn't fall through. Have Tilemap selected on left, go to inspector on right, click tileset and go to physics layers -> Add element. Now go to tileset in bottom and click paint and then paint properties. Select Physics layer 0 and click on the tiles you want to have a collider.  You can modify how much of the colliders cover the tile in the box on the left.

Take tilemap in the order menu in top left and drag it to being right under game so you can always find it. Hit play and player will land on tiles and not fall through. 

To get the camera to follow the player, take the camera2d in top left and drag it onto player also in top left making it a child of the player (Check if it is indeed centered on top of player). Go to inspector on right while camera is selected and enable position smoothing. When you click play camera should follow the player. 


Platforms:

Make a new scene (New tab with plus above game view), click the top left plus and search for animatableBody2D. While selected click plus and add sprite2d. From assets folder drag in the png you want into the inspector. Hit F and zoom in. In the inspector click region, enabled and then edit region to only show a part of the png. Select AnimatableBody2D again and hit plus add a collisionShape2D (Rectangle shape). Rename top node to platform and save the scene. Select CollisionShape2D and in the inspector click one way collision. 

Go to game tab and drag in platform from the scenes folder bottom left to the game view. 

Whatever is lower in the top left box is on top in the game view. For an easier fix, go to player scene (Tab at the top) and in the inspector go to ordering -> z index and write 5. By default all visible nodes have a z index of 0.

Drag in second platform to the game view. This one will move. Select it in the tree on the left, click plus to add new node and search animation player. In the bottom, click animation -> new. Name it "move".
Click the platform you're working on rn in the tree and in the inspector go to transform for the position. Click on the key and click create. 
In the animator, drag blue line forward to 1 second and then drag platform to the right end point while holding shift to snap to axis, then click on key again. Click play to see the animation play. Click the looping arrows on top right on animator to loop animation, and click twice for bounce back loop. If it is too fast change number next to clock in top right (1-> 1.5) and drag last key frame to the end. Click A Arrow to the left of Edit in animator to play on load.

Pickups:
Click plus on tab to create new scene and then click plus in top left, search for area2D. You cannot collide with objects in area2D but it can detect collisions. While selected click plus again and search for sprite2D. 

Optional: Instead of sprite2D select AnimatedSprite2D. In the inspector click new -> spriteframes. Click sprite frames and in the animator click the 3x3 grid button to select spritesheet. Set the horizontal and vertical grid and click the frames you want in the animation. Hit F and zoom in, click auto play. 

In the tree select Area2D and click plus, search for CollisionShape2D (in inspector circleShape2D). Select area2D and rename it to coin and save scene. Go back to game tab and drag it into game view from bottom left folder.

Click coin tab -> click Coin node -> click scroll to add script. Choose default template and for path put it under the scripts folder. 

The ready function happens as soon as the game starts, try this line of code to test it;

func _ready():
    print("I'm a coin") 

It will show up in the output window, click output at the very bottom of the screen to see it. 

Remove the two functions, only leave extends Area2D.
Click on coin node in the tree on the left (Area2D node) and click the node tab next to the inspector on the right. We want to use the body entered signal, double click this and hit connect. This creates new function in script with a green arrow in front of it.


Foreground and Background:

Select game tab, in tree select tile map in inspector make sure the button tile set is not clicked. Go into layers in the actual inspector and name it Mid. Click add element, name it background and move it to the top to put it behind the mid layer in game. When painting make sure you've selected the right layer to paint in the the bottom window. 


Enemy:
Create new scene (New Tab) and add a node2D using the plus in the top left. While selecting this add a Sprite 2D (Or animated sprite if you want). Drag and drop png from folder into the inspector. Hit F and zoom in. 
Click weird symbol next to plus in top left to select a scene to add (Killzone). Select killzone node in tree and click plus to add a CollisionShape2D (rectangle). Rename top node to slime and save it as scene. Go to game tab and drag in enemy from folder. Press play and try it out. 

Enemy movement:
Go into slime tab click scroll to add new script to slime node, template = default, path = script, hit create. Get rid of ready function. 

const SPEED = 60

func _process(delta):
    position.x += SPEED * delta

It will move 60 pixels per second.


const SPEED = 60

var direction = 1 

func _process(delta):
    position.x += direction * SPEED * delta

This choosed the direction it travels in for now.

Click on slime tab -> slime node and click plus to add raycast2D. Move starting point to middle of enemy and end to just outside the right of it. Name it RaycastRight, duplicate and switch it around to make RaycastLeft. Select both, click and drag it into the script and hold cntrl while releasing. Do the same for Sprite2D

const SPEED = 60

var direction = 1 

@onready var ray_cast_right = $RayCastRight
@onready var ray_cast_left = &RayCastLeft
@onready var sprite_2D = $sprite2D


func _process(delta):
    if ray_cast_right.is_colliding():
        direction = -1
        sprite_2D.flip_h = true
    if ray_cast_left.is_colliding():
        direction = 1
        sprite_2D.flip_h = false

    position.x += direction * SPEED * delta

To make sprite flip around when going other way go to sprite2D (or animated sprite 2D) in tree and then in inspector click flip H on.

Rebinding input keys:
Go to project (in very top left) -> project settings -> input Map. Write an action to add in with button on right, for example "jump", "move_left" and "move_right". Press the plus sign next to each action and hit whatever button you want to bind to it, it'll appear and you can hit okay to confirm it. You can also at multiple key bindings to an action for example for "move_left" you can add "left_arrow_key" and "A". 

Go back to your movement script on the collisionshape2D of the player node while in the player tab, and replace the line

if Input.is_action_just_pressed("ui_accept") and is_on_floor():

with

if Input.is_action_just_pressed("jump") and is_on_floor():

and replace the line

var direction = Input.get_axis("ui_left", "ui_right")

with 

var direction = Input.get_axis("move_left", "move_right")

Now you can use the keys you selected to move around. 


To flip sprite based on direction:
Click and drag Sprite2D (or animatedSprite2D) into the scripts above the function _physics_process(delta) and hold cntrl when releasing. Then change code to this

#Get the input direction: -1, 0, 1
var direction = Input.get_axis("move_left", "move_right")

#Flip the Sprite
if direction > 0 
    Sprite_2D.flip_h = false
elif direction < 0
    Sprite_2D.flip_h = true

#Apply movement
if direction:
    velocity.x = direction * SPEED
else:
    velocity.x = move+toward(velocity.x, 0, SPEED)

move_and_slide()


Text:

Select Game tab and click plus on tree, search Label, hit F and zoom. Add text in the field in the right, if text looks blurry you are zoomed in very far and you should add a font. Make sure to use the right size aswel to make it less blurry. Create a base node and place all labels in this node. 

Score:

Click the plus in the top left again to add a new base node (This one is not node2D unlike all other nodes used so far, including other base nodes), name it GameManager and place it at the top of the tree. Click the scroll to give it a script, template = empty, path = scripts (rename it in the folder to game_manager). 

var score = 0

func add_point():
    score += 1
    print(score)

Right click GameManager go to the bottom and select Access as Unique Name.Go into coin and click and drag the GameManager node into it holding cntrl when you let go. This will now have no path and only it's name. The % sign indicates the unique name instead of a path.

@onready var game_manager = %GameManager

func _on_body_entered(body):
    print("+1 coin!")
    queue_free()

Now replace the print line.

@onready var game_manager = %GameManager

func _on_body_entered(body):
    game_manager.add_point()
    queue_free()

It will now print the score in the output window when you pick up the coins. 

Add a label node, write "You collected X amount of coins!" and name it ScoreLabel. Drag it under GameManager, go into the game_manager script and Click and Drag the new Label into the top of the script while holding cntrl. Then rewrite the script to this:


var score = 0

@onready var score_label = $ScoreLabel

func add_point():
    score += 1
    score_label.text = "You collected" + str(score) + " coins!"

It will now update in game
