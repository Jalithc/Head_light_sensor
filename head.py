class HeadLight:
    def __init__(self, sun_light = 0.5):
        self.chance_to_night = sun_light
        self.is_light_on = True
        self.is_light_off = True
        self.is_a_day = False
        self.is_a_night = True

    def light_turned_on(self, chance_to_night):
        if self.is_a_night:
            print("Head lights are turned on!")
            return self.is_light_off
        
        elif chance_to_night > self.chance_to_night:
            print("Head light turned on!")
            return self.is_light_on
        
        else:

            return not self.is_light_on
        

    def light_turned_off(self, chance_to_morning):
        if self.is_a_day:
            print("Lights are Turned off!")

        elif chance_to_morning < self.chance_to_night:
            print("Head light turned off!")
            return self.is_light_off
        
        else:

            return not self.is_light_off
        
        
head = HeadLight()
head.light_turned_on(0.4)
head.light_turned_off(0.4)
        