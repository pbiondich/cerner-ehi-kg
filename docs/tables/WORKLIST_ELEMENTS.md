# WORKLIST_ELEMENTS

> Defines the service resource (instrument or bench), ordered procedures, and/or detail procedures that are included on the worklist.

**Description:** Worklist Elements  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CATALOG_CD` | DOUBLE | NOT NULL |  | A unique code value that identifies a specific order catalog procedure that was included on a worklist. |
| 2 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL |  | A unique code value that identifies a specific service resource (such as instrument, bench, or sub-section) associated with a worklist. |
| 3 | `TASK_ASSAY_CD` | DOUBLE | NOT NULL |  | A unique code value that identifies a specific discrete task assay that is included on a worklist. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 9 | `WORKLIST_ID` | DOUBLE | NOT NULL | FK→ | A unique, internal, system-assigned number that identifies a specific worklist. Creates a relationship to the worklist table. |
| 10 | `WORKLIST_SEQ` | DOUBLE | NOT NULL |  | Sequential number used to uniquely identify the worklist elements associated with a specific worklist. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `WORKLIST_ID` | [WORKLIST](WORKLIST.md) | `WORKLIST_ID` |

