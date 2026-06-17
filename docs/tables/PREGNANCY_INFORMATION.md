# PREGNANCY_INFORMATION

> This table contains key clinical information used in a pregnancy assessment

**Description:** PREGNANCY INFORMATION  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The details saved by clinician is active or not |
| 2 | `BEGIN_DT_TM` | DATETIME | NOT NULL |  | Information entered date and time |
| 3 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to encounter table |
| 4 | `END_DT_TM` | DATETIME |  |  | N/A at this point of time |
| 5 | `FILTER_TYPE_TXT` | VARCHAR(25) |  |  | Filter type would hold the type of the information the clinician saves. |
| 6 | `LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to long_text. Pregnancy related Information saved by a Clinician |
| 7 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to Person table |
| 8 | `PREGNANCY_INFORMATION_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 9 | `PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to prsnl table. User who saved the Pregnancy information |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

