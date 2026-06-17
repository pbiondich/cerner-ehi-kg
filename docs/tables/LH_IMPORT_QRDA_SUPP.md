# LH_IMPORT_QRDA_SUPP

> Stores supplemental data from the QRDA Category 1 files being imported.

**Description:** LH_IMPORT_QRDA_SUPP  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `LH_IMPORT_QRDA_SUPP_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_IMPORT_QRDA_SUPP table. |
| 2 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 3 | `PARENT_ENTITY_ID` | DOUBLE |  |  | Identifies the unique source within the delivery network responsible for supplying the data. |
| 4 | `PARENT_ENTITY_NAME` | VARCHAR(30) |  |  | The table name associated to the parent_entity_id column. Currently that is LH_IMPORT_QRDA |
| 5 | `PERSON_ID` | DOUBLE | NOT NULL |  | The primary key of the PERSON table for the person associated to the record. |
| 6 | `SUPP_DATA_TXT` | VARCHAR(100) |  |  | The value of the supplemental type stored on the record coming from the file. |
| 7 | `SUPP_DATA_TYPE` | VARCHAR(50) |  |  | Identifies the type of supplemental data that is being stored for this record |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_SOURCE` | VARCHAR(50) | NOT NULL |  | The name of the program that updated the record last. |
| 11 | `UPDT_TASK` | VARCHAR(50) | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

