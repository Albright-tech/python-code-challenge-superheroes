from models import db, Hero, Power, HeroPower
from app import app
from random import randint, choice as rc

hero_list = [
    { "name": "Kamala Khan", "super_name": "Ms. Marvel" },
    { "name": "Doreen Green", "super_name": "Squirrel Girl" },
    { "name": "Gwen Stacy", "super_name": "Spider-Gwen" },
    { "name": "Janet Van Dyne", "super_name": "The Wasp" },
    { "name": "Wanda Maximoff", "super_name": "Scarlet Witch" },
    { "name": "Carol Danvers", "super_name": "Captain Marvel" },
    { "name": "Jean Grey", "super_name": "Dark Phoenix" },
    { "name": "Ororo Munroe", "super_name": "Storm" },
    { "name": "Kitty Pryde", "super_name": "Shadowcat" },
    { "name": "Elektra Natchios", "super_name": "Elektra" }
]

power_list = [
  { "name": "super strength", "description": "gives the wielder super-human strengths" },
  { "name": "flight", "description": "gives the wielder the ability to fly through the skies at supersonic speed" },
  { "name": "super human senses", "description": "allows the wielder to use her senses at a super-human level" },
  { "name": "elasticity", "description": "can stretch the human body to extreme lengths" }
]

with app.app_context():
    
    Hero.query.delete()
    Power.query.delete()
    HeroPower.query.delete()
    
    heroes = []
    for hero in hero_list:
        h = Hero(name = hero['name'], super_name = hero['super_name'])
        heroes.append(h)
    db.session.add_all(heroes)
    
    powers = []
    for power in power_list:
        p = Power(name = power['name'], description = power['description'])
        powers.append(p)
    db.session.add_all(powers)
    db.session.commit()
    
    hero_powers = []
    for hero in heroes:
        hp = HeroPower(hero = hero, power = rc(powers), strength = rc(['Strong', 'Weak', 'Average']))
        hero_powers.append(hp)
    db.session.add_all(hero_powers)
    db.session.commit()
    
    