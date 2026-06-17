# ENCNTR_SLICE_ACT

> Used to store the current state of an encounter slice's activity related to the parent entity tables.

**Description:** Encounter Slice Activity  
**Table type:** ACTIVITY  
**Primary key:** `ENCNTR_SLICE_ACT_ID`  
**Columns:** 12  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `COLUMN_CD` | DOUBLE | NOT NULL |  | The identifier for the column that the value_cd contains data for. |
| 3 | `COLUMN_VALUE_CD` | DOUBLE | NOT NULL |  | The value of the column on the parent_entity_name table and the parent_entity_id row. |
| 4 | `ENCNTR_SLICE_ACT_ID` | DOUBLE | NOT NULL | PK | The unique primary key of the ENCNTR_SLICE_ACT table. |
| 5 | `ENCNTR_SLICE_ID` | DOUBLE | NOT NULL | FK→ | Identifies which encounter slice the activity row applies to. |
| 6 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | The ID for the table row which for the table represented by the parent_entity_name. |
| 7 | `PARENT_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | The table which is being referenced. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_SLICE_ID` | [ENCNTR_SLICE](ENCNTR_SLICE.md) | `ENCNTR_SLICE_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [ENCNTR_SLICE_ACT_HIST](ENCNTR_SLICE_ACT_HIST.md) | `ENCNTR_SLICE_ACT_ID` |

