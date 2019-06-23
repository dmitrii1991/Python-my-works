import requests
import time, datetime

ACCESS_TOKEN = ""

class Id_user:


    def __init__(self, token: str, name: str):
        self.token = token
        self.name = str(name)
        self.fields = 'domain'  # запрашиваемые поля в методах/required fields
        self.params = {
            # 'user_id': None,
            'access_token': self.token,
            'v': '5.92',
            'fields': self.fields
        }

        try:  # проверка на данные ID/ check for ID data
            if self.name.isdigit():
                self.params['user_id'] = self.name
            elif self.name[0:1] == 'id' and self.name[2:].isdigit():
                self.params['user_id'] = self.name[2:]
            else:
                self.params['user_ids'] = self.name
                response = requests.get('https://api.vk.com/method/users.get', self.params)
                data_user = response.json()
                self.params['user_id'] = data_user['response'][0]['id']
                del self.params['user_ids']
        except KeyError:
            print('ERROR in NAME user / work with owner of token')


    def __str__(self):
        return 'https://vk.com/id' + str(self.params['user_id'])


    def friends_birthday(self):  # данные пользователя
        ''' Displays a list of friends with  dates (birthday) and dates to the nearest birthday '''

        try:
            now = datetime.datetime.now()  # сегодняшняя дата/today
            self.params['fields'] = 'lists'
            response = requests.get('https://api.vk.com/method/friends.get', self.params)
            data_friends = response.json()  # получаем список друзей/ get list of friends

            # Выдергиваем дату рождения из друзей попутно отсеевая удаленных/sort the friends list and remove deleted friends
            self.params['fields'] = 'bdate'  

            for friend in data_friends['response']['items']:
                self.params['user_ids'] = friend['id']  
                response = requests.get('https://api.vk.com/method/users.get', self.params)
                data = response.json()
                birthday = data.get('response')[0].setdefault('bdate', "скрыто")  # получаем ДР друга

                if birthday != "скрыто":
                    day, month, *args = birthday.split('.')

                    if int(month) > now.month or (int(month) == now.month and int(day) > now.day): 
                        next_birthday = datetime.datetime(2019, int(month), int(day))
                    else:
                        next_birthday = datetime.datetime(2020, int(month), int(day))

                if friend['last_name']:
                    delta_days = next_birthday - now
                    num_dayth_for, *args = str(delta_days).split(',')
                    if birthday == 'скрыто':
                        num_dayth_for = 'неизвестен'
                    print("{:^10}|{:^10}|{:^12}|{:8}".format(friend['first_name'], friend['last_name'], birthday, num_dayth_for))
                time.sleep(0.35)

        except KeyError:
            print('ERROR in ID user')

if __name__ == "__main__":
    try:
        Dima = Id_user(ACCESS_TOKEN, "")
        Dima.friends_birthday()
    except NameError as name:
        print(f"{name}| enter string!")
