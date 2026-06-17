# MIC_BIO_PROFILE_DETAIL

> This reference table contains percent positive data for a specific organism, group biochemical, and detail biochemical combination.

**Description:** Microbiology Biochemical Profile Detail  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DETAIL_BIOCHEMICAL_CD` | DOUBLE | NOT NULL |  | This field identifies the code value associated with the detail biochemical. |
| 2 | `NEG_FREQUENCY_VALUE` | DOUBLE |  |  | This field contains the calculated 'negative' frequency of the PERCENT_POS column. |
| 3 | `PERCENT_POS` | DOUBLE | NOT NULL |  | This field contains the organism's percentage positive value for a detail biochemical. Valid values are from 0 to 100. |
| 4 | `POS_FREQUENCY_VALUE` | DOUBLE |  |  | This field contains the calculated 'positive' frequency of the PERCENT_POS column. |
| 5 | `PROFILE_ID` | DOUBLE | NOT NULL |  | This field contains the foreign key value used to join to the parent MIC_BIO_PROFILE_DETAIL table. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

