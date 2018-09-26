from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Intro(Page):
    pass


class Setup(Page):
    pass


class MakingDecisions(Page):
    pass


class CollectingInformation(Page):
    pass


class TimeLimits(Page):
    pass


class EndSession(Page):
    pass


page_sequence = [
    Intro,
    Setup,
    MakingDecisions,
    CollectingInformation,
    TimeLimits,
    EndSession
]
