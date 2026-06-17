# OEN_SCRIPT_HIST_CLOB

> History table for holding oen_script row revisions. This table contains the CLOB fields that save SCRIPT BODY and CHANGE LOG data. (1 row for each type of content)

**Description:** OEN SCRIPT HISTORY - CLOB Fields.  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `OEN_SCRIPT_HIST_CLOB_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 2 | `OEN_SCRIPT_HIST_ID` | DOUBLE | NOT NULL | FK→ | OEN SCRIPT HIST ID - Unique key value for a row in the OEN_SCRIPT_HIST Table |
| 3 | `SCRIPT_CLOB` | LONGTEXT |  |  | A large character field which can contain either the script body, or the Revision Change Log data. A separate text flag column identifies the type. |
| 4 | `SCRIPT_CLOB_CONTENT_TYPE_TFLG` | VARCHAR(20) | NOT NULL |  | script CLOB content type text flag. Can be either SCRIPT BODY or CHANGE LOG. |
| 5 | `UPDT_APPLCTX` | DOUBLE |  |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 6 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 7 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_ID` | DOUBLE |  |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_TASK` | DOUBLE |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `OEN_SCRIPT_HIST_ID` | [OEN_SCRIPT_HIST](OEN_SCRIPT_HIST.md) | `OEN_SCRIPT_HIST_ID` |

