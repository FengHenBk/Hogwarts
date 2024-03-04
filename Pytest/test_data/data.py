import yaml

with open('D:\code\pythonProject\pythonProject\Hogwarts\Pytest\\test_data\\test_hero.yaml', 'r', encoding="utf8") as file:
    data = yaml.safe_load(file)
print(data)
print(type("123"))
