# BH_GROUP_DOC_PRSNL_ACT

> Actions performed by personnel for a behavioral health group.

**Description:** Behavioral Health Group Documentation Personnel Activity  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BH_GD_ACTIVITY_CD` | DOUBLE | NOT NULL |  | The activity that is to be performed. Example: Review, Co-Sign. |
| 2 | `BH_GD_ACTIVITY_STATUS_CD` | DOUBLE | NOT NULL |  | The status of the activity. Example Requested, Completed. |
| 3 | `BH_GROUP_DOC_PRSNL_ACT_ID` | DOUBLE | NOT NULL |  | Unique, generated number that identifies a single row on the BH_GROUP_DOC_PRSNL_ACT table. |
| 4 | `BH_GROUP_DOC_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The personnel that performed this activity. |
| 5 | `REQUESTED_DT_TM` | DATETIME | NOT NULL |  | Requested date and time for sign/review of the Therapeutic Note. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BH_GROUP_DOC_PRSNL_ID` | [BH_GROUP_DOC_PRSNL](BH_GROUP_DOC_PRSNL.md) | `BH_GROUP_DOC_PRSNL_ID` |

