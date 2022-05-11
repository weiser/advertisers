from asyncore import write
from typing import Set
from lib.jaccard_similarity import jaccard_smilarity
from lib.shingle import shingle 

def potential_duplicates(shingles: Set[str], shingle_advertisers: dict[str, Set[str]]) -> Set[str]:
    """
    given a set of shingles, and a mapping from a shingle to all the advertisers that contain that shingle, calculate the set of potential duplicates
    
    A potential duplicate is an advertiser which has at least one shared shingle with the input set of shingles
    """
    pds = set()
    for s in shingles:            
        pds.update(shingle_advertisers.get(s, set()))
    return pds


if __name__ == "__main__":
    advertisers: list[str] = open('advertisers.txt').readlines()
    advertisers = [l.strip() for l in advertisers]
    advertisers_shingles = {}
    shingle_advertisers = {}
    print("Shingling dataset")
    for advert in advertisers:
        shingles = shingle(advert.strip(), 3)
        advertisers_shingles[advert] = shingles
        for s in shingles:
            if shingle_advertisers.get(s, None) == None:
                shingle_advertisers[s] = {advert}
            else:
                shingle_advertisers[s].add(advert)
    
    results = []
    print("Looking for duplicates in dataset")    
    for idx, advertiser in enumerate(advertisers):        
        if idx % 1000 == 0:
            print(f"Looking at duplicates at index: {idx}/{len(advertisers)}")        
        
        for pd in potential_duplicates(advertisers_shingles[advertiser], shingle_advertisers):
            sim_score = jaccard_smilarity(advertisers_shingles[advertiser], advertisers_shingles[pd])
            # We use a similarity score of 0.75 as a cut off as a result of manual introspection
            if sim_score > 0.75 and pd != advertiser:
                results.append({"sim_score": sim_score, "advertiser": advertiser, "potential_duplicate": pd})
    
    # sort by similarity score, most similar at the top
    results.sort(reverse=True, key=lambda r: r["sim_score"])

    print(f"found {len(results)} potential matches.  Outputting to potential_matches.tsv")

    output = open("potential_matches.tsv", "w")
    for r in results:
        row = "\t".join([str(r["sim_score"]), r["advertiser"], r["potential_duplicate"]])
        output.write(row)
        output.write("\n")
    output.close()

        
        
    
    


