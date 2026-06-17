# KIA_EVENT_SET_CODE_VALUE_SNP

> This request is to create new snapshot table for code_value (code set 93 only).

**Description:** KIA EVENT SET CODE_VALUE SNAPSHOT  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 27

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_DT_TM` | DATETIME |  |  | Same as in CODE_VALUE table |
| 2 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 4 | `ACTIVE_TYPE_CD` | DOUBLE | NOT NULL |  | Same as in CODE_VALUE table |
| 5 | `BEGIN_EFFECTIVE_DT_TM` | DATETIME |  |  | Same as in CODE_VALUE table |
| 6 | `CDF_MEANING` | VARCHAR(12) |  |  | Same as in CODE_VALUE table |
| 7 | `CKI` | VARCHAR(255) |  |  | Same as in CODE_VALUE table |
| 8 | `CODE_SET` | DOUBLE | NOT NULL |  | Same as in CODE_VALUE table |
| 9 | `CODE_VALUE` | DOUBLE | NOT NULL |  | Same as in CODE_VALUE table |
| 10 | `COLLATION_SEQ` | DOUBLE |  |  | Same as in CODE_VALUE table |
| 11 | `CONCEPT_CKI` | VARCHAR(255) |  |  | Same as in CODE_VALUE table |
| 12 | `DATA_STATUS_CD` | DOUBLE | NOT NULL |  | Data status indicates a level of authenticity of the row data. Typically this will either be AUTHENTICATED or UNAUTHENTICATED. |
| 13 | `DATA_STATUS_DT_TM` | DATETIME |  |  | The date and time that the data_status_cd was set. |
| 14 | `DATA_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the data_status_cd to be set or change. |
| 15 | `DEFINITION` | VARCHAR(100) |  |  | Same as in CODE_VALUE table |
| 16 | `DESCRIPTION` | VARCHAR(60) |  |  | Same as in CODE_VALUE table |
| 17 | `DISPLAY` | VARCHAR(40) |  |  | Same as in CODE_VALUE table |
| 18 | `DISPLAY_KEY` | VARCHAR(40) |  |  | Same as in CODE_VALUE table |
| 19 | `DISPLAY_KEY_A_NLS` | VARCHAR(160) |  |  | Same as in CODE_VALUE table |
| 20 | `DISPLAY_KEY_NLS` | VARCHAR(255) |  |  | NO LONGER USED |
| 21 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 22 | `INACTIVE_DT_TM` | DATETIME |  |  | Same as in CODE_VALUE table |
| 23 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 24 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 25 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 26 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 27 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

