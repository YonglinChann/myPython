class Game(object):
    top_score = 0
    def __init__(self, player_name):
        self.player_name = player_name
    @staticmethod
    def show_help():
        print('【游戏帮助信息】\n')
    @classmethod
    def show_top_score(cls):
        print('分数为：%d'%cls.top_score,'\n')
    def start_game(self):
        print('%s:游戏开始啦!'%self.player_name)

Game.show_help()
Game.show_top_score()
player1 = Game('阿林')
player1.start_game()