# MLTM_ADDITIONAL_DOSEFORM

> This table contains a listing of additional terms that may be used to describe a solid oral dosage form (such as sugar coated, film coated, or layered). Each description has a unique identifier.

**Description:** Multum additional doseform  
**Table type:** REFERENCE  
**Primary key:** `ADDITIONAL_DOSEFORM_ID`  
**Columns:** 7  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ADDITIONAL_DOSEFORM_DESC` | VARCHAR(255) |  |  | additional terms that may be used to describe a solid oral dosage form |
| 2 | `ADDITIONAL_DOSEFORM_ID` | DOUBLE | NOT NULL | PK | The PK value for this table. |
| 3 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 4 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 5 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 6 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 7 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [MLTM_NDC_IMAGE](MLTM_NDC_IMAGE.md) | `ADDITIONAL_DOSEFORM_ID` |

