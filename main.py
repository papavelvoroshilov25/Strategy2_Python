from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

class Context():
    """Контекст определяет интерфейс, представляющий интерес для клиента"""

    def __init__(self, strategy: Strategy) -> None:

        """Обычно контекст принимает стратегию через конструктор, а также предоставляет
        сеттер для ее изменения во время выполнения"""

        self._strategy = strategy
    @property
    def strategy(self) -> Strategy:

        """Контекст хранит ссылку на один из объектов Стратегии. Контекст не знает конкретного класса
        стратегии. Он должен работать со всеми стратегиями через интерфейс Стратегии."""

        return self._strategy

    @strategy.setter

    def strategy(self, stratedy: Strategy) -> None:

        """Обычно Контекст позволяет заменить объект стратегии во время выполнения."""

        self._strategy = stratedy

    def do_some_business_logic(self) -> None:

        """Вместо того, чтобы самостоятельно реализовать множественные версии алгоритма, 
        Контекст делегирует некоторую работу объекта Стратегии"""

        print("Context: Sorting data using the strategy (not sure how it'll do it)")
        result = self._strategy.do_algorithm(["a", "b", "c", "d", "e"])
        print(",".join(result))

class Strategy(ABC):
    """Интерфейс стратегии обновляет операции, общие для всех поддерживаемых версий некоторого
    алгоритма. Контекст использует этот интерфейс для вызова алгоритма, определенного
    Конкретными Стратегиями"""

    @abstractmethod
    def do_algorithm(self, data:List):
        pass

class ConcreteStrategyA(Strategy):
    def do_algorithm(self, data: List) -> List:
        return sorted(data)

class ConcreteStrategyB(Strategy):
    def do_algorithm(self, data: List) -> List:
        return reversed(sorted(data))

if __name__ == "__main__":
    #Клиентский код выбирает конкретную стратегию и передает ее в контекст.
    #Клиент должен знать о различиях между стратегиями, чтобы сделать
    #правильный выбор

    context = Context(ConcreteStrategyA())
    print("Client: Strategy is set to normal sorting.")
    context.do_some_business_logic()
    print()

    print("Client: Strategy is set to reversed sorting.")
    context.strategy = ConcreteStrategyB()
    context.do_some_business_logic()



