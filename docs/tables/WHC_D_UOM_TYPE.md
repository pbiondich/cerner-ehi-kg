# WHC_D_UOM_TYPE

> WHC Reporting - Dimension table identifying Unit of Measure Tye and associated Nomenclature

**Description:** WHC_D_UOM_TYPE  
**Table type:** REFERENCE  
**Primary key:** `WHC_D_UOM_TYPE_ID`  
**Columns:** 8  
**Referenced by:** 8 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `MILL_CODEVALUE_ID` | DOUBLE |  |  | This value comes from code_value.code_value, represeting the corresponding -unit of mesure type- value in millennium. |
| 2 | `UOM_DESC` | VARCHAR(255) |  |  | user-readable description of -Unit Of Measure Type- value |
| 3 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 4 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 5 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 6 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 7 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `WHC_D_UOM_TYPE_ID` | DOUBLE | NOT NULL | PK | PRIMARY KEY |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (8)

| From table | Column |
|------------|--------|
| [WHC_F_CHILD](WHC_F_CHILD.md) | `ABDOMINAL_CIRCUMFRNCE_UOM_ID` |
| [WHC_F_CHILD](WHC_F_CHILD.md) | `BIRTH_HEIGHT_UOM_ID` |
| [WHC_F_CHILD](WHC_F_CHILD.md) | `BIRTH_WEIGHT_UOM_ID` |
| [WHC_F_CHILD](WHC_F_CHILD.md) | `CHEST_CIRCUMFERENCE_UOM_ID` |
| [WHC_F_CHILD](WHC_F_CHILD.md) | `HEAD_CIRCUMFERNENCE_UOM_ID` |
| [WHC_F_DELIVERY](WHC_F_DELIVERY.md) | `EBL_ANTEPARTUM_NBR_UOM_ID` |
| [WHC_F_DELIVERY](WHC_F_DELIVERY.md) | `EBL_DELIVERY_NBR_UOM_ID` |
| [WHC_F_DELIVERY](WHC_F_DELIVERY.md) | `EBL_POSTPART_NBR_UOM_ID` |

