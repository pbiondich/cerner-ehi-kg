# WHC_D_COMPLICATION_GROUP

> A Dimension Group table to allow the connection of the Fact table row to many Complication Dimensions

**Description:** WHC_D_COMPLICATION_GROUP  
**Table type:** REFERENCE  
**Primary key:** `WHC_D_COMPLICATION_GROUP_ID`  
**Columns:** 6  
**Referenced by:** 4 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 2 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 3 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 4 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 5 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 6 | `WHC_D_COMPLICATION_GROUP_ID` | DOUBLE | NOT NULL | PK | PRIMARY KEY |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (4)

| From table | Column |
|------------|--------|
| [WHC_D_COMPLICATION_BRIDGE](WHC_D_COMPLICATION_BRIDGE.md) | `WHC_D_COMPLICATION_GROUP_ID` |
| [WHC_F_CHILD](WHC_F_CHILD.md) | `FETAL_COMPLICATION_GROUP_ID` |
| [WHC_F_CHILD](WHC_F_CHILD.md) | `NEONATE_COMPLICATION_GROUP_ID` |
| [WHC_F_DELIVERY](WHC_F_DELIVERY.md) | `MATERNAL_COMPLICATION_GROUP_ID` |

