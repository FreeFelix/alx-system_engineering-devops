#!/usr/bin/python3

"""
    A recursive function that queries the Reddit API, parses the
    title of all hot articles, and prints a sorted count of given
    keywords (case-insensitive, delimited by spaces. Javascript should
    count as javascript, but java should not).

    Requirements:

    Prototype: def count_words(subreddit, word_list)
    Note: You may change the prototype, but it must be able to be called
    with just a subreddit supplied and a list of keywords. AKA you can add
    a counter or anything else, but the function must work without supplying 
    a starting value in the main.

    If word_list contains the same word (case-insensitive), the final count
    should be the sum of each duplicate (example below with java)

    Results should be printed in descending order, by the count, and if the
    count is the same for separate keywords, they should then be sorted
    alphabetically (ascending, from A to Z). Words with no matches should
    be skipped and not printed. Words must be printed in lowercase.

    Results are based on the number of times a keyword appears, not titles
    it appears in. java java java counts as 3 separate occurrences of java.

    To make life easier, java. or java! or java_ should not count as java
    If no posts match or the subreddit is invalid, print nothing.

    NOTE: Invalid subreddits may return a redirect to search results.
    Ensure that you are NOT following redirects.

"""
import requests
def count_words(subreddit, word_list, word_count=[], page_after=None):
    """
    Prints the count of the given words present in the title of the
    subreddit's hottest articles.
    """
    headers = {'User-Agent': 'HolbertonSchool'}

    word_list = [word.lower() for word in word_list]

    if bool(word_count) is False:
        for word in word_list:
            word_count.append(0)

    if page_after is None:
        url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
        r = requests.get(url, headers=headers, allow_redirects=False)
        if r.status_code == 200:
            for child in r.json()['data']['children']:
                i = 0
                for i in range(len(word_list)):
                    for word in [w for w in child['data']['title'].split()]:
                        word = word.lower()
                        if word_list[i] == word:
                            word_count[i] += 1
                    i += 1

            if r.json()['data']['after'] is not None:
                count_words(subreddit, word_list,
                            word_count, r.json()['data']['after'])
    else:
        url = ('https://www.reddit.com/r/{}/hot.json?after={}'
               .format(subreddit,
                       page_after))
        r = requests.get(url, headers=headers, allow_redirects=False)

        if r.status_code == 200:
            for child in r.json()['data']['children']:
                i = 0
                for i in range(len(word_list)):
                    for word in [w for w in child['data']['title'].split()]:
                        word = word.lower()
                        if word_list[i] == word:
                            word_count[i] += 1
                    i += 1
            if r.json()['data']['after'] is not None:
                count_words(subreddit, word_list,
                            word_count, r.json()['data']['after'])
            else:
                dicto = {}
                for key_word in list(set(word_list)):
                    i = word_list.index(key_word)
                    if word_count[i] != 0:
                        dicto[word_list[i]] = (word_count[i] *
                                               word_list.count(word_list[i]))

                for key, value in sorted(dicto.items(),
                                         key=lambda x: (-x[1], x[0])):
                    print('{}: {}'.format(key, value))
