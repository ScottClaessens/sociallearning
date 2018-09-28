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

    def before_next_page(self):
        self.participant.vars['previous_decision'] = 0
        self.participant.vars['previous_revenue'] = 0
        self.participant.vars['total_earnings'] = 2500


class Begin(Page):
    def is_displayed(self):
        return self.player.round_number == 1


class Wait(WaitPage):
    pass


class SocialLearning1(Page):
    form_model = 'player'
    form_fields = ['sl1']

    def is_displayed(self):
        return self.player.round_number >= 2


class SocialLearning2(Page):
    form_model = 'player'

    def get_form_fields(self):
        qlist = ['sl2_1a', 'sl2_1b', 'sl2_2a', 'sl2_2b',
                 'sl2_3a', 'sl2_3b', 'sl2_4a', 'sl2_4b',
                 'sl2_5a', 'sl2_5b', 'sl2_6a', 'sl2_6b',
                 'sl2_7a', 'sl2_7b', 'sl2_8a', 'sl2_8b']
        i = self.player.id_in_group
        del qlist[(2 * i) - 2:2 * i]  # delete myself
        return qlist

    def error_message(self, values):
        elist = ['sl2_1a', 'sl2_1b', 'sl2_2a', 'sl2_2b',
                 'sl2_3a', 'sl2_3b', 'sl2_4a', 'sl2_4b',
                 'sl2_5a', 'sl2_5b', 'sl2_6a', 'sl2_6b',
                 'sl2_7a', 'sl2_7b', 'sl2_8a', 'sl2_8b']
        i = self.player.id_in_group
        del elist[(2 * i) - 2:2 * i]  # delete myself
        total = 0
        for s in range(1, len(elist)):
            total += int(values[elist[s-1]] or 0)
        if total > self.session.config['choices']:
            return 'You cannot choose more than ' + str(self.session.config['choices']) + ' pieces of information!'

    def is_displayed(self):
        return self.player.round_number >= 2 and self.player.sl1 == 1

    def vars_for_template(self):
        other_players = []
        for p in self.player.get_others_in_group():
            other_players += ['Farmer ' + str(p.id_in_group)]
        return {'other_players': other_players}


class Decision(Page):
    form_model = 'player'
    form_fields = ['decision']

    def vars_for_template(self):
        qlist_top = [self.player.sl2_1a, self.player.sl2_2a, self.player.sl2_3a, self.player.sl2_4a,
                     self.player.sl2_5a, self.player.sl2_6a, self.player.sl2_7a, self.player.sl2_8a]
        qlist_bottom = [self.player.sl2_1b, self.player.sl2_2b, self.player.sl2_3b, self.player.sl2_4b,
                        self.player.sl2_5b, self.player.sl2_6b, self.player.sl2_7b, self.player.sl2_8b]
        del qlist_top[self.player.id_in_group-1]  # delete myself
        del qlist_bottom[self.player.id_in_group-1]  # delete myself
        other_players = []
        prev_list_top = []
        prev_list_bottom = []
        for p in self.player.get_others_in_group():
                other_players += ['Farmer ' + str(p.id_in_group)]
                prev_list_top += [p.participant.vars['previous_decision']]
                prev_list_bottom += [p.participant.vars['previous_revenue']]
        zipped_top = zip(qlist_top, prev_list_top)
        zipped_bottom = zip(qlist_bottom, prev_list_bottom)
        # print('other_players: ', other_players)
        # print('qlist_top: ', qlist_top)
        # print('qlist_bottom: ', qlist_bottom)
        # print('prev_list_top: ', prev_list_top)
        # print('prev_list_bottom: ', prev_list_bottom)
        return {'other_players': other_players,
                'zipped_top': zipped_top,
                'zipped_bottom': zipped_bottom}


class ResultsWait(WaitPage):
    def after_all_players_arrive(self):
        self.group.calculate_revenue()


class Results(Page):
    def vars_for_template(self):
        return {'decision': self.player.get_decision_display(),
                'earnings': self.player.revenue - int(self.player.sl1 or 0)*25}

    def before_next_page(self):
        if self.player.sl1 == 1:
            cost = 25
        else:
            cost = 0
        self.participant.vars['previous_decision'] = self.player.get_decision_display()
        self.participant.vars['previous_revenue'] = int(self.player.revenue)
        self.participant.vars['total_earnings'] += self.player.revenue - int(self.player.sl1 or 0)*25


class Final(Page):
    def vars_for_template(self):
        return {'total': self.participant.vars['total_earnings']}

    def is_displayed(self):
        return self.round_number == Constants.num_rounds


page_sequence = [
    Intro,
    MarketRules,
    Quiz,
    Begin,
    Wait,
    SocialLearning1,
    SocialLearning2,
    Decision,
    ResultsWait,
    Results,
    Final
]
