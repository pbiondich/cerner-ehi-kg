# RX_IMAGE_QUEUE_TIME

> Stores the day of week and open/close times for a specific RX_IMAGE_QUEUE at a specific LOCATION.

**Description:** Image Queue Time  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CLOSE_TM_NBR` | DOUBLE | NOT NULL |  | The time that a specific queue at a specific location is closed for a given day_of_week. |
| 2 | `DAY_OF_WEEK_FLAG` | DOUBLE | NOT NULL |  | The day of week that a specific Queue is open at a specific location. |
| 3 | `IMAGE_QUEUE_LOC_RELTN_ID` | DOUBLE | NOT NULL | FK→ | Identifies the specific Queue and Location relationship. |
| 4 | `IMAGE_QUEUE_TIME_ID` | DOUBLE | NOT NULL |  | The unique identifier for the Day of Week and Times related to a RX_IMAGE_QUEUE and LOCATION. |
| 5 | `OPEN_TM_NBR` | DOUBLE | NOT NULL |  | The time that a specific Queue at a specific Location on a specific Day is open. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `IMAGE_QUEUE_LOC_RELTN_ID` | [RX_IMAGE_QUEUE_LOC_RELTN](RX_IMAGE_QUEUE_LOC_RELTN.md) | `IMAGE_QUEUE_LOC_RELTN_ID` |

