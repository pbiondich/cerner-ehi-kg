# ENCNTR_BENEFIT_SCH_R

> This table allows the user to capture a range of entries specific for each encounter.

**Description:** Encounter Benefit Schedules Relationship  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 22

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `DATA_STATUS_CD` | DOUBLE | NOT NULL |  | Data status indicates a level of authenticity of the row data. Typically this will either be AUTHENTICATED or UNAUTHENTICATED. |
| 7 | `DATA_STATUS_DT_TM` | DATETIME |  |  | The date and time that the data_status_cd was set. |
| 8 | `DATA_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the data_status_cd to be set or change. |
| 9 | `ENCNTR_BENEFIT_R_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the encounter benefit relation table. It is an internal system assigned number. |
| 10 | `ENCNTR_BENEFIT_SCH_R_ID` | DOUBLE | NOT NULL |  | Primary Key |
| 11 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 12 | `MEMBER_RESP_TYPE_CD` | DOUBLE | NOT NULL |  | The responsibility type associated with the set. |
| 13 | `RESP_RANGE_AMT` | DOUBLE | NOT NULL |  | The amount associated with the member responsibility type and corresponding range (if entered). |
| 14 | `RESP_RANGE_END_NBR` | DOUBLE | NOT NULL |  | The ending value of each range associated with the member responsibility type. |
| 15 | `RESP_RANGE_QUAL_CD` | DOUBLE | NOT NULL |  | Descriptor of the values entered in each range indicated in the Type start and Type end. |
| 16 | `RESP_RANGE_START_NBR` | DOUBLE | NOT NULL |  | The starting value of each range associated with the member responsibility type. |
| 17 | `RESP_TYPE_QUAL_CD` | DOUBLE | NOT NULL |  | Descriptor of the values entered in each range indicated in the Type start and Type end. |
| 18 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 19 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 20 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 21 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 22 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_BENEFIT_R_ID` | [ENCNTR_BENEFIT_R](ENCNTR_BENEFIT_R.md) | `ENCNTR_BENEFIT_R_ID` |

