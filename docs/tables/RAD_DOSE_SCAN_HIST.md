# RAD_DOSE_SCAN_HIST

> Store the history information for the rows in the rad_dose_scan table for auditing purposes.

**Description:** Radiology Dose Scan History  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 2 | `BODY_PART_CD` | DOUBLE | NOT NULL |  | *** OBSOLETE*** |
| 3 | `BODY_PART_ID` | DOUBLE | NOT NULL | FK→ | The body part the conversion factor applies to. |
| 4 | `EFFECTIVE_DOSE_AMT` | DOUBLE | NOT NULL |  | Stores the calculated effective dose for the scan. |
| 5 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 6 | `IRRADIATION_EVENT_UID` | VARCHAR(255) | NOT NULL |  | Stores the irradiation event uid received from DICOM. |
| 7 | `LAST_UPDT_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | the person that last updated this row. |
| 8 | `RAD_DOSE_SCAN_HIST_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the RAD_DOSE_SCAN_HIST table. |
| 9 | `RAD_DOSE_SCAN_ID` | DOUBLE | NOT NULL | FK→ | Unique identifier to a single row on the rad_dose_scan table. Identifies the Rad Dose Scan that this row is history for. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BODY_PART_ID` | [RAD_DOSE_SNOMED_RT_GLOSSARY](RAD_DOSE_SNOMED_RT_GLOSSARY.md) | `RAD_DOSE_SNOMED_RT_GLOSSARY_ID` |
| `LAST_UPDT_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `RAD_DOSE_SCAN_ID` | [RAD_DOSE_SCAN](RAD_DOSE_SCAN.md) | `RAD_DOSE_SCAN_ID` |

