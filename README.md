# Team_9
Team 9 repository
### Our Team:
- Team-lead: Safronov Andrey
- Code review: Hanov Alexey
- QA: Makarov Alexandr 



DZ_Networking:
test table

|---------------------| Request-response| CPU bound(fibonacci(25)) | 
| --------------------|-----------------|--------------------------|
| Pure socket server  | 14600 per-sec   | 0.5582435131072998 sec   |
| Select              | 9400  per-sec   | 0.7350335121154785 sec   |
| Selectors           | 13000 per-sec   | 0.7619962692260742 sec   |
| HTTP-servers        | 75    per-sec   | 0.8204889297485352 sec   |

