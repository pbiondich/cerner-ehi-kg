# DM_RESIZING_TEMP

> Will contain physical data statistics for any given object at any time like total space, unused space and so forth

**Description:** Will contain physical data statistics for any given object at any time.  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `LUB` | DOUBLE |  |  | Last used block for a given object |
| 2 | `LUEBI` | DOUBLE |  |  | Last used extent block id for a given object |
| 3 | `LUEFI` | DOUBLE |  |  | Last used extent file id for a given object |
| 4 | `OWNER` | VARCHAR(20) |  |  | The name of the owner |
| 5 | `SEGMENT_NAME` | VARCHAR(40) | NOT NULL |  | The name of the object |
| 6 | `SEGMENT_TYPE` | VARCHAR(20) | NOT NULL |  | The type of the object |
| 7 | `TABLESPACE_NAME` | VARCHAR(30) | NOT NULL |  | The name of the table space |
| 8 | `TBLOCKS` | DOUBLE |  |  | Total blocks allocated for a given object in a given tablespace |
| 9 | `TBYTES` | DOUBLE |  |  | Total bytes allocated for a given object in a given tablespace |
| 10 | `UBLOCKS` | DOUBLE |  |  | Unused blocks (free) for a given object in a given tablespace |
| 11 | `UBYTES` | DOUBLE |  |  | Unused bytes (free) for a given object in a given tablespace |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

