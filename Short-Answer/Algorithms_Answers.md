#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n) - linear: each iteration is n^3 but n^2 is being added to a so if you divide n^2 from n^3 you're left with just n


b) O(n log n) - linearithmic: the for loop depends on the n input making it linear but during the while loop, because j is doublind through each iteration it is halving the computations so its logarithmic (O(log n)) & after multiplying linear by logarithmic you get linearithmic.


c) O(n) - linear: Assuming this isn't a trick question because there is no actual input n being referenced like the other 2 code blocks have, this appears to be linear because the output depends on the input amount of bunnies and grows in size relative to it.

## Exercise II

An 'n-story building' reminds me of a sorted list starting at 1 but is just vertical instead of horizontal so this seems like a good case to use binary search. I would find the middle floor by adding the first & last floors together & dividing by 2, then i'd drop an egg & depending on if it breaks or not, I can rule out one of the two halves & repeat the process until I find floor f. I would say this search method is logarithmic - O(log n) because you're eliminating half the computations as the size of n increases.
