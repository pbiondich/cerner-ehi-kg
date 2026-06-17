# RC_D_VARIANCE_ACTION

> Contains the data associated to variance attributes for reporting purposes.

**Description:** Revenue Cycle Dimension Variance Action  
**Table type:** REFERENCE  
**Primary key:** `RC_D_VARIANCE_ACTION_ID`  
**Columns:** 15  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION` | VARCHAR(200) |  |  | Contains action display values that can be applied to work item based on the MILL_ACTION_CD or MILL_REASON_CD. |
| 2 | `ACTION_DESCRIPTION` | VARCHAR(200) |  |  | Contains the description of the corresponding action applied on the work item based on the MILL_REASON_CD column. |
| 3 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 4 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 5 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 6 | `FIRST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the first ETL process started that created this record. |
| 7 | `LAST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the last ETL process started that updated this record. |
| 8 | `MILL_ACTION_CD` | DOUBLE | NOT NULL |  | Contains the user custom action code value applied to the work item. |
| 9 | `MILL_REASON_CD` | DOUBLE | NOT NULL |  | Applied action code or reason code in case system applied action code. |
| 10 | `RC_D_VARIANCE_ACTION_ID` | DOUBLE | NOT NULL | PK | Uniquely identifies data associated to variance attributes for Reporting purposes. |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (3)

| From table | Column |
|------------|--------|
| [RC_F_VARIANCE](RC_F_VARIANCE.md) | `RC_D_VARIANCE_ACTION_ID` |
| [RC_F_VAR_CLAIM_SMRY](RC_F_VAR_CLAIM_SMRY.md) | `RC_D_VARIANCE_ACTION_ID` |
| [RC_F_VAR_LINE_ITEM_SMRY](RC_F_VAR_LINE_ITEM_SMRY.md) | `RC_D_VARIANCE_ACTION_ID` |

