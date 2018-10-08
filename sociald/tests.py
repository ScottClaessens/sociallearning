from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):

    def play_round(self):
        if self.round_number == 1:
            yield (pages.Intro)
            yield (pages.MarketRules)
            yield (pages.Quiz, {'quiz1': 1,
                                'quiz2': 1,
                                'quiz3': 0,
                                'quiz4': 1})
            yield (pages.Begin)
        if self.round_number > 1:
            yield (pages.SocialLearning1, {'sl1': 1})
            yield (pages.SocialLearning2)
        yield (pages.Decision, {'decision': 1})
        yield (pages.Results)
        if self.round_number == Constants.num_rounds:
            yield (pages.Final)