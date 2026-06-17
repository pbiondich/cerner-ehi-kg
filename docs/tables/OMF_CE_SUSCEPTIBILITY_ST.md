# OMF_CE_SUSCEPTIBILITY_ST

> omf_ce_susceptibility_st

**Description:** Stores organism susceptibility data  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 20

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ANTIBIOTIC_CD` | DOUBLE | NOT NULL |  | The type of antibiotic for microbiology susceptibility results |
| 2 | `DETAIL_SUSCEPTIBILITY_CD` | DOUBLE | NOT NULL |  | The actual susceptibility that an organism has to an antibiotic |
| 3 | `EVENT_ID` | DOUBLE | NOT NULL |  | Unique identifier to the event stored on the omf_clinical_event_st table. |
| 4 | `MICRO_SEQ_NBR` | DOUBLE | NOT NULL |  | Combined with the event_id to form foreign key to the omf_ce_microbiology_st table |
| 5 | `RESULT_CD` | DOUBLE | NOT NULL |  | The resistance of an organism to a particular antibiotic (susceptibility interpretation). |
| 6 | `RESULT_DT_NBR` | DOUBLE |  |  | The Julian date for the result |
| 7 | `RESULT_DT_TM` | DATETIME |  |  | The date and time of the results. |
| 8 | `RESULT_MIN_NBR` | DOUBLE |  |  | The minute that the result occurred. |
| 9 | `RESULT_NUMERIC_VALUE` | DOUBLE |  |  | The numeric value of the results. |
| 10 | `RESULT_TEXT_KEY` | VARCHAR(255) |  |  | RESULT_TEXT_KEY |
| 11 | `RESULT_TEXT_VALUE` | VARCHAR(100) |  |  | The free text description of the results. |
| 12 | `RESULT_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 13 | `RESULT_UNIT_CD` | DOUBLE | NOT NULL |  | The unit of measure for the susceptibility interpretation. |
| 14 | `SUSCEPTIBILITY_TEST_CD` | DOUBLE | NOT NULL |  | The type of susceptibility testing done (MIC, Kirby-Bauer). |
| 15 | `SUSCEP_SEQ_NBR` | DOUBLE | NOT NULL |  | Sequence number to make the primary key unique, when there are more than one susceptibility test per growth. |
| 16 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 17 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 18 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 19 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 20 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

