## Data Model 

**students**
| field | type |
|----------|-------|
| firstname | String |
| lastname | String |
| classOf | String (optional) |

**appointments**

| field | type |
|----------|-------|
| title | String |
| date | String | 
| students | Array (String) |
| fulltimers | Array (String) |
| notes | String (optional) |

**events**

| field | type |
|----------|-------|
| title | String |
| date | String |
| students | Array (String) |
| fulltimers | Array (String) (optional) |
| notes | String (optional) |

**gospel**

| field | type |
|----------|-------|
| date | String |
| tractspassed | Int |
| peoplecontacted | Int |
| notes | String (optional) |