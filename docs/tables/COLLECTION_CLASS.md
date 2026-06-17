# COLLECTION_CLASS

> Stores all collection classes (codeset 231) and their attributes.

**Description:** Collection Class  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 18

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `COLL_CLASS_CD` | DOUBLE | NOT NULL |  | The internal number assigned by the system to the Collection Class. |
| 2 | `CONTAINER_ID_PRINT` | CHAR(1) |  |  | Determines whether or not and how container id's should be printed on labels. |
| 3 | `DEF_STORAGE_MINUTES` | DOUBLE |  |  | The default storage retention time in minutes that will be assigned to containers having this Collection Class code. The storage minutes are used to calculate the discard time for a container at the time it is placed in storage. |
| 4 | `MAX_ACCESSION_SIZE` | DOUBLE |  |  | The maximum number of characters to be included in the accession number bar code. |
| 5 | `MAX_CLASS_VOLUME` | DOUBLE |  |  | The numeric value which, along with the Maximum Collection Class Volume Units, represents the largest amount of specimen to be collected for netted orders having this Collection Class. |
| 6 | `MAX_CLASS_VOL_UNITS` | CHAR(15) |  |  | The units associated with the numeric value defined as the Maximum Collection Class Volume. |
| 7 | `MAX_CLASS_VOL_UNITS_CD` | DOUBLE | NOT NULL |  | The internal number assigned by the system to the Maximum Collection Class Volume Units. |
| 8 | `SEQUENCE` | DOUBLE | NOT NULL |  | Sequence field is used to indicate the print sequence of order label. The sequence will be used for label netting purpose. Collection class is not required to have sequence number, and 0 is the default value is sequence number is not assigned. |
| 9 | `SMG_BARCODE_ADJUST` | DOUBLE | NOT NULL |  | Determines left or right barcode adjustment on the label. |
| 10 | `SMG_FORMAT` | CHAR(1) |  |  | Determines left or right justification of the barcode on the label. |
| 11 | `STORAGE_TEMP_CD` | DOUBLE | NOT NULL |  | The default storage temperature for containers assigned to this collection class. |
| 12 | `SYMBOLOGY` | CHAR(1) |  |  | Determines what barcode symbology to use on the label. |
| 13 | `TRANSFER_TEMP_CD` | DOUBLE | NOT NULL |  | The default transfer temperature for containers assigned to this collection class. |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

