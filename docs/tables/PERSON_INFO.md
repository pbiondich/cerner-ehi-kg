# PERSON_INFO

> Person level comments

**Description:** PERSON INFO  
**Table type:** ACTIVITY  
**Primary key:** `PERSON_INFO_ID`  
**Columns:** 24  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `CHARTABLE_IND` | DOUBLE | NOT NULL |  | Determines whether this Person Level comment can be charted |
| 7 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 8 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 9 | `INFO_SUB_TYPE_CD` | DOUBLE |  |  | This column stores more detailed information about what information is written to the row. Such as the actual field name of the information being stored on this row. |
| 10 | `INFO_TYPE_CD` | DOUBLE | NOT NULL |  | This column stores what type of information is written to the row. |
| 11 | `INTERNAL_SEQ` | DOUBLE |  |  | Internal Person Management sequence |
| 12 | `LONG_TEXT_ID` | DOUBLE | NOT NULL |  | Foreign Key to the LONG_TEXT table. Allows textual Person level comments |
| 13 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 14 | `PERSON_INFO_ID` | DOUBLE | NOT NULL | PK | The unique primary key of this table. |
| 15 | `PRIORITY_SEQ` | DOUBLE |  |  | Identifies a sequencing priority to be used when a duplicate relationship of the same type are created. |
| 16 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 17 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 18 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 19 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 20 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 21 | `VALUE_CD` | DOUBLE |  |  | If the comment if of a codified type, the value should be placed in this attribute |
| 22 | `VALUE_DT_TM` | DATETIME |  |  | If the comment is of a date type, it is stored in this attribute. If the INFO_SUB_TYPE_CD is a date field, then this column will be filled out. |
| 23 | `VALUE_NUMERIC` | DOUBLE |  |  | If the comment is of a numeric type, it is stored in this attribute |
| 24 | `VALUE_NUMERIC_IND` | DOUBLE | NOT NULL |  | Indicates whether or not the input from the front end tool for column VALUE_NUMBER is 0 or NULL. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [PERSON_INFO_HIST](PERSON_INFO_HIST.md) | `PERSON_INFO_ID` |

