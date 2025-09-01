class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        key_index = {"type": 0, "color": 1, "name": 2}[ruleKey]
        return sum(1 for item in items if item[key_index] == ruleValue)

        