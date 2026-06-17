# COLLECTION_LIST_CONTAINER

> The cross reference table between collection/transfer lists and containers. This table will tell you all of the containers on a collection lists or a specimen transfer list.

**Description:** Collection List Container  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCESSION` | VARCHAR(20) |  |  | The accession number identifies a specimen. The accession number contains the current year, Julian date and a sequential number. |
| 2 | `ACCESSION_CONTAINER_NBR` | DOUBLE |  |  | Accession numbers may have multiple containers. These containers are sequenced by the accession container number. |
| 3 | `COLLECTION_LIST_ID` | DOUBLE | NOT NULL |  | Unique system identifier of a collection list or transfer list. |
| 4 | `CONTAINER_ID` | DOUBLE | NOT NULL |  | Unique system identifier of a container. |
| 5 | `LINE_NBR` | DOUBLE |  |  | Each accession in each collection list will have its own line number. |
| 6 | `RESPONSIBLE_PARTY_ID` | DOUBLE | NOT NULL |  | System identifier for the person who is responsible for the list. Not currently used. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

