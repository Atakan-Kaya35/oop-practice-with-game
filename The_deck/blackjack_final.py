import random
import time
from xlwt import Workbook
import pygame

pygame.init()
suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
ranks = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]
value_key = {"Ace": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9,
             "Ten": 10, "Jack": 10, "Queen": 10, "King": 10}
bg_img = pygame.image.load('Blackjack_table.jpg')
default_image_size = (750, 750)
default_card_size = (70, 100)
bg_img = pygame.transform.scale(bg_img, default_image_size)
bg_patch = pygame.image.load('Capture.JPG')
bg_patch = pygame.transform.scale(bg_patch, (60, 50))
white_color = (255,255,255)


class Card:
    def __init__(self, suit, rank):
        self.rank = rank
        self.suit = suit
        self.value = value_key[rank]
        self.name = self.rank + " of " + self.suit
        if self.rank not in ["Ace", "King", "Queen", "Jack"]:
            self.card_name = str(self.value) + "_of_" + self.suit
        elif self.rank in ["Ace", "King", "Queen", "Jack"]:
            self.card_name = self.rank.lower() + "_of_" + self.suit.lower()

        self.appearance = pygame.image.load(f'{self.card_name}.png')
        self.appearance = pygame.transform.scale(self.appearance, default_card_size)

    def __str__(self):
        return self.rank + " of " + self.suit


class Deck:
    def __init__(self):
        self.all_cards = []
        for j in range(4):
            for l in suits:
                for i in ranks:
                    created = Card(l, i)
                    self.all_cards.append(created)

    def shuffle(self):
        random.shuffle(self.all_cards)

    def __str__(self):
        for i in range(len(self.all_cards)):
            print(self.all_cards[i])


class Player:
    def __init__(self, card1, card2, xandy):
        self.cards_in_hand = [card1, card2]
        self.value = 0
        for i in self.cards_in_hand:
            self.value = self.value + i.value
        if card1.rank == "Ace" or card2.rank == "Ace":
            self.value = self.value + 10
        self.is_bust = False
        self.bj = False
        self.x = xandy[0]
        self.y = xandy[1]


    def __str__(self):
        rreturn = "Player has: "
        for i in self.cards_in_hand:
            rreturn = rreturn + i.name + " (" + str(i.value) + "), "
        rreturn = rreturn + f"(total: {self.value})"
        return rreturn

    def went_bust(self):
        if self.value > 21:
            self.is_bust = True
            return True

    def hit(self, card):
        self.cards_in_hand.append(card)
        self.value = (self.value + 11) if card.rank == "Ace" and self.value <= 10 else (self.value + card.value)

    def show_where(self):
        for i in range(len(self.cards_in_hand)):
            final = self.x - (i * 30)
            finall = self.y - (i * 30)
            screen.surface.blit(self.cards_in_hand[i].appearance, (final, finall))
            pygame.display.update()

    def show_score(self):
        y = self.y + 100
        x = self.x + 5
        screen.surface.blit(font.render(str(self.value), True, white_color), (x, y))



        screen.surface.blit(font.render(str(self.value), True, white_color), (x, y))

    def get_value(self):
        pygame.display.update()
        y = self.y + 100
        x = self.x + 5
        whl_in = True
        display_table(False)
        while whl_in:
            if self.value <10:
                screen.surface.blit(font.render("_", True, (255,0,0)), (x, y))
            else:
                screen.surface.blit(font.render("__", True, (255,0,0)), (x, y))
            pygame.display.update()
            if self.went_bust():
                self.is_bust = True
                print("HHHHHEEEEEEERRRRRRREEEEEE")
                screen.surface.blit(font.render("BUST", True, (54,69,79)), (self.x, self.y))
            if self.value == 21:
                self.bj = True
                whl_in = False
            if self.value == 21:
                self.bj = True
                whl_in = False
            if self.value > 21:
                self.is_bust
                whl_in = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_y:
                        self.hit(ddeck.all_cards.pop(-1))
                        print(self)
                        display_table(False)
                    if event.key == pygame.K_n:
                        whl_in = False
                        break


        pygame.display.update()

    def special_occasion(self):
        if self.bj:
            screen.surface.blit(font.render("BLACKJACK", True, (218, 165, 32)), ((self.x - 90), self.y))
            pygame.display.update()

        elif self.is_bust:
            screen.surface.blit(font.render("BUST", True, (33, 49, 59)), ((self.x - 40), self.y))
            pygame.display.update()

    def print_outcome(self, x, y, letter, number):
        table.went_bust()
        self.went_bust()

        if table.is_bust and self.is_bust == False:
            print(f"Player won, table went bust with value {table.value}")
            display_specific(f"Player won, table went bust with value {table.value}", x, y)

        elif table.is_bust == False and self.is_bust:
            print(f"Table won, player went bust with {self.value}")
            display_specific(f"Table won, player went bust with {self.value}", x, y)

        elif table.value > self.value and self.value < 22:
            print(f"Table won, with table value {table.value} against {self.value}.")
            display_specific(f"Table won, with table value {table.value} against {self.value}.", x, y)


        elif table.value == self.value:
            print(f"Player drew with the table value is: {self.value}.")
            display_specific(f"Player drew with the table value is: {self.value}.", x, y)


        elif table.is_bust and self.is_bust:
            print(f"Table won, player went bust with: {self.value}")
            display_specific(f"Table won, player went bust with: {self.value}", x, y)


        elif table.value < self.value:
            print(f"Player won, with a higher hand {self.value} vs. {table.value}")
            display_specific(f"Player won, with a higher hand {self.value} vs. {table.value}", x, y)


    def full_bundle(self):
        self.show_where()
        self.show_score()
        self.special_occasion()


class Table:

    def __init__(self, card1, card2):
        self.cards_in_hand = [card1, card2]
        self.value = 0
        for i in self.cards_in_hand:
            self.value = self.value + i.value
        if card1.rank == "Ace" or card2.rank == "Ace":
            self.value = self.value + 10
        self.displayed = card1.value if card1.rank != "Ace" else 11
        self.is_bust = False

    def __str__(self):
        rreturn = "Table has: "
        for i in self.cards_in_hand:
            rreturn = rreturn + i.name + " (" + str(i.value) + "), "
        rreturn = rreturn + f"(total: {self.value})"
        return rreturn

    def went_bust(self):
        if self.value > 21:
            self.is_bust = True
            return True


    def hit(self, card):
        self.cards_in_hand.append(card)
        self.value = (self.value + 11) if card.rank == "Ace" and self.value <= 10 else (self.value + card.value)
        if self.value == 21:
            self.bj = True


class Screen():
    def __init__(self):
        self.background = pygame.image.load('blackjack_icon.png')
        pygame.display.set_icon(self.background)
        pygame.display.set_caption("Blackjack")
        self.surface = pygame.display.set_mode((750, 750))


def display_table(tableturn):
    if tableturn == False:
        screen.surface.blit(bg_img, (0, 0))

        if 2 == len(table.cards_in_hand):
            pygame.display.update()
            screen.surface.blit(table.cards_in_hand[0].appearance, (335, 100))
            joker = pygame.image.load('red_joker.png')
            joker = pygame.transform.scale(joker, default_card_size)
            screen.surface.blit(joker, (365, 130))
            screen.surface.blit(font.render(str(table.displayed), True, white_color), (365, 50))
            pygame.display.update()
        else:
            for i in range(len(table.cards_in_hand)):
                final = 335 + (i * 30)
                finall = 100 + (i * 30)
                screen.surface.blit(table.cards_in_hand[i].appearance, (final, finall))
                pygame.display.update()
                time.sleep(.2)

        player.full_bundle()

        player1.full_bundle()

        player2.full_bundle()


        pygame.display.update()
    elif tableturn == True:
        yakami_birak_artik()
        time.sleep(1)
        j = len(table.cards_in_hand) - 1
        screen.surface.blit(table.cards_in_hand[j].appearance, ((335 + (j * 30)), (100 + (j * 30))))
        tottal_rn(False)
        pygame.display.update()


def display_specific(message, x, y):
    messsage = font1.render(str(message), True, white_color)
    screen.surface.blit(messsage, (x, y)),
    pygame.display.update()
    time.sleep(1.2)


def yakami_birak_artik():
    screen.surface.blit(bg_img, (0, 0))

    player.full_bundle()

    player1.full_bundle()

    player2.full_bundle()

    for i in range(len(table.cards_in_hand) - 1):
        final = 335 + (i * 30)
        finall = 100 + (i * 30)
        screen.surface.blit(table.cards_in_hand[i].appearance, (final, finall))
        tottal_rn(True)
        pygame.display.update()


def tottal_rn(truee):
    if truee == True:
        total_rn = 0
        for i in range(len(table.cards_in_hand) - 1):
            total_rn = total_rn + table.cards_in_hand[i].value

        table_total = font.render(str(total_rn), True, white_color)
        screen.surface.blit(table_total, (365, 50))
        pygame.display.update()

    else:
        screen.surface.blit(bg_patch, (365, 50))
        total_rn = table.value

        table_total = font.render(str(total_rn), True, white_color)
        screen.surface.blit(table_total, (365, 50))
        pygame.display.update()



font = pygame.font.Font("freesansbold.ttf", 50)
font1 = pygame.font.Font("freesansbold.ttf", 10)
font2 = pygame.font.Font("freesansbold.ttf", 100)


game_on = True
x_y_values = [[375, 520], [135, 350], [600, 350]]
num=0

while game_on:
    whl_in = True
    screen = Screen()
    ddeck = Deck()
    ddeck.shuffle()
    player = Player( ddeck.all_cards.pop(-1), ddeck.all_cards.pop(-1), x_y_values[0])
    player1 = Player(ddeck.all_cards.pop(-1), ddeck.all_cards.pop(-1), x_y_values[1])
    player2 = Player(ddeck.all_cards.pop(-1), ddeck.all_cards.pop(-1), x_y_values[2])
    table = Table(ddeck.all_cards.pop(-1),ddeck.all_cards.pop(-1))
    print(table)
    print(player1)
    print(player)
    print(player2)
    display_table(False)
    all_bust = False
    player1.get_value()
    player.get_value()
    player2.get_value()

    if player.is_bust == True and player1.is_bust == True and player2.is_bust == True:
            all_bust = True

    while table.is_bust == False and table.value <= player.value and table.value <= player1.value and table.value <= player2.value and all_bust == False:
        table.went_bust()
        table.hit(ddeck.all_cards.pop(-1))
        print(table)

    display_table(True)
    player1.print_outcome(70, 500, 1, num)
    player.print_outcome(315, 700, 2, num)
    player2.print_outcome(550, 500, 3, num)
    print("\n\n")
"""
while True:
    screen = Screen()
    ddeck = Deck()
    ddeck.shuffle()
    player = Player(ddeck.all_cards.pop(-1), ddeck.all_cards.pop(-1), x_y_values[0])
    player1 = Player(ddeck.all_cards.pop(-1), ddeck.all_cards.pop(-1), x_y_values[1])
    player2 = Player(ddeck.all_cards.pop(-1), ddeck.all_cards.pop(-1), x_y_values[2])

    table = Table(ddeck.all_cards.pop(-1), ddeck.all_cards.pop(-1))
    print(table)
    print(player1)
    print(player)
    print(player2)
    display_table(False)
    all_bust = False

    player1.get_value()
    player.get_value()
    player2.get_value()


    if player.is_bust == True and player1.is_bust == True and player2.is_bust == True:
        all_bust = True

    while table.is_bust == False and table.value <= player.value and table.value <= player1.value and table.value <= player2.value and all_bust == False:
        table.went_bust()
        table.hit(ddeck.all_cards.pop(-1))
        print(table)
        display_table(True)

    display_table(True)
    player1.print_outcome(70, 500, 1, num)
    player.print_outcome(315, 700, 2, num)
    player2.print_outcome(550, 500, 3, num)
    print("\n\n")

#=COUNTIF(B1:M500,B2)
"""