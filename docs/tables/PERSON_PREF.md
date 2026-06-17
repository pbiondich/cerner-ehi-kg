# PERSON_PREF

> Stores information relating to a person's preferences

**Description:** Person Preference  
**Table type:** ACTIVITY  
**Primary key:** `PERSON_ID`  
**Columns:** 21  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `APPT_PROXIMITY_ADDR_TYPE_CD` | DOUBLE | NOT NULL |  | identifies the appointment proximity address type (i.e., home, business, etc.). |
| 6 | `FACILITY_ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | The identifier of the preferred facility organization. |
| 7 | `FRIDAY_APPT_TIME_CD` | DOUBLE |  |  | The preferred appointment time for Friday. |
| 8 | `MONDAY_APPT_TIME_CD` | DOUBLE |  |  | The preferred appointment time for Monday. |
| 9 | `PERSON_ID` | DOUBLE | NOT NULL | PK FK→ | this is the value of the unique primary identifier of the person table. it is an internal system assigned number. |
| 10 | `PROVIDER_LANGUAGE_CD` | DOUBLE |  |  | The preferred provider's language. |
| 11 | `PROVIDER_SEX_CD` | DOUBLE | NOT NULL |  | The preferred provider's gender (sex). |
| 12 | `SATURDAY_APPT_TIME_CD` | DOUBLE |  |  | The preferred appointment time for Saturday |
| 13 | `SUNDAY_APPT_TIME_CD` | DOUBLE |  |  | The preferred appointment time for Sunday |
| 14 | `THURSDAY_APPT_TIME_CD` | DOUBLE |  |  | The preferred appointment time for Thursday |
| 15 | `TUESDAY_APPT_TIME_CD` | DOUBLE |  |  | The preferred appointment time for Tuesday |
| 16 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 21 | `WEDNESDAY_APPT_TIME_CD` | DOUBLE |  |  | The preferred appointment time for Wednesday. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `FACILITY_ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [PERSON_PREF_HIST](PERSON_PREF_HIST.md) | `PERSON_ID` |

