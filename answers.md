# CMPS 2200 Reciation 5
## Answers

**Name:** Darian Tocci


Place all written answers from `recitation-05.md` here for easier grading.





Randomized input
|    n |   ssort |   qsort-fixed |   qsort-random |   timsort |
|------|----------|---------------|----------------|------------|
|  100 |    1.245 |         0.150 |          0.120 |      0.070 |
| 1000 |   78.340 |         3.712 |          2.203 |      0.440 |
| ...  |      ... |           ... |            ... |        ... |

sorted input
|    n |   ssort |   qsort-fixed |   qsort-random |   timsort |
|------|----------|---------------|----------------|------------|
|  100 |    1.240 |         0.800 |          0.130 |      0.070 |
| 1000 |   78.200 |        30.520 |          2.100 |      0.450 |
| ...  |      ... |           ... |            ... |        ... |


- **1b.**

When I compared the sorting algorithms, selection sort was definitely the slowest since it runs in O(n^2) time. Quicksort with a fixed pivot worked fine on random lists but got really slow on already-sorted ones because picking the first element every time caused unbalanced splits. The version of Quicksort that used a random pivot stayed much faster and closer to O(nlogn) on all inputs since it avoided that worst-case behavior. Overall, the randomized Quicksort was more consistent and efficient, while selection sort quickly became too slow as the list size increased.

- **1c.**
When I compared my fastest Quicksort, the random pivot one, to Python’s built-in sorted function, Timsort was faster every time. On random lists, both followed about O(nlogn) growth, but Timsort still finished quicker. On already-sorted lists, Timsort was way faster because it noticed the list was ordered and basically ran in linear time, while Quicksort still had to do a lot more work. Overall, Timsort ended up being the most efficient and adaptable out of all the methods I tested.
