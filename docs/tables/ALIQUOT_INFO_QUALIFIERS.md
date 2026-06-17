# ALIQUOT_INFO_QUALIFIERS

> This table will hold the collection requirements for aliquots.

**Description:** Aliquot information qualifiers  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 17

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ALIQUOT_SEQ` | DOUBLE | NOT NULL |  | Indicates the position of each of the requirements. |
| 2 | `CATALOG_CD` | DOUBLE | NOT NULL |  | Reference number for the order catalog item associated with the requirements. |
| 3 | `COLL_CLASS_CD` | DOUBLE | NOT NULL |  | Reference number for the collection class associated with these requirements. |
| 4 | `COLL_INFO_SEQ` | DOUBLE | NOT NULL |  | The sequence with which the collection requirements and aliquot requirements are associated. |
| 5 | `MIN_VOL` | DOUBLE |  |  | Defines the smallest amount of specimen needed for these requirements. |
| 6 | `MIN_VOL_UNITS` | CHAR(15) |  |  | The units associated with the Minimum Volume numeric value. |
| 7 | `NET_IND` | DOUBLE |  |  | Determines if each orderable will go into a unique aliquot container. |
| 8 | `SPECIMEN_TYPE_CD` | DOUBLE | NOT NULL |  | Reference number for the specimen type associated with these requirements. |
| 9 | `SPEC_CNTNR_CD` | DOUBLE | NOT NULL |  | Reference number for the specimen container associated with the requirements. |
| 10 | `SPEC_HNDL_CD` | DOUBLE | NOT NULL |  | Reference number for the special handling associated with these requirements. |
| 11 | `STORAGE_TEMP_CD` | DOUBLE | NOT NULL |  | Reference number for the storage temperature associated with the requirements. |
| 12 | `UNITS_CD` | DOUBLE | NOT NULL |  | Not used at this time. |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

