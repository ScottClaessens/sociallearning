from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):

    def play_round(self):
        yield (pages.Intro)
        yield (pages.Setup)
        yield (pages.MakingDecisions)
        yield (pages.CollectingInformation)
        yield (pages.TimeLimits)
        yield (pages.EndSession)
