import unittest
from unittest.mock import AsyncMock
from fc_server import Operator, DroneStatusNotifier


class TestObserverPattern(unittest.TestCase):

    def setUp(self):
        self.websocket = AsyncMock()
        self.operator = Operator(self.websocket)
        self.notifier = DroneStatusNotifier()

    async def test_observer_receives_update(self):
        self.notifier.add_observer(self.operator)
        await self.notifier.notify_observers("Drone1 is connected")
        self.websocket.send.assert_called_with("Drone1 is connected")


if __name__ == '__main__':
    unittest.main()
