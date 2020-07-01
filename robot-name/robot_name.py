class Robot:
    import random
    def __init__(self):
        pass
    def name(self):
        alphabet = [chr(x) for x in range(ord('A'), ord('Z') + 1)]
        robo_name = random.choice(alphabet) + random.choice(alphabet) + str(random.choice(range(100,1000)))
        print(robo_name)
        return robo_name