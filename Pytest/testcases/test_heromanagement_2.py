import pytest

import get_data_1
from HeroManagement import HeroManagement
from get_data2 import get_hero_name_success, get_hero_volume_success, get_hero_power_success, get_hero_name_falied, \
    get_hero_volume_falied, get_hero_power_falied, get_hero_volume_success_add


def get_hero_name_failed():
    pass


def get_hero_volume_failed():
    pass


def get_hero_power_failed():
    pass


class TestHeroManagement_2:
    def setup_class(self):
        self.hero = HeroManagement()

    # 有效等价类
    @pytest.mark.Effective
    @pytest.mark.parametrize('name', get_hero_name_success())
    @pytest.mark.parametrize('volume', get_hero_volume_success())
    @pytest.mark.parametrize('power', get_hero_power_success())
    def test_add_hero_success(self, name, volume, power):
        print(f"hero: {name}, volume: {volume}, power: {power}")
        assert self.hero.create_hero(name, volume, power)
        
    # 无效等价类
    @pytest.mark.invalid
    @pytest.mark.parametrize('name', get_hero_name_falied())
    @pytest.mark.parametrize('volume', get_hero_volume_falied())
    @pytest.mark.parametrize('power', get_hero_power_falied())
    def test_add_hero_failed(self, name, volume, power):
        print(f"hero: {name}, volume: {volume}, power: {power}")
        assert self.hero.create_hero(name, volume, power)

    # 不改变测试数据,修改获取数据的方法,一下两个是重新获取测试数据后的测试案例执行
    @pytest.mark.parametrize('name', get_hero_name_success())
    @pytest.mark.parametrize('volume', get_hero_volume_success_add())
    @pytest.mark.parametrize('power', get_hero_power_success())
    def test_add_hero_success2(self, name, volume, power):
        print(f"hero: {name}, volume: {volume}, power: {power}")
        assert self.hero.create_hero(name, volume, power)

    @pytest.mark.parametrize('name', get_hero_name_falied())
    @pytest.mark.parametrize('volume', get_hero_volume_falied())
    @pytest.mark.parametrize('power', get_hero_power_falied())
    def test_add_hero_failed2(self, name, volume, power):
        print(f"hero: {name}, volume: {volume}, power: {power}")
        assert self.hero.create_hero(name, volume, power)