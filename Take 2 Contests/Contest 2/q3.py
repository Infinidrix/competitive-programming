class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        favorite_index = collections.defaultdict(set)
        for fav in range(len(favoriteCompanies)):
            for company in favoriteCompanies[fav]:
                favorite_index[company].add(fav)
        
        result = []
        for fav in range(len(favoriteCompanies)):
            subsets = set()
            first = True
            for company in favoriteCompanies[fav]:
                if first:
                    subsets = subsets.union(favorite_index[company])
                    first = False
                else:
                    subsets = subsets.intersection(favorite_index[company])
                    # print(f'for {fav} on {company}: {subsets}')
                if len(subsets) == 1:
                    result.append(fav)
                    break
        return result