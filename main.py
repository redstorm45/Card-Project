import pygame
import random


SCR_CONNECT = 1


def loadCards():
    """
    :return: loaded cards

    Loads a standard deck of 52 cards
    """
    cards = {}
    for i in range(1, 14):
        for f in 'CDSH':
            n = str(i) + f
            im = pygame.image.load('ressources/cards/'+n+'.png')
            cards[n] = pygame.transform.smoothscale(im, (100, 140))
    for n in ['back', 'J1', 'J2']:
        im = pygame.image.load('ressources/cards/'+n+'.png')
        cards[n] = pygame.transform.smoothscale(im, (100, 140))
    return cards


def shuffle(deck):
    """
    :param deck: a deck to be shuffled
    :return: the shuffled deck
    """


def split(deck):
    """
    :param cards: a starting deck of cards
    :return: two decks of equal size, with random splitting
    """
    # initialisation
    selected = []
    available = list(range(len(deck)))
    # split half the main deck
    while len(selected) < len(deck)//2:
        sel = random.choice(available)
        selected.append(sel)
        available.remove(sel)
    # odd number of cards: selection or not of 1 more card
    if len(deck) % 2 == 1:
        if random.choice([0, 1]) == 0:
            sel = random.choice(available)
            selected.append(sel)
            available.remove(sel)
    # build the two decks
    d1 = [deck[i] for i in selected]
    d2 = [deck[i] for i in available]
    # finished
    return [d1, d2]


def drawDeck(win, deck, cards, cpos, visible=True):
    """
    :param win: the drawing surface
    :param deck: list of cards in the deck
    :param cards: textures of cards
    :param cpos: position of the center of the first card of the pack
    :param visible: shows the color of the last card of the pack?
    :return: None
    """
    if len(deck) > 0:
        drawing = 'back'
        if visible:
            drawing = deck[-1]
        W, H = cards[drawing].get_width(), cards[drawing].get_height()
        win.blit(cards[drawing], (cpos[0]-W//2, cpos[1]-H//2))


def printDeckSize(win, deck, cpos, font):
    """
    :param win:
    :param deck:
    :param cpos:
    :param font:
    :return:
    """


def main():
    # initialisation
    pygame.init()
    windowSize = (640, 480)
    win = pygame.display.set_mode(windowSize)
    screen = SCR_CONNECT

    # prepare a game
    cards = loadCards()
    decks = split([c for c in cards.keys() if c not in ['back', 'J1', 'J2']])
    decks = [decks[0]] + [[], []] + [decks[1]]

    # main loop
    clock = pygame.time.Clock()
    running = True
    while running:
        # events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if len(decks[0]) > 0 and len(decks[3]) > 0:
                        decks[1].append(decks[0].pop())
                        decks[2].append(decks[3].pop())

        # drawing procedure
        win.fill((0, 0, 0))

        drawDeck(win, decks[0], cards, (100, 280), False)
        drawDeck(win, decks[1], cards, (260, 280))
        drawDeck(win, decks[2], cards, (380, 280))
        drawDeck(win, decks[3], cards, (540, 280), False)

        pygame.display.flip()

        # wait for new frame
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
