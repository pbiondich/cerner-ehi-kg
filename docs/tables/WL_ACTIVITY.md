# WL_ACTIVITY

> This table will be used to create activity data for mp worklist rows.

**Description:** MP WORKLIST ACTIVITY  
**Table type:** ACTIVITY  
**Primary key:** `WL_ACTIVITY_ID`  
**Columns:** 17  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | The ENCOUNTER related to this ACTIVITY |
| 7 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 8 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | The PERSON for which this Worklist is being created |
| 9 | `SCH_APPT_ID` | DOUBLE | NOT NULL | FK→ | The Scheduling Appointment for this worklist activity |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 15 | `WL_ACTIVITY_ID` | DOUBLE | NOT NULL | PK | PRIMARY KEY |
| 16 | `WL_CRITERIA_ID` | DOUBLE | NOT NULL | FK→ | Identifies the Critera for why an ACTIVITY row was created. FK Value from table WL_CRITERIA. |
| 17 | `WORKLIST_CD` | DOUBLE | NOT NULL |  | Identifies which Worklist type we are working with for this activity |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `SCH_APPT_ID` | [SCH_APPT](SCH_APPT.md) | `SCH_APPT_ID` |
| `WL_CRITERIA_ID` | [WL_CRITERIA](WL_CRITERIA.md) | `WL_CRITERIA_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [WL_ACTIVITY_DETAIL](WL_ACTIVITY_DETAIL.md) | `WL_ACTIVITY_ID` |

