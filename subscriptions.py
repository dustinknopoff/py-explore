import argparse
import json
from typing import List, Dict, Any

# Example Output
#     Subscription            Cost             Frequency      
# ============================================================
#         Bear               $15.99                1          
#        Sketch              $50.00                1          
# ============================================================
#        Total:              $65.99            (per year)     


Frequency: Dict[str, int] = {
    'DAILY': 365,
    'WEEKLY': 52,
    'MONTHLY': 12,
    'YEARLY': 1
}


class Subscription:
    def __init__(self, title: str, cost: float, frequency: int):
        self.title: str = title
        self.cost: float = cost
        self.frequency: int = frequency

    def as_dict(self) -> Dict[str, Any]:
        """
        Converts subscription to a Dict.
        :return: Dict representing this subscription.
        """
        return {
            'title': self.title,
            'cost': self.cost,
            'frequency': self.frequency
        }


class Subscriptions:
    def __init__(self):
        self.subscriptions: List[Subscription] = self.__load()
        self.total = 0

    @staticmethod
    def __load():
        """
        Read in saved JSON and convert to Subscriptions.
        :return: List of Subscriptions.
        """
        out = []
        try:
            with open('./subscriptions.json', 'r') as f:
                result = json.loads(f.read())
                for sub in result['subscriptions']:
                    d = Subscription(sub['title'], sub['cost'], sub['frequency'])
                    self.total += d.cost * d.frequency
                    out.append(d)
        except FileNotFoundError:
            pass
        return out

    def __str__(self):
        """
        String representation of Subscriptions.
        :return: formatted string. Such that:
        Subscription, Cost, Frequency
        =============================
        """
        result = ""
        result += "{:^20}{:^20}{:^20}\n".format(
            "Subscription", "Cost", "Frequency")
        result += "=" * 60 + '\n'
        total = 0
        for sub in self.subscriptions:
            total += (sub.cost * sub.frequency)
            result += '{:^20}{:^20}{:^20}\n'.format(
                sub.title, "$" + format(sub.cost, '.2f'), sub.frequency)
        result += "=" * 60 + '\n'
        result += "{:^20}{:^20}{:^20}".format("Total:",
                                              "$" + format(total, '.2f'), "(per year)")
        return result

    def add_subscription(self, title, cost, frequency):
        """
        Converts parameters into a Subscription.
        :param title: name of a subscribed service.
        :param cost: price per given frequency.
        :param frequency: YEARLY, MONTHLY, WEEKLY, or DAILY
        """
        sub = Subscription(title, cost, frequency)
        self.subscriptions.append(sub)

    def remove_subscriptions(self, title):
        """
        Search for a given title and remove it.
        :param title: Name of a subscription.
        """
        num = None
        for index, sub in enumerate(self.subscriptions):
            if title in sub.title:
                num = index
                break
        if num is not None:
            self.subscriptions.pop(num)

    def save(self):
        """
        Write changes to disk.
        """
        result = {
            "subscriptions": []
        }
        for sub in self.subscriptions:
            result["subscriptions"].append(sub.as_dict())
        with open('../subscriptions.json', 'w+', encoding='utf8') as f:
            json.dump(result, f, indent=4)


if __name__ == '__main__':
    subscriptions = Subscriptions()

    argsparsed = argparse.ArgumentParser(
        description='A quick, easy subscription tracker for the terminal.')
    argsparsed.add_argument(
        '-a', '--add', help='Add a subscription.', action='store_true')
    argsparsed.add_argument(
        '-d', '--delete', help='Deletes a subscription', action='store_true')
    argsparsed.add_argument(
        '-p', '--print', help='Prints all subscriptions.', action='store_true')
    args = argsparsed.parse_args()

    if args.add:
        title = input("Title: ")
        cost = input("Cost: ")
        print("Enter one of: YEARLY, MONTHLY, DAILY, WEEKLY")
        frequency = input("Frequency: ")
        print(Frequency[frequency])
        subscriptions.add_subscription(
            title, float(cost), int(Frequency[frequency]))
        print(subscriptions)
        subscriptions.save()
    elif args.delete:
        title = input("Title: ")
        subscriptions.remove_subscriptions(title)
        print(subscriptions)
        subscriptions.save()
    elif args.print:
        print(subscriptions)
    else:
        print("Please enter a valid argument.")
    subscriptions.save()

#     Usage:
# usage: subscriptions.py [-h] [-a] [-d] [-p]

# A quick, easy subscription tracker for the terminal.

# optional arguments:
#   -h, --help    show this help message and exit
#   -a, --add     Add a subscription.
#   -d, --delete  Deletes a subscription
#   -p, --print   Prints all subscriptions.
