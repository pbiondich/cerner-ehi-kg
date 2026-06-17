# DMS_MEDIA_XREF

> Contains information about the general classification of media items.

**Description:** DMS media cross reference.  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DMS_MEDIA_IDENTIFIER_ID` | DOUBLE | NOT NULL |  | References the DMS_MEDIA_IDENTIFIER table for the media object identifier. |
| 2 | `DMS_MEDIA_XREF_ID` | DOUBLE | NOT NULL |  | Unique identifier for this row. |
| 3 | `IDENTIFIER` | VARCHAR(64) |  |  | OBSOLETE - NO LONGER USED - Media cross ref identifier. |
| 4 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | The foreign key that this media instance is referencing. |
| 5 | `PARENT_ENTITY_ID_STRING` | VARCHAR(128) |  |  | We now have a non-Millennium implementation and need the ability to create cross references to UIDs represented as strings instead of only indexes to other Millennium tables. So instead of just parent_entity_name/id of orders(table)/1234 we may have something like orders(table)/1234@domainxyz where the parent_entiry_id_string is a string representation of the ID. |
| 6 | `PARENT_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | The name of the foreign table that the parent_entity_id refers to. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

