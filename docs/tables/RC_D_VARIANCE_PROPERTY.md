# RC_D_VARIANCE_PROPERTY

> Contains the data associated to variance attributes for Reporting purposes

**Description:** Revenue Cycle Dimension Variance Property  
**Table type:** REFERENCE  
**Primary key:** `RC_D_VARIANCE_PROPERTY_ID`  
**Columns:** 14  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 4 | `FIRST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the first ETL process started that created this record. |
| 5 | `LAST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the last ETL process started that updated this record. |
| 6 | `MILL_PFT_ENTITY_STATUS_CD` | DOUBLE | NOT NULL |  | Contains all the current state for the work Items. |
| 7 | `RC_D_VARIANCE_PROPERTY_ID` | DOUBLE | NOT NULL | PK | Uniquely identifies data associated to variance attributes for reporting purposes. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 13 | `VARIANCE_STATUS` | VARCHAR(40) |  |  | Contains all the statuses associated to a variance work item based on the MILL_PFT_ENTITY_STATUS_CD |
| 14 | `WORK_ITEM_ACTION` | VARCHAR(40) |  |  | Contains supported performed actions on this queue item |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (3)

| From table | Column |
|------------|--------|
| [RC_F_VARIANCE](RC_F_VARIANCE.md) | `RC_D_VARIANCE_PROPERTY_ID` |
| [RC_F_VAR_CLAIM_SMRY](RC_F_VAR_CLAIM_SMRY.md) | `RC_D_VARIANCE_PROPERTY_ID` |
| [RC_F_VAR_LINE_ITEM_SMRY](RC_F_VAR_LINE_ITEM_SMRY.md) | `RC_D_VARIANCE_PROPERTY_ID` |

