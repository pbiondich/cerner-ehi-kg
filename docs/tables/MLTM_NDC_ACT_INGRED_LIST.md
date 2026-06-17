# MLTM_NDC_ACT_INGRED_LIST

> This table identifies all of the active ingredients (and their individual strengths) in each group of drug products that shares the same Main Multum Drug Code (MMDC)

**Description:** Multum NDC Active Ingredient List  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_INGREDIENT_CODE` | DOUBLE | NOT NULL | FK→ | This field contains the code from the active ingredient table (Foreign Key) |
| 2 | `INGREDIENT_STRENGTH_CODE` | DOUBLE | NOT NULL |  | This field contains a unique code for each ingredient strength |
| 3 | `MAIN_MULTUM_DRUG_CODE` | DOUBLE | NOT NULL |  | The Main Multum Drug Code is Multum's designator for groups of similar drug products. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ACTIVE_INGREDIENT_CODE` | [MLTM_NDC_ACTIVE_INGRED](MLTM_NDC_ACTIVE_INGRED.md) | `ACTIVE_INGREDIENT_CODE` |

