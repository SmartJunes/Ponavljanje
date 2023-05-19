
se1 = ["sowtware engineer", "Max", "20", "Junior", 5000]
se2 = ["sowtware engineer", "Lisa", "24", "Senior", 7000]
di = ["designer","Filip"]



def codea(a):
    print(f"{a[1]} is writing code.  .." )



class SofwareEngineer():
    #class atributes
    alias = "Kyboard"

    def __init__ (self, name, age, level, salary):
        #  instance atributes
        self.name = name
        self.age = age
        self.level = level
        self.salary = salary

    def code(self):
        print(f"{self.name} is writing code......" )

    def code_in_lenguage(self, language):
        print(f"{self.name} is writeing code in {language}..." )

    #def informations(self):
        #informations = f"name={self.name}, age={self.age}, level={self.level}"
        #return informations

    #dunder method -- special method
    def __str__(self) -> str:
        informations = f"name={self.name}, age={self.age}, level={self.level}"
        return informations

    def __eq__(self, other) -> bool:
        return self.name == other.name and self.age == other.age

    #sa dekoratorom mozemo ispritntati instancu bez self param ali nemamo pristup atributima instance
    @staticmethod
    def entry_salary(age):
            if age < 25:
                 return 5999
            if age < 30:
                 return 6999
            return 90000




se1 = SofwareEngineer("Marin",33,"junior",300)
se2 = SofwareEngineer("Lisa",33,"junior",300)
se3 = SofwareEngineer("Lisa",33,"junior",300)


#se1.code()
#se2.code()

#se1.code_in_lenguage("python")
#print(se1.informations())
#print(se1.name)

#print(se2 == se3)

print(se1.entry_salary(24))
print(SofwareEngineer.entry_salary(27))