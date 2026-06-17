# WHC_D_CSECTION_INDCN

> WHC Reporting - Dimension Table identifying Csection Indication information and associated Nomenclature

**Description:** WHC_D_CSECTION_INDCN  
**Table type:** REFERENCE  
**Primary key:** `WHC_D_CSECTION_INDCN_ID`  
**Columns:** 8  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CSECTION_INDICATION_DESC` | VARCHAR(255) |  |  | User-readable description of 'C-section Indication' value, taken from the clinical result recorded against CKI CERNER!7963B3E1-0F6C-40A0-AA21-4D57220CF9AE. |
| 2 | `MILL_NOMENCLATURE_ID` | DOUBLE | NOT NULL |  | Foreign key to NOMENCLATURE.NOMENCLATURE_ID, represeting the corresponding 'C-section Indication' value in Millennium. |
| 3 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 4 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 5 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 6 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 7 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 8 | `WHC_D_CSECTION_INDCN_ID` | DOUBLE | NOT NULL | PK | Primary Key |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [WHC_F_DELIVERY_CHILD](WHC_F_DELIVERY_CHILD.md) | `CSECTION_INDCN_ID` |

