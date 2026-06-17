# BR_EVENT_GROUPER_RELTN

> Event Codes that have been grouped.

**Description:** Bedrock Event Grouper Relation  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BR_EVENT_GROUPER_ID` | DOUBLE | NOT NULL | FK→ | The group that this event code belongs to. |
| 2 | `BR_EVENT_GROUPER_RELTN_ID` | DOUBLE | NOT NULL |  | Unique, generated number that identifies a single row on the BR_EVENT_GROUPER_RELTN table. |
| 3 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | The event that is being grouped |
| 4 | `PARENT_ENTITY_NAME` | VARCHAR(32) | NOT NULL |  | The name of the table where PARENT_ENTITY_ID is sourced from. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BR_EVENT_GROUPER_ID` | [BR_EVENT_GROUPER](BR_EVENT_GROUPER.md) | `BR_EVENT_GROUPER_ID` |

