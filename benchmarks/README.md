## Steps for Benchmarking
1. Make sure that all of the pods are running (with injected Environment Variables)
2. Run the following line for benchmarking this project
```
locust -H http://127.0.0.1 -f try_p1.py -u 50 -r 2 PasteBin
```
3. Go to http://localhost:8089 to view the RPS

## Scenario
1. Task Ratio:
    - `/api/paste`: 1
    - `/api/<int:paste_id>`: 2
    - `/api/recents`: 3
    - I assume that each user will view more pastes than actually pasting them. Normally users will view their own pastes and maybe others as well, so I choose the `GET` request to be twice as many as the `POST` request for `paste`. Moreover, I assume that a lot of the users will typically also want to see the most recent pastes more often than actually pasting / viewing individual pastes, so I choose to make viewing recents to be thrice as many as pasting.
2. Benchmarking Code:
    - Initially, I will call `/api/paste` once so that there will be no `404 RESPONSE` for the `GET` API.
    - I keep track of the current number of pastes via `PASTES_SO_FAR` global variable and continue incrementing it whenever there has been a paste posted. This will be used to generate a valid `GET` request.
    - `@task /api/paste`: Use the paste number as the title and randomize a random number in the content so each paste have different titles and content
    - `@task /api/<int:paste_id>`: Randomize a random id between 1 and half of `PASTES_SO_FAR` to make sure that the paste actually exists
    - `@task /api/recents`: Just call the post request with no input 

## Locust Command
- Max Users: 50
- Spawn Rate: 2
- I kept these values small enough so the CPU consumption isn't too high, however the maximum users should also be not too low so the RPS can reach the target. Maximum 50 users is more than enough to get 500 responses per second.
