text = """Uh
Yeah, yeah
When I was young, I fell in love
We used to hold hands, man, that was enough (yeah)
Then we grew up, started to touch
Used to kiss underneath the light on the back of the bus (yeah)
Oh no, your daddy didn't like me much
And he didn't believe me when I said you were the one
Oh, every day she found a way out of the window to sneak out late
She used to meet me on the Eastside
In the city where the sun don't set
And every day you know that we ride
Through the backstreets of a blue Corvette
Baby, you know I just wanna leave tonight
We can go anywhere we want
Drive down to the coast, jump in the seat
Just take my hand and come with me, yeah
We can do anything if we put our minds to it
Take your whole life then you put a line through it
My love is yours if you're willing to take it
Give me your heart 'cause I ain't gonna break it
So come away, starting today
Start a new life, together in a different place
We know that love is how these ideas came to be
So baby, run away, away with me
Seventeen and we got a dream to have a family
A house and everything in between
And then, oh, suddenly we turned twenty-three
Now we got pressure for taking our life more seriously
We got our dead-end jobs and got bills to pay
Have old friends and know our enemies
Now I, I'm thinking back to when I was young
Back to the day when I was falling in love
He used to meet me on the Eastside
In the city where the sun don't set
And every day you know where we ride
Through the backstreets in a blue Corvette
And baby, you know I just wanna leave tonight
We can go anywhere we want
Drive down to the coast, jump in the seat
Just take my hand and come with me
Singing
We can do anything if we put our minds to it
Take your whole life then you put a line through it
My love is yours if you're willing to take it
Give me your heart 'cause I ain't gonna break it
So come away, starting today
Start a new life, together in a different place
We know that love is how these ideas came to be
So baby, run away with me
Run away, now
Run away, now
Run away, now
Run away, now
Run away, now
Run away, now
He used to meet me on the Eastside
She used to meet me on the Eastside
He used to meet me on the Eastside
She used to meet me on the Eastside
In the city where the sun don't set"""

print(text)

print(len(text))

print(text.split())

print(len(text.split()))

text = """
a b c A a b 
"""

print(text.split())

word_count = {}

for word in text.lower().split():
  if word in word_count:
    word_count[word] +=1
  else: 
   word_count[word] = 1

print(word_count)

