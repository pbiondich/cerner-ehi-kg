# MLLD_DRC_GROUP_RELTN

> This table is a staging table used to help facilitate the MLTM tables load process. It is not intended for client use or use by any other process.

**Description:** MLLD_DRC_GROUP_RELTN  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `GROUPER_ID` | DOUBLE | NOT NULL |  | Externally assigned identifier for dose range check group |
| 2 | `GROUPER_NAME` | VARCHAR(250) |  |  | Name assigned to Multum Dose Range check grouper |
| 3 | `MAIN_MULTUM_DRUG_CODE` | DOUBLE | NOT NULL |  | Multum's designator for groups of similar drug products. |
| 4 | `SYNONYM_ID` | DOUBLE | NOT NULL |  | Multum's identifier for a unique drug name. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 10 | `VERSION` | VARCHAR(25) |  |  | VersionColumn |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

