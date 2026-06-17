# RAD_WORKLIST_FILTER

> Radiology worklist filter

**Description:** This table contains the filter criteria for a given radiology reading worklist.  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `INCLUDE_CRITERIA_IND` | DOUBLE | NOT NULL |  | Indicates if orders criteria should be included in the filter. |
| 2 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | The primary id of the table that this row is a child of. |
| 3 | `PARENT_ENTITY_NAME` | VARCHAR(255) |  |  | The name of the table that the row on this table is a child of. |
| 4 | `RAD_WORKLIST_FILTER_ID` | DOUBLE | NOT NULL |  | The rad_worklist_filter_id uniquely identifies a row in the Rad_worklist_filter table. It serves no other purpose other than to uniquely identify the row. |
| 5 | `RAD_WORKLIST_ID` | DOUBLE | NOT NULL | FK→ | Attribute that defines what worklist this is. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `RAD_WORKLIST_ID` | [RAD_WORKLIST](RAD_WORKLIST.md) | `RAD_WORKLIST_ID` |

