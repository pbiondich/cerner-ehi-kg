# PL_SEG_CAT_CD_XREF

> This table stores the segment data for specific orderable items.

**Description:** PL SEG CAT CD XREF  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_DATA_IND` | DOUBLE | NOT NULL |  | Indicator used to determine if the data stored in SEGMENT_DATA_ID is active. |
| 2 | `CATALOG_CD` | DOUBLE | NOT NULL | FK→ | Stores the order catalog item. |
| 3 | `SEGMENT_DATA_ID` | DOUBLE | NOT NULL |  | Unique identifier to the LONG_BLOB table used to store segment data. |
| 4 | `SEGMENT_ID` | DOUBLE | NOT NULL | FK→ | Unique identifier to the PL_CATALOG_SEGMENTS table for specific segment. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CATALOG_CD` | [ORDER_CATALOG](ORDER_CATALOG.md) | `CATALOG_CD` |
| `SEGMENT_ID` | [PL_CATALOG_SEGMENTS](PL_CATALOG_SEGMENTS.md) | `SEGMENT_ID` |

