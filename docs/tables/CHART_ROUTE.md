# CHART_ROUTE

> This table defines the individual chart routes.

**Description:** Chart Routing  
**Table type:** REFERENCE  
**Primary key:** `CHART_ROUTE_ID`  
**Columns:** 11  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BANNER_PAGE_IND` | DOUBLE | NOT NULL |  | Stores if a banner page is requested to print with chart route. 0 = no, 1 = yes. |
| 3 | `CHART_ROUTE_ID` | DOUBLE | NOT NULL | PK | Stores the unique identifier for the chart route |
| 4 | `ROUTE_NAME` | VARCHAR(255) | NOT NULL |  | Stores the display name of the chart route |
| 5 | `ROUTE_NAME_KEY` | VARCHAR(255) | NOT NULL |  | Stores the display name of the chart route in all upper case and without spaces or special characters |
| 6 | `ROUTE_TYPE_FLAG` | DOUBLE | NOT NULL |  | Stores the type of the route. 0 = Provider, 1 = Organization, 2 = Location |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (3)

| From table | Column |
|------------|--------|
| [CHART_REQUEST](CHART_REQUEST.md) | `CHART_ROUTE_ID` |
| [CHART_SEQUENCE_GROUP](CHART_SEQUENCE_GROUP.md) | `CHART_ROUTE_ID` |
| [CR_REPORT_REQUEST](CR_REPORT_REQUEST.md) | `ROUTE_ID` |

