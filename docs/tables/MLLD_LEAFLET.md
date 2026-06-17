# MLLD_LEAFLET

> This table is a staging table used to help facilitate the MLTM tables load process. It is not intended for client use or use by any other process.

**Description:** MLLD_LEAFLET  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DATE_REVISED` | DATETIME |  |  | Last Revision date for the leaflet |
| 2 | `FILENAME` | VARCHAR(255) |  |  | Filename for the leafelet |
| 3 | `FUNCTION_ID` | DOUBLE | NOT NULL |  | Value from the Multum Function Type table (FK) |
| 4 | `LEAFLETID` | DOUBLE | NOT NULL |  | Leaflet ID. Part of the key for this table. |
| 5 | `LEAFLET_VERSION` | DOUBLE |  |  | The version number of this leafelet |
| 6 | `TITLE` | VARCHAR(110) |  |  | The leafelet Title |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

