def iter_rank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    # createempty dict to fill later
    iterate_PR = {}
    # safe the number of pages in variable
    num_pages = len(corpus)
    # iterate over all corpus pages and initially assign 1/number of pages to each
    for page in corpus:
        iterate_PR[page] = 1/num_pages

    changes = 1
    iterations = 1
    while changes >= 0.001:
        # print(f'Iteration {iterations}')
        # reset change value
        changes = 0
        # copy current state to calculate new PRs without influence from newly calculated values
        previous_state = iterate_PR.copy()
        # iterate over pages
        for page in iterate_PR:
            # grab "parent"-pages that link to it
            parents = [link for link in corpus if page in corpus[link]]
            # add first part of equation
            first = ((1-damping_factor)/num_pages)
            # iterate over parents to add second part of the equation iteratively
            second = []
            if len(parents) != 0:
                for parent in parents:
                    # number of links starting from parent page
                    num_links = len(corpus[parent])
                    val =  previous_state[parent] / num_links
                    second.append(val)

            # sum values in second list together
            second = sum(second)
            iterate_PR[page] = first + (damping_factor * second)
            # calculate change during this iteration
            new_change = abs(iterate_PR[page] - previous_state[page])
            # print(f'\tProbability for {page}: {iterate_PR[page]}')
            # update change-value if it is new change-value is larger --> this way only the largest change is recorded for following while iteration
            if changes < new_change:
                changes = new_change
        iterations += 1
    # normalize values
    dictsum = sum(iterate_PR.values())
    iterate_PR = {key: value/dictsum for key, value in iterate_PR.items()}
    print(f'\nPageRank value stable after {iterations} iterations.')
    print(f'Sum of iterate_pagerank values: {round(sum(iterate_PR.values()),10)}')
    return iterate_PR