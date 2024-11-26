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
        +float fat_percentage
        +float vitamins_percentage
        +str __str__()
    }

    class MilkProduction {
        -datetime __date
        -float __liters
        -MilkQualityControl __milk_quality_control
        +datetime date
        +float liters
        +MilkQualityControl milk_quality_control
        +str __str__()
    }

    class Breed {
    }

    class Bull {
        -EarTag __ear_tag
        -datetime __birth_date
        -float __weight
        -Breed __breed
        +EarTag ear_tag
        +datetime birth_date
        +float weight
        +Breed breed
        +str __str__()
    }

    class Cow {
        -EarTag __ear_tag
        -datetime __birth_date
        -float __weight
        -Breed __breed
        +EarTag ear_tag
        +datetime birth_date
        +float weight
        +Breed breed
        +str __str__()
        +void add_milk_production(datetime, float, float, float, float)
    }

    class Herd {
        -list~Bull~ __bulls
        -list~Cow~ __cows
        +void add_cattle(Bull)
        +void add_cattle(Cow)
        +str __str__()
    }

    EarTag --> Bull
    EarTag --> Cow
    MilkQualityControl --> MilkProduction
    MilkProduction --> Cow
    Bull --> Herd
    Cow --> Herd
    Breed --> Bull
    Breed --> Cow