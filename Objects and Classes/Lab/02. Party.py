class Party:

    def __init__(self, people=[]):
        self.people = people

    def Task(self):
        counter = 0
        while True:
            names = input()

            if names == "End":
                break

            self.people.append(names)

            counter += 1
        
        final = ", ".join(self.people)

        return f"Going: {final} \nTotal: {counter}"

Final = Party()

print(Final.Task())
