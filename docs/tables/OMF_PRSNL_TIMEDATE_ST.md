# OMF_PRSNL_TIMEDATE_ST

> omf_prsnl_timedate_st

**Description:** Operations Profiling - Personnel timesheet data  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 42

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `COST_CENTER_CD` | DOUBLE | NOT NULL |  | The cost center at which the person clocked in. |
| 2 | `DEPARTMENT_CD` | DOUBLE | NOT NULL |  | The department at which the person clocked in. |
| 3 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time when the data were extracted. |
| 4 | `EXTRACT_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 5 | `FACILITY_CD` | DOUBLE | NOT NULL |  | The facility at which the person clocked in. |
| 6 | `HIRE_DT_NBR` | DOUBLE |  |  | The internal Cerner date representation of the day the person was hired. |
| 7 | `MISC_NUM_HRS` | DOUBLE |  |  | The number of productive hours (excluding regular an overtime) worked during the work period. |
| 8 | `MISC_NUM_MIN` | DOUBLE |  |  | The number of productive minutes (excluding regular an overtime) worked during the work period. |
| 9 | `NUM_HRS` | DOUBLE |  |  | The number of hours worked from clock in to clock out. |
| 10 | `NUM_MIN` | DOUBLE |  |  | The number of minutes worked from clock in to clock out. |
| 11 | `OT_NUM_HRS` | DOUBLE |  |  | The number of overtime hours worked during the work period. |
| 12 | `OT_NUM_MIN` | DOUBLE |  |  | The number of overtime minutes worked during the work period. |
| 13 | `OT_START_DT_NBR` | DOUBLE |  |  | The internal Cerner date representation of the day which overtime started to accrue during the work period. |
| 14 | `OT_START_DT_TM` | DATETIME |  |  | The date/time at which overtime started to accrue during the work period. |
| 15 | `OT_START_MIN_NBR` | DOUBLE |  |  | The minute of the day which overtime started to accrue (1..1440). |
| 16 | `OT_START_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 17 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 18 | `PERSON_POSITION_CD` | DOUBLE | NOT NULL |  | The Cerner-defined position for the person. |
| 19 | `PROCESS_FLAG` | DOUBLE |  |  | Flag to determine those rows that need omf_prsnl_timehour_st rows built/updated. |
| 20 | `PRSNL_ALIAS` | VARCHAR(200) |  |  | The external personnel identifier used to import data. |
| 21 | `PRSNL_ALIAS_POOL_CD` | DOUBLE | NOT NULL |  | The set of identifiers from which the prsnl_alias originated from. |
| 22 | `PRSNL_PAYPERIOD_ID` | DOUBLE | NOT NULL |  | Not used. |
| 23 | `PRSNL_TIMEDATE_ID` | DOUBLE | NOT NULL |  | The unique row identifier for the table. |
| 24 | `REG_NUM_HRS` | DOUBLE |  |  | The number of regular hours worked during the work period. |
| 25 | `REG_NUM_MIN` | DOUBLE |  |  | The number of regular minutes worked during the work period. |
| 26 | `ROLE_CD` | DOUBLE | NOT NULL |  | The role of the person at the time of the clock in. |
| 27 | `ROLE_GRP_CD` | DOUBLE | NOT NULL |  | Role grouping |
| 28 | `ROLE_START_DT_NBR` | DOUBLE |  |  | The internal Cerner date representation of the day on which the person started the role. |
| 29 | `SHIFT_GRP_CD` | DOUBLE | NOT NULL |  | Not used |
| 30 | `TIME_IN_DT_NBR` | DOUBLE |  |  | The internal Cerner date representation of the day when the person clocked in. |
| 31 | `TIME_IN_DT_TM` | DATETIME |  |  | The date/time at which the person clocked in. |
| 32 | `TIME_IN_MIN_NBR` | DOUBLE |  |  | The minute of the day when the person clocked in (1..1440). |
| 33 | `TIME_IN_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 34 | `TIME_OUT_DT_NBR` | DOUBLE |  |  | The internal Cerner date representation of the day the person clocked out. |
| 35 | `TIME_OUT_DT_TM` | DATETIME |  |  | The date/time at which the person clocked out. |
| 36 | `TIME_OUT_MIN_NBR` | DOUBLE |  |  | The minute of the day when the person clocked out (1..1440). |
| 37 | `TIME_OUT_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 38 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 39 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 40 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 41 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 42 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

