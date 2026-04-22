def voting_system(votes):
    counted_votes = {}
    voters = set()

    for voter_id, candidate in votes:
        if voter_id in voters:
            continue  # skip duplicate vote
        voters.add(voter_id)

        counted_votes[candidate] = counted_votes.get(candidate, 0) + 1

    winner = max(counted_votes, key=counted_votes.get)

    return counted_votes, winner