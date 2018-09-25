from grid import Grid


class BasePlayer:

    def play(self, state: Grid) -> int:
        raise NotImplementedError
        # return random.randint(0, len(state))
