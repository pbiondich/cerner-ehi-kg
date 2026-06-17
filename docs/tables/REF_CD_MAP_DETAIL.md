# REF_CD_MAP_DETAIL

> Detail table used to store associations between results (events, orders, etc.) and reference codes (nomenclature_ids)

**Description:** Reference Code Mapping Detail  
**Table type:** ACTIVITY  
**Primary key:** `REF_CD_MAP_DETAIL_ID`  
**Columns:** 15  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ASSIGNMENT_METHOD_CD` | DOUBLE | NOT NULL |  | Assignment method which was used to make the reference code assignment. |
| 2 | `BEGIN_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | Contains the beginning point at which a row in the table is valid. |
| 3 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 4 | `ENTITY_CD` | DOUBLE | NOT NULL |  | Reference code entity value. Identifies the type of result. |
| 5 | `ENTITY_COLUMN_VALUE` | DOUBLE | NOT NULL |  | Value to identify a specific result (used along with entity_cd) related to the reference code. |
| 6 | `NOMENCLATURE_ID` | DOUBLE | NOT NULL | FK→ | The reference information associated to a result. |
| 7 | `PARENT_REF_CD_MAP_DETAIL_ID` | DOUBLE | NOT NULL | FK→ | Provides a mechanism for logically grouping reference codes. Will be the same as REF_CD_MAP_DETAIL_ID if current row is the highest level parent. |
| 8 | `PREV_REF_CD_MAP_DETAIL_ID` | DOUBLE | NOT NULL | FK→ | This field contains the unique ID of the previous version of the current row. |
| 9 | `REF_CD_MAP_DETAIL_ID` | DOUBLE | NOT NULL | PK | Unique, generated number that identifies a single row on the REF_CD_MAP_DETAIL table. |
| 10 | `REF_CD_MAP_HEADER_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to the REF_CD_MAP_HEADER table, which identifies the result that was evaluated for reference coding. |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `NOMENCLATURE_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |
| `PARENT_REF_CD_MAP_DETAIL_ID` | [REF_CD_MAP_DETAIL](REF_CD_MAP_DETAIL.md) | `REF_CD_MAP_DETAIL_ID` |
| `PREV_REF_CD_MAP_DETAIL_ID` | [REF_CD_MAP_DETAIL](REF_CD_MAP_DETAIL.md) | `REF_CD_MAP_DETAIL_ID` |
| `REF_CD_MAP_HEADER_ID` | [REF_CD_MAP_HEADER](REF_CD_MAP_HEADER.md) | `REF_CD_MAP_HEADER_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [REF_CD_MAP_DETAIL](REF_CD_MAP_DETAIL.md) | `PARENT_REF_CD_MAP_DETAIL_ID` |
| [REF_CD_MAP_DETAIL](REF_CD_MAP_DETAIL.md) | `PREV_REF_CD_MAP_DETAIL_ID` |

