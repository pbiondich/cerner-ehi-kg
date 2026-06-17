# OMF_LOCATION_HIST_ST

> Stores location history for a given encounter.

**Description:** OMF LOCATION HIST ST  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 33

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BEG_TRANSACTION_DT_NBR` | DOUBLE |  |  | The Julian date for the date on which the person was moved to this location. |
| 2 | `BEG_TRANSACTION_DT_TM` | DATETIME |  |  | The date/time on which the person was moved to this location. |
| 3 | `BEG_TRANSACTION_MIN_NBR` | DOUBLE |  |  | The minute of the day on which the person was moved to this location. |
| 4 | `BEG_TRANSACTION_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 5 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 6 | `ENCNTR_LOC_HIST_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the encounter location history table. It is an internal system assigned number. |
| 7 | `END_TRANSACTION_DT_NBR` | DOUBLE |  |  | The Julian date on which the person was moved from this location. |
| 8 | `END_TRANSACTION_DT_TM` | DATETIME |  |  | The date/time on which the person was moved from this location. |
| 9 | `END_TRANSACTION_MIN_NBR` | DOUBLE |  |  | The minute of the day on which the person was moved from this location. |
| 10 | `END_TRANSACTION_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 11 | `LOC_BED_CD` | DOUBLE | NOT NULL |  | The code_value for the bed in which the patient is located. |
| 12 | `LOC_BUILDING_CD` | DOUBLE | NOT NULL |  | The code value for the building at which the patient is located. |
| 13 | `LOC_FACILITY_CD` | DOUBLE | NOT NULL |  | The code value for the facility at which the patient is located. |
| 14 | `LOC_NURSE_UNIT_CD` | DOUBLE | NOT NULL |  | The code value for the nurse unit at which the patient is located. |
| 15 | `LOC_NURSE_UNIT_GRP2_CD` | DOUBLE | NOT NULL |  | The code_value representing the second nurse unit grouping as defined within the OMF Grouping Tool. |
| 16 | `LOC_NURSE_UNIT_GRP_CD` | DOUBLE | NOT NULL |  | The code_value representing the nurse unit grouping as defined within the OMF Grouping Tool. |
| 17 | `LOC_ROOM_CD` | DOUBLE | NOT NULL |  | The code_value representing the room in which the patient is located. |
| 18 | `NU_ARRIVE_DT_NBR` | DOUBLE |  |  | The Julian date for on which the person arrived at the nurse unit. |
| 19 | `NU_ARRIVE_DT_TM` | DATETIME |  |  | The date/time on which the person arrived at the nurse unit. |
| 20 | `NU_ARRIVE_MIN_NBR` | DOUBLE |  |  | The minute at which the person arrived at the nurse unit. |
| 21 | `NU_ARRIVE_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 22 | `NU_DEPART_DT_NBR` | DOUBLE |  |  | The Julian date on which the person transferred from the nurse unit. |
| 23 | `NU_DEPART_DT_TM` | DATETIME |  |  | The date/time on which the person was transferred from the nurse unit. |
| 24 | `NU_DEPART_MIN_NBR` | DOUBLE |  |  | The minute on which the person was transferred from the nurse unit. |
| 25 | `NU_DEPART_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 26 | `PREVIOUS_NURSE_UNIT_CD` | DOUBLE | NOT NULL |  | The code_value representing the nurse unit from which the patient was transferred. |
| 27 | `TRANSACTION_IND` | DOUBLE |  |  | Transaction counter - value should always be 1. |
| 28 | `TRANSFER_REASON_CD` | DOUBLE | NOT NULL |  | The reason for the patient transfer |
| 29 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 30 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 31 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 32 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 33 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |

