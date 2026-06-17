# TRACK_FIELD_SPEC_BEHAVIOR

> Reference data that describes the behavior of tracking fields.

**Description:** Tracking Field Specification Behavior  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BEHAVIOR_NAME` | VARCHAR(64) | NOT NULL |  | Describes which field behavior is being defined |
| 2 | `BEHAVIOR_VALUE_TXT` | VARCHAR(255) | NOT NULL |  | Describes the desired behavior of the field |
| 3 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Key from another table that describes the behavior of this field |
| 4 | `PARENT_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | Table name |
| 5 | `TRACK_FIELD_SPEC_BEHAVIOR_ID` | DOUBLE | NOT NULL |  | Primary Key |
| 6 | `TRACK_FIELD_SPEC_ID` | DOUBLE | NOT NULL | FK→ | Foreign Key value from TRACK_FIELD_SPEC table |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `TRACK_FIELD_SPEC_ID` | [TRACK_FIELD_SPEC](TRACK_FIELD_SPEC.md) | `TRACK_FIELD_SPEC_ID` |

