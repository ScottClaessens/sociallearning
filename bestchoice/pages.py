from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Intro(Page):
    def is_displayed(self):
        return self.player.round_number == 1


class MarketRules(Page):
    def is_displayed(self):
        return self.player.round_number == 1


class Quiz(Page):
    form_model = 'player'
    form_fields = ['quiz1', 'quiz2', 'quiz3', 'quiz4']

    def quiz1_error_message(self, value):
        if value == 0:
            return 'This is incorrect. You CAN decide to produce Potatoes or Wheat in each Season of this experiment.'

    def quiz2_error_message(self, value):
        if value == 0:
            return 'This is incorrect. Before your decision, you CAN collect information about the decisions of others.'

    def quiz3_error_message(self, value):
        if value == 1:
            return 'This is incorrect. Your revenue DOES NOT depend on the decisions of other Farmers.'

    def quiz4_error_message(self, value):
        if value == 0:
            return 'This is incorrect. New groups WILL be formed randomly after this experiment.'

    def is_displayed(self):
        return self.player.round_number == 1


class Begin(Page):
    def is_displayed(self):
        return self.player.round_number == 1


class SocialLearning1(Page):
    form_model = 'player'
    form_fields = ['sl1']

    def is_displayed(self):
        return self.player.round_number >= 2


class SocialLearning2(Page):
    form_model = 'player'

    def get_form_fields(self):
        qlist = self.subsession.qlist
        i = self.player.id_in_group
        del qlist[(2 * i) - 2:2 * i]  # delete myself
        return qlist

    def error_message(self, values):
        qlist = self.subsession.qlist
        i = self.player.id_in_group
        del qlist[(2 * i) - 2:2 * i]  # delete myself
        total = 0
        for s in range(1, len(qlist)):
            total += int(values[qlist[s-1]] or 0)
        if total > self.session.config['choices']:
            return 'You cannot choose more than ' + str(self.session.config['choices']) + ' pieces of information!'

    def is_displayed(self):
        return self.player.round_number >= 2 and self.player.sl1 == 1

    def vars_for_template(self):
        other_players = []
        for p in range(1, 9):
            if p == self.player.id_in_group:
                pass
            else:
                other_players += ['Farmer ' + str(p)]
        return {'other_players': other_players}


class Decision(Page):
    form_model = 'player'
    form_fields = ['decision']


class ResultsWait(WaitPage):
    def after_all_players_arrive(self):
        


class Results(Page):
    pass


page_sequence = [
    Intro,
    MarketRules,
    Quiz,
    Begin,
    SocialLearning1,
    SocialLearning2,
    Decision,
    ResultsWait
]
