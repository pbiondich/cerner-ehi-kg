# STRT_MODEL_CUSTOM

> Stores interface specific codes that turns on/off site specific custom functionality.

**Description:** Stores interface specific codes.  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CUSTOM_OPTION` | VARCHAR(50) |  |  | Contains a string that is an interface specific flag to turn on/off custom interface functionality. |
| 2 | `DESCRIPTION` | LONGTEXT |  |  | Contains a description of the custom option. |
| 3 | `DISPLAY` | VARCHAR(50) |  |  | Reserved for future use. |
| 4 | `PROCESS_FLAG` | DOUBLE | NOT NULL |  | This field indicates how the software flag should be processed. 1 - RTL, 2 - Interface, 3 - Both. |
| 5 | `RESULT_SIZE` | DOUBLE |  |  | Size of the user-defined options |
| 6 | `STRT_CONFIG_ID` | DOUBLE | NOT NULL |  | Key field. Contains the DBMS assigned unique value. |
| 7 | `STRT_MODEL_ID` | DOUBLE | NOT NULL | FK→ | Contains the DBMS assigned unique key field value from strt_model table. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `STRT_MODEL_ID` | [STRT_MODEL](STRT_MODEL.md) | `STRT_MODEL_ID` |

