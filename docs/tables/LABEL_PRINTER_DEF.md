# LABEL_PRINTER_DEF

> This table stores the default specimen label printers, medial label printers, and label printer filters. When 'immediate print' Lab orders come across an HIS interface, this table tells the system where to print the labels.

**Description:** Label Printer Defaults  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 16

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `COLL_PRIORITY_CD` | DOUBLE | NOT NULL |  | A collection priority which will route labels to a printer if an order is placed with the given collection priority. A zero value indicates the printer is valid for all collection priorities. |
| 3 | `DEFAULT_TYPE_FLAG` | DOUBLE | NOT NULL |  | Type of printer default. Label routing defaults direct where an order's label should be printed. Label filtering defaults indicate which printers should default in the printer accept for the location. |
| 4 | `KEY_ID` | DOUBLE | NOT NULL |  | A unique identifier for a row. |
| 5 | `LBL_PRINTER_ID` | DOUBLE | NOT NULL |  | Label Routing - the system identifier for a label printer any orders meeting the criteria will print to. Label Filtering - the system identifier for a label printer that should be available for the location_cd. |
| 6 | `LBL_QUEUE_NAME` | VARCHAR(20) |  |  | The queue name for the label printer. |
| 7 | `LOCATION_CD` | DOUBLE | NOT NULL | FK→ | An facility, ambulatory, login location or nurse unit which will route labels to a printer if an order is placed on a patient is at the given location or logged in at the given location. Filters will show available printers based on this location. A value of zero indicates the printer is valid for all locations. |
| 8 | `NURSE_PRINTER_ID` | DOUBLE | NOT NULL |  | The system identifier for a label printer that nurse collect orders should print to. |
| 9 | `NURSE_QUEUE_NAME` | VARCHAR(20) |  |  | The queue name for the label printer. |
| 10 | `SEQUENCE` | DOUBLE | NOT NULL |  | Field to make default type, location, service resource, collection priority combination unique. This combination is always unique for routing defaults, but not for filter defaults. |
| 11 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL |  | Aliquot or Media labels determine which label to print to based on service resource. A value of zero indicates the printer is valid for all service resources at that login location. |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LOCATION_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |

