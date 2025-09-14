from transformers import pipeline
import torch

sentiment_pipeline = pipeline("sentiment-analysis")

bleeker_st_reviews = ['''
We went on Saturday night and we queued twice for around 5-10’. Not too bad.

The best pizza was the champions 🍄‍🟫 one although a bit too much cheese.

The classic pizza was good but the sauce a bit too sweet for us.

The pepperoni square pizza was not fully cooked. The dough didn’t feel fully cooked. We should have returned it as we didn’t finish it/enjoy it.

We would have preferred if instead of a ricotta, there would have been a pizza with a blue cheese like Gorgonzola for example.

The staff was super kind and the atmosphere inside/outside is very friendly.

Prices aren’t too expensive and there’s the option of buying slices, which we loved.

Best part? How thin and crunchy the dough was.''', 

'''I came here to try the Nonna Maria pizza and im so glad i did because it was very delicious! The ingredients were fresh, sauce was flavorful but not overpowering, and the crust was thin with just the right amount of crisp. Not greasy and it’s cooked perfectly. One of the best tasting pizza i ever had.

The space is tidy with many indoor and outdoor sitting. The staff were friendly and service was quick.

I’ll definitely be coming back!''', 
'''
On a corner of Bleecker Street you can visit euphoria if you so choose to. Bleecker Street Pizza is a flavorful punch of a slice, well positioned amongst the hierarchy of New York pizzerias. The inside is unassuming, a lot like a million other places but whatever is going on in that oven is the truth. When we stopped by there was a decent sized line but they do keep it pushing well. Despite the amount of people indoors the place is still pretty clean and there is an order to all the madness going on around you. Lining the walls they have photos of celebrities who made the trek (or swiped a Metrocard) to enjoy a slice here. Like any pizzeria they offer a lot of different slices but since we’ve heard this place was one of the best slices in the city we opted for a regular cheese slice, no frills to make sure we were hearing correctly.

After getting our slice and sitting outside (yes, they do have outdoor seating but it is hard to come by), we were ready to dig in. Here’s our careful analysis: the crust is undoubtedly New York style. Firm, crisp, not too much give and not burnt to high heavens like a New Haven slice. A little flop to it but a firm underbelly to the slice, which seems like an over evaluation, but trust that it is not. The first bite was incredible. The cheese is stretchy and light, the sauce rich but complimenting the cheese. Easily one of the 3 best pizza slices in our lives based on the first bite alone and by the final bite we were questioning if it was the best period. Needless to say, Bleecker Street Pizza is not an if you’re in the city or an if you’re in the area excursion; this is a go out of your way and eat this slice place. Phenomenal and trying to find excuses to come back for seconds ASAP.
''', 
'''
Just ok pizza nothing special overpriced cheese slice $4.80 . Little to no sauce a there are 6 guys behind the counter and the place is still dirty . They don’t keep inside clean . I ask the guy to give me a specific slice an he act like he switched it to give me the same slice he originally picked out. Shady
''', 
'''
First off. Best garlic knots around not gonna lie. One star though for the customer service. The way my family was treated ruined the whole experience. We walk in and immediately get yelled at to order. (Never been here before) and I’m not kidding we were not given even 15 seconds to look at anything before literally being yelled at. Actually yelled at too not just loudly spoken too. “WHAT DO YOU WANT? IF YOU AREN’T READY STEP ASIDE!” however there was nobody behind us and it was just three of us, they could have said hello, welcome in, order when you’re ready, get any slice you want, here are our options, etc. And then while one employee was yelling at us to get our order, the women on the register started asking us what we were getting as well. Never been in an establishment where two people took my order at the same time, so aggressively at that. The woman was rude as hell. Pizza isn’t bad at all, it’s just not worth the hype. The garlic knots are though but I will never return regardless.

''', 

'''
Best pizza I’ve had so far in NYC. If you’re in Manhattan, you need to stop in and get the Nona slice. It’s amazing. The crust is light and airy, and the toppings are so incredibly good!

''', 
'''
Bleecker Street Pizza is a NY classic. Visiting town and stopped in. The guys that run this shop are friendly but they offer few modifications so you either like what’s in the case or head to Joe’s down the street with more options. Personally, I think Bleecker is much better and I don’t think you can go wrong with any of the slices in the case but everyone has a picky friend. There’s plenty of room to stand at the table in the middle or the small side tables inside and out. You might wait a few minutes but pizza is a quick meal so table turnover is fast and the guys are good about wiping them down in between. They also sell white claw and beer for anyone looking for a drink with their slice.
''']

# print(len(bleeker_st_reviews))

result = sentiment_pipeline(bleeker_st_reviews)
print(result)