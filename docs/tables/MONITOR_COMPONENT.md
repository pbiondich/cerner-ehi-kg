# MONITOR_COMPONENT

> This table describes the relationship between a monitor and the locations associated with the monitor

**Description:** Monitor Component  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `COMPONENT_REFERENCE_ID` | DOUBLE | NOT NULL |  | Describes a location that will be associated with this monitor. Can be a location or service resource |
| 2 | `COMPONENT_SEQUENCE` | DOUBLE |  |  | Describes the order in which the locations will appear on a monitor |
| 3 | `COMPONENT_TYPE_FLAG` | DOUBLE |  |  | Indicates either list view (1) or icon view (0) for a component. |
| 4 | `MONITOR_COMPONENT_ID` | DOUBLE | NOT NULL |  | Meaningless number that uniquely defines a row on the table. |
| 5 | `MONITOR_VIEW_ID` | DOUBLE | NOT NULL |  | Foreign key to the monitor_view_table. This number identifies the monitor that this component is associated to. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

