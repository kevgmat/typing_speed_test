import time
import pygame
pygame.init()

display = pygame.display.set_mode((920,480))
color_inactive = pygame.Color((255,0,0))
color_active = pygame.Color((0, 255, 0))
default = pygame.Color((0,0,0))

text = ["victorians once used leeches to predict the weather.",
        "your funny bone is actually a nerve.",
        "the chief translator of the european parliament speaks 32 languages fluently."]
        # "the most requested funeral song in england is by monty python.",
        # "research shows that all blue-eyed people may be related.",
        # "charles darwin's personal pet tortoise didn't die until recently.",
        # "the average person will spend six months of their life waiting for red lights to turn green.",
        # "a bolt of lightning contains enough energy to toast 100,000 slices of bread.",
        # "cherophobia is the word for the irrational fear of being happy.",
        # "you can hear a blue whale's heartbeat from two miles away.",
        # "nearly 30,000 rubber ducks were lost at sea in 1992 and are still being discovered today.",
        # "the inventor of the frisbee was turned into a frisbee after he died.",
        # "subway footlongs aren't always a foot long.",
        # "marie curie's notebooks are still radioactive.",
        # "blood banks in sweden notify donors when blood is used.",
        # "the netherlands is so safe, it imports criminals to fill jails.",
        # "coke saved one town from the great depression."]

display.fill((255,255,255))
pygame.display.update()
y_location = 0
x_location = 0

for i in range(len(text)):
    for j in range(len(text[i])):
        text_surface = pygame.font.SysFont("monospace", 20).render(text[i][j], True, default)
        display.blit(text_surface,(x_location,y_location))
        x_location += 10
    y_location += 18
    x_location = 0
pygame.display.update()

t_2 = time.perf_counter()

input_box = pygame.Rect(0, 0, 1000, 480)
done = False
active = False

entered = []
i = 0
j = 0

correct = 0
wrong = 0

length = 0
for i in range(len(text)):
    for j in range(len(text[i])):
        length +=1

print(length)

x_location = 0
y_location = 0
count = 0
b = True
c = True

t_1 = time.perf_counter()
while not done:
    for i in range(len(text)):
        a = True
        for j in range((len(text[i]))):
            count +=1
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        done = True
                        pygame.quit()

                    if event.type == pygame.KEYDOWN:

                        ch = event.unicode

                        if ch == text[i][j]:
                            print(ch, text[i][j], "CORRECT")
                            text_surface = pygame.font.SysFont("monospace", 20).render(ch, True, color_active)
                            display.blit(text_surface, (x_location, y_location))
                            pygame.display.update()
                            correct += 1
                            x_location += 10
                        else:
                            print(ch, text[i][j], "WRONG")
                            # box_to_use = pygame.Rect(x, y, 120, 30)
                            # pygame.draw.rect(display, box_color, box_to_use)k
                            white_box = pygame.Rect(x_location, y_location, 10, 20)
                            pygame.draw.rect(display, pygame.Color((255, 255, 255)), white_box)
                            pygame.display.update()
                            text_surface = pygame.font.SysFont("monospace", 20).render(ch, True, color_inactive)
                            display.blit(text_surface, (x_location, y_location))
                            pygame.display.update()
                            x_location += 10
                            wrong += 1

                        if count > (length-1):
                            a = False
                            b= False
                            t_2 = time.perf_counter()
                            break
                        if pygame.key.get_focused():
                            a = False
                            break
                if a == False:
                    a = True
                    break
            if b== False:
                c = False
                break
        if c== False:
            done = True
            break
        y_location += 18
        x_location = 0

time_taken = t_2 - t_1
print("correct = ", correct)
print("wrong = ", wrong)

net_words = correct/4
speed = (net_words/time_taken)*60
accuracy = (correct/length)*100
print("accuracy = ", accuracy)
print("speed = ", speed)

