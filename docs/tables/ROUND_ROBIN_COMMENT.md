# ROUND_ROBIN_COMMENT

> Comments for a Round Robin template, accession, service resource.

**Description:** Round Robin Comment  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCESSION_ID` | DOUBLE | NOT NULL | FK→ | A unique, internal, system-assigned number that identifies a specific accession number associated with a round robin comment. |
| 2 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 3 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 4 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 5 | `LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | A unique, internal, system-assigned number that identifies the specific storage location for the text of the comment. Creates a relationship to the long text table. |
| 6 | `ROUND_ROBIN_REF_ID` | DOUBLE | NOT NULL | FK→ | A unique, internal, system-assigned number that identifies the specific round robin template associated with the comment. Creates a relationship to the round robin reference table. |
| 7 | `SEQUENCE` | DOUBLE | NOT NULL |  | Defines the sequence of changes made to a given round robin comment. When a comment is updated, the previous sequence is inactivated and a new row is added with the next sequence number. |
| 8 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL |  | A unique code value that identifies the specific service resource (i.e. instrument, bench, etc.) associated with the round robin comment. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ACCESSION_ID` | [RR_ACCESSION_R](RR_ACCESSION_R.md) | `ACCESSION_ID` |
| `LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `ROUND_ROBIN_REF_ID` | [RR_ACCESSION_R](RR_ACCESSION_R.md) | `ROUND_ROBIN_REF_ID` |

