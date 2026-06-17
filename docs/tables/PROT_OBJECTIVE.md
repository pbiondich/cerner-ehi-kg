# PROT_OBJECTIVE

> Stores the objectives associated with the amendment

**Description:** PROT OBJECTIVE  
**Table type:** REFERENCE  
**Primary key:** `PROT_OBJECTIVE_ID`  
**Columns:** 15  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 2 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 3 | `LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | References the long_text for the objective. Foreign Key from Long_Text_Reference table. |
| 4 | `OBJECTIVE` | VARCHAR(2000) | NOT NULL |  | *OBSOLETE - Replaced by value associate with LONG_TEXT_ID from Long Text Reference |
| 5 | `OBJECTIVE_NBR` | VARCHAR(30) | NOT NULL |  | This field contains a number indicating whether the objective is the first, second, third, ... nth objective |
| 6 | `OBJECTIVE_TYPE_CD` | DOUBLE | NOT NULL |  | This field contains an indicator as to whether the objective is a primary objective or secondary objective. |
| 7 | `PARENT_PROT_OBJECTIVE_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the parent of the current objective |
| 8 | `PROT_AMENDMENT_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the Amendment |
| 9 | `PROT_OBJECTIVE_ID` | DOUBLE | NOT NULL | PK | Primary Key |
| 10 | `SEQUENCE_NBR` | DOUBLE | NOT NULL |  | This field contains a number indicating whether the objective is the first, second, third, ... nth objective. |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LONG_TEXT_ID` | [LONG_TEXT_REFERENCE](LONG_TEXT_REFERENCE.md) | `LONG_TEXT_ID` |
| `PARENT_PROT_OBJECTIVE_ID` | [PROT_OBJECTIVE](PROT_OBJECTIVE.md) | `PROT_OBJECTIVE_ID` |
| `PROT_AMENDMENT_ID` | [PROT_AMENDMENT](PROT_AMENDMENT.md) | `PROT_AMENDMENT_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [PROT_OBJECTIVE](PROT_OBJECTIVE.md) | `PARENT_PROT_OBJECTIVE_ID` |

