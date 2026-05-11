from gamelib import *

#Game Functions
def player_update():
    player.draw()

    player.forward(0)
    if keys.Pressed[K_a]:
        player.images = walk.images
        player.rotateBy(-8)
    elif keys.Pressed[K_d]:
        player.images = walk.images
        player.rotateBy(8)
    elif keys.Pressed[K_w]:
        player.images = walk.images
        player.forward(5)
    elif keys.Pressed[K_s]:
        player.images = walk.images
        player.forward(-5)
    elif keys.Pressed[K_SPACE]:
        player.images = stab.images
        slash.play()
    else:
        player.images = walk.images

def gun_update():
    pgun.draw()

    health.moveTo(pgun.x-30, pgun.y+50)
    health.width=pgun.health/4

    pgun.forward(0)
    if keys.Pressed[K_a]:
        pgun.images = gwalk.images
        pgun.rotateBy(-8)
    elif keys.Pressed[K_d]:
        pgun.images = gwalk.images
        pgun.rotateBy(8)
    elif keys.Pressed[K_w]:
        pgun.images = gwalk.images
        pgun.forward(5)
    elif keys.Pressed[K_s]:
        pgun.images = gwalk.images
        pgun.forward(-5)
    elif keys.Pressed[K_SPACE]:
        pgun.images = shot.images
        shoot.play()
    else:
        pgun.images = gwalk.images


def positionObjects(objects):
    for i in range(len(objects)):
        x = randint(50, 750)
        y = randint(-3000, -100)
        objects[i].moveTo(x, y)
        objects[i].setSpeed(4, 180)
        objects[i].visible = True

#Main Program
game = Game(800,600, "Monster Survival")
field = Image("images/grassfield.jpg", game)
field.resizeTo(game.width, game.height)
game.setBackground(field)



#Lists
rocks = []
trees = []
zombs = []
vamps = []
meds = []
#variables
player = Animation("images/player_1.png", 6, game, 50, 268/6, 5)
walk = Animation("images/player_1.png", 6, game, 50, 268/6, 5)
stab = Animation("images/playerknife_attack.png", 8, game, 59, 357/8, 6)
pgun = Animation("images/gunwalk.png", 6, game, 42, 263/6, 5)
gwalk = Animation("images/gunwalk.png", 6, game, 42, 263/6, 5)
shot = Animation("images/gunshot.png", 4, game, 40, 222/4, 5)
death = Animation("images/death.png", 9, game, 47, 331/9, 9)

boss = Animation("images/Boss.png", 8, game, 539/8, 82, 4)
boss.y=-300
boss.health = 20


reload = Sound("sounds/reload.mp3", 1)
shoot = Sound("sounds/shoot.mp3", 2)
slash = Sound("sounds/slash.mp3", 3)
zdie = Sound("sounds/zombiedie.mp3", 4)
swin = Sound("sounds/win.mp3", 5)
slose = Sound("sounds/loss.mp3", 6)
groan = Sound("sounds/bossgroan.mp3", 0)
chop = Sound("sounds/treehit.mp3", 7)


bullet = Image("images/bullet.png", game)
bullet.resizeBy(-96)
bullet.setSpeed(8, 0)
bullet.visible = False

win = Image("images/WinImage.png", game)
win.resizeTo(800, 600)
win.visible = False

lose = Image("images/LoseImage.png", game)
lose.resizeTo(800, 600)
lose.visible = False


storyText = Image("images/Storyline.png", game)
storyText.resizeTo(800, 600)
storyText.visible = False

howplay = Image("images/HowPlay.png", game)
howplay.resizeTo(800, 600)
howplay.visible = False

howto = Image("images/HowTo.png", game)
howto.y = 375

story = Image("images/Story.png", game)
story.y = 225

play = Image("images/Play.png", game)
play.y = 525

title = Image("images/Title.png", game)
title.y = 150

player.wood = 0
player.rock = 0
player.vamp = 0

for i in range(10):
    zombie = Animation("images/zombie.png", 6, game, 323/6.225, 75, 4)
    zombie.resizeBy(-25)
    zombs.append(zombie)
positionObjects(zombs)

for i in range(5):
    vampire = Animation("images/vampire.png", 8, game, 922/8, 147, 4)
    vampire.resizeBy(-30)
    vampire.health = 15
    vamps.append(vampire)
positionObjects(vamps)

for i in range(30):
    stone1 = Image("images/stone1.png", game)
    stone1.resizeBy(-85)
    rocks.append(stone1)
positionObjects(rocks)

for i in range(50):
    tree1 = Image("images/tree_1.png", game)
    tree1.resizeBy(-70)
    trees.append(tree1)
positionObjects(trees)

for i in range(20):
    medkit = Image("images/medkit.png", game)
    medkit.resizeBy(-40)
    meds.append(medkit)
positionObjects(meds)

tprogress = Shape("bar", game, 200, 10, brown)
tprogress.moveTo(10, 30)
rprogress = Shape("bar", game, 200, 10, gray)
rprogress.moveTo(10, 60)
health = Shape("bar", game, pgun.width, 10, green)
bbar = Shape("bar", game, 200, 10, red)

#Start Screen
while not game.over:
    game.processInput()
    game.scrollBackground("down", 2)
    field.draw()
    player.draw()
    story.draw()
    howto.draw()
    play.draw()
    title.draw()
    howplay.draw()
    storyText.draw()

    if mouse.collidedWith(story, "rectangle") and mouse.LeftClick:
        storyText.visible = True
    if keys.Pressed[K_SPACE]:
        storyText.visible = False

    if mouse.collidedWith(howto, "rectangle") and mouse.LeftClick:
        howplay.visible = True
    if keys.Pressed[K_SPACE]:
        howplay.visible = False

    if mouse.collidedWith(play, "rectangle") and mouse.LeftClick:
        game.over = True
        mouse.visible = False
    game.update(30)

# Grace Pd
game.over = False
while not game.over:
    game.processInput()
    game.scrollBackground("down", 2)
    player_update()
    field.draw()

    for i in range(len(rocks)):
        rocks[i].move()
        if rocks[i].y > game.height + 100 and rocks[i].visible:
            rocks[i].x = randint(50, 750)
            rocks[i].y = randint(-5000, -100)
    player.move()

    for i in range(len(trees)):
        trees[i].move()
        if player.images == stab.images and player.collidedWith(trees[i]):
            trees[i].visible = False
            player.wood += 1
            chop.play()
        if player.wood >=25:
            game.over = True
        else:
            if trees[i].y > game.height + 100 and trees[i].visible:
                trees[i].x = randint(50, 750)
                trees[i].y = randint(-5000, -100)
            
    tprogress.draw()
    tprogress.width = player.wood * 8
    game.drawText("Wood: " + str(player.wood), 0, 0)
    game.drawText("Grace Period", 350, 0)
    game.update(30)
game.over = False
# Wave 1
while not game.over:
    game.processInput()
    game.scrollBackground("down", 2)
    gun_update()
    bullet.move()
    field.draw()
    pgun.move()
    if keys.Pressed[K_SPACE] and bullet.visible == False:
        bullet.moveTo(pgun.x, pgun.y)
        bullet.setSpeed(8, pgun.getAngle())
        bullet.visible = True
        shoot.play()
    
    if bullet.y > game.height or bullet.y < 0 or bullet.x > game.width or bullet.x < 0:
        bullet.visible = False
        reload.play(False)


    
    for i in range(len(zombs)):
        zombs[i].rotateTowards(pgun)
        zombs[i].moveTowards(pgun, randint(2,4))
        if zombs[i].collidedWith(pgun):
            pgun.health -= 1
            
        if bullet.collidedWith(zombs[i]):
            game.score+=1
            zombs[i].visible = False
            bullet.visible = False
            zdie.play()
            
    for i in range(len(trees)):
         trees[i].move()
         if trees[i].y > game.height + 100 and trees[i].visible:
                trees[i].x = randint(50, 750)
                trees[i].y = randint(-5000, -100)

    if pgun.health < 0 or game.score == 10:
        game.over = True
    game.drawText("Wave 1", 350, 0)
    game.drawText("Score: " + str(game.score), 0, 0)
    game.update(30)
game.over = False

positionObjects(trees)
positionObjects(rocks)

#Grace 2
while not game.over and pgun.health > 0 and player.health > 0:
    game.processInput()
    game.scrollBackground("down", 2)
    player_update()
    field.draw()

    for i in range(len(rocks)):
        rocks[i].move()
        if player.images == stab.images and player.collidedWith(rocks[i]):
            rocks[i].visible = False
            player.rock += 1
            chop.play()
        if rocks[i].y > game.height + 100 and rocks[i].visible:
            rocks[i].x = randint(50, 750)
            rocks[i].y = randint(-5000, -100)
    player.move()
    for i in range(len(meds)):
        meds[i].move()
        if meds[i].collidedWith(player):
            pgun.health += 5
            meds[i].visible = False
    for i in range(len(trees)):
        trees[i].move()
        if player.images == stab.images and player.collidedWith(trees[i]):
            trees[i].visible = False
            player.wood += 1
            chop.play()
        if trees[i].y > game.height + 100 and trees[i].visible:
            trees[i].x = randint(50, 750)
            trees[i].y = randint(-5000, -100)
    if player.wood >=50 and player.rock >=15:
        game.over = True

    rprogress.draw()
    rprogress.width = player.rock * 8
    
    tprogress.draw()
    tprogress.width = player.wood * 8
    game.drawText("Wood: " + str(player.wood), 0, 0)
    game.drawText("Stone: " + str(player.rock), 0, 90)
    game.drawText("Grace Period 2", 350, 0)
    game.update(30)
game.over = False
game.score = 0

positionObjects(zombs)

#Wave 2
while not game.over and pgun.health > 0 and player.health > 0:
    game.processInput()
    game.scrollBackground("down", 2)
    gun_update()
    bullet.move()
    field.draw()
    pgun.move()
    if keys.Pressed[K_SPACE] and bullet.visible == False:
        bullet.moveTo(pgun.x, pgun.y)
        bullet.setSpeed(8, pgun.getAngle())
        bullet.visible = True
        shoot.play()
    
    if bullet.y > game.height or bullet.y < 0 or bullet.x > game.width or bullet.x < 0:
        bullet.visible = False
        reload.play(False)


    
    for i in range(len(zombs)):
        zombs[i].rotateTowards(pgun)
        zombs[i].moveTowards(pgun, randint(2,4))
        if zombs[i].collidedWith(pgun):
            pgun.health -= 1
        if bullet.collidedWith(zombs[i]):
            game.score+=1
            zombs[i].visible = False
            bullet.visible = False
            zdie.play()
    for i in range(len(vamps)):
        vamps[i].rotateTowards(pgun)
        vamps[i].moveTowards(pgun, randint(4,6))
        if vamps[i].collidedWith(pgun):
            pgun.health -= 0.25
        if bullet.collidedWith(vamps[i]):
            vamps[i].health -= 5
            bullet.visible = False
        if vamps[i].health <= 0:
            vamps[i].visible = False
            player.vamp += 1
            zdie.play()
            

    for i in range(len(trees)):
         trees[i].move()
         if trees[i].y > game.height + 100 and trees[i].visible:
                trees[i].x = randint(50, 750)
                trees[i].y = randint(-5000, -100)
        
    if pgun.health < 0 or game.score == 10 and player.vamp >= 5:
        game.over = True
    game.drawText("Wave 2", 350, 0)
    game.drawText("Score: " + str(game.score), 0, 0)
    game.update(30)

game.over = False

positionObjects(zombs)
positionObjects(vamps)

#BOSS FIGHT
while not game.over and pgun.health > 0 and player.health > 0:
    game.processInput()
    game.scrollBackground("down", 2)
    gun_update()
    bullet.move()
    field.draw()
    pgun.move()
    boss.move()
    for i in range(len(zombs)):
        zombs[i].rotateTowards(pgun)
        zombs[i].moveTowards(pgun, randint(2,4))
        if zombs[i].collidedWith(pgun):
            pgun.health -= 1
        if bullet.collidedWith(zombs[i]):
            zombs[i].visible = False
            bullet.visible = False
            zdie.play()
    for i in range(len(vamps)):
        vamps[i].rotateTowards(pgun)
        vamps[i].moveTowards(pgun, randint(4,6))
        if vamps[i].collidedWith(pgun):
            pgun.health -= 0.25
        if bullet.collidedWith(vamps[i]):
            vamps[i].health -= 5
            bullet.visible = False
        if vamps[i].health <= 0:
            vamps[i].visible = False
            zdie.play()

    for i in range(len(trees)):
         trees[i].move() 

    boss.rotateTowards(pgun)
    boss.moveTowards(pgun, 1)

    for i in range(len(meds)):
        meds[i].move()
        if meds[i].collidedWith(pgun):
            pgun.health += 5
            meds[i].visible = False

    if boss.collidedWith(pgun):
        pgun.health -= 5
    
    if keys.Pressed[K_SPACE] and bullet.visible == False:
        bullet.moveTo(pgun.x, pgun.y)
        bullet.setSpeed(8, pgun.getAngle())
        bullet.visible = True
        shoot.play()
    
    if bullet.y > game.height or bullet.y < 0 or bullet.x > game.width or bullet.x < 0:
        bullet.visible = False
        reload.play(False)

    if bullet.collidedWith(boss):
        bullet.visible = False
        boss.health -= 1
        groan.play()

    if boss.health <= 0:
        game.over = True

    bbar.draw()
    bbar.moveTo(boss.x-50, boss.y-50)
    bbar.width = boss.health * 2

    game.drawText("BOSS FIGHT", 350, 0)
    
    game.update(30)

#Game Over
game.over = False

if pgun.health >= 0 and boss.health <= 0:
    swin.play(False)
else:
    slose.play(False)


while not game.over:
    game.processInput()
    game.scrollBackground("down", 2)
    win.draw()
    lose.draw()

    if pgun.health >= 0 and boss.health<= 0:
        win.visible = True
    else:
        lose.visible = True
    game.update(30)

game.quit()
