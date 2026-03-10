from Game import Warrior, Mage, Archer
from abc import ABC

characters = []

def simulate_battle():
    print("\n" + "="*50)
    print("BATTLE SIMULATION - ABSTRACTION DEMO")
    print("="*50)
    
    for c in characters:
        print(f"\n🎮 {c.name} turn:")
        print(c.attack())  # ABSTRACT METHOD IMPLEMENTATION
        print(c.defend())  # ABSTRACT METHOD IMPLEMENTATION

while True:
    print("\n=== GAME BATTLE ===")
    print("1. Create Character")
    print("2. Simulate Battle")
    print("0. Exit")
    
    try:
        choice = input("Choose: ")
        
        if choice == "1":
            print("\n1. Warrior ⚔️")
            print("2. Mage 🔮")
            print("3. Archer 🏹")
            
            classes = input("Class: ")
            name = input("Name: ")
            
            if classes == "1":
                characters.append(Warrior(name))
            elif classes == "2":
                characters.append(Mage(name))
            elif classes == "3":
                characters.append(Archer(name))
            else:
                print(" No Extra class!")
                continue
                
            print(f"✅ Created {name} the {['Warrior','Mage','Archer'][int(classes)-1]}")
        
        elif choice == "2":
            if not characters:
                print(" No Servants in battle!")
            else:
                simulate_battle()
        
        elif choice == "0":
            print("Game over!")
            break
        
        else:
            print(" Invalid choice!")
    
    except Exception as e:
        print(f" Error: {e}")