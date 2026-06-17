# FN_OMF_ENCNTR

> Contains basic patient information from FirstNet tracking tables. PowerVision subject areas can be built against the table

**Description:** FirstNet OMF Encounter information  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 59

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ARRIVE_REQ_EVT_DT_TM` | DATETIME |  |  | Arrival request event date and time from tracking_event |
| 3 | `ARRIVE_REQ_EVT_OMF_DT` | DOUBLE |  |  | Date portion of arrival event request date/time. Allows joining to OMF_DATE |
| 4 | `ARRIVE_REQ_EVT_OMF_TM` | DOUBLE |  |  | Time portion of arrival event request date/time. Allows joining to OMF_TIME |
| 5 | `BED_ASSIGN_COMP_EVT_DT_TM` | DATETIME |  |  | Bed assign event complete date and time from tracking_event |
| 6 | `BED_ASSIGN_COMP_EVT_OMF_DT` | DOUBLE |  |  | Date portion of bed assign event complete date/time. Allows joining to OMF_DATE |
| 7 | `BED_ASSIGN_COMP_EVT_OMF_TM` | DOUBLE |  |  | Time portion of bed assign event complete date/time. Allows joining to OMF_TIME |
| 8 | `CHECKIN_ACUITY_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to TRACK_REFERENCEColumn |
| 9 | `CHECKIN_DT_TM` | DATETIME |  |  | Date and time of patient checkin to ED |
| 10 | `CHECKIN_OMF_DT` | DOUBLE |  |  | Allows join to OMF_DATE |
| 11 | `CHECKIN_OMF_TM` | DOUBLE |  |  | Allows join to OMF_TIME |
| 12 | `CHECKOUT_ACUITY_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to TRACK_REFERENCEColumn |
| 13 | `CHECKOUT_DT_TM` | DATETIME |  |  | Date and time of patient checkout of ED |
| 14 | `CHECKOUT_OMF_DT` | DOUBLE |  |  | Allows join to OMF_DATE |
| 15 | `CHECKOUT_OMF_TM` | DOUBLE |  |  | Allows join to OMF_TIME |
| 16 | `DISCH_DIAG` | VARCHAR(250) |  |  | Diagnosis of patient at discharge |
| 17 | `DISPO_COMP_EVT_DT_TM` | DATETIME |  |  | Date and time of Disposition event complete |
| 18 | `DISPO_COMP_EVT_OMF_DT` | DOUBLE |  |  | Allows join to OMF_DATE |
| 19 | `DISPO_COMP_EVT_OMF_TM` | DOUBLE |  |  | Allows joining to OMF_TIME |
| 20 | `DISPO_REQ_EVT_DT_TM` | DATETIME |  |  | Date and time of disposition event request |
| 21 | `DISPO_REQ_EVT_OMF_DT` | DOUBLE |  |  | Allows joining to OMF_DATE |
| 22 | `DISPO_REQ_EVT_OMF_TM` | DOUBLE |  |  | Allows joining to OMF_TIME |
| 23 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 24 | `FN_OMF_ENCNTR_ID` | DOUBLE | NOT NULL |  | Unique FirstNet OMF Encounter identifierColumn |
| 25 | `LOC_AMBULATORY_UNIT_CD` | DOUBLE | NOT NULL |  | Ambulatory location of patient |
| 26 | `LOC_BED_CD` | DOUBLE | NOT NULL |  | Bed location |
| 27 | `LOC_BED_GRP` | DOUBLE |  |  | Group number for bed location |
| 28 | `LOC_BUILDING_CD` | DOUBLE | NOT NULL |  | Building location of patient |
| 29 | `LOC_FACILITY_CD` | DOUBLE | NOT NULL |  | facility location of patient |
| 30 | `LOC_NURSE_UNIT_CD` | DOUBLE | NOT NULL |  | Nurse unit location of patient |
| 31 | `LOC_NURSE_UNIT_GRP` | DOUBLE |  |  | Nurse unit location group allows grouping of nurse units. |
| 32 | `LOC_ROOM_CD` | DOUBLE | NOT NULL |  | Room location of patient |
| 33 | `LOC_ROOM_GRP` | DOUBLE |  |  | Room location groupColumn |
| 34 | `MD_ASSESS_START_EVT_DT_TM` | DATETIME |  |  | Start date and time of doctor assessment event |
| 35 | `MD_ASSESS_START_EVT_OMF_DT` | DOUBLE |  |  | Allows joining to OMF_DATE |
| 36 | `MD_ASSESS_START_EVT_OMF_TM` | DOUBLE |  |  | Allows joining to OMF_TIME |
| 37 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 38 | `PRIMARY_CARE_PHYSICIAN_ID` | DOUBLE | NOT NULL | FK→ | Person ID of patient's primary care physician |
| 39 | `PRIMARY_DOC_ID` | DOUBLE | NOT NULL | FK→ | Patient's primary ED doctor's person ID |
| 40 | `PRIMARY_NURSE_ID` | DOUBLE | NOT NULL | FK→ | Patient's primary nurse |
| 41 | `REG_COMP_EVT_DT_TM` | DATETIME |  |  | Registration event complete date/time from tracking_event table |
| 42 | `REG_COMP_EVT_OMF_DT` | DOUBLE |  |  | Allows joining to OMF_DATE |
| 43 | `REG_COMP_EVT_OMF_TM` | DOUBLE |  |  | Allows joining to OMF_TIME |
| 44 | `RN_ASSESS_START_EVT_DT_TM` | DATETIME |  |  | Nurse assessment event start date/time from tracking_event table |
| 45 | `RN_ASSESS_START_EVT_OMF_DT` | DOUBLE |  |  | Allows joining to OMF_DATE |
| 46 | `RN_ASSESS_START_EVT_OMF_TM` | DOUBLE |  |  | Allows joining to OMF_TIME |
| 47 | `SECONDARY_DOC_ID` | DOUBLE | NOT NULL | FK→ | Patient's secondary ED doctor's person ID |
| 48 | `SECONDARY_NURSE_ID` | DOUBLE | NOT NULL | FK→ | Patient's secondary ED nurse's person ID |
| 49 | `SPECIALTY_ID` | DOUBLE | NOT NULL | FK→ | Patient categorization based on complaint or diagnosis |
| 50 | `TRACKING_GROUP_CD` | DOUBLE | NOT NULL |  | Tracking Group Code used to identify which tracking group this patient is currently checked into. |
| 51 | `TRACKING_ID` | DOUBLE | NOT NULL | FK→ | Tracking IdentifierColumn |
| 52 | `TRIAGE_COMP_EVT_DT_TM` | DATETIME |  |  | Triage event complete date/time from tracking_event table. |
| 53 | `TRIAGE_COMP_EVT_OMF_DT` | DOUBLE |  |  | Allows joining to OMF_DATE |
| 54 | `TRIAGE_COMP_EVT_OMF_TM` | DOUBLE |  |  | Allows join to OMF_TIME |
| 55 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 56 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 57 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 58 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 59 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CHECKIN_ACUITY_ID` | [TRACK_REFERENCE](TRACK_REFERENCE.md) | `TRACKING_REF_ID` |
| `CHECKOUT_ACUITY_ID` | [TRACK_REFERENCE](TRACK_REFERENCE.md) | `TRACKING_REF_ID` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `PRIMARY_CARE_PHYSICIAN_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `PRIMARY_DOC_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `PRIMARY_NURSE_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `SECONDARY_DOC_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `SECONDARY_NURSE_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `SPECIALTY_ID` | [TRACK_REFERENCE](TRACK_REFERENCE.md) | `TRACKING_REF_ID` |
| `TRACKING_ID` | [TRACKING_ITEM](TRACKING_ITEM.md) | `TRACKING_ID` |

