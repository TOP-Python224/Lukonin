class Tetrahedron:
    """Описывает правильный тетраэдр ."""
    def __init__(self, edge: int | float):
        self.edge = edge

    def area(self) -> int | float:
        return round((self.edge**2 * 3**0.5), 2)

    def volume(self) -> int | float:
        return round((self.edge**3 * 2**0.5)/12, 2)


th1 = Tetrahedron(5)
area_1 = th1.area()
volume_1 = th1.volume()
print(f'{area_1 = }')
print(f'{volume_1 = }')
