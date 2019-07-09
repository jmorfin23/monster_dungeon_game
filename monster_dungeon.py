
from IPython.display import clear_output
from random import randint

class MonsterDungeon():
    def __init__(self, cols, rows):
        self.cols = cols
        self.rows = rows
        self.num_monsters = 1

    def getNumMonsters(self):
        return self.num_monsters

#     def difficulty(self, difficulty):
#         if difficulty == 'easy':
#             pass
#         elif difficulty == 'medium':
#             self.num_monsters = 2
#         elif difficulty == 'hard':
#             pass
#         else:
#             pass

    def makeGrid(self, player, monster, door):
#         print(f'Difficulty setting: {})
        print(f'Player Name: {player.getName()}')
        print(f'Player Lives: {player.getLives()}')
        print(f'Player Coordinates: {player.getCoords()} ')
        for monster in monsters:
            print(f'Monster Coordinates: {monster.getCoords()}')
        print(f'Door Coordinates: {door.getCoords()}')
        for row in range(self.rows):
            #create top border before inner loop starts
            print('+---'* self.cols + '+')
            for cols in range(self.cols):
                flag = False

                if player.getCoords() == [cols,row] and self.cols - 1 ==cols:
                    print('| p ', end = '|')
                    flag = True
                elif player.getCoords() == [cols,row]:
                    print('| p ', end = '')
                    flag = True
                elif player.getCoords() == [cols,row] and self.cols - 1 ==cols:
                    print('| e ', end = '|')
                    flag = True
                elif egg.getCoords() == [cols, row]:
                    print('| e ', end = '')
                    flag = True
                # loop over list of monsters
                for monster in monsters:
                    if monster.getCoords() == [cols,row] and self.cols - 1 ==cols and flag == False:
                        print('| M ', end = '|')
                        flag = True
                    elif monster.getCoords() == [cols, row] and flag == False:
                        print('| M ', end = '')
                        flag = True
                if door.getCoords() == [cols,row] and self.cols - 1 ==cols and flag == False:
                    print('| D ', end = '|')
                elif door.getCoords() == [cols, row] and flag == False:
                    print('| D ', end = '')
                elif cols == self.cols - 1 and flag == False:
                    print('|   ', end = '|')
                elif flag == False:
                    print('|   ', end = '')

        #inner loop completes, create new lines
            print('')

        print('+---'* self.cols + '+' )

    def checkCollision(self, obj1, obj2):
        return obj1.getCoords() == obj2.getCoords()

    def handleMonsterHit(self, player, monsters):
        for monster in monsters:
            if self.checkCollision(player, monster):
                player.decrementLives()
            print(f'You got eaten by the monster. You have {player.getLives()} lives left.')
    def checkWinCondition(self, player, door):
        if self.checkCollision(player, door):
            print('Congratulations you won!')
            return False
        return True
    def checkLoseCondition(self, player):
        if player.getLives() <= 0:
            print(f'Sorry you lost all your lives {player.getName()}. Better luck next time sucker!')
        return False if player.getLives() <= 0 else True

class Player():
    def __init__(self, name = 'player', coords=[0,0], lives = 3):
        self.name = name
        self.lives = lives
        self.coords = coords

    def getCoords(self):
        return self.coords

    def getName(self):
        return self.name

    def makeName(self,name):
        self.name = name

    def decrementLives(self):
        self.lives -= 1

    def setLives(self, num):
        self.lives = num

    def getLives(self):
        return self.lives

    def movePlayer(self, move):
        if move == 'up':
            self.coords[1] -= 1
        elif move == 'down':
            self.coords[1] += 1
        elif move == 'left':
            self.coords[0] -= 1
        elif move == 'right':
            self.coords[0] += 1
        else:
            print('Invalid response. Please try again. ')

class Monster():
    def __init__(self, name = 'monster', coords=[2,2]):
        self.name = name
        self.coords = coords

    def moveMonster(self, cols, rows):
        self.coords = [randint(0, cols - 1), randint(0, rows - 1)]     #cols, row

    def getCoords(self):
        return self.coords

class Door():
    def __init__(self, coords=[3,3]):
        self.coords = coords

    def getCoords(self):
        return self.coords

class Eggs():
    def __init__(self, coords = [randint(0,4),randint(0,4)]):
        self.coords = coords

    def getCoords(self):
        return self.coords

class Menu():
    def __init__(self):
        pass

    def displayMenu(self):
        pass


while True:

    #global game variables
    rows = 5
    cols = 5
    playing = True
    game = MonsterDungeon(cols, rows)
    player = Player(coords = [0,0])
#   monster = Monster(coords = [2,2])

    monsters = [Monster([2,2]) for i in range(game.getNumMonsters())]
    door = Door(coords = [4,3])
    egg = Eggs()

    #ask for user for name and difficulty setting
    n = input('Hello Player. Enter your gamer name:')
    player.makeName(n)

    #asks user to set the difficulty
#     d = input('Enter your difficulty (Easy, Medium, Hard: ').lower()
#     game.difficulty(d)

    #game loop
    while playing:
        game.makeGrid(player, monsters, door)

        #ask player for movement or quit
        ans = input('what would you like to do? up down left right quit: ').lower()

        clear_output()
        #base case
        if ans == 'quit':
            playing = False
            print('Thanks for playing')
        else:
            player.movePlayer(ans)

            for monster in monsters:
                monster.moveMonster(cols,rows)
        #check any collision


            #check win condition
            playing = game.checkWinCondition(player, door)


            #check monster collision
            game.handleMonsterHit(player, monsters) # add an s

            #check lose condition
            if playing:
                playing = game.checkLoseCondition(player)

    #ask player if they would like to play again
    #if yes, do nothing, will go to top of loop and reset all global game variables, and restat game loop
    if input('Would you like to play again').lower() == 'no':
        clear_output()
        print('Thanks for playing, come back soon!')
        break
    else:
        clear_output()
