# SCH_APPT_ACTION

> Scheduling appointment action

**Description:** Scheduling appointment action  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 24

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `APPT_TYPE_CD` | DOUBLE | NOT NULL |  | The unique identifier for the scheduling appointment type. |
| 6 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 7 | `CANDIDATE_ID` | DOUBLE | NOT NULL |  | A sequence-generated number to uniquely identify the specific row in the database. |
| 8 | `CHILD_APPT_SYN_CD` | DOUBLE | NOT NULL | FK→ | identifier for the associated appointment synonym |
| 9 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 10 | `LOCATION_CD` | DOUBLE | NOT NULL |  | The field identifies the current permanent location of the patient. |
| 11 | `OFFSET_BEG_UNITS` | DOUBLE | NOT NULL |  | Scheduling Offset Beg Units |
| 12 | `OFFSET_BEG_UNITS_CD` | DOUBLE | NOT NULL |  | Scheduling Offset Beg Units Code |
| 13 | `OFFSET_BEG_UNITS_MEANING` | VARCHAR(12) |  |  | Scheduling Offset Beg Units Meaning |
| 14 | `OFFSET_END_UNITS` | DOUBLE | NOT NULL |  | Scheduling Offset End Units |
| 15 | `OFFSET_END_UNITS_CD` | DOUBLE | NOT NULL |  | Scheduling Offset End Units Code |
| 16 | `OFFSET_END_UNITS_MEANING` | VARCHAR(12) |  |  | Scheduling Offset End Units Meaning |
| 17 | `SCH_ACTION_CD` | DOUBLE | NOT NULL |  | schedule action code |
| 18 | `SCH_FLEX_ID` | DOUBLE | NOT NULL | FK→ | Scheduling Flexing Identifier |
| 19 | `SEQ_NBR` | DOUBLE | NOT NULL |  | Determines the order among the children of a group. |
| 20 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 21 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 22 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 23 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 24 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CHILD_APPT_SYN_CD` | [SCH_APPT_SYN](SCH_APPT_SYN.md) | `APPT_SYNONYM_CD` |
| `SCH_FLEX_ID` | [SCH_FLEX_STRING](SCH_FLEX_STRING.md) | `SCH_FLEX_ID` |

