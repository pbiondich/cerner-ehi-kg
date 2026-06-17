# RC_D_VARIANCE_ORIGIN

> Contains the data associated to variance attributes for reporting purposes.

**Description:** Revenue Cycle Dimension Variance Origin  
**Table type:** REFERENCE  
**Primary key:** `RC_D_VARIANCE_ORIGIN_ID`  
**Columns:** 10  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `FIRST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the first ETL process started that created this record. |
| 2 | `LAST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the last ETL process started that updated this record. |
| 3 | `MILL_WORKITEM_ORIGIN_CD` | DOUBLE | NOT NULL |  | Stores the code value for the origin of the work item created. |
| 4 | `RC_D_VARIANCE_ORIGIN_ID` | DOUBLE | NOT NULL | PK | Unique generated nuymber that identifies a single row on the RC_D_VARIANCE_ORIGIN table. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 10 | `WORKITEM_ORIGIN_DESC` | VARCHAR(50) | NOT NULL |  | Stores the description of origin for the Wrok Item created. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (3)

| From table | Column |
|------------|--------|
| [RC_F_VARIANCE](RC_F_VARIANCE.md) | `RC_D_VARIANCE_ORIGIN_ID` |
| [RC_F_VAR_CLAIM_SMRY](RC_F_VAR_CLAIM_SMRY.md) | `RC_D_VARIANCE_ORIGIN_ID` |
| [RC_F_VAR_LINE_ITEM_SMRY](RC_F_VAR_LINE_ITEM_SMRY.md) | `RC_D_VARIANCE_ORIGIN_ID` |

