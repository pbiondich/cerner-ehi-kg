# RXS_WORKLIST_LOCATION_R

> Stores locations that will be queried for task creation on a worklist.

**Description:** RxStation Worklist Location Relation  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `LOC_CD` | DOUBLE | NOT NULL | FK→ | Location related to the worklist. Could be an type of location in the location model: facility, cluster, device, etc. |
| 2 | `RXS_WORKLIST_ID` | DOUBLE | NOT NULL | FK→ | The worklist that relates to the specified location. |
| 3 | `RXS_WORKLIST_LOCATION_R_ID` | DOUBLE | NOT NULL |  | Unique, generated number that identifies a single row in the RXS_WORKLIST_LOCATION_R table. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LOC_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `RXS_WORKLIST_ID` | [RXS_WORKLIST](RXS_WORKLIST.md) | `RXS_WORKLIST_ID` |

