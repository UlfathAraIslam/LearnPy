class EmailNotification:
    def __init__(self, recipient, message):
        self.recipient = recipient
        self.message = message

    def send(self):
        print(f"[EMAIL] To {self.recipient}: {self.message}")


class SMSNotification:
    def __init__(self, recipient, message):
        self.recipient = recipient
        self.message = message

    def send(self):
        print(f"[SMS] To {self.recipient}: {self.message}")


class PushNotification:
    def __init__(self, recipient, message):
        self.recipient = recipient
        self.message = message

    def send(self):
        print(f"[PUSH] To {self.recipient}: {self.message}")


def main():
    notifications = []

    while True:
        n_type = input("Notification type (email/sms/push, or 'done' to finish): ")
        if n_type == "done":
            break

        recipient = input("Recipient: ")
        message = input("Message: ")

        if n_type == "email":
            notifications.append(EmailNotification(recipient, message))
        elif n_type == "sms":
            notifications.append(SMSNotification(recipient, message))
        elif n_type == "push":
            notifications.append(PushNotification(recipient, message))
        else:
            print("Unknown notification type, skipping.")
            continue

    for n in notifications:
        n.send()


if __name__ == "__main__":
    main()