# MLTM_DUPLICATION_SUB_XREF

> Therapeutic duplication categories. It allows assignment of one or more (sub) categories to a more general category.

**Description:** Multum Duplication Sub Cross-Reference  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `MULTUM_CATEGORY_ID` | DOUBLE | NOT NULL | FK→ | Used to assign a therapeutic/chemical category to a specific drug. |
| 2 | `SUB_CATEGORY_ID` | DOUBLE | NOT NULL | FK→ | This field is used to assign a therapeutic/chemical sub-category to a specific drug. |
| 3 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 4 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 5 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 6 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 7 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `MULTUM_CATEGORY_ID` | [MLTM_DUPLICATION_CATEGORIES](MLTM_DUPLICATION_CATEGORIES.md) | `MULTUM_CATEGORY_ID` |
| `SUB_CATEGORY_ID` | [MLTM_DUPLICATION_CATEGORIES](MLTM_DUPLICATION_CATEGORIES.md) | `MULTUM_CATEGORY_ID` |

