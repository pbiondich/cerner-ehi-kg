# OMF_PRSNL_PAYPERIOD_ST

> omf_prsnl_payperiod_st

**Description:** Operations Profiling -- Personnel pay period data  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 42

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `AGENCY_AMT` | DOUBLE |  |  | The amount of agency pay earned during the pay period. The agency pay type is considered productive. |
| 2 | `AGENCY_HRS` | DOUBLE |  |  | The amount of agency hours worked during the pay period. The agency pay type is considered productive. |
| 3 | `CALLIN_AMT` | DOUBLE |  |  | The amount of call-in pay earned during the pay period. The call-in pay type is considered productive. |
| 4 | `CALLIN_HRS` | DOUBLE |  |  | The amount of call-in hours worked during the pay period. The call-in pay type is considered productive. |
| 5 | `COMMISSION_AMT` | DOUBLE |  |  | The amount of commission/bonus pay earned. |
| 6 | `COST_CENTER_CD` | DOUBLE | NOT NULL |  | The cost center to which the person is assigned to. |
| 7 | `DEPARTMENT_CD` | DOUBLE | NOT NULL |  | The department to which the person is assigned. |
| 8 | `EMP_PAID_TAX` | DOUBLE |  |  | The amount of taxes paid by the employer during the pay period. |
| 9 | `EXP_HRS` | DOUBLE |  |  | The number of hours the person is expected to have worked during the pay period. |
| 10 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time the data were extracted. |
| 11 | `EXTRACT_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 12 | `FACILITY_CD` | DOUBLE | NOT NULL |  | The facility were the person worked. |
| 13 | `HIRE_DT_NBR` | DOUBLE |  |  | The Cerner internal date representation of the day the person was hired. |
| 14 | `OTHER_NONP_AMT` | DOUBLE |  |  | The amount of other non-productive pay earned during the pay period. |
| 15 | `OTHER_NONP_HRS` | DOUBLE |  |  | The amount of other non-productive hours worked during the pay period. |
| 16 | `OTHER_PROD_AMT` | DOUBLE |  |  | The amount of other productive pay earned during the pay period. |
| 17 | `OTHER_PROD_HRS` | DOUBLE |  |  | The amount of other productive hours worked during the pay period. |
| 18 | `OT_AMT` | DOUBLE |  |  | The amount of overtime pay earned during the pay period. Overtime is considered a productive pay type. |
| 19 | `OT_HRS` | DOUBLE |  |  | The amount of overtime hours worked during the pay period. Overtime is considered a productive pay type. |
| 20 | `PERIOD_END_DT_NBR` | DOUBLE |  |  | The internal Cerner date representation of the day the pay period ended. |
| 21 | `PERIOD_NBR` | DOUBLE |  |  | The client defined pay period number. |
| 22 | `PERIOD_START_DT_NBR` | DOUBLE |  |  | The internal Cerner date representation of the day the pay period started. |
| 23 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 24 | `PERSON_POSITION_CD` | DOUBLE | NOT NULL |  | The Cerner-defined position for the person. |
| 25 | `PRSNL_ALIAS` | VARCHAR(200) |  |  | The external personnel identifier used to import the pay period data. |
| 26 | `PRSNL_ALIAS_POOL_CD` | DOUBLE | NOT NULL |  | The set of identifiers the prsnl_alias belongs to. |
| 27 | `PRSNL_PAYPERIOD_ID` | DOUBLE | NOT NULL |  | The unique identifier for a row on the table. |
| 28 | `REG_AMT` | DOUBLE |  |  | The amount of regular pay earned during the pay period. Regular is considered a productive pay type. |
| 29 | `REG_HRS` | DOUBLE |  |  | The amount of regular hours worked during the pay period. Regular is considered a productive pay type. |
| 30 | `ROLE_CD` | DOUBLE | NOT NULL |  | The role of the person at the time of the pay period. |
| 31 | `ROLE_GRP_CD` | DOUBLE | NOT NULL |  | Role grouping |
| 32 | `ROLE_START_DT_NBR` | DOUBLE |  |  | The internal Cerner date representation of the day the person started working under the role. |
| 33 | `STAND_BY_AMT` | DOUBLE |  |  | The amount of stand by pay earned during the pay period. Stand by is NOT considered a productive pay type. |
| 34 | `STAND_BY_HRS` | DOUBLE |  |  | The amount of stand by hours worked during the pay period. Stand by is NOT considered a productive pay type. |
| 35 | `STD_HRS` | DOUBLE |  |  | The standard number of hours in the pay period. This is the number of hours a full time person is expected to work during the pay period. |
| 36 | `TIME_OFF_AMT` | DOUBLE |  |  | The amount of time off pay earned during the pay period. Time off is NOT considered a productive pay type. |
| 37 | `TIME_OFF_HRS` | DOUBLE |  |  | The amount of time off hours the person used during the pay period. Time off is NOT considered a productive pay type. |
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

