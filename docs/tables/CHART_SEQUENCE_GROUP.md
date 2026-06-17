# CHART_SEQUENCE_GROUP

> Stores the different groups and their sequence numbers. Each group belongs to a group type (either Provider or Organization) and the sequence numbers are in reference to a specific group type.

**Description:** Chart Sequence Group  
**Table type:** REFERENCE  
**Primary key:** `SEQUENCE_GROUP_ID`  
**Columns:** 14  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `CHART_ROUTE_ID` | DOUBLE | NOT NULL | FK→ | Chart Route ID. Foreign Key for unique identifier to the CHART_ROUTE table. |
| 6 | `GROUP_NAME` | VARCHAR(255) | NOT NULL |  | Stores the group name. |
| 7 | `GROUP_TYPE_FLAG` | DOUBLE | NOT NULL |  | 1=Provider, 2=Organization This column became OBSOLETE when new table CHART_ROUTE was created and implemented. CAPE-128299. |
| 8 | `SEQUENCE_GROUP_ID` | DOUBLE | NOT NULL | PK | A number that uniquely identifies a row on this table. |
| 9 | `SEQUENCE_NBR` | DOUBLE | NOT NULL |  | Stores the sequence number of the group. Only groups within the same group_type_flag are related by their sequence number. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CHART_ROUTE_ID` | [CHART_ROUTE](CHART_ROUTE.md) | `CHART_ROUTE_ID` |

## Referenced by (3)

| From table | Column |
|------------|--------|
| [CHART_REQUEST](CHART_REQUEST.md) | `SEQUENCE_GROUP_ID` |
| [CHART_SEQ_GROUP_RELTN](CHART_SEQ_GROUP_RELTN.md) | `SEQUENCE_GROUP_ID` |
| [CR_REPORT_REQUEST](CR_REPORT_REQUEST.md) | `ROUTE_STOP_ID` |

