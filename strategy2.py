from __future__ import annotations
from abc import ABC, abstractmethod
class Compressor():
    """Контекст определяет интерфейс, представляющий интерес для клиента"""

    def __init__(self, compression: Compression) -> None:

        """Обычно контекст принимает стратегию через конструктор, а также предоставляет
        сеттер для ее изменения во время выполнения"""


        self.p = compression

    @property
    def compression(self) -> Compression:

        """Контекст хранит ссылку на один из объектов Стратегии. Контекст не знает конкретного класса
        стратегии. Он должен работать со всеми стратегиями через интерфейс Стратегии."""

        return self.p

    @compression.setter

    def compression(self, compression: Compression) -> None:

        """Обычно Контекст позволяет заменить объект стратегии во время выполнения."""

        self.p = compression

    def compress(self) -> None:

        self.p.compress()

        """Вместо того, чтобы самостоятельно реализовать множественные версии алгоритма,
        Контекст делегирует некоторую работу объекта Стратегии"""

class Compression(ABC):
    """Интерфейс стратегии обновляет операции, общие для всех поддерживаемых версий некоторого
    алгоритма. Контекст использует этот интерфейс для вызова алгоритма, определенного
    Конкретными Стратегиями"""

    @abstractmethod
    def compress(self):
        pass

class ARJ_Compressor(Compression):
    def compress(self) -> None:
        print("Client: ARJ_Compression")

class RAR_Compressor(Compression):
    def compress(self) -> None:
        print("Client: RAR_Compression")

class ZIP_Compressor(Compression):
    def compress(self) -> None:
        print("Client: ZIP_Compression")




if __name__ == "__main__":
    compressor = Compressor(RAR_Compressor())
    compressor.compress()
    print()
    compressor.compression = ZIP_Compressor()
    compressor.compress()
