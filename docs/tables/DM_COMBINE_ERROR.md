# DM_COMBINE_ERROR

> This table logs errors from the combine and uncombine processes. The error log will wrap after it reaches the max_value of combine_error_seq.

**Description:** This table logs errors from the combine and uncombine processes.  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 21

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `APPLICATION_FLAG` | DOUBLE |  |  | Tells which type of application sends the transaction. |
| 2 | `CALLING_SCRIPT` | VARCHAR(30) |  |  | The script that was initially called. Dm_combine can either be called directly, or it can be called by dm_uncombine. If dm_combine was called by dm_uncombine, dm_uncombine is the calling_script - if it's called directly, dm_call_combine is the calling_script. |
| 3 | `COMBINE_ERROR_ID` | DOUBLE | NOT NULL |  | A unique identifier for a row in the dm_combine_error table. It is a sequence generated number. Note: once the max_value of combine_error_seq is used, the sequence will start over with a value of 1, and the log will wrap. |
| 4 | `COMBINE_ID` | DOUBLE | NOT NULL |  | If calling_script='dm_uncombine,' this field will be filled out with the value of the combine_id that dm_uncombine attempted to uncombine. If parent_entity='person,' combine_id is a person_combine_id - if parent_entity='encounter', combine_id is an encntr_combine_id. |
| 5 | `COMBINE_MODE` | VARCHAR(20) |  |  | Mode that the combine was run in. Examples: blank means normal; "review" means combine was run again to clean up rows that may have been added after the original combine. |
| 6 | `CREATE_DT_TM` | DATETIME |  |  | Date and time the record was created. |
| 7 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 8 | `ERROR_MSG` | VARCHAR(132) |  |  | If a ccl error is encountered, the error message is stored in this field. |
| 9 | `ERROR_TABLE` | VARCHAR(32) |  |  | The table that was being processed when an error was encountered. This cannot always be captured, so it will not always be filled out. |
| 10 | `ERROR_TYPE` | VARCHAR(50) |  |  | The type of error that was encountered. This type corresponds to an error type within the combine or uncombine code, and is useful for debugging. |
| 11 | `FROM_ID` | DOUBLE | NOT NULL |  | This is the value of the 'from_id' (i.e. from person_id or from encntr_id) during the combine/uncombine. |
| 12 | `OPERATION_TYPE` | VARCHAR(20) | NOT NULL |  | The operation that was being performed when the error was encountered. Useful for errors with 'calling_script' = dm_uncombine. If calling_script='dm_uncombine' and operation_type='combine', dm_uncombine called dm_combine, and an error occurred while dm_combine was executing. |
| 13 | `PARENT_ENTITY` | VARCHAR(32) | NOT NULL |  | Parent entity for the combine/uncombine (i.e. person, encounter). |
| 14 | `RESOLVED_IND` | DOUBLE |  |  | Set to 0 if the error has not been resolved, and 1 if it has been resolved. |
| 15 | `TO_ID` | DOUBLE | NOT NULL |  | This is the value of the 'to_id' (i.e. from person_id or from encntr_id) during the combine/uncombine. |
| 16 | `TRANSACTION_TYPE` | VARCHAR(8) |  |  | The type of transaction that triggers the combine. For ESI transactions, the transaction_type will be the MSH event, e.g., A01, A02, ... For the combine tool, the transaction_type will be blank. |
| 17 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 18 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 19 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 20 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 21 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |

