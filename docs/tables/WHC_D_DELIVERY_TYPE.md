# WHC_D_DELIVERY_TYPE

> WHC Reporting - Dimension Table identifying Delivery Type information and associated Nomenclature

**Description:** WHC_D_DELIVERY_TYPE  
**Table type:** REFERENCE  
**Primary key:** `WHC_D_DELIVERY_TYPE_ID`  
**Columns:** 9  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DELIVERY_TYPE_DESC` | VARCHAR(255) |  |  | User-readable description of 'delivery type' value, taken from clinical result recorded against cki cerner!0b07155e-2e5c-461f-ade6-cb5768257107 for millennium pregnancy or delivery method' value recorded against pregnancy child record for historical pregnancy |
| 2 | `MILL_CODEVALUE_ID` | DOUBLE | NOT NULL |  | foreign key to code_value.code_value, represeting the corresponding 'delivery method' value in millennium. |
| 3 | `MILL_NOMENCLATURE_ID` | DOUBLE |  |  | Foreign key to NOMENCLATURE.NOMENCLATURE_ID, represeting the corresponding 'Delivery type' value in Millennium. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `WHC_D_DELIVERY_TYPE_ID` | DOUBLE | NOT NULL | PK | Primary Key |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (2)

| From table | Column |
|------------|--------|
| [WHC_F_CHILD](WHC_F_CHILD.md) | `DELIVERY_TYPE_ID` |
| [WHC_F_DELIVERY_CHILD](WHC_F_DELIVERY_CHILD.md) | `DELIVERY_TYPE_ID` |

