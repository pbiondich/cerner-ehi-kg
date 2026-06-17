# TRACK_FILTER

> Stores tracking filter configurations

**Description:** TRACK FILTER  
**Table type:** REFERENCE  
**Primary key:** `TRACK_FILTER_ID`  
**Columns:** 14  
**Referenced by:** 4 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `AND_IND` | DOUBLE | NOT NULL |  | Indicates that this filter is the intersection of two child filters. |
| 2 | `FIELD_ENUM` | DOUBLE | NOT NULL |  | If FILTER_TYPE_FLAG is 0 (FIELD), this will specify which tracking field is being filtered on. |
| 3 | `FILTER_NAME` | VARCHAR(64) | NOT NULL |  | A unique name for the filter describing its function. |
| 4 | `FILTER_TYPE_FLAG` | DOUBLE | NOT NULL |  | Filter Type. FIELD = 1, ADMITTED = 2, DISCHARGED = 3, CHECKED OUT = 4, CHECKED IN = 5, ENCOUNTER = 6, PREARRIVAL = 7, MY PATIENTS = 8, SURGINET CASE = 8, SURGINET EVENT = 10, SURGINET OP. ROOM = 11, SURGINET FIELD = 12, SURGINET ANTICIPATED DURING = 13 |
| 5 | `LIST_TYPE_FLAG` | DOUBLE | NOT NULL |  | List Type. NOT SPECIFIED = 0, GROUP LIST = 1, BED LIST = 2, LOCATION LIST = 4, PROVIDER LIST = 8, CASE TRACKING LIST = 16 |
| 6 | `NOT_IND` | DOUBLE | NOT NULL |  | Indicates that the result of this filter will be negated. |
| 7 | `OR_IND` | DOUBLE | NOT NULL |  | Indicates that this filter is the union of two child filters. |
| 8 | `PARENT_TRACK_FILTER_ID` | DOUBLE | NOT NULL | FK→ | TRACK_FILTER_ID of parent filter. This creates a hierarchy of relationships of rows. |
| 9 | `TRACK_FILTER_ID` | DOUBLE | NOT NULL | PK | PRIMARY KEY |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PARENT_TRACK_FILTER_ID` | [TRACK_FILTER](TRACK_FILTER.md) | `TRACK_FILTER_ID` |

## Referenced by (4)

| From table | Column |
|------------|--------|
| [TRACK_FILTER](TRACK_FILTER.md) | `PARENT_TRACK_FILTER_ID` |
| [TRACK_FILTER_REFINEMENT](TRACK_FILTER_REFINEMENT.md) | `TRACK_FILTER_ID` |
| [TRACK_FILTER_VALUE](TRACK_FILTER_VALUE.md) | `TRACK_FILTER_ID` |
| [TRACK_LIST_FILTER_RELTN](TRACK_LIST_FILTER_RELTN.md) | `TRACK_FILTER_ID` |

