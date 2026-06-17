# ACCESSION_EXTERNAL_SMRY

> This table contains a single record of the summary for the external accession assigned to the contents of an accession in Millennium

**Description:** Accession External Summary  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCESSION_EXTERNAL_SMRY_ID` | DOUBLE | NOT NULL |  | Uniquely identifies a summary record for the external accession assigned to the contents of an accession in Millennium. |
| 2 | `ACCESSION_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the accession that the external summary has been recorded for. |
| 3 | `COLLECTED_DT_TM` | DATETIME |  |  | This is the collected date and time associated with the external accession. |
| 4 | `EXTERNAL_ACCESSION` | VARCHAR(40) | NOT NULL |  | This field contains the formatted representation of the accession number. |
| 5 | `EXTERNAL_ACCESSION_COMMENT_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the comment describing the external accession. |
| 6 | `EXTERNAL_ACCESSION_KEY` | VARCHAR(40) | NOT NULL |  | This field contains the alpha numeric characters of the external accession. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ACCESSION_ID` | [ACCESSION](ACCESSION.md) | `ACCESSION_ID` |
| `EXTERNAL_ACCESSION_COMMENT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |

