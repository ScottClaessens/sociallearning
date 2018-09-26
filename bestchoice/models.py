from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Scott Claessens'

doc = """
Social Learning Experiment - Best Choice
"""


class Constants(BaseConstants):
    name_in_url = 'bestchoice'
    players_per_group = 8
    num_rounds = 2

    rules = 'bestchoice/rules.html'


class Subsession(BaseSubsession):
    qlist = ['sl2_1a', 'sl2_1b', 'sl2_2a', 'sl2_2b',
            'sl2_3a', 'sl2_3b', 'sl2_4a', 'sl2_4b',
            'sl2_5a', 'sl2_5b', 'sl2_6a', 'sl2_6b',
            'sl2_7a', 'sl2_7b', 'sl2_8a', 'sl2_8b']


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    quiz1 = models.IntegerField(choices=[[1, 'True'], [0, 'False']], widget=widgets.RadioSelect)
    quiz2 = models.IntegerField(choices=[[1, 'True'], [0, 'False']], widget=widgets.RadioSelect)
    quiz3 = models.IntegerField(choices=[[1, 'True'], [0, 'False']], widget=widgets.RadioSelect)
    quiz4 = models.IntegerField(choices=[[1, 'True'], [0, 'False']], widget=widgets.RadioSelect)
    sl1 = models.IntegerField(choices=[[1, 'Yes'], [0, 'No']], widget=widgets.RadioSelect)
    sl2_1a = models.BooleanField(widget=widgets.CheckboxInput, blank=True)
    sl2_2a = models.BooleanField(widget=widgets.CheckboxInput, blank=True)
    sl2_3a = models.BooleanField(widget=widgets.CheckboxInput, blank=True)
    sl2_4a = models.BooleanField(widget=widgets.CheckboxInput, blank=True)
    sl2_5a = models.BooleanField(widget=widgets.CheckboxInput, blank=True)
    sl2_6a = models.BooleanField(widget=widgets.CheckboxInput, blank=True)
    sl2_7a = models.BooleanField(widget=widgets.CheckboxInput, blank=True)
    sl2_8a = models.BooleanField(widget=widgets.CheckboxInput, blank=True)
    sl2_1b = models.BooleanField(widget=widgets.CheckboxInput, blank=True)
    sl2_2b = models.BooleanField(widget=widgets.CheckboxInput, blank=True)
    sl2_3b = models.BooleanField(widget=widgets.CheckboxInput, blank=True)
    sl2_4b = models.BooleanField(widget=widgets.CheckboxInput, blank=True)
    sl2_5b = models.BooleanField(widget=widgets.CheckboxInput, blank=True)
    sl2_6b = models.BooleanField(widget=widgets.CheckboxInput, blank=True)
    sl2_7b = models.BooleanField(widget=widgets.CheckboxInput, blank=True)
    sl2_8b = models.BooleanField(widget=widgets.CheckboxInput, blank=True)
    decision = models.IntegerField(choices=[[1, 'Potatoes'], [2, 'Wheat']], widget=widgets.RadioSelect)
    revenue = models.CurrencyField()
