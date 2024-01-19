## Data Model 

**students**
|field | type |
|----------|-------|
| firstname | String
| lastname | String (optional)
| classOf | String (optional)

**appointments**

|field | type |
|----------|-------|
| title | String |
| date | String | 
| students | Array (String) |
| fulltimers | Array (String) |
| notes | String (optional) |

**events**

|field | type |
|----------|-------|
| title | String |
| date | String |
| students | Array (String) |
| fulltimers | Array (String) |

**gospel**