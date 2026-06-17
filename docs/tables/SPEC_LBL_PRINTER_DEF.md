# SPEC_LBL_PRINTER_DEF

> This table stores the default label printers for nurse units, ambulatory locations and clinics. When 'immediate print' Lab orders come across an HIS interface, this table tells the system where to print the collection labels.

**Description:** Specimen Label Printer Default  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `COLLECTION_CLASS_CD` | DOUBLE | NOT NULL |  | A collection class which will route labels to a printer based on the orderables collection class. Not implemented at this time. |
| 2 | `COLL_PRIORITY_CD` | DOUBLE | NOT NULL |  | A collection priority which will route labels to a printer if an order is placed with the given collection priority. |
| 3 | `KEY_ID` | DOUBLE | NOT NULL |  | A unique identifier for a row. |
| 4 | `LBL_PRINTER_ID` | DOUBLE | NOT NULL |  | The system identifier for a label printer any orders meeting the criteria will print to. |
| 5 | `LBL_PRINT_QUEUE` | VARCHAR(20) |  |  | The queue name for the label printer. |
| 6 | `LOCATION_CD` | DOUBLE | NOT NULL | FK→ | An ambulatory, clinic, or nurse unit which will route labels to a printer if an order is placed on a patient is at the given location. |
| 7 | `NURSE_COLLECT_IND` | DOUBLE |  |  | An indicator that will route labels to a printer based on if the order is flagged as a nurse collect. |
| 8 | `NURSE_COLL_LBL_PRINTER_ID` | DOUBLE | NOT NULL |  | The system identifier for a label printer any orders meeting the criteria will print too. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LOCATION_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |

