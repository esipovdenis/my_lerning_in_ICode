
# Создайте класс User, с атрибутами name, email, my_wish и методом introduce(),
# который печатает: "Привет, я Адам, моя почта adam@gmail.com и у меня есть мечта "

class User():
    """описание пользователя"""
    def __init__(self, name, email, my_wish):
        """свойства пользователя"""
        self.name = name
        self.email = email
        self.my_wish = my_wish
        self.age = 0

    def introduce(self):
        """представление"""
        print(f"Привет, я {self.name}, моя почта {self. email} и у меня есть мечта {self.my_wish }")

    """возраст пользователя"""
    def age_of_user(self,year):
        self.age += year

user = User("Denis", "esipovdenis@bk.ru", "стать программистом")
user.introduce()

user2 = User('Albert', 'molbert@mail.ru', 'стать художником')
user2.introduce()

print(user.name)
print(user2.email)

user.introduce()

user.age_of_user(39)
print(user.age)

class AdminUser(User):
    """суб класс пользователя"""
    def __init__(self,name, email,my_wish, permissions):
        super().__init__(name,email,my_wish)
        self.permissions = permissions

    def introduce(self):
        """представление"""
        print(f"Привет, я {self.name}, моя почта {self. email} и у меня есть мечта: {self.my_wish } и у меня есть разрешения: {self.permissions}")
adminUser = AdminUser('Володя', 'admin@gmail.com', 'сделать мир лучше', 'на все')
adminUser.introduce()

