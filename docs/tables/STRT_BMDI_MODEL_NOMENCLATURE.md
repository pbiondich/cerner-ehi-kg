# STRT_BMDI_MODEL_NOMENCLATURE

> Identifies the alpha translations that can be performed for a given strt_model.

**Description:** Starter BMDI Model Nomenclature  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ALPHA_TRANSLATION` | VARCHAR(50) | NOT NULL |  | Resulting translated value. |
| 2 | `DEFAULT_VALUE` | VARCHAR(50) | NOT NULL |  | Default Device value requiring translation |
| 3 | `STRT_MODEL_ID` | DOUBLE | NOT NULL | FK→ | This value is used to standardize Model information across systems. |
| 4 | `STRT_MODEL_NOMENCLATURE_ID` | DOUBLE | NOT NULL |  | Unique identifier to be used as a primary key for this table. |
| 5 | `STRT_MODEL_PARAMETER_ID` | DOUBLE | NOT NULL | FK→ | Unique identifier for a parameter. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `STRT_MODEL_ID` | [STRT_MODEL](STRT_MODEL.md) | `STRT_MODEL_ID` |
| `STRT_MODEL_PARAMETER_ID` | [STRT_BMDI_MODEL_PARAMETER](STRT_BMDI_MODEL_PARAMETER.md) | `STRT_MODEL_PARAMETER_ID` |

