# SN_TEMPERATURE_HIST

> History of the temperature recorded for locations and item instances.

**Description:** SN_Temperature_History  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `MANUAL_ENTRY_IND` | DOUBLE | NOT NULL |  | indicates whether the temperature was manually recorded |
| 2 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | identifier of the parent entity whose temperature was recorded. It¿s the primary key to the table specified by parent_entity_name column. Eg mm_instance_id or location_cd |
| 3 | `PARENT_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | name of the parent table that defines parent_entity_id. Eg ""LOCATION"" if parent_entity_id is a location_cd or ""MM_INSTANCE"" if parent_entity_id is a mm_instance_id |
| 4 | `PRSNL_ID` | DOUBLE | NOT NULL | FK→ | identifier of the personnel recording the temperature. |
| 5 | `SN_TEMPERATURE_HIST_ID` | DOUBLE | NOT NULL |  | Primary Key |
| 6 | `TEMPERATURE_DT_TM` | DATETIME | NOT NULL |  | Date and time when the temperature was recorded |
| 7 | `TEMPERATURE_IN_VALID_RANGE_IND` | DOUBLE | NOT NULL |  | Indicates if the temperature is within the valid range defined for the entity |
| 8 | `TEMPERATURE_UNIT_CD` | DOUBLE | NOT NULL |  | code value of the temperature specified at temp column |
| 9 | `TEMPERATURE_VALUE` | DOUBLE | NOT NULL |  | recorded temperature |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

