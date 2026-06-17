# CNT_SECTION_DTA_R

> SECTION DTA RELATION

**Description:** CNT SECTION DTA R  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CNT_DTA_KEY_ID` | DOUBLE | NOT NULL | FK→ | Sequence generated ID (Value: 0.0) |
| 2 | `CNT_SECTION_DTA_R_ID` | DOUBLE | NOT NULL |  | Sequence generated ID - PRIMARY KEY |
| 3 | `CNT_SECTION_KEY_ID` | DOUBLE | NOT NULL | FK→ | Sequence generated ID (Value: 0.0) |
| 4 | `IGNORE_IND` | DOUBLE | NOT NULL |  | Indicator for Bedrock Wizard whether to ignore section to DTA relationship |
| 5 | `SECTION_UID` | VARCHAR(100) | NOT NULL |  | Unique identifier for Section |
| 6 | `TASK_ASSAY_UID` | VARCHAR(100) | NOT NULL |  | Unique identifier for DTA |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CNT_DTA_KEY_ID` | [CNT_DTA_KEY2](CNT_DTA_KEY2.md) | `CNT_DTA_KEY_ID` |
| `CNT_SECTION_KEY_ID` | [CNT_SECTION_KEY2](CNT_SECTION_KEY2.md) | `CNT_SECTION_KEY2_ID` |

