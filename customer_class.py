# customer_class.py
# The customer class represents a customer at the lemondade stand.
# The customer has preferences for lemonade sweetness and ice level,
# and a price point they are willing to pay.
# All of these attributes will influence their purchasing decision and
# are returned as a list of attributes.

import random as ran



class Customer:
    def __init__(self, sweetness_preference=None, ice_preference=None, water_preference=None, price_point=None, leniency=None, duck=None):
        self.sweetness_preference = (
            sweetness_preference if sweetness_preference is not None
            else ran.randint(-2, 3)
        )
        self.ice_preference = (
            ice_preference if ice_preference is not None
            else ran.randint(0, 3)
        )
        self.water_preference = (
            water_preference if water_preference is not None
            else ran.randint(-225,250)
        )
        self.price_point = (
            price_point if price_point is not None
            else round(ran.uniform(0.25, 4.0),2)
        )
        self.leniency = (
            leniency if leniency is not None
            else ran.randint(-1, 1)
        )
        self.duck = (
            duck if duck is not None
            else (True if ran.randint(0, 500) == 333 else False)
        )



    def get_customer_attributes(self):
        return {
            "sweetness": self.sweetness_preference,
            "ice": self.ice_preference,
            "water": self.water_preference,
            "price": self.price_point,
            "leniency": self.leniency,
            "duck": self.duck
        }