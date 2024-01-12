class Human:
    age=0
    def print_age(self,additional_text):
        print(self.age,additional_text)

usr1=Human()
usr2=Human()

usr1.age=20     #method 1
usr2.age=30     #method 2

usr1.print_age("Jamal")
usr2.print_age("Kamal")