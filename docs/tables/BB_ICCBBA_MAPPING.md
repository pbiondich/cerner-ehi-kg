# BB_ICCBBA_MAPPING

> This table will store the various database mappings used by the ICCBBA database.

**Description:** Blood Bank ICCBBAA Mapping  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BB_ICCBBA_MAPPING_ID` | DOUBLE | NOT NULL |  | This is the unique identifier of specific table/column mapping |
| 2 | `COLUMN_NAME` | VARCHAR(60) | NOT NULL |  | This is the name of the column on the e ICCBBA database. |
| 3 | `COLUMN_TYPE_DESC` | VARCHAR(12) | NOT NULL |  | This is the type of column referenced in the column_name column. |
| 4 | `TABLE_NAME` | VARCHAR(60) | NOT NULL |  | This is the name of the table on the ICCBBA database. |
| 5 | `TABLE_TYPE_DESC` | VARCHAR(12) | NOT NULL |  | This is the type of table referenced in the table_name column. |
| 6 | `UNIQUE_VERSION_IND` | DOUBLE | NOT NULL |  | This indicates whether or not the column contains a concatenation of values to maintain uniqueness. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 12 | `VERSION_NBR` | DOUBLE | NOT NULL |  | This is the version number of the ICCBBA database mapping. This number will be incremented with each new database release. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

