# CV_ACRONYM

> Defines replacement strings used to expand acronyms placed in documentation using a default/ user preference model. If the current provider does not have personal acronyms defined, the default set of acronyms will be used (i.e., ones for which the provider id is zero).

**Description:** CV ACRONYM  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACRONYM_CATEGORY_CD` | DOUBLE | NOT NULL | FK→ | Indicates the Acronym Category to which the Acronym belongs to. |
| 2 | `ACRONYM_STR` | VARCHAR(32) | NOT NULL |  | The acronym string that will be replaced. |
| 3 | `COLLATION_SEQ` | DOUBLE | NOT NULL |  | Used to order acronyms with ties decided alphabetically by acronym. |
| 4 | `CV_ACRONYM_ID` | DOUBLE | NOT NULL |  | Primary key |
| 5 | `PROVIDER_ID` | DOUBLE | NOT NULL | FK→ | Provider Id. The provider for whom this acronym is defined. |
| 6 | `REPLACEMENT_STR` | VARCHAR(4000) | NOT NULL |  | The string used to replace the acronym string. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ACRONYM_CATEGORY_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `PROVIDER_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

