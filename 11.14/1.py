class Person:
    """Описывает человека."""

    def __init__(self,
                 surname: str,
                 name: str,
                 patronymic: str):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic

    def is_educating(self) -> bool:
        return isinstance(self, Student)

    def is_employed(self) -> bool:
        return isinstance(self, Employee)

    def __str__(self):
        return f"{self.surname} {self.name} {self.patronymic}"


class Employee(Person):
    """Описывает работающего человека."""

    def __init__(self,
                 surname: str,
                 name: str,
                 patronymic: str,
                 company: str,
                 salary: int):
        super().__init__(surname, name, patronymic)
        self.company = company
        self.salary = salary


class Student(Person):
    """Описывает студента."""

    def __init__(self,
                 surname: str,
                 name: str,
                 patronymic: str,
                 educational_organization: str,
                 commercial: bool = False):
        super().__init__(surname, name, patronymic)
        self.educational_organization = educational_organization
        self.commercial = commercial

    def __str__(self):
        return super().__str__() + \
               f" учится в {self.educational_organization}" \
               f" на {'коммерческой' if self.commercial else 'бюджетной'} основе."

    def __str__(self):
        return super().__str__() + \
               f"работает в {self.company} " \
               f"с зарплатой {self.salary} рублей."
