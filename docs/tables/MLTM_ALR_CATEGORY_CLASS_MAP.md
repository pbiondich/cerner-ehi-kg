# MLTM_ALR_CATEGORY_CLASS_MAP

> This table is used to assign allergy categories to an allergy drug class. For example, the category cephalosporins is assigned to the class penicillins and related drugs in this table. (For purposes of working with Multum's allergy tables, allergy classes can be defined as a group of allergy categories that share allergic cross-reactivity potential.)

**Description:** Multum allergy category class map  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ALR_CATEGORY_ID` | DOUBLE | NOT NULL | FK→ | FK from MLTM ALR CATEGORY table |
| 2 | `CLASS_ID` | DOUBLE | NOT NULL | FK→ | The allergy drug class Identifier. Classes can be defined as a group of allergy categories that share allergic cross-reactivity potential.) |
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
| `CLASS_ID` | [MLTM_ALR_CLASS](MLTM_ALR_CLASS.md) | `CLASS_ID` |

