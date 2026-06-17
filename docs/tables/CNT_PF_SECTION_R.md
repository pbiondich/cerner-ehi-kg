# CNT_PF_SECTION_R

> PF SECTION RELTN

**Description:** CNT PF SECTION R  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CNT_PF_KEY_ID` | DOUBLE | NOT NULL | FK→ | Sequence generated ID (Value: 0.0) - FK from CNT_PF_KEY2 |
| 2 | `CNT_PF_SECTION_R_ID` | DOUBLE | NOT NULL |  | Sequence generated ID - PRIMARY KEY |
| 3 | `CNT_SECTION_KEY2_ID` | DOUBLE | NOT NULL | FK→ | Sequence generated ID (Value: 0.0) - FK from CNT_SECTION_KEY2 |
| 4 | `FORM_UID` | VARCHAR(100) | NOT NULL |  | Unique identifier for PowerForm |
| 5 | `IGNORE_IND` | DOUBLE | NOT NULL |  | Indicates whether to ignore the relationship in the Bedrock wizard |
| 6 | `SECTION_SEQ` | DOUBLE |  |  | Sequence of the section within the PowerForm |
| 7 | `SECTION_UID` | VARCHAR(100) | NOT NULL |  | Unique identifier for Section |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CNT_PF_KEY_ID` | [CNT_PF_KEY2](CNT_PF_KEY2.md) | `CNT_PF_KEY_ID` |
| `CNT_SECTION_KEY2_ID` | [CNT_SECTION_KEY2](CNT_SECTION_KEY2.md) | `CNT_SECTION_KEY2_ID` |

