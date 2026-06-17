# CODE_VALUE_FILTER

> The CODE_VALUE_FILTER table stores CODE_SET(s) that have been filtered.

**Description:** CODE VALUE FILTER  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 25

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `CODE_SET` | DOUBLE | NOT NULL |  | The code set of the filter.Column |
| 7 | `CODE_VALUE_FILTER_ID` | DOUBLE | NOT NULL |  | Primary Key.Column |
| 8 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 9 | `FILTER_IND` | DOUBLE | NOT NULL |  | Indicates inclusive (0) or exclusive (1) filter.Column |
| 10 | `FILTER_TYPE_CD` | DOUBLE | NOT NULL |  | Indicates the type of filter, such as Immunization or Location as examples.Column |
| 11 | `FLEX1_ID` | DOUBLE | NOT NULL |  | Value of the primary identifier of associate parent entity.Column |
| 12 | `FLEX2_ID` | DOUBLE | NOT NULL |  | Value of the primary identifier of associate parent entity.Column |
| 13 | `FLEX3_ID` | DOUBLE | NOT NULL |  | Value of the primary identifier of associate parent entity.Column |
| 14 | `FLEX4_ID` | DOUBLE | NOT NULL |  | Value of the primary identifier of associate parent entity.Column |
| 15 | `FLEX5_ID` | DOUBLE | NOT NULL |  | *** OBSOLETE COLUMN *** Value of the primary identifier of associate parent entity.Column |
| 16 | `PARENT_ENTITY_NAME1` | VARCHAR(32) |  |  | The upper case table name to which this row is associated.Column |
| 17 | `PARENT_ENTITY_NAME2` | VARCHAR(32) |  |  | The upper case table name to which this row is associated.Column |
| 18 | `PARENT_ENTITY_NAME3` | VARCHAR(32) |  |  | The upper case table name to which this row is associated.Column |
| 19 | `PARENT_ENTITY_NAME4` | VARCHAR(32) |  |  | The upper case table name to which this row is associated.Column |
| 20 | `PARENT_ENTITY_NAME5` | VARCHAR(32) |  |  | *** obsolete column *** The upper case table name to which this row is associated.Column |
| 21 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 22 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 23 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 24 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 25 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

