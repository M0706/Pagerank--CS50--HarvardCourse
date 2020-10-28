import random
from transition_model import transition


def rank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    sample_PR = {}
    for page in corpus:
        sample_PR[page] = 0

    # sample is initially none
    sample = None

    for iteration in range(n):
        # if sample is None (in first round)
        if sample == None:
            # list of all choices
            choices = list(corpus.keys())
            # randomly choose a sample --> random.choice chooses from choices with equal probability
            sample = random.choice(choices)
            sample_PR[sample] += 1
        else:
            # get probability distribution based on current sample
            next_sample_prob = transition(corpus, sample, damping_factor)
            # list with possible choices
            choices = list(next_sample_prob.keys())
            # weights for choices in choices list based on transition_model() output for current sample
            weights = [next_sample_prob[key] for key in choices]
            """choose a sample --> random.choices chooses from choices with defined probability distribution
               random.choices returns a list of values --> either grab that value by using .pop() or by using index [0]
            """
            sample = random.choices(choices, weights).pop()
            sample_PR[sample] += 1
    # after sampling is finished --> divide stored values by number of iterations to get percentages
    sample_PR = {key: value/n for key, value in sample_PR.items()}
    # check if dict-values add up to 1
    if round(sum(sample_PR.values()),5) != 1:
        print('ERROR! Probabilities do not add up to 1')
    else:
        # print(f'sample PR: {sample_PR}')
        print(f'Sum of sample_pagerank values: {round(sum(sample_PR.values()),10)}')
    return sample_PR