from project.waiters.base_waiter import BaseWaiter


class FullTimeWaiter(BaseWaiter):
    HOURLY_RATE = 15.0


    def report_shift(self):
        return f"{self.name} worked a full-time shift of {self.hours_worked} hours."

