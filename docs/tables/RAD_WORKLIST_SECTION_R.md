# RAD_WORKLIST_SECTION_R

> Radioilogy worklist/sections relationship

**Description:** Defines the radiolgy sections that are part of a worklist  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `RAD_WORKLIST_ID` | DOUBLE | NOT NULL | FK→ | Attribute that defines what worklist this is. |
| 2 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL | FK→ | The Service_Resource_Cd identifies the Exam Room that the detail exam is to be performed within. |
| 3 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 4 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 5 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 6 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 7 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `RAD_WORKLIST_ID` | [RAD_WORKLIST](RAD_WORKLIST.md) | `RAD_WORKLIST_ID` |
| `SERVICE_RESOURCE_CD` | [SECTION](SECTION.md) | `SERVICE_RESOURCE_CD` |

