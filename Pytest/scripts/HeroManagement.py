"""
英雄管理系统的主要功能为增删查改，用户通过输入不同的信息，选择不同的操作。
增加英雄：输入英雄姓名、血量、和攻击力，名称为字符串，血量、攻击力为正整数，其中血量的最大值为 99，最小值为 1。
删除英雄：输入英雄姓名，如果删除成功，返回英雄列表，如果英雄不存在返回 False。
修改英雄血量：输入英雄姓名、血量，如果更新成功，返回更新后的英雄信息，如果英雄不存在或更新失败返回 False。
查找英雄：输入英雄信息，在英雄列表中存在则返回成功，不存在则返回失败。
"""


class HeroManagement:
    def __init__(self):
        self.hero_list = []

    def update_hero(self, hero_name, hero_volume):

        for i in self.hero_list:
            if i.get("name") == hero_name:
                i["volume"] = hero_volume
                return i
        return False

    def delete_hero(self, hero_name):
        """
        :param hero_list:  英雄列表信息
        :param hero_name:  英雄的名字
        :return:
        """
        for i in self.hero_list:
            if hero_name == i["name"]:
                self.hero_list.remove(i)
                return self.hero_list
        return False

    def create_hero(self, hero_name, hero_volume, hero_power):
        if hero_volume <= 0 or hero_volume >= 100:
            return False
        if hero_power <= 0:
            return False
        if type(hero_name) != str:
            return False
        if type(hero_volume) != int:
            return False
        hero_info = {"name": hero_name, "volume": hero_volume, "power": hero_power}
        self.hero_list.append(hero_info)
        return True

    def find_hero(self, res):
        """
        如果查询到英雄，则返回英雄信息。
        如果没有查询到英雄，则返回False
        :param res:
        :return:
        """
        # 遍历所有的英雄信息，
        for i in self.hero_list:
            if res == i["name"]:
                return i
        return False
