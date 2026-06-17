# DM_SEGMENTS

> Contains the same info as USER_SEGMENTS

**Description:** DM SEGMENTS  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BLOCKS` | DOUBLE |  |  | Number of blocks used by the segment |
| 2 | `BYTES` | DOUBLE |  |  | Number of bytes used by the segment |
| 3 | `EXTENTS` | DOUBLE |  |  | The number of extents used by the segment |
| 4 | `FREELISTS` | DOUBLE |  |  | Free lists for the segment |
| 5 | `FREELIST_GROUPS` | DOUBLE |  |  | Free list groups for the segment |
| 6 | `INITIAL_EXTENT` | DOUBLE |  |  | The initial extent allocated to the segment |
| 7 | `MAX_EXTENTS` | DOUBLE |  |  | The maximum extent allowed for the segment |
| 8 | `MIN_EXTENTS` | DOUBLE |  |  | The minimum extent for the segment |
| 9 | `NEXT_EXTENT` | DOUBLE |  |  | The next extent for the segment |
| 10 | `PCT_INCREASE` | DOUBLE |  |  | The percent increase for the segment |
| 11 | `SEGMENT_NAME` | VARCHAR(81) | NOT NULL |  | Name of the segment (index or table) |
| 12 | `SEGMENT_TYPE` | VARCHAR(18) | NOT NULL |  | The type of the segment |
| 13 | `TABLESPACE_NAME` | VARCHAR(30) |  |  | The name of the table space |
| 14 | `TABLE_NAME` | VARCHAR(30) | NOT NULL |  | The Table name associated with the segment (index or table) |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

