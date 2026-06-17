# MLTM_REF_DRUG

> This table contains the links between clinical content in VantageRx Database and the specific medical articles and references from which the content is derived.

**Description:** Reference Drug  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DRUG_IDENTIFIER` | VARCHAR(6) | NOT NULL | FK→ | This field contains Multum's identification codes for generic drugs. |
| 2 | `FUNCTION_ID` | DOUBLE | NOT NULL |  | FK from Functin_Type table |
| 3 | `KEYWORD` | VARCHAR(45) |  |  | Drug Reference Keyword |
| 4 | `REF_ID` | DOUBLE | NOT NULL | FK→ | FK from Multum REF_DETAIL table. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DRUG_IDENTIFIER` | [MLTM_DRUG_ID](MLTM_DRUG_ID.md) | `DRUG_IDENTIFIER` |
| `REF_ID` | [MLTM_REF_DETAIL](MLTM_REF_DETAIL.md) | `REF_ID` |

