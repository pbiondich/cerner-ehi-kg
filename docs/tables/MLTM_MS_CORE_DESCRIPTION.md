# MLTM_MS_CORE_DESCRIPTION

> This table contains a listing of information about specific NDC-labeled medical items.

**Description:** Multum Medical Supplies Core Description  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `MS_BRAND_DESCRIPTION` | VARCHAR(45) | NOT NULL |  | This field contains drug names as they appear on the label of a medical supply. |
| 2 | `MS_CATEGORY` | VARCHAR(50) | NOT NULL |  | This field provides a general textual description of the medical supply type: Medical Supplies, Diagnostic Supplies, Nutritional Supplements |
| 3 | `MS_CATEGORY_ID` | DOUBLE | NOT NULL | FK→ | This field assigns a more specific category to a medical supply. |
| 4 | `MS_INNER_PACKAGE_DESCRIPTION` | VARCHAR(30) |  |  | This field contains a textual description of the packaging units. |
| 5 | `MS_INNER_PACKAGE_SIZE` | DOUBLE | NOT NULL |  | This field represents the number of individual units present in the innermost packaging of a drug. |
| 6 | `MS_NDC_CODE` | VARCHAR(11) | NOT NULL |  | The National Drug Code is the standard 11 digit identifier for each drug product, as recognized by HCFA, other federal and state agencies, and many commercial enterprises. It is unique to each specific product. The first 5 numbers identify the manufacturer of a product. The second 4 numbers identify the product, and the last 2 numbers identify the package size of that product. |
| 7 | `MS_OUTER_PACKAGE_SIZE` | DOUBLE |  |  | This field designates the total number of inner packages present in the final packaged product. Not all products require an outer package size for a complete representation of the packaging. (The package unit may suffice.) |
| 8 | `MS_SOURCE_DESCRIPTION` | VARCHAR(120) | NOT NULL |  | This field contains the names of manufacturers, redistributors, and repackagers of the medical product. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `MS_CATEGORY_ID` | [MLTM_MS_CATEGORIES](MLTM_MS_CATEGORIES.md) | `MS_CATEGORY_ID` |

