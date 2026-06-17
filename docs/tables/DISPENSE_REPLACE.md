# DISPENSE_REPLACE

> Tracks when a dispense was replaced by a new dispense, and which dispense replaced it.

**Description:** Dispense Replace  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 3 | `CREATE_DT_TM` | DATETIME |  |  | The date and time the replacement dispense was created. |
| 4 | `DISPENSE_REPLACE_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the DISPENSE_REPLACE table. |
| 5 | `INIT_DISPENSE_HX_ID` | DOUBLE | NOT NULL | FK→ | The DISPENSE_HX_ID of the dispense from the DISPENSE_HX table that was replaced by a new dispense. The initiating dispense that caused the replacement. |
| 6 | `ORIG_DISPENSE_HX_ID` | DOUBLE | NOT NULL | FK→ | The very first dispense that got replaced in a chain of replaced dispenses. |
| 7 | `PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The personnel who prompted the dispense to be replaced. |
| 8 | `REPLACE_DISPENSE_HX_ID` | DOUBLE | NOT NULL | FK→ | The DISPENSE_HX_ID of the dispense from the DISPENSE_HX table that was created to replace the previous dispense. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `INIT_DISPENSE_HX_ID` | [DISPENSE_HX](DISPENSE_HX.md) | `DISPENSE_HX_ID` |
| `ORIG_DISPENSE_HX_ID` | [DISPENSE_HX](DISPENSE_HX.md) | `DISPENSE_HX_ID` |
| `PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `REPLACE_DISPENSE_HX_ID` | [DISPENSE_HX](DISPENSE_HX.md) | `DISPENSE_HX_ID` |

