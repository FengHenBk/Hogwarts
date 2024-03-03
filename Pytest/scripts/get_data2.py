import yaml

file_url = 'D:\code\pythonProject\pythonProject\Hogwarts\Pytest\\test_data\\test_hero_data.yaml'


def get_hero_name_success():
    """
    获取测试数据
    :return: 正例-英雄姓名
    """
    with open(file_url, mode="r",
              encoding="utf-8") as f:
        data = yaml.safe_load(f)
        return data["create_hero"]["hero_name"]["success"]


def get_hero_name_falied():
    """
    获取测试数据
    :return: 反例-英雄姓名
    """
    with open(file_url, mode="r",
              encoding="utf-8") as f:
        data = yaml.safe_load(f)
        return data["create_hero"]["hero_name"]["falied"]


# print(get_hero_name_falied())

def get_hero_volume_success():
    with open(file_url, mode="r",
              encoding="utf-8") as f:
        data = yaml.safe_load(f)
        return data["create_hero"]["hero_volume"]["success"]


# print(get_hero_volume_success())

def get_hero_volume_falied():
    with open(file_url, mode="r",
              encoding="utf-8") as f:
        data = yaml.safe_load(f)
        return data["create_hero"]["hero_volume"]["falied"]


# print(get_hero_volume_falied())

def get_hero_power_success():
    with open(file_url, mode="r",
              encoding="utf-8") as f:
        data = yaml.safe_load(f)
        return data["create_hero"]["hero_power"]["success"]


# print(get_hero_volume_success())

def get_hero_power_falied():
    with open(file_url, mode="r",
              encoding="utf-8") as f:
        data = yaml.safe_load(f)
        return data["create_hero"]["hero_power"]["falied"]


# print(get_hero_volume_falied())


def get_hero_volume_success_add():
    """
    测试数据不变，边界值+1
    :return:
    """
    with open(file_url, mode="r",
              encoding="utf-8") as f:
        data = yaml.safe_load(f)
        return [volume + 1 for volume in data["create_hero"]["hero_volume"]["success"]]


# print(get_hero_volume_success_add())

