# SHX_ACTION

> Each row on the table represents clinician's access to the patient's social history assessment record

**Description:** SHX_ACTION  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_DT_TM` | DATETIME | NOT NULL |  | Action taken date and time |
| 2 | `ACTION_TYPE_MEAN` | VARCHAR(12) | NOT NULL |  | Indicates the type of entry on the social history personnel relation table. it can be CREATE, REVIEW, INACTIVATE |
| 3 | `ACTION_TZ` | DOUBLE | NOT NULL |  | Action taken date time zone |
| 4 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 7 | `PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Prsnl id. This is the value of the unique primary identifier of the person table. it is an internal system assigned number |
| 8 | `SHX_ACTION_ID` | DOUBLE | NOT NULL |  | SEQUENCE NAME = :PROBLEM_SEQ This is the table's primary key. the unique identifier for a shx_action table. |
| 9 | `SHX_ACTIVITY_GROUP_ID` | DOUBLE | NOT NULL |  | ACTIVITY GROUP ID FROM THE SHX_ACTIVITY table |
| 10 | `SHX_ACTIVITY_ID` | DOUBLE | NOT NULL | FK→ | SEQUENCE NAME: PROBLEM_SEQ unique identifier for the SHX_ ACTIVITY table. |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `SHX_ACTIVITY_ID` | [SHX_ACTIVITY](SHX_ACTIVITY.md) | `SHX_ACTIVITY_ID` |

