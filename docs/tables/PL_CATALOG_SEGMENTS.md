# PL_CATALOG_SEGMENTS

> Stores procedure catalog segments specific to organization and orderable.

**Description:** PL CATALOG SEGMENTS  
**Table type:** REFERENCE  
**Primary key:** `SEGMENT_ID`  
**Columns:** 13  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_DATA_IND` | DOUBLE | NOT NULL |  | Indicator used to determine if the data stored in SEGMENT_DATA_ID is active. |
| 2 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 3 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | Unique identifier from the Organization table. |
| 4 | `SEGMENT_DATA_ID` | DOUBLE | NOT NULL |  | Unique identifier to the LONG_BLOB table used to store segment data. |
| 5 | `SEGMENT_ID` | DOUBLE | NOT NULL | PK | Unique identifier for this table. |
| 6 | `SEGMENT_LABEL` | VARCHAR(60) |  |  | Non-HTML representation of segment label. |
| 7 | `SEGMENT_LABEL_ID` | DOUBLE | NOT NULL |  | Unique identifier to LONG_TEXT table used to store HTML representation of segment label. |
| 8 | `SEGMENT_TYPE_CD` | DOUBLE | NOT NULL |  | Segment type associated with a specific segment. Code set 2225. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [PL_SEG_CAT_CD_XREF](PL_SEG_CAT_CD_XREF.md) | `SEGMENT_ID` |

