# MLTM_DOSE_FORM

> This table contains a listing of dose forms (cream, tablet, suppository, etc.), along with an abbreviation and a unique identifier for each dose form.

**Description:** This table contains a listing of dose forms.  
**Table type:** REFERENCE  
**Primary key:** `DOSE_FORM_CODE`  
**Columns:** 8  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DOSE_FORM_ABBR` | VARCHAR(30) |  |  | This field contains Multum's abbreviations for dosage forms. |
| 2 | `DOSE_FORM_CODE` | DOUBLE | NOT NULL | PK | This field contains a numeric designation for a dose form. |
| 3 | `DOSE_FORM_DESCRIPTION` | VARCHAR(255) |  |  | This field contains the full text description of the product's dose form. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [MLTM_NDC_MAIN_DRUG_CODE](MLTM_NDC_MAIN_DRUG_CODE.md) | `DOSE_FORM_CODE` |

