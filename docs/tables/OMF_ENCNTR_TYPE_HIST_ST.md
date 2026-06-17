# OMF_ENCNTR_TYPE_HIST_ST

> Stores the encounter type history by encounter.

**Description:** OMF ENCNTR TYPE HIST ST  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 19

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BEG_TRANSACTION_DT_NBR` | DOUBLE |  |  | The Julian date number for the date that the person was changed to this encounter type. |
| 2 | `BEG_TRANSACTION_DT_TM` | DATETIME |  |  | The date/time on which the person was changed to this encounter type. |
| 3 | `BEG_TRANSACTION_MIN_NBR` | DOUBLE |  |  | The minute of the day that the person was changed to this encounter type. |
| 4 | `BEG_TRANSACTION_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 5 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 6 | `ENCNTR_LOC_HIST_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the encounter location history table. It is an internal system assigned number. |
| 7 | `ENCNTR_TYPE_CD` | DOUBLE | NOT NULL |  | The code value for the encounter type. |
| 8 | `ENCNTR_TYPE_CLASS_CD` | DOUBLE | NOT NULL |  | The encounter type grouping. |
| 9 | `END_TRANSACTION_DT_NBR` | DOUBLE |  |  | The Julian date for the date on which the person's encounter type was changed from this encounter type. |
| 10 | `END_TRANSACTION_DT_TM` | DATETIME |  |  | The date/time on which the person's encounter type was changed from this encounter type. |
| 11 | `END_TRANSACTION_MIN_NBR` | DOUBLE |  |  | The minute of the day at which the person's encounter type was changed from this encounter type. |
| 12 | `END_TRANSACTION_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 13 | `NBR_BED_DAYS` | DOUBLE |  |  | The number of bed days for a person by encounter type. |
| 14 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 15 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 16 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 17 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 18 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 19 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

