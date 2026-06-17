# AV_STATUS_EVENT

> This table used as a event table. Rows are written when an user runs loads the AVStatus.dll and turns on/off autoverification for an instrument.

**Description:** Auto Verify Status Event  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCESSION_ID` | DOUBLE | NOT NULL |  | A unique, internal, system-assigned number that identifies a specific accession for which autoverification was turned on or off. Creates a relationship to the accession table. |
| 2 | `AV_EVENT_ID` | DOUBLE | NOT NULL |  | A unique, internal, system-assigned number that identifies a specific autoverification event row. |
| 3 | `AV_IND` | DOUBLE | NOT NULL |  | Indicates whether this event was to turn on or off autoverification. A value of 0 indicates autoverification was turned off. A value of 1 indicates autoverification was turned on. |
| 4 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal, system-assigned number. |
| 5 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL |  | A unique code value that identifies the specific service resource for which autoverification was turned on or off. |
| 6 | `TASK_ASSAY_CD` | DOUBLE | NOT NULL |  | A unique code value that identifies the specific task assay for which autoverification was turned on or off. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

