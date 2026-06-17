# BB_PRINTER

> Contains blood bank printer information

**Description:** Blood Bank Printer  
**Table type:** REFERENCE  
**Primary key:** `BB_PRINTER_ID`  
**Columns:** 23  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BAUD_RATE_NBR` | DOUBLE | NOT NULL |  | Contains the baud rate of the blood bank printer. |
| 6 | `BB_PRINTER_ID` | DOUBLE | NOT NULL | PK | Uniquely identifies a blood bank printer. |
| 7 | `CRC_IND` | DOUBLE | NOT NULL |  | Indicates whether or not an error detection protocol is to be used with a blood bank printer that is serially attached to a com port. |
| 8 | `HORIZONTAL_OFFSET_NBR` | DOUBLE | NOT NULL |  | The horizontal offset in decimal format in millimeters fom the upper left corner of the printable area of a label. An example could be: 2.35 (meaning that the image will now be shifted to the right by 2.35 mm). |
| 9 | `LABEL_TYPE_CD` | DOUBLE | NOT NULL |  | The label form type that is currently loaded in the printer. |
| 10 | `MODEL_CD` | DOUBLE | NOT NULL |  | Contains the model of the blood bank printer. |
| 11 | `PORT_ADDR` | VARCHAR(50) | NOT NULL |  | The printer port address of the blood bank printer. |
| 12 | `PRINTER_ADDR` | VARCHAR(50) | NOT NULL |  | The network address of the blood bank printer. |
| 13 | `PRINTER_DESCRIPTION_TXT` | VARCHAR(100) | NOT NULL |  | A textual description of the blood bank printer. |
| 14 | `PRINTER_NAME` | VARCHAR(50) | NOT NULL |  | Name of the blood bank printer. |
| 15 | `PRINTER_NAME_KEY` | VARCHAR(50) | NOT NULL |  | Stores a corresponding string values for the printer name for the purposes of searching in UPPER case, less SPACES or special characters. |
| 16 | `PRINTER_NAME_KEY_A_NLS` | VARCHAR(200) |  |  | PRINTER_NAME_KEY_A_NLS column |
| 17 | `PRINTER_NAME_KEY_NLS` | VARCHAR(102) | NOT NULL |  | Stores the corresponding non-English character set values for the printer_name_key column. |
| 18 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 19 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 20 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 21 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 22 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 23 | `VERTICAL_OFFSET_NBR` | DOUBLE | NOT NULL |  | Contains the vertical offset in decimal format in millimeters from the upper left corner of the printable area of a label. An example could be: 4.35 (meaning that the image will now be shifted down from the top most position on the label by 4.35 mm). |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (2)

| From table | Column |
|------------|--------|
| [BB_FACILITY_PRINTER_R](BB_FACILITY_PRINTER_R.md) | `BB_PRINTER_ID` |
| [BB_SERVER_PRINTER_R](BB_SERVER_PRINTER_R.md) | `BB_PRINTER_ID` |

