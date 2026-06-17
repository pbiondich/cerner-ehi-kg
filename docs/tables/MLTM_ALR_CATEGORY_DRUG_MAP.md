# MLTM_ALR_CATEGORY_DRUG_MAP

> This table is used to assign drugs to an allergy category. For example, the drug cephalexin is assigned to the category cephalosporins in this table.

**Description:** Multum allergy category drug map  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ALR_CATEGORY_ID` | DOUBLE | NOT NULL | FK→ | FK from the MLTM_ALR_CATEGORY table |
| 2 | `DRUG_IDENTIFIER` | VARCHAR(6) | NOT NULL | FK→ | This field contains Multum's identification codes for generic drugs. These are extremely important codes for developers who are using Multum's database products because they serve as the primary link to all of Multum's advanced clinical services. Multum's drug_id is always of the form "d#####". Together, the drug_id and the ndc_main_Multum_drug_code (MMDC), described elsewhere in this guide, provide a mechanism for relating high-level clinical drug information (like drug dosing algorithms, |
| 3 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 4 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 5 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 6 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 7 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ALR_CATEGORY_ID` | [MLTM_ALR_CATEGORY](MLTM_ALR_CATEGORY.md) | `ALR_CATEGORY_ID` |
| `DRUG_IDENTIFIER` | [MLTM_DRUG_ID](MLTM_DRUG_ID.md) | `DRUG_IDENTIFIER` |

