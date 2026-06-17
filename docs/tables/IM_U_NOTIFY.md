# IM_U_NOTIFY

> This table contains data that will be sent to the archive upon match/unmatch.

**Description:** IM U Notify  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 21

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CQM_NBR_RETRIES` | DOUBLE | NOT NULL |  | This column indicates the number of communication attempts made to the CQM server. |
| 2 | `CQM_STATUS_CD` | DOUBLE | NOT NULL |  | This column indicates the status of the CQM trigger. The CQM trigger will initiate a procedure update to be sent via HL7. |
| 3 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to the ENCOUNTER table for the order. |
| 4 | `IM_ACQUIRED_STUDY_ID` | DOUBLE | NOT NULL | FK→ | This column contains a foreign key to the IM_ACQUIRED_STUDY table. |
| 5 | `IM_DEVICE_ID` | DOUBLE | NOT NULL | FK→ | Device id for the archive being updated. |
| 6 | `IM_SERIES_ID` | DOUBLE | NOT NULL | FK→ | This column contains a foreign key to the IM_SERIES table. |
| 7 | `IM_STUDY_ID` | DOUBLE | NOT NULL | FK→ | This column contains a foreign key to the IM_STUDY table. |
| 8 | `IM_U_NOTIFY_ID` | DOUBLE | NOT NULL |  | This column contains a meaningless number that only serves the purpose of uniquely identifying a row. |
| 9 | `INSERT_DT_TM` | DATETIME |  |  | This column contains the date/time that the IM_U_NOTIFY row was inserted. |
| 10 | `NUMBER_OF_TRIES` | DOUBLE |  |  | This column contains the number of communication attempts have been made with the archive. |
| 11 | `PATIENT_IDENTIFIER` | VARCHAR(64) |  |  | This column contains the patient's identifier that is known by the archive. |
| 12 | `PATIENT_NAME` | VARCHAR(64) |  |  | This column contains the patient name that the archive knows about. |
| 13 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to the PERSON table for the row being processed. |
| 14 | `REPLACED_IM_STUDY_ID` | DOUBLE | NOT NULL | FK→ | Identifies the IM_STUDY table foreign key to be used to replace the specified study specified |
| 15 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 16 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 17 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 18 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 19 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 20 | `U_NOTIFY_CD` | DOUBLE | NOT NULL |  | This column indicates if this u-notify message is a match, unmatch or move series. |
| 21 | `U_NOTIFY_STATUS_CD` | DOUBLE | NOT NULL |  | This column indicates the status of the U-Notify message |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `IM_ACQUIRED_STUDY_ID` | [IM_ACQUIRED_STUDY](IM_ACQUIRED_STUDY.md) | `IM_ACQUIRED_STUDY_ID` |
| `IM_DEVICE_ID` | [IM_DEVICE](IM_DEVICE.md) | `IM_DEVICE_ID` |
| `IM_SERIES_ID` | [IM_SERIES](IM_SERIES.md) | `IM_SERIES_ID` |
| `IM_STUDY_ID` | [IM_STUDY](IM_STUDY.md) | `IM_STUDY_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `REPLACED_IM_STUDY_ID` | [IM_STUDY](IM_STUDY.md) | `IM_STUDY_ID` |

