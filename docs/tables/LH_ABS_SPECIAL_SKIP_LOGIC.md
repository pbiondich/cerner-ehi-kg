# LH_ABS_SPECIAL_SKIP_LOGIC

> Holds skip information for special skip cases

**Description:** lh_abs_special_skip_logic  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 16

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 2 | `BR_DATAMART_CATEGORY_ID` | DOUBLE | NOT NULL | FK→ | Category_id the skip logic belongs to |
| 3 | `CHECK_KEY` | VARCHAR(30) | NOT NULL |  | Identifier to group a given skip logic |
| 4 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 5 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 6 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time the record was first loaded into the table. |
| 7 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL | FK→ | Identifies the unique source within the delivery network responsible for supplying the data. |
| 8 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time the record was last loaded into the table. |
| 9 | `LH_ABS_QUESTION_ID` | DOUBLE | NOT NULL | FK→ | Question that is skipped in the logic case |
| 10 | `LH_ABS_SPECIAL_SKIP_LOGIC_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the lh_abs_special_skip_logic table. |
| 11 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 12 | `LOGIC_TYPE` | VARCHAR(30) | NOT NULL |  | Type of logic |
| 13 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 14 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. |
| 15 | `UPDT_SOURCE` | VARCHAR(50) |  |  | The script name responsible for updating the record. |
| 16 | `UPDT_TASK` | VARCHAR(50) |  |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BR_DATAMART_CATEGORY_ID` | [BR_DATAMART_CATEGORY](BR_DATAMART_CATEGORY.md) | `BR_DATAMART_CATEGORY_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_ABS_QUESTION](LH_ABS_QUESTION.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `LH_ABS_QUESTION_ID` | [LH_ABS_QUESTION](LH_ABS_QUESTION.md) | `LH_ABS_QUESTION_ID` |

