# LOCATION_GROUP

> The location group table information about the hierachial relationship between different locations.

**Description:** Location Group  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 17

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `CHILD_LOC_CD` | DOUBLE | NOT NULL | FK→ | This field is the location code which is the child in a relationship. If the relationship is facility to building, facility is the parent, building is child. |
| 7 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 8 | `LOCATION_GROUP_TYPE_CD` | DOUBLE | NOT NULL |  | The location group type identifies the kind of location associated with the parent location. Location group type codes have Cerner defined meanings in the common data foundation. |
| 9 | `PARENT_LOC_CD` | DOUBLE | NOT NULL | FK→ | This field is the location code which is the parent in a relationship. If the relationship is facility to building, facility is the parent, building is child. |
| 10 | `ROOT_LOC_CD` | DOUBLE | NOT NULL | FK→ | References the location code that is the highest level in a view's hierarchy. For patient care locations, the root code is 0. |
| 11 | `SEQUENCE` | DOUBLE |  |  | The relative position of the child location. Controls the order in which the child location displays relative to other children locations. |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 17 | `VIEW_TYPE_CD` | DOUBLE | NOT NULL |  | Precursor to root_location_cd. Needed for a conversion utility "LOC_CONVERT_VIEW_TYPES". No longer needed after the utility is performed. NO LONGER USED PROGRAMATICALLY |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CHILD_LOC_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `PARENT_LOC_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `ROOT_LOC_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |

