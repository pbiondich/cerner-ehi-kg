# WHC_D_DIAGNOSIS

> WHC Reporting - Dimension Table identifying Diagnosis and associated Nomenclature

**Description:** WHC_D_DIAGNOSIS  
**Table type:** REFERENCE  
**Primary key:** `WHC_D_DIAGNOSIS_ID`  
**Columns:** 8  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DIAGNOSIS_DESC` | VARCHAR(255) | NOT NULL |  | User-readable description of the diagnosis, retrieved by querying the diagnosis (by ENCOUNTER.encntr_id for the delivery encounter for associated pregnancy) and nomenclature (by DIAGNOSIS.NOMENCLATURE_ID) table for diagnosis_display or diag_ftdesc, and source_string, depending on the situation. If diagnosis_display is longer than 1 character use it, but if not, check if diag_ftdesc is longer than 1 character, and if that is not long enough, use the source_string from the nomenclature table. |
| 2 | `MILL_NOMENCLATURE_ID` | DOUBLE |  |  | Foreign key to NOMENCLATURE.NOMENCLATURE_ID, represeting the corresponding diagnosis value in Millennium. |
| 3 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 4 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 5 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 6 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 7 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 8 | `WHC_D_DIAGNOSIS_ID` | DOUBLE | NOT NULL | PK | Primary Key |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [WHC_D_DIAGNOSIS_BRIDGE](WHC_D_DIAGNOSIS_BRIDGE.md) | `WHC_D_DIAGNOSIS_ID` |

