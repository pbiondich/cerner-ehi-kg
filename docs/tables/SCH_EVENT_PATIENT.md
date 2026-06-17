# SCH_EVENT_PATIENT

> Contains the patient(s)/person(s) associated with an appointment.

**Description:** Event Patient  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 21

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `CANDIDATE_ID` | DOUBLE | NOT NULL |  | A sequence-generated number to uniquely identify the specific row in the database. |
| 7 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 8 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 9 | `NULL_DT_TM` | DATETIME | NOT NULL |  | contains 31-DEC-2100 00:00:00.00 |
| 10 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 11 | `PERSON_PLAN_PROFILE_ID` | DOUBLE | NOT NULL | FK→ | The identifier of the person health plan profile. |
| 12 | `PROFILE_TYPE_CD` | DOUBLE | NOT NULL |  | Indicates the type of health insurance profile for the person plan profile row (i.e., professional, institutional, workmen's comp). |
| 13 | `REFERRAL_IDENT` | VARCHAR(50) |  |  | referral id from the referrral row in the cloud |
| 14 | `SCH_EVENT_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for the requested/scheduled appointment. |
| 15 | `SCH_PEND_ENCNTR_DETAIL_ID` | DOUBLE | NOT NULL | FK→ | The identifier of the pending encounter detail row for this appointment. |
| 16 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 17 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 18 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 19 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 20 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 21 | `VERSION_DT_TM` | DATETIME | NOT NULL |  | The version date and time marks the date the record became historical. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `PERSON_PLAN_PROFILE_ID` | [PERSON_PLAN_PROFILE](PERSON_PLAN_PROFILE.md) | `PERSON_PLAN_PROFILE_ID` |
| `SCH_EVENT_ID` | [SCH_EVENT](SCH_EVENT.md) | `SCH_EVENT_ID` |
| `SCH_PEND_ENCNTR_DETAIL_ID` | [SCH_PEND_ENCNTR_DETAIL](SCH_PEND_ENCNTR_DETAIL.md) | `SCH_PEND_ENCNTR_DETAIL_ID` |

