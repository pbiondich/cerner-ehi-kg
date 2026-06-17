# MLTM_PRODUCT_STRENGTH

> Contains a textual list of product strengths designed for end user display and a unique identifier for each product strength.

**Description:** List of product strengths for display and unique id for each product strength.  
**Table type:** REFERENCE  
**Primary key:** `PRODUCT_STRENGTH_CODE`  
**Columns:** 7  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `PRODUCT_STRENGTH_CODE` | DOUBLE | NOT NULL | PK | This field contains a unique code for each product strength description. |
| 2 | `PRODUCT_STRENGTH_DESCRIPTION` | VARCHAR(255) |  |  | This field contains full textual descriptions of drug product strengths. |
| 3 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 4 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 5 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 6 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 7 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [MLTM_NDC_MAIN_DRUG_CODE](MLTM_NDC_MAIN_DRUG_CODE.md) | `PRODUCT_STRENGTH_CODE` |

