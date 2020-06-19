# Location Selection - Greedy Algorithm

# Scenario:
The company would like to open 4 distribution centers in North American to service and delivery products to end-customers. We want to cover as much customers as we can with minimum overlap.

# Solution:
We’re going to use greedy algorithm to decide idea locations. The basic logic is choosing p1 location that can cover most population. Then choose p2 location that covers the most of the rest population， and so on。

# Input: The populaton, location of each city. The furthest distance that a DC can cover.
# Output: Idea location of each DC. Cities and total population covered by each DC.
