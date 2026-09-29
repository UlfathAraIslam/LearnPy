class Rider:
    def __init__(self, name, deliveries=0):
        self.name = name
        self.deliveries = deliveries

    def pay(self):
        return self.deliveries * 100   # ফ্ল্যাট রেট প্লেসহোল্ডার


class BicycleRider(Rider):
    def pay(self):
        return self.deliveries * 100   # প্রতি ডেলিভারিতে ¥১০০


class MotorbikeRider(Rider):
    def __init__(self, name, deliveries=0, fuel_cost=30):
        super().__init__(name, deliveries)
        self.fuel_cost = fuel_cost

    def pay(self):
        gross = self.deliveries * 150   # প্রতি ডেলিভারিতে ¥১৫০, বেশি রেট
        return gross - (self.deliveries * self.fuel_cost)


def main():
    riders = []

    while True:
        rider_type = input("Rider type (bike/moto, or 'done' to finish): ")
        if rider_type == "done":
            break

        name = input("Rider name: ")
        deliveries = int(input("Deliveries completed: "))

        if rider_type == "bike":
            riders.append(BicycleRider(name, deliveries))
        elif rider_type == "moto":
            riders.append(MotorbikeRider(name, deliveries))
        else:
            print("Unknown rider type, skipping.")
            continue

    for r in riders:
        print(f"{r.name} earned ¥{r.pay()}")


if __name__ == "__main__":
    main()