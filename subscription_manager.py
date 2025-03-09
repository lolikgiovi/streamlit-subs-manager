from datetime import datetime
from dateutil.relativedelta import relativedelta

class Application:
    def __init__(self, name, price, due_date):
        self.name = name
        self.price = price
        self.due_date = datetime(datetime.today().year, datetime.today().month, due_date)
        self.start_date = datetime.now()
        self.is_paid = False
        self.is_active = True
        if self.due_date < self.start_date:
            self.due_date += relativedelta(months=1)
        print(f"New Subscription: {self.name} - {self.due_date} - {self.is_active} - {self.is_paid}")

    def due_in(self):
        days_until_due = (self.due_date - datetime.today()).days
        return days_until_due

    def __str__(self):
        return f"{self.name} - {self.price} - {self.due_date} - {self.is_paid}"
    
class SubscriptionManager:
    def __init__(self):
        self.applications = []
    
    def add_application(self, application:Application):
        self.applications.append(application)

    def remove_application(self, application:Application):
        application.is_active = False
        self.applications.remove(application)

    def pay_subscription(self, application:Application):
        application.is_paid = True
        application.due_date += relativedelta(months = 1)
        print(f"Subscription {application.name} has been paid")
    
    def list_applications(self, mode="all"):
        active_applications = []
        for app in self.applications:
            if mode == "all" and app.is_active:
                active_applications.append({
                    'name': app.name,
                    'due_days': app.due_in(),
                    'price': app.price
                })
            elif mode == "unpaid" and app.is_active and not app.is_paid:
                active_applications.append({
                    'name': app.name,
                    'due_days': app.due_in(),
                    'price': app.price
                })
        return active_applications