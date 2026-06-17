# ASSEMBLY_TWEET

> A tweet for assemblies created in a lab system

**Description:** Assembly Tweet  
**Table type:** ACTIVITY  
**Primary key:** `ASSEMBLY_TWEET_ID`  
**Columns:** 15  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_DIRECTIONAL_FLAG` | DOUBLE | NOT NULL |  | The direction of the action. |
| 2 | `ACTION_FLAG` | DOUBLE | NOT NULL |  | The action that was tweeted about. |
| 3 | `ACTION_LOCATION_CD` | DOUBLE | NOT NULL |  | Uniquely identifies the location the action occurred. |
| 4 | `ACTION_LOCATION_NAME` | VARCHAR(60) | NOT NULL |  | The location the action occurred. |
| 5 | `ACTION_USER_NAME` | VARCHAR(60) | NOT NULL |  | The user that performed the action in the tweet. |
| 6 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 7 | `ASSEMBLY_TWEET_ID` | DOUBLE | NOT NULL | PK | Uniquely identifies a tweet for assemblies created in a lab system. |
| 8 | `EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date from which the tweet is effective. |
| 9 | `FROM_LAB_SYSTEM_NAME` | VARCHAR(40) | NOT NULL |  | The name of the lab system that provided the tweet. |
| 10 | `ISSUED_DT_TM` | DATETIME | NOT NULL |  | The date and time the tweet was issued. |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [ASSEMBLY_TWEET_LOCATOR](ASSEMBLY_TWEET_LOCATOR.md) | `ASSEMBLY_TWEET_ID` |

