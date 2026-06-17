# PM_MOH_INPAT_CENSUS

> Ministry of Health (Canada) inpatient census.

**Description:** PM MOH INPAT CENSUS  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 32

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ADMITTED_DAY` | DOUBLE |  |  | Admitted day. |
| 6 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 7 | `DATE_START` | DATETIME | NOT NULL |  | Date start. |
| 8 | `DECEASED_DAY` | DOUBLE |  |  | Deceased count for the day. |
| 9 | `DISCHARGED_DAY` | DOUBLE |  |  | Discharge count for the day. |
| 10 | `ENCNTR_REPORT_TYPE` | CHAR(30) | NOT NULL |  | Encounter report type. |
| 11 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 12 | `INPATIENT_START` | DOUBLE |  |  | Inpatient start. |
| 13 | `INTENSIVE_DAY` | DOUBLE |  |  | Intensive care count for the day. |
| 14 | `LOCATION_CD` | DOUBLE | NOT NULL | FK→ | Location code value |
| 15 | `MEDICAL_DAY` | DOUBLE |  |  | Medical count for the day. |
| 16 | `NB_ADMITTED_DAY` | DOUBLE |  |  | Newborn count for the day. |
| 17 | `NB_DECEASED_DAY` | DOUBLE |  |  | Newborn death count for the day. |
| 18 | `NB_DISCHARGED_DAY` | DOUBLE |  |  | Newborn discharge count for the day. |
| 19 | `NB_SAME_DAY` | DOUBLE |  |  | Newborn same day count for the day. |
| 20 | `NB_START` | DOUBLE |  |  | Newborn start count. |
| 21 | `OBGYN_DAY` | DOUBLE |  |  | OBGYN count for the day. |
| 22 | `OTHER_DAY` | DOUBLE |  |  | Other count for the day. |
| 23 | `PEDIATRIC_DAY` | DOUBLE |  |  | Pediatric count for the day. |
| 24 | `PM_MOH_INPAT_CENSUS_ID` | DOUBLE | NOT NULL |  | Primary key. |
| 25 | `PSYCHIATRIC_DAY` | DOUBLE |  |  | Pshychiatric count for the day. |
| 26 | `SAME_DAY` | DOUBLE |  |  | Same day visit count for the day. |
| 27 | `SURGICAL_DAY` | DOUBLE |  |  | Surgical count for the day. |
| 28 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 29 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 30 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 31 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 32 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LOCATION_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |

