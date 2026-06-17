# LOC_RESOURCE_CALENDAR

> Contains the calendar rows for a resource which indicate when the resource can accept work (routing). Attributes included in the calendar include service area, day of week, time of day, etc.

**Description:** Location Resource Calendar  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 28

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `AGE_FROM_MINUTES` | DOUBLE |  |  | The beginning age in minutes for the routing rule. |
| 6 | `AGE_FROM_UNITS_CD` | DOUBLE | NOT NULL |  | The units associated with the age_from_minutes such as days, months or years. |
| 7 | `AGE_TO_MINUTES` | DOUBLE |  |  | The ending age in minutes for the routing rule |
| 8 | `AGE_TO_UNITS_CD` | DOUBLE | NOT NULL |  | The units associated with the age_to_minutes such as days, months or years. |
| 9 | `AVAIL_IND` | DOUBLE |  |  | Whether the calendar is available. This will be removed in the future. Currently, all rows are set to 1. |
| 10 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 11 | `CALENDAR_SEQ` | DOUBLE | NOT NULL |  | The order in which a set of attributes should be considered for routing relative to other sets of attributes. The user may create information for a 5 day week, followed by information for the weekend. The rows associated with the 5 day week contain a calendar sequence lower than those rows associated with the weekend. |
| 12 | `CLOSE_TIME` | DOUBLE |  |  | The time of day which the resource is no longer available to have work routed to it. Possible values are 0 to 2359. |
| 13 | `DESCRIPTION` | VARCHAR(200) |  |  | Text which describes the calendar row for human interpretation. |
| 14 | `DISPENSE_TYPE_CD` | DOUBLE | NOT NULL |  | Used by PharmNet. The valid dispense types associated with the calendar row. |
| 15 | `DOW` | DOUBLE |  |  | Indicates the days of the week that the resource can accept work to be done. Valid values are 0 through 6 (Sun thru Sat). A value of indicates all days of the week. |
| 16 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 17 | `LOCATION_CD` | DOUBLE | NOT NULL | FK→ | The location which is supported by the resource. For PathNet and RadNet this is usually a location with a cdf_meaning for Service Area. |
| 18 | `LOC_RESOURCE_TYPE_CD` | DOUBLE | NOT NULL | FK→ | Indicates the product associated with the resource's calendar. Examples include Lab, Rad, etc. |
| 19 | `OPEN_TIME` | DOUBLE |  |  | Indicates when the resource is open or available to receive work on a 24 hour clock. Valid values are 0 to 2359 |
| 20 | `PRIORITY_CD` | DOUBLE | NOT NULL |  | The reporting priorities associated with the resource's availability. |
| 21 | `SEQUENCE` | DOUBLE | NOT NULL | FK→ | Sequence. Used to differentiate rows with the same resource and service area location. The user may create more than one calendar row with the same service area (may make the priorities, dow, time of day, etc. different but the service area is the same). |
| 22 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL | FK→ | The resource for which the calendar is being built. |
| 23 | `SPECIMEN_TYPE_CD` | DOUBLE | NOT NULL |  | Used by PathNet. The specimen types associated with the resources availability. |
| 24 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 25 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 26 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 27 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 28 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LOCATION_CD` | [LOC_RESOURCE_R](LOC_RESOURCE_R.md) | `LOCATION_CD` |
| `LOC_RESOURCE_TYPE_CD` | [LOC_RESOURCE_R](LOC_RESOURCE_R.md) | `LOC_RESOURCE_TYPE_CD` |
| `SEQUENCE` | [LOC_RESOURCE_R](LOC_RESOURCE_R.md) | `SEQUENCE` |
| `SERVICE_RESOURCE_CD` | [LOC_RESOURCE_R](LOC_RESOURCE_R.md) | `SERVICE_RESOURCE_CD` |

