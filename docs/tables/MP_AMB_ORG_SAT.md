# MP_AMB_ORG_SAT

> Tracks manually satisfied expectations for a scheduling appointment and resource from the ambulatory Organizer Mpage Open Items tab.

**Description:** MPages Ambulatory Organizer Satisfier  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `MANUAL_IND` | DOUBLE | NOT NULL |  | Indicates if the item has been manually satisfied or system satisfied. |
| 2 | `MP_AMB_ORG_SAT_ID` | DOUBLE | NOT NULL |  | Unique, generated number that identifies a single row on the MP_AMB_ORG_SAT table. |
| 3 | `OPEN_ITEM_TYPE_CD` | DOUBLE | NOT NULL |  | The type of open item chosen to be satisfied. |
| 4 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Identifies the appointment that this row contains data for. |
| 5 | `PARENT_ENTITY_NAME` | VARCHAR(32) | NOT NULL |  | Relates to the table that contains the appropriate appointment type for this row. Values can be ('SCH_EVENT','SURG_CASE_PROCEDURE') |
| 6 | `RESOURCE_CD` | DOUBLE | NOT NULL | FK→ | Physician resource associated to the appointment. |
| 7 | `SATISFIED_IND` | DOUBLE | NOT NULL |  | %satisifie |
| 8 | `SATISFIED_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The provider who is manually satisfying a row on the open items, Ambulatory Organizer MPage. |
| 9 | `SCH_EVENT_ID` | DOUBLE | NOT NULL | FK→ | The event for the open item row on the ambulatory organizer Mpage. |
| 10 | `STATUS_DT_TM` | DATETIME | NOT NULL |  | Date and time when satisfied_ind was last changed. |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `RESOURCE_CD` | [SCH_RESOURCE](SCH_RESOURCE.md) | `RESOURCE_CD` |
| `SATISFIED_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `SCH_EVENT_ID` | [SCH_EVENT](SCH_EVENT.md) | `SCH_EVENT_ID` |

