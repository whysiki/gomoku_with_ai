import time


class TimeCounter:

    def __init__(self):
        self.total_time_start = None
        self.player_time_start = None
        self.ai_time_start = None

    @property
    def player_time_elapsed(self):
        if self.player_time_start:
            return time.time() - self.player_time_start
        else:
            return 0

    @property
    def ai_time_elapsed(self):
        if self.ai_time_start:
            return time.time() - self.ai_time_start
        else:
            return 0

    @property
    def total_time_elapsed(self):
        if self.total_time_start:
            return time.time() - self.total_time_start
        else:
            return 0

    def start_total_time(self):
        self.total_time_start = time.time()

    def start_player_time(self):
        self.player_time_start = time.time()

    def start_ai_time(self):
        self.ai_time_start = time.time()

    def get_total_time(self):
        # 当前总用时 - 总开始用时
        return int(self.total_time_elapsed)

    def get_player_time(self):
        # 当前玩家用时 - 玩家开始用时
        return int(self.player_time_elapsed)

    def get_ai_time(self):
        # 当前AI用时 - AI开始用时
        return int(self.ai_time_elapsed)

    def reset(self):
        self.total_time_start = None
        self.player_time_start = None
        self.ai_time_start = None

    def print(self):
        print(f"total_time_start: {self.total_time_start}")
        print(f"player_time_start: {self.player_time_start}")
        print(f"ai_time_start: {self.ai_time_start}")
        print(f"total_time_elapsed: {self.total_time_elapsed}")
        print(f"player_time_elapsed: {self.player_time_elapsed}")
        print(f"ai_time_elapsed: {self.ai_time_elapsed}")
