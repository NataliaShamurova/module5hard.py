import time

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = int(hash(password))
        self.age = age

    def __hash__(self, password):
        return hash(password)

    def __str__(self):
        return f"{self.nickname}"


class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        passw_hash = hash(password)
        for i in self.users:
            if i.nickname == nickname and i.password == passw_hash:
                self.current_user = i
                return self.current_user
            print('Неверный логин или пароль')

    def log_out(self):
        self.current_user = None

    def add(self, *videos):
        for video in videos:
            exists = False
            for v in self.videos:
                if v.title == video.title:
                    exists = True
                    break
            if not exists:
                self.videos.append(video)

    def get_videos(self, word_search: str):
        word_search_lower = word_search.lower()
        video_list = []

        for video in self.videos:
            if word_search_lower in video.title.lower():
                video_list.append(video.title)
        return video_list

    def register(self, nickname: str, password: str, age: int):
        for user in self.users:
            if user.nickname == nickname:
                print(f"Пользователь {nickname} уже существует")
                return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user

    def watch_video(self, title: str):
        if not self.current_user:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return

        for video in self.videos:
            if video.title == title:
                if video.adult_mode and self.current_user.age < 18:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    return

                for second in range(video.time_now, video.duration):
                    print(f"{second + 1} ", end='')
                    video.time_now += 1
                    time.sleep(1)
                print("Конец видео")
                video.time_now = 0
                return

        print("Видео не найдено")

user1 = User('vasya_pupkin', 'lolkekcheburek', 13)
user2 = User('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)

ur = UrTube()
ur.log_in('vasya_pupkin', 'lolkekcheburek')
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
v3 = Video('программа?', 10, adult_mode=True)
# Добавление видео
ur.add(v1, v2, v3)
#
 # Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('?'))
#
# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')
#
# # Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

#
# # Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
#
