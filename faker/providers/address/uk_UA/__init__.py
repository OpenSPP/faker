# coding=utf-8
from __future__ import unicode_literals

from .. import Provider as AddressProvider


class Provider(AddressProvider):
    address_formats = ['{{street_address}}, {{city}}, {{postcode}}']
    building_number_formats = ['#', '##', '###']
    city_formats = ['{{city_prefix}} {{first_name}}']
    street_address_formats = ['{{street_name}}, {{building_number}}']
    street_name_formats = ('{{street_prefix}} {{street_title}}', )

    city_prefixes = ['місто', 'село', 'селище', 'хутір']
    countries = [
        'Австралія', 'Австрія', 'Азербайджан', 'Албанія', 'Алжир', 'Ангола',
        'Андорра', 'Антигуа і Барбуда', 'Аргентина', 'Афганістан',
        'Багамські Острови', 'Бангладеш', 'Барбадос', 'Бахрейн', 'Беліз',
        'Бельгія', 'Бенін', 'Білорусь', 'Болгарія', 'Болівія',
        'Боснія і Герцеговина', 'Ботсвана', 'Бразилія', 'Бруней',
        'Буркіна-Фасо', 'Бурунді', 'Бутан', 'Вануату', 'Ватикан',
        'Велика Британія', 'Венесуела', 'В\'єтнам', 'Вірменія', 'Габон',
        'Гаїті', 'Гаяна', 'Гамбія', 'Гана', 'Гватемала', 'Гвінея',
        'Гвінея-Бісау', 'Гондурас', 'Гренада', 'Греція', 'Грузія', 'Данія',
        'Джибуті', 'Домініка', 'Домініканська Республіка', 'Еквадор',
        'Екваторіальна Гвінея', 'Еритрея', 'Естонія', 'Ефіопія', 'Єгипет',
        'Ємен', 'Замбія', 'Західна Сахара', 'Зімбабве', 'Ізраїль', 'Індія',
        'Індонезія', 'Ірак', 'Іран', 'Ірландія', 'Ісландія', 'Іспанія',
        'Італія', 'Йорданія', 'Кабо-Верде', 'Казахстан', 'Камбоджа', 'Камерун',
        'Канада', 'Катар', 'Кенія', 'Киргизстан', 'КНР', 'Кіпр', 'Кірибаті',
        'Колумбія', 'Коморські Острови', 'Конго', 'ДР Конго', 'Південна Корея',
        'Північна Корея', 'Косово', 'Коста-Рика', 'Кот-д\'Івуар', 'Куба',
        'Кувейт', 'Лаос', 'Латвія', 'Лесото', 'Литва', 'Ліберія', 'Ліван',
        'Лівія', 'Ліхтенштейн', 'Люксембург', 'Маврикій', 'Мавританія',
        'Мадагаскар', 'Республіка Македонія', 'Малаві', 'Малайзія', 'Малі',
        'Мальдіви', 'Мальта', 'Марокко', 'Маршаллові Острови', 'Мексика',
        'Федеративні Штати Мікронезії', 'Мозамбік', 'Молдова', 'Монако',
        'Монголія', 'М\'янма', 'Намібія', 'Науру', 'Непал', 'Нігер', 'Нігерія',
        'Нідерланди', 'Нікарагуа', 'Німеччина', 'Нова Зеландія', 'Норвегія',
        'ОАЕ', 'Оман', 'Пакистан', 'Палау', 'Палестинська держава', 'Панама',
        'Папуа Нова Гвінея', 'ПАР', 'Парагвай', 'Перу', 'Південний Судан',
        'Польща', 'Португалія', 'Росія', 'Руанда', 'Румунія', 'Сальвадор',
        'Самоа', 'Сан-Марино', 'Сан-Томе і Принсіпі', 'Саудівська Аравія',
        'Свазіленд', 'Сейшельські Острови', 'Сенегал',
        'Сент-Вінсент і Гренадини', 'Сент-Кіттс і Невіс', 'Сент-Люсія',
        'Сербія', 'Сінгапур', 'Сирія', 'Словаччина', 'Словенія',
        'Соломонові Острови', 'Сомалі', 'Судан', 'Суринам', 'Східний Тимор',
        'США', 'Сьєрра-Леоне', 'Таджикистан', 'Таїланд', 'Тайвань', 'Танзанія',
        'Того', 'Тонга', 'Тринідад і Тобаго', 'Тувалу', 'Туніс', 'Туреччина',
        'Туркменістан', 'Уганда', 'Угорщина', 'Узбекистан', 'Україна',
        'Уругвай', 'Фіджі', 'Філіппіни', 'Фінляндія', 'Франція', 'Хорватія',
        'Центральноафриканська Республіка', 'Чад', 'Чехія', 'Чилі',
        'Чорногорія', 'Швейцарія', 'Швеція', 'Шрі-Ланка', 'Ямайка', 'Японія'
    ]
    street_prefixes = [
        'вулиця', 'набережна'
    ]
    street_suffixes = ['узвіз']

    street_titles = [
        '40-летия Октября',
        'Академика Шлихтера',
        'Алексея Давыдова',
        'Анищенко',
        'Антонова-Овсеенко',
        'Артема',
        'Бабушкина',
        'Бакинских Комиссаров',
        'Баумана',
        'Блюхера',
        'Боженко',
        'Бонч-Бруевича',
        'Буденного',
        'Ветрова',
        'Воровского',
        'Воссоединения',
        'Гамарника',
        'Горького',
        'Дзержинского',
        'Димитрова',
        'Дубового Ивана',
        'Дундича Олеко',
        'Жданова',
        'Ивана Клименко',
        'Ивана Лепсе',
        'Иванова Андрея',
        'Ильича',
        'Калининская',
        'Киквидзе',
        'Кирова',
        'Коллективизации',
        'Коллонтай',
        'Командарма Уборевич',
        'Комиссара Рыкова',
        'Коммунистическая',
        'Комсомольская',
        'Котовского',
        'Кравченко Николая',
        'Красикова Петра',
        'Красноармейская',
        'Красногвардейская',
        'Краснопартизанская',
        'Краснофлотская',
        'Крупской',
        'Крыленко',
        'Кутузова',
        'Лазо Сергея',
        'Лайоша Гавро',
        'Ластовского',
        'Ленина',
        'Ленинская',
        'Луначарского',
        'Майорова Михаила',
        'Маршала Буденного',
        'Маршала Тухачевского',
        'Мате Залки',
        'Машина Михаила',
        'Мильчакова Александра',
        'Михаила Скрипника',
        'Московская',
        'Октябрьская',
        'Омельяна Горбачова',
        'Островского Николая',
        'Павла Дибенко',
        'Павлика Морозова',
        'Патриса Лумумбы',
        'Перспективная',
        'Петра Дегтяренко',
        'Петра Шелеста',
        'Петровского',
        'Пика Вильгельма',
        'Полупанова',
        'Примакова',
        'Профинтерна',
        'Руднева Николая',
        'Сагайдика Степана',
        'Сарафимовича',
        'Сергея Струтинского',
        'Смирнова-Ласточкина',
        'Советская',
        'Софьи Перовской',
        'Строкача Тимофея',
        'Суворова',
        'Терешковой Валентины',
        'Трутенко Онуфрия',
        'Фадеева',
        'Федько Ивана',
        'Фрунзе',
        'Фурманова',
        'Цурюпинская',
        'Чапаева',
        'Чекистов',
        'Чеслава Белинского',
        'Чудновского',
        'Шаумяна',
        'Щербакова',
        'Щорса',
        'Юрия Коцюбинского',
        'Якира'
    ]

    def city_prefix(self):
        return self.random_element(self.city_prefixes)

    def postcode(self):
        """The code consists of five digits (01000-99999)"""
        return '{}{}'.format(
            self.generator.random.randint(
                0, 10), self.generator.random.randint(
                1000, 10000))

    def street_prefix(self):
        return self.random_element(self.street_prefixes)

    def street_title(self):
        return self.random_element(self.street_titles)
