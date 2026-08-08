from project.waiters.base_waiter import BaseWaiter


class HalfTimeWaiter(BaseWaiter):
    HOURLY_RATE = 12.0

    def report_shift(self):
        return f"{self.name} worked a half-time shift of {self.hours_worked} hours."