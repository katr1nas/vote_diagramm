from typing import List, Optional
from datetime import datetime


class Vote:
    def __init__(self, voter_id: str, candidate: str, region: str):
        self.voter_id = voter_id
        self.candidate = candidate
        self.region = region
        self.confirmed = False
        self.timestamp = datetime.now()

    def confirm_vote(self):
        self.confirmed = True

    def change_vote(self, new_candidate: str):
        self.candidate = new_candidate
        self.confirmed = False

    def display_info(self):
        print("\nVote info:")
        print(f"Voter: {self.voter_id}")
        print(f"Candidate: {self.candidate}")
        print(f"Region: {self.region}")
        print(f"Confirmed: {self.confirmed}")
        print(f"Time: {self.timestamp}")


class Voter:
    def __init__(self, voter_id: str, name: str, region: str):
        self.voter_id = voter_id
        self.name = name
        self.region = region
        self.has_voted = False
        self.my_vote = None

    def cast_vote(self, candidate: str, election):
        if self.has_voted:
            print(f"{self.name} already voted")
            return None

        if not election.is_open:
            print("Election is closed")
            return None

        if candidate not in election.candidates:
            print("Invalid candidate")
            return None

        vote = Vote(self.voter_id, candidate, self.region)
        vote.confirm_vote()

        self.my_vote = vote
        self.has_voted = True
        election.add_vote(vote)

        return vote

    def view_status(self):
        print(f"\n{self.name} - ID: {self.voter_id}")
        print(f"Region: {self.region}")
        print(f"Voted: {self.has_voted}")
        if self.my_vote:
            print(f"Choice: {self.my_vote.candidate}")


class Election:
    def __init__(self, name: str, candidates: List[str]):
        self.name = name
        self.candidates = candidates
        self.votes = []
        self.is_open = False

    def open_election(self):
        self.is_open = True
        print(f"\nElection opened: {self.name}")
        print(f"Candidates: {', '.join(self.candidates)}")

    def close_election(self):
        self.is_open = False
        print(f"\nElection closed: {self.name}")
        self.count_votes()

    def add_vote(self, vote):
        self.votes.append(vote)

    def count_votes(self):
        results = {}
        for c in self.candidates:
            results[c] = 0

        for vote in self.votes:
            if vote.confirmed:
                results[vote.candidate] += 1

        print(f"\nResults for {self.name}:")
        total = sum(results.values())
        print(f"Total votes: {total}")

        for candidate, count in sorted(results.items(), key=lambda x: x[1], reverse=True):
            if total > 0:
                pct = (count / total) * 100
                print(f"{candidate}: {count} ({pct:.1f}%)")
            else:
                print(f"{candidate}: {count}")

        return results


def main():
    election = Election("Election 2024", ["Johnson", "Smith", "Brown"])

    v1 = Voter("001", "John Doe", "District A")
    v2 = Voter("002", "Jane Smith", "District B")
    v3 = Voter("003", "Bob Wilson", "District A")

    election.open_election()

    v1.cast_vote("Johnson", election)
    v2.cast_vote("Smith", election)
    v3.cast_vote("Johnson", election)

    v1.view_status()

    election.close_election()


if __name__ == "__main__":
    main()
