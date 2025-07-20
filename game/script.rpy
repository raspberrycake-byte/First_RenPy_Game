# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Waltz")

 
# The game starts here.

label start:     

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    
    play music "bg audio.ogg" fadeout 1.0 fadein 1.0 volume 0.1
    scene bg:
        fit "contain"
        xsize 2000
        xalign 0.5  
        yalign 0.5
        

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show guy:
        fit "contain"
        xsize 800
        xalign 0.5
        yalign 0.5

    # These display lines of dialogue.

    e "Hi!"

    e "Once you add a story, pictures, and music, you can release it to the world!"
    
    # This ends the game.
    stop music 
    return
