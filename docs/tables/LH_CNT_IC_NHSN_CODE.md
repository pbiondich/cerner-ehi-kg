# LH_CNT_IC_NHSN_CODE

> Lighthouse reference table for Infection Control that stores the NHSN code value information for CDA components submitted to NHSN>

**Description:** LH_CNT_IC_NHSN_CODE  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CODE_MEANING` | VARCHAR(200) | NOT NULL |  | The unique identifier of the NHSN commit |
| 2 | `CODE_SYSTEM` | VARCHAR(200) |  |  | The code system of the NHSN code value. |
| 3 | `CODE_SYSTEM_NAME` | VARCHAR(200) |  |  | The display name of the code system of the NHSN code value. |
| 4 | `CODE_TXT` | VARCHAR(100) |  |  | The actual NHSN code value to be used within the CDA |
| 5 | `CODE_TYPE` | VARCHAR(200) |  |  | The type of the NHSN code value. |
| 6 | `DISPLAY_NAME` | VARCHAR(200) |  |  | The display name of the NHSN code value. |
| 7 | `LH_CNT_IC_NHSN_CODE_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_CNT_IC_NHSN_CODE table. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

