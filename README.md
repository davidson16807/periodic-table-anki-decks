#Visualizing the Periodic Table
This is not designed to be one of those pointless periodic table decks where you memorize obscure numbers for every element. It teaches the most important concept you have to remember: behavior. 

Behavior, namely, through position. If you learn that silicon is right below carbon, it automatically tells you something about how silicon behaves. The deck could be made simple by asking you to recite a list of elements for every group, but list-based answers like that don't make for good flash cards. Flash cards work best when you want to store mappings in your head: sets of tuples where for each question there's a single answer. If you do want to store a list in your head, it's best to store it as a linked list: a mapping where for each element there's a single successor element. If you want to recall a list forwards and backwards, you actually remember two mappings: one that produces the single successor element, and another producing the single preceding element. 

In the case of the periodic table, you might also want to know the element left or right of another. This is for, say, remembering nucleosynthesis processes, or maybe for when your friends want to test your knowledge by reciting the table in order. So you now have four mappings:

* given an element, produce the element below
* given an element, produce the element above
* given an element, produce the element to the left
* given an element, produce the element to the right

So in short, we're going to be learning how to visualize the table. 

I recommend you learn the deck in order. I've ordered the deck roughly by how frequent the elements occur in the universe, so the first things you remember should be the most applicable to real life. So if you get bored and don't want to learn the deck anymore you've still maximized the value you can get out of it. 