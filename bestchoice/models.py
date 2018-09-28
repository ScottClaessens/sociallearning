from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import numpy as np


author = 'Scott Claessens'

doc = """
Social Learning Experiment - Best Choice
"""


class Constants(BaseConstants):
    name_in_url = 'bestchoice'
    players_per_group = 8
    num_rounds = 20

    rules = 'bestchoice/rules.html'


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    def calculate_revenue(self):
        # determine p (players choosing 1 == A)
        count = 0
        for player in self.get_players():
            if player.decision == 1:  # A
                count += 1
        p = count / 8
        # print('p:', p)
        # calculate revenue for each player
        a = self.session.config['bestchoice_a_payoff']
        b = self.session.config['bestchoice_b_payoff']
        c = self.session.config['bestchoice_c_payoff']
        d = self.session.config['bestchoice_d_payoff']
        for player in self.get_players():
            if player.decision == 1:  # A
                player.revenue = (p * a) + ((1 - p) * b) + int(np.random.normal(0, self.session.config['sigma'], 1))
            else:
                player.revenue = (p * c) + ((1 - p) * d) + int(np.random.normal(0, self.session.config['sigma'], 1))
            # print('revenue:', player.revenue)


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
