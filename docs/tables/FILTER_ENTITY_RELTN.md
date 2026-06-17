# FILTER_ENTITY_RELTN

> This table contains Filter Entity Relationships that allow for filtering of data based on different entities

**Description:** Filter Entity Relation  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 22

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 2 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 3 | `EXCLUSION_FILTER_IND` | DOUBLE |  |  | Determines if the filter is an Exclusion or an Inclusion Filter |
| 4 | `FILTER_ENTITY1_ID` | DOUBLE | NOT NULL |  | The value of the primary identifier of the table to which contains the filter data |
| 5 | `FILTER_ENTITY1_NAME` | VARCHAR(30) | NOT NULL |  | The upper case name of the table which contains the filter data |
| 6 | `FILTER_ENTITY2_ID` | DOUBLE | NOT NULL |  | The value of the primary identifier of the table to which contains the filter data |
| 7 | `FILTER_ENTITY2_NAME` | VARCHAR(30) |  |  | The upper case name of the table which contains the filter data |
| 8 | `FILTER_ENTITY3_ID` | DOUBLE | NOT NULL |  | The value of the primary identifier of the table to which contains the filter data |
| 9 | `FILTER_ENTITY3_NAME` | VARCHAR(30) |  |  | The upper case name of the table which contains the filter data |
| 10 | `FILTER_ENTITY4_ID` | DOUBLE | NOT NULL |  | The value of the primary identifier of the table to which contains the filter data |
| 11 | `FILTER_ENTITY4_NAME` | VARCHAR(30) |  |  | The upper case name of the table which contains the filter data |
| 12 | `FILTER_ENTITY5_ID` | DOUBLE | NOT NULL |  | The value of the primary identifier of the table to which contains the filter data |
| 13 | `FILTER_ENTITY5_NAME` | VARCHAR(30) |  |  | The upper case name of the table which contains the filter data |
| 14 | `FILTER_ENTITY_RELTN_ID` | DOUBLE | NOT NULL |  | The primary key of the Filter Entity Relation table |
| 15 | `FILTER_TYPE_CD` | DOUBLE | NOT NULL |  | The type of filter that is being used |
| 16 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | The value of the primary identifier of the table to which the Entity is stored on. |
| 17 | `PARENT_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | The upper case name of the table to which this Entity row is stored on |
| 18 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 21 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 22 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

