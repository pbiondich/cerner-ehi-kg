# OMF_RADTRANS_ORDER_ST

> Summary table storing transcriptionist information for radiology mgmt.

**Description:** OMF RADTRANS ORDER ST  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 22

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `NBR_CHARACTERS` | DOUBLE |  |  | The number of characters associated with this transcription. |
| 2 | `NBR_LINES` | DOUBLE |  |  | The number of lines associated with this transcription. |
| 3 | `NBR_WORDS` | DOUBLE |  |  | The number of words associated with this transcription. |
| 4 | `OMF_RADTRANS_ORDER_ST_ID` | DOUBLE | NOT NULL |  | Unique identifier for the radiology transcription summary table. |
| 5 | `ORDER_ID` | DOUBLE | NOT NULL |  | The identification number associated with this order. |
| 6 | `ORIG_TRANSCRIBE_DT_NBR` | DOUBLE |  |  | Original transcribed date number used to calculate other date dimensions and filters |
| 7 | `ORIG_TRANSCRIBE_MIN_NBR` | DOUBLE |  |  | Original transcribe minute number used to create time related dimensions and filters |
| 8 | `ORIG_TRANSCRIBE_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 9 | `ORIG_TRANS_DT_TM` | DATETIME |  |  | This column contains the date that the report was originally transcribed. |
| 10 | `RADIOLOGIST_ID` | DOUBLE | NOT NULL | FK→ | This column contains the unique identifier for the Radiologist that is associated with the report. |
| 11 | `RAD_REPORT_ID` | DOUBLE | NOT NULL | FK→ | The Radnet report identification number associated with this order. |
| 12 | `RAD_REPORT_SEQ` | DOUBLE | NOT NULL |  | Provides uniqueness to a radiology report. |
| 13 | `TRANSCRIBE_DT_NBR` | DOUBLE |  |  | Transcribe Date Number used to create date related dimensions and filters |
| 14 | `TRANSCRIBE_DT_TM` | DATETIME |  |  | The last date/time that this Radnet report was transcribed (updated). |
| 15 | `TRANSCRIBE_MIN_NBR` | DOUBLE |  |  | Transcribe minute number used to create time related dimensions and filters |
| 16 | `TRANSCRIBE_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 17 | `TRANSCRIPTIONIST_ID` | DOUBLE | NOT NULL | FK→ | The identification number for the transcriptionist associated with this report. |
| 18 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 19 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 20 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 21 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 22 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `RADIOLOGIST_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `RAD_REPORT_ID` | [RAD_REPORT](RAD_REPORT.md) | `RAD_REPORT_ID` |
| `TRANSCRIPTIONIST_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

