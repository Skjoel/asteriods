# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    timer = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    my_font = pygame.font.SysFont("calibri", 15)

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    bullets = pygame.sprite.Group()

    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()

    player_score = 0
    dt = 0
    Shot.containers = (updatable, drawable, bullets)
    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    

    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        score_board = my_font.render("Score: " + str(player_score), 1, "white")
        
        screen.fill(000)
            
        for object in drawable:
            object.draw(screen)

        for object in updatable:
            object.update(dt)
        
        screen.blit(score_board, (50, 50))  


        for a in asteroids:
            if player.collision_check(a):

                raise SystemExit("Game over!")
               
            for b in bullets:
                if b.collision_check(a):
                    player_score += 1
                    b.kill()
                    a.split()

        pygame.display.flip()
        dt = timer.tick(60) / 1000

if __name__ == "__main__":
    main()