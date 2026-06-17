# SURG_REQ_FAVORITE

> Mpage component, Request for Surgery allows users to save different combinations of surgery location, staff, procedure, ect as favorites. This table will store those different combinations for each user.

**Description:** Surgical Request Favorties  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `FAVORITE_NAME` | VARCHAR(255) |  |  | Name of the Favorite |
| 3 | `PRSNL_ID` | DOUBLE | NOT NULL | FK→ | personnel identifier |
| 4 | `SURG_REQ_FAVORITE_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 5 | `SURG_REQ_ID` | DOUBLE | NOT NULL | FK→ | FK value from SURG_REQ table |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `SURG_REQ_ID` | [SURG_REQ](SURG_REQ.md) | `SURG_REQ_ID` |

