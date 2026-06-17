# ONC_CHEMO_VERIFY

> Stores the chemotherapy dosing initiated plan verification status and action information.

**Description:** CHEMOTHERAPY DOSING VERIFICATION STATUS  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 18

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_DT_TM` | DATETIME |  |  | To store the verified action date and time . |
| 2 | `ACTION_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Person_id of the person from personnel table(prsnl) that caused the last action in the table. |
| 3 | `ACTION_TYPE_CD` | DOUBLE | NOT NULL |  | Primary key of CODE_VALUE table for code_set 1305. To store the status code for the specific action. |
| 4 | `ACTION_TYPE_DESC` | VARCHAR(256) |  |  | To store the verification action status information. |
| 5 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 6 | `COMMENT_TXT` | VARCHAR(256) |  |  | To store the user comments, while withdrawing the verify action; |
| 7 | `LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Primary key from LONG_TEXT table,in this case used to get order information in xml format from LONG_TEXT . |
| 8 | `ONC_CHEMO_VERIFY_ID` | DOUBLE | NOT NULL |  | Primary key of the ONC_CHEMO_VERIFY table |
| 9 | `PLAN_ID` | DOUBLE | NOT NULL |  | Foreign key for Pathway Table, in this case used for plan information from PW_GROUP_NBR . |
| 10 | `POSITION_FREE_TEXT` | VARCHAR(256) |  |  | To store the free text name of position type. |
| 11 | `POSITION_ROLE_CD` | DOUBLE | NOT NULL | FK→ | Primary key of CODE_VALUE table for code_set 88. It is used to store the position code for the person. |
| 12 | `POSITION_ROLE_TYPE_ID` | DOUBLE | NOT NULL |  | ** OBSOLETE ** this field is not used. it has been replaced, functionally, by column POSITION_ROLE_CD. |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `VERIFICATION_GROUP` | DOUBLE |  |  | To store the verification group number for initial verifications and subsequent re-vertifications; |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ACTION_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `POSITION_ROLE_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |

