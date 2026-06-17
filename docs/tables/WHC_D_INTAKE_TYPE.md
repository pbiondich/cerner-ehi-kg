# WHC_D_INTAKE_TYPE

> WHC Reporting - Dimension Table identifying Intake Type (Feeding) information

**Description:** WHC_D_INTAKE_TYPE  
**Table type:** REFERENCE  
**Primary key:** `WHC_D_INTAKE_TYPE_ID`  
**Columns:** 8  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `FEEDING_DESC` | VARCHAR(255) |  |  | User-readable description of 'Newborn Intake' value, taken from the clinical result recorded against CKI CERNER!E3108DDF-A5DF-4CDD-BEBE-3D630E081472 (for child) and of 'Feeding Type Newborn' value, taken from the clinical result recorded against CKI CERNER!67FD02F4-5BA3-4EF2-9E3D-16CEB449F5EC (for mother). |
| 2 | `MILL_NOMENCLATURE_ID` | DOUBLE |  |  | Foreign key to NOMENCLATURE.NOMENCLATURE_ID, represeting the corresponding 'Intake type' value in Millennium. |
| 3 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 4 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 5 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 6 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 7 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 8 | `WHC_D_INTAKE_TYPE_ID` | DOUBLE | NOT NULL | PK | Primary Key |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (2)

| From table | Column |
|------------|--------|
| [WHC_F_CHILD](WHC_F_CHILD.md) | `NEWBORN_INTAKE_TYPE_ID` |
| [WHC_F_MOTHER_PREGNANCY](WHC_F_MOTHER_PREGNANCY.md) | `BIRTH_PLAN_FEEDING_ID` |

