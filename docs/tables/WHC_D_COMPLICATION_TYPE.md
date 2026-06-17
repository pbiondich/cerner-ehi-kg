# WHC_D_COMPLICATION_TYPE

> WHC Reporting - Dimension Table identifying Complicatiion Type and associated Nomenclature

**Description:** WHC_D_COMPLICATION_TYPE  
**Table type:** REFERENCE  
**Primary key:** `WHC_D_COMPLICATION_TYPE_ID`  
**Columns:** 8  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `COMPLICATION_DESC` | VARCHAR(255) |  |  | user-readable description of 'complication type' value, taken from the clinical result recorded against cki cerner!07b2090c-7ae6-4e14-a702-c20ee3e7d4fd , cerner!2d13d00f-bfd4-44da-bfc3-73392a695b93 and CERNER!28CD17AC-F1BD-4AE3-A9F6-1282F19618AB |
| 2 | `MILL_NOMENCLATURE_ID` | DOUBLE |  |  | Primary Key value from nomenclature.nomenclature_id, represeting the corresponding -complication type- value in millennium. |
| 3 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 4 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 5 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 6 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 7 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `WHC_D_COMPLICATION_TYPE_ID` | DOUBLE | NOT NULL | PK | PRIMARY KEY |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [WHC_D_COMPLICATION_BRIDGE](WHC_D_COMPLICATION_BRIDGE.md) | `WHC_D_COMPLICATION_TYPE_ID` |

