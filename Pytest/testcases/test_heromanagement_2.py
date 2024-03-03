import pytest

import get_data_1
from HeroManagement import HeroManagement
from get_data2 import get_hero_name_success, get_hero_volume_success, get_hero_power_success, get_hero_name_falied, \
    get_hero_volume_falied, get_hero_power_falied, get_hero_volume_success_add



class TestHeroManagement_2:
    def setup_class(self):
        self.manage = HeroManagement()

    # 有效等价类
    @pytest.mark.Effective
    @pytest.mark.parametrize('name', get_hero_name_success())
    @pytest.mark.parametrize('volume', get_hero_volume_success())
    @pytest.mark.parametrize('power', get_hero_power_success())
    def test_add_hero_success(self, name, volume, power):
        print(f"hero: {name}, volume: {volume}, power: {power}")
        # 执行增加英雄方法前,列表应为空,获取当前列表长度
        pre = len(self.manage.hero_list)
        # 根据测试数据执行,增加成功,self.manage.hero_list列表长度应+1;增加失败,self.manage.hero_list长度不变
        if self.manage.create_hero(name, volume, power):
            pre += 1
        # 断言:增加成功,self.manage.hero_list列表长度应+1;增加失败,self.manage.hero_list长度不变
        assert len(self.manage.hero_list) == pre


    # 无效等价类
    @pytest.mark.invalid
    @pytest.mark.parametrize('name', get_hero_name_falied())
    @pytest.mark.parametrize('volume', get_hero_volume_falied())
    @pytest.mark.parametrize('power', get_hero_power_falied())
    def test_add_hero_failed(self, name, volume, power):
        print(f"hero: {name}, volume: {volume}, power: {power}")
        # 执行增加英雄方法前,列表应为空,获取当前列表长度
        pre = len(self.manage.hero_list)
        # 根据测试数据执行,增加成功,self.manage.hero_list列表长度应+1;增加失败,self.manage.hero_list长度不变
        if self.manage.create_hero(name, volume, power):
            pre += 1
        # 断言:增加成功,self.manage.hero_list列表长度应+1;增加失败,self.manage.hero_list长度不变
        assert len(self.manage.hero_list) == pre


    # 不改变测试数据,修改获取数据的方法,一下两个是重新获取测试数据后的测试案例执行
    @pytest.mark.parametrize('name', get_hero_name_success())
    @pytest.mark.parametrize('volume', get_hero_volume_success_add())
    @pytest.mark.parametrize('power', get_hero_power_success())
    def test_add_hero_success2(self, name, volume, power):
        print(f"hero: {name}, volume: {volume}, power: {power}")
        # 执行增加英雄方法前,列表应为空,获取当前列表长度
        pre = len(self.manage.hero_list)
        # 根据测试数据执行,增加成功,self.manage.hero_list列表长度应+1;增加失败,self.manage.hero_list长度不变
        if self.manage.create_hero(name, volume, power):
            pre += 1
        # 断言:增加成功,self.manage.hero_list列表长度应+1;增加失败,self.manage.hero_list长度不变
        assert len(self.manage.hero_list) == pre

    @pytest.mark.parametrize('name', get_hero_name_falied())
    @pytest.mark.parametrize('volume', get_hero_volume_falied())
    @pytest.mark.parametrize('power', get_hero_power_falied())
    def test_add_hero_failed2(self, name, volume, power):
        print(f"hero: {name}, volume: {volume}, power: {power}")
        # 执行增加英雄方法前,列表应为空,获取当前列表长度
        pre = len(self.manage.hero_list)
        # 根据测试数据执行,增加成功,self.manage.hero_list列表长度应+1;增加失败,self.manage.hero_list长度不变
        if self.manage.create_hero(name, volume, power):
            pre += 1
        # 断言:增加成功,self.manage.hero_list列表长度应+1;增加失败,self.manage.hero_list长度不变
        assert len(self.manage.hero_list) == pre
