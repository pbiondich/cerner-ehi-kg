# WF_XFI_SHIFT_RESP

> This is a staging table storing the responsibilities associated to the shift coming from third party system.

**Description:** Workforce Interface Shift Responsibility  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_FLAG` | DOUBLE |  |  | Flag used to determine the type of action to apply to the record. |
| 2 | `CONTRIBUTOR_CD` | DOUBLE | NOT NULL |  | The contributor code is used when building an alias for a code_value to determine the matching alias. |
| 3 | `PROCESS_FLAG` | DOUBLE |  |  | Flag used to determine the status of the reocrd being processed. |
| 4 | `RESPONSIBILITY_CD` | DOUBLE | NOT NULL |  | The responsibility of the person for the specified shift. |
| 5 | `RESPONSIBILITY_TXT` | VARCHAR(60) |  |  | The responsibility of the person for the specified shift. |
| 6 | `TRANSACTION_ID` | DOUBLE | NOT NULL |  | Uniquely identifies a row on the wf_xfi_shift_resp table. Primary Key. |
| 7 | `TRANS_PARENT_ID` | DOUBLE | NOT NULL |  | Relates the workforce interface shift responsibility record to a specific workforce interface shift schedule record. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

