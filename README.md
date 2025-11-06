# vote_diagramm

Simple electronic voting system implementation in Python.

## Classes

### Vote
Represents a single vote in the election.

**Attributes:**
- `voter_id` - unique voter identifier
- `candidate` - selected candidate name
- `region` - voter's region
- `confirmed` - vote confirmation status
- `timestamp` - when vote was cast

**Methods:**
- `confirm_vote()` - confirms the vote
- `change_vote(new_candidate)` - changes candidate selection
- `display_info()` - displays vote information

### Voter
Represents a voter in the system.

**Attributes:**
- `voter_id` - unique identifier
- `name` - voter name
- `region` - voter's region
- `has_voted` - voting status
- `my_vote` - reference to cast vote

**Methods:**
- `cast_vote(candidate, election)` - cast a vote in election
- `view_status()` - view voting status

### Election
Represents an election with candidates and votes.

**Attributes:**
- `name` - election name
- `candidates` - list of candidates
- `votes` - list of all votes
- `is_open` - election status

**Methods:**
- `open_election()` - opens election for voting
- `close_election()` - closes election and counts votes
- `add_vote(vote)` - adds vote to election
- `count_votes()` - counts and displays results

## Usage
```python
election = Election("Election 2024", ["Johnson", "Smith", "Brown"])

v1 = Voter("001", "John Doe", "District A")
v2 = Voter("002", "Jane Smith", "District B")

election.open_election()

v1.cast_vote("Johnson", election)
v2.cast_vote("Smith", election)

election.close_election()
```

## Features

- Prevents double voting
- Vote confirmation system
- Regional tracking
- Results calculation with percentages
- Timestamp tracking

## Requirements

Python 3.6+
