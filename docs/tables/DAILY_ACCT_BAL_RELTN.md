# DAILY_ACCT_BAL_RELTN

> STORE ADDITIONAL INFORAMTION RELATED TO DAILY ACCT BAL ROW

**Description:** DAILY ACCOUNT BALANCE RELATION  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DAILY_ACCT_BAL_ID` | DOUBLE | NOT NULL | FK→ | DAILY_ACCT_BAL_ID is the key to identify the parent row in the DAILY_ACCT_BAL table for this DAILY_ACCT_BAL_RELTN row |
| 2 | `DAILY_ACCT_BAL_RELTN_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 3 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | PARENT_ENTITY_ID is the key to identify a specific row in a table as set by the PARENT_ENTITY_NAME |
| 4 | `PARENT_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | PARENT_ENTITY_NAME holds the table name for the PARENT_ENTITY_ID key |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `VALUE_AMT` | DOUBLE | NOT NULL |  | The VALUE_AMT is a child transaction amount directly related to a specific PARENT_ENTITY_ID\PARENT_ENTITY_NAME. The VALUE_CRITERIA_CD will determine how this amount will be used. |
| 11 | `VALUE_CRITERIA_CD` | DOUBLE | NOT NULL |  | Specifies the VALUE_CRITERIA_CD that describes how this DAILY_ACCT_BAL_RELTN row is related back to the parent DAILY_ACCT_BAL row. |
| 12 | `VALUE_CRITERIA_NBR` | DOUBLE | NOT NULL |  | The VALUE_CRITERIA_NBR is defined by the VALUE_CRITERIA_CD |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DAILY_ACCT_BAL_ID` | [DAILY_ACCT_BAL](DAILY_ACCT_BAL.md) | `DAILY_ACCT_BAL_ID` |

