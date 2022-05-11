# Find Duplicate Advertisers

The purpose of this repo is to demonstrate my solution to finding a list of duplicate advertisers in [this](https://s3.amazonaws.com/ym-hosting/tomtest/advertisers.txt) file.

## Approach

When solving this problem, I wanted to avoid any approaches that required language-specific knowledge (e.g. English contractions, any abbreviations, etc.).  In previous work, I was already aware of [shingling and the Jaccard Similarity](https://www.cs.utah.edu/~jeffp/teaching/cs5955/L4-Jaccard+Shingle.pdf), so I took that approach here, ensuring that I lowercased all input.

I'm assuming that this code runs in an offline manner, infrequently because the list of advertisers does not change very often.  

In short, my approach:
- creates shingles (3-grams) of each advertiser in `advertisers.txt`.
- defines potential duplicates within the set of advertisers as any advertiser that shares at least one shingle with another advertiser.
- admits a potential duplicate as an actual duplicate if the jaccard similarity between an advertiser and the potential duplicate is greater than 0.75

## Output

The output of running the code is a tab-seperated file called `potential_matches.tsv`.  You'll see that there are 122 matches. The file a row structure of: `similarity score, advertiser, potential duplicate`. This file is sorted by `similarity score`, descending.
    
## Analysis

On my '21 Macbook Air, it took ~90 seconds to run, according to:
```
time python3 main.py  
```

### Why did I choose 0.75 as a similarity score cut off?

I did this after doing manual inspection of the output and it seemed like a good start.  Obviously there are some false positives like:
```
0.8723404255319149      The Twilight Saga Breaking Dawn - Part 2 Movie  The Twilight Saga Breaking Dawn - Part 1 Movie
```

But my overall approach was "If I didn't know anything about the nouns that each string represents, could I get them confused for each other?"  I'm reasonably satisfied with the results, but I'm also confident that there is room for improvement,

### What would I do differently if I had more time?
- You'll notice that for each row: `<score> <x> <y>`, there is another row `<score> <y> <x>`.  This could be cleaned up, since the rows are essentially duplicates, but I only have so much time and it isn't core to understanding my solution.
- The code takes 90 seconds to run.  Could it run faster if I paralelized finding potential duplicates for each advertiser?
- This code assumes that the list of advertisers can fit into memory.  If the list has millions of entries, it may not fit into memory.  In this case, I'd explore using a map-reduce approach. 

## How do I run this?

### Prerequisites

- `python3`
- `pip3`

```
python3 main.py # => output is written to `potential_matches.tsv` (tab-seperated)
```

### Tests

If you want to run the tests in this repo:

```
pip3 install -r requirements.txt
pytest
```



