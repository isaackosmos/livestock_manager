# Livestock Manager
This project was developed with the purpose of completing the Object-Oriented Programming course in Python, as part of my studies in Big Data in Agribusiness at university.

This project aims to develop a cattle management system. It allows the separation of cattle into cows and bulls, tracking their age, breed, and, for cows, managing their milk production. Additionally, it tracks when each animal was added to the herd.

Classes diagram:
```mermaid
classDiagram
    class EarTag {
        -int __number
        -str __color
        +int number
        +str color
        +str __str__()
    }

    class MilkQualityControl {
        -float __score
        -float __fat_percentage
        -float __vitamins_percentage
        +float score
        +void score(float)
        +float fat_percentage
        +void fat_percentage(float)
        +float vitamins_percentage
        +void vitamins_percentage(float)
        +str __str__()
    }

    class MilkProduction {
        -datetime __date
        -float __liters
        -MilkQualityControl __milk_quality_control
        +datetime date
        +float liters
        +void liters(float)
        +MilkQualityControl milk_quality_control
        +MilkQualityControl get_milk_quality_control()
        +void update_milk_quality_control(float, float, float)
        +void delete_milk_quality_control()
        +str __str__()
    }

    class Breed {
    }

    class Bovine {
        -EarTag __ear_tag
        -datetime __birth
        -float __weight
        -Breed __breed
        +EarTag ear_tag
        +int age
        +Breed breed
        +float weight
        +void weight(float)
        +str __str__()
    }

    class Bull {
        +str __str__()
    }

    class Cow {
        +void add_milk_production(datetime, float, float, float, float)
        +MilkProduction get_milk_production(datetime)
        +void update_milk_production(datetime, float, float, float, float)
        +void delete_milk_production(datetime)
        +str __str__()
    }

    class Herd {
        -list~dict~ __cattle
        +list~dict~ cattle
        +void add_cattle(Bovine)
        +Bovine get_cattle(int)
        +void update_cattle(int, Bovine)
        +void delete_cattle(int)
        +str __str__()
    }

    Bovine <|-- Bull
    Bovine <|-- Cow
    Cow "1" *-- "many" MilkProduction
    MilkProduction "1" *-- "1" MilkQualityControl
    Herd "1" *-- "many" Bovine
    Bovine "1" *-- "1" EarTag
    Bovine "1" *-- "1" Breed