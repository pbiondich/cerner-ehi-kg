# ROUTE_START_TIME

> Stores the start times for collection routes.

**Description:** Route Start Time  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `COLLECTION_ROUTE_CD` | DOUBLE | NOT NULL |  | The collection route for the associated collection time. |
| 2 | `CUTOFF_MINUTES_FOR_ORDERS` | DOUBLE |  |  | This field will determine when a collection can no longer schedule for a collection time. When scheduling an order, the system will not schedule the order for a collection time if it is ordered after the cutoff time (collection time - cutoff minutes). |
| 3 | `LOOK_AHEAD_MINUTES` | DOUBLE |  |  | This defines the number of minutes the system will look ahead when a collection list is generated for a collection time. By default, the system will always look ahead to one minute before the next collection time. If the look ahead minutes is set to a higher value, then any orders scheduled before the look ahead time (collection time + look ahead minutes) will be printed. |
| 4 | `NURSE_COLLECT_IND` | DOUBLE |  |  | This determines if orders flagged as nurse collects can be scheduled for a collection time. It has the following values : 1 - Schedule any order for this time. 2 - Do not schedule nurse collects for this collection time. 3 - Schedule only nurse collects for this time. |
| 5 | `PRINTER_ID` | DOUBLE | NOT NULL |  | If this field is assigned a value, orders scheduled for this time will be printed to the given printer. It may be overridden if all orders are printed to the same printer. |
| 6 | `PRINT_QUEUE` | VARCHAR(20) |  |  | The name of the printer queue assigned to the printer_id value. |
| 7 | `ROUTE_START_TIME` | DOUBLE | NOT NULL |  | The collection times defined for scheduling orders. Orders with collection priority, specimen type, and nurse collect values that are assigned to the collection route will be scheduled for the appropriate collection time based on the requested collection time. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

