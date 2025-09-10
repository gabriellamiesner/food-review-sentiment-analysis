from transformers import pipeline
import torch
sentiment_pipeline = pipeline("sentiment-analysis")
data = ["I love you", "I hate you"]
food_reviews = ['''We went on Saturday night and we queued twice for around 5-10’. Not too bad.

The best pizza was the champions 🍄‍🟫 one although a bit too much cheese.

The classic pizza was good but the sauce a bit too sweet for us.

The pepperoni square pizza was not fully cooked. The dough didn’t feel fully cooked. We should have returned it as we didn’t finish it/enjoy it.

We would have preferred if instead of a ricotta, there would have been a pizza with a blue cheese like Gorgonzola for example.

The staff was super kind and the atmosphere inside/outside is very friendly.

Prices aren’t too expensive and there’s the option of buying slices, which we loved.

Best part? How thin and crunchy the dough was.''', 
'''Bleecker Street Pizza is a must-visit for anyone looking for a classic New York slice. Located in the heart of the West Village, this small and casual spot serves up thin, crispy, and flavorful pizza that consistently lives up to the hype. The Nonna Maria slice is especially popular and truly delivers — rich tomato sauce, fresh mozzarella, and a perfect crust. Service is quick, and the atmosphere is no-frills, just like a real NYC pizzeria should be. Whether you’re grabbing a late-night bite or a quick lunch, it’s a solid and satisfying choice.''', 
'''I came here to try the Nonna Maria pizza and im so glad i did because it was very delicious! The ingredients were fresh, sauce was flavorful but not overpowering, and the crust was thin with just the right amount of crisp. Not greasy and it’s cooked perfectly. One of the best tasting pizza i ever had.

The space is tidy with many indoor and outdoor sitting. The staff were friendly and service was quick.

I’ll definitely be coming back!''']
result = sentiment_pipeline(food_reviews)
print(result)

