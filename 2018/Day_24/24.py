#!/usr/bin/env python3#
import Common
import re
import copy


class Group:
    def __init__(self, group_id, unit_count, hit_points, attack_damage, attack_type, initiative):
        self.group_id = group_id
        self.unit_count = unit_count
        self.hit_points = hit_points
        self.attack_damage = attack_damage
        self.attack_type = attack_type
        self.initiative = initiative
        self.weaknesses = []
        self.immunities = []
        self.is_immune_group = False

    def effective_power(self):
        return self.unit_count * self.attack_damage

    def select_target(self, possible_target_groups, current_targets):
        possible_targets = [target for target in possible_target_groups.values() if
                            target.group_id not in current_targets.values()]
        if len(possible_targets) == 0:
            return None
        max_damage_target = max(possible_targets,
                                key=lambda target:
                                (target.calc_damage(self), target.effective_power(), target.initiative))
        if max_damage_target.calc_damage(self) == 0:
            return None
        else:
            return max_damage_target

    def calc_damage(self, attacking_group):
        if attacking_group.attack_type in self.immunities:
            return 0
        elif attacking_group.attack_type in self.weaknesses:
            return 2 * attacking_group.effective_power()
        else:
            return attacking_group.effective_power()

    def is_dead(self):
        return self.unit_count <= 0

    def receive_attack(self, attacking_group):
        damage = self.calc_damage(attacking_group)
        units_killed = int(damage / self.hit_points)
        self.unit_count -= units_killed

    def attack(self, target_group):
        target_group.receive_attack(self)


class ArmyParser:
    def __init__(self, lines):
        is_immune_group = True
        self._immune_army = {}
        self._infection_army = {}
        for line in lines:
            if not line.strip():
                continue
            elif "Immune System" in line:
                is_immune_group = True
                continue
            elif "Infection" in line:
                is_immune_group = False
                continue
            else:
                group = self.parse_group(line)
                if is_immune_group:
                    group.is_immune_group = True
                    self._immune_army[group.group_id] = group
                else:
                    group.is_immune_group = False
                    self._infection_army[group.group_id] = group

    def _get_new_group_id(self):
        return len(self._immune_army) + len(self._infection_army)

    def parse_group(self, line):
        unit_string = re.search(r"\d+ units", line).group()
        unit_count = int(unit_string.split()[0])
        hit_point_string = re.search(r"\d+ hit points", line).group()
        hit_points = int(hit_point_string.split()[0])
        attack_string = re.search(r"\d+ \w+ damage", line).group()
        attack_damage = int(attack_string.split()[0])
        attack_type = attack_string.split()[1]
        initiative_string = re.search(r"initiative \d+", line).group()
        initiative = int(initiative_string.split()[1])
        group = Group(self._get_new_group_id(), unit_count, hit_points, attack_damage, attack_type, initiative)
        defenses_match = re.search(r"\(.+\)", line)
        if defenses_match:
            defense_strings = defenses_match.group().split(";")
            for defense_string in defense_strings:
                cleaned_defense_string = re.sub("[^a-zA-Z ]", "", defense_string)
                if "weak" in cleaned_defense_string:
                    weaknesses = cleaned_defense_string.split()[2:]
                    group.weaknesses = weaknesses
                elif "immune" in cleaned_defense_string:
                    immunities = cleaned_defense_string.split()[2:]
                    group.immunities = immunities

        return group

    def get_immune_army(self):
        return copy.deepcopy(self._immune_army)

    def get_infection_army(self):
        return copy.deepcopy(self._infection_army)


class ImmuneSimulator:
    def __init__(self, infection_army, immune_army, boost = 0):
        self.infection_army = infection_army
        self.immune_army = immune_army
        for group in immune_army.values():
            group.attack_damage += boost

    def last_standing_after_battle(self):
        last_unit_count = self.get_total_unit_count()
        while len(self.infection_army) > 0 and len(self.immune_army) > 0:
            current_targets = self._targeting_phase()
            self._attacking_phase(current_targets)

            if all([target is None for target in current_targets]) or last_unit_count == self.get_total_unit_count():
                break
            last_unit_count = self.get_total_unit_count()
        return self.get_total_unit_count()

    def get_total_unit_count(self):
        return sum(group.unit_count for group in self.infection_army.values()) + \
               sum(group.unit_count for group in self.immune_army.values())

    def _targeting_phase(self):
        current_targets = {}
        all_groups = list(self.infection_army.values()) + list(self.immune_army.values())
        targeting_order = sorted(all_groups, key=lambda group: (group.effective_power(), group.initiative),
                                 reverse=True)
        for group in targeting_order:
            if group.is_immune_group:
                target = group.select_target(self.infection_army, current_targets)
            else:
                target = group.select_target(self.immune_army, current_targets)
            if target:
                current_targets[group.group_id] = target.group_id
            else:
                current_targets[group.group_id] = None
        return current_targets

    def _attacking_phase(self, current_targets):
        all_groups = list(self.infection_army.values()) + list(self.immune_army.values())
        attacking_order = sorted(all_groups, key=lambda group: group.initiative, reverse=True)
        for group in attacking_order:
            target_id = current_targets[group.group_id]
            if target_id is None:
                continue
            if group.is_immune_group:
                if group.is_dead():
                    continue
                else:
                    target = self.infection_army[target_id]
                    group.attack(target)
                    if target.is_dead():
                        del self.infection_army[target_id]
            else:
                if group.is_dead():
                    continue
                else:
                    target = self.immune_army[target_id]
                    group.attack(target)
                    if target.is_dead():
                        del self.immune_army[target_id]

    def did_immune_win(self):
        return len(self.immune_army) > 0 and len(self.infection_army) == 0


class BoostedImmuneSimulator:
    def __init__(self, army_parser):
        self.army_parser = army_parser
        self.max_boost = 1000
        self.min_boost = 0

    def get_next_boost(self):
        return int((self.max_boost + self.min_boost)/2)

    def get_units_at_min_boost_to_win(self):
        while (self.max_boost - self.min_boost) > 1:
            curr_boost = self.get_next_boost()
            boost_simulator = ImmuneSimulator(self.army_parser.get_infection_army(), self.army_parser.get_immune_army(), curr_boost)
            boost_simulator.last_standing_after_battle()
            if boost_simulator.did_immune_win():
                self.max_boost = curr_boost
            else:
                self.min_boost = curr_boost
        return boost_simulator.get_total_unit_count()


lineInput = Common.inputAsLines()
parser = ArmyParser(lineInput)
simulator = ImmuneSimulator(parser.get_infection_army(), parser.get_immune_army())

print(simulator.last_standing_after_battle())

boosted_simulator = BoostedImmuneSimulator(parser)
print(boosted_simulator.get_units_at_min_boost_to_win())
