def transition(corpus, page, damping_factor):

    trans_mod = {}
    
    # number of files in corpus
    num_files = len(corpus)

    # get number of links from current page
    num_links = len(corpus[page])

    if num_links != 0 :
        # calculate random probability (which is applicable for all pages)
        rand_prob = (1 - damping_factor) / num_files
        # calculate specific page-related probability
        spec_prob = damping_factor / num_links
    else:
        # calculate random probability (which is applicable for all pages)
        rand_prob = (1 - damping_factor) / num_files
        # calculate specific page-related probability
        spec_prob = 0

    # iterate over files
    for file in corpus:
        # check if current page has any links
        if len(corpus[page]) == 0:
            trans_mod[file] = 1 / num_files
        else:
            # if file is not current page, there is no need to get its links
            if file not in corpus[page]:
                # probability of non-linked page is 1-damp
                trans_mod[file] = rand_prob
            else:
                # probability for linked page is specific plus random probability
                trans_mod[file] = spec_prob + rand_prob
    # check if sum of probabilities is 1
    if round(sum(trans_mod.values()),5) != 1:     # round sum so that 0.99999... will be recognized as 1
        print(f'ERROR! Probabilities add up to {sum(trans_mod.values())}')
    # else:
    #     print(f'\tTransition model probabilities add up to 1: CHECK!')
    return trans_mod